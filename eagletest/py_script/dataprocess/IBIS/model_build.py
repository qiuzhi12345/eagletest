import pandas as pd
import numpy as np
import shutil
import collections

class ibisModelBuild(object):
    '''simulation data is used to construct below model file.

    - NOTE:
        - a header file is required to be modified before contruction
        - example file see share_drive/ONE PIECE/ESP32/IBIS/esp32_head.ibs
        - see esp32_ibis.ibs as pst_process model file example, under same path as above
        - use ibischk64 to check syntax for ibis model file built by this script
    '''
    def __init__(self):
        self._note_mark = '|'
        self._end = '\n'
        self._line_sep = self._note_mark + 68 * '*' + self._end
        self._line_iv = '|Voltage' + ' ' * 3 + \
            'I(typ)' + ' ' * 7 + 'I(min)' + ' ' * 7 + 'I(max)' + self._end
        self._line_rmp = self._note_mark + ' ' * 10 + 'typ' + \
            ' ' * 15 + 'min' + ' ' * 15 + 'max' + self._end
        self._line_vt = self._note_mark + 'time' + ' ' * 11 + \
            'V(typ)' + ' ' * 7 + 'V(min)' + ' ' * 7 + 'V(max)' + self._end

    def _f_wr(self,line, file_name):
        with open(file_name, 'a') as f:
            f.write(line)
            f.flush()

    def _tbl_fmt(self,df):
        '''change expression format to be xxe01
        '''
        for i in df.columns[1:]:
            df[i] = df[i].map(lambda x: '%.3e' % x)


    def _tbl_fmt_vt(self,dt_file_name):
        '''change expression format to be xxe01
        '''
        df = pd.read_csv(dt_file_name)
        if ('_pd_r' in dt_file_name) or ('pu_f' in dt_file_name):
            df['TIME'] -= 3e-8
        else:
            df['TIME'] -= 1e-8
        for i in df.columns[1:]:
            df[i][df[i].abs() < 0.001] = 0
        for i in df.columns:
            df[i] = df[i].map(lambda x: '%.3e' % x)
        df = df.drop_duplicates(subset=['min', 'max', 'typ'], keep='first')
        return df


    def _model_h_e(self,file_name, model_name, model_head=True):
        ''' adds model header or ender to file
        '''
        self._f_wr(file_name=file_name, line=self._line_sep)
        _header = 'Model:' if model_head else 'End of Model:'
        self._f_wr(file_name=file_name, line=self._note_mark +
              ' ' * 20 + '%s %s\n' % (_header, model_name))
        self._f_wr(file_name=file_name, line=self._line_sep + self._note_mark + self._end)


    def _model_def(self,file_name, model_name):
        line = '[Model]' + ' ' * 5 + '%s' % model_name + self._end
        if model_name == 'io_pud':
            line += 'Model_type' + ' ' * 2 + '3-state' + self._end
        else:
            line += 'Model_type' + ' ' * 2 + 'I/O' + self._end
        line += 'Polarity    Non-Inverting' + self._end
        if 'io_drv' in model_name:
            line += 'Vinh = 1.668\n' + 'Vinl = 1.668\n' + 'Vmeas = 1.65\n'

        line += '|       typ       min       max\n'
        line += 'C_comp  5.090fF   5.001fF   5.228fF\n'

        if 'io_drv' in model_name:
            line += '[Model Spec]\n'
            line += '|           typ       min       max\n'
            line += 'Vinh        1.668     1.324     1.892   |Input logic "high" DC Voltage\n'
            line += 'Vinl        1.668     1.324     1.892   |Input logic "low" DC Voltage\n'

        if 'pud' in model_name:
            line += 'Vmeas = 1.65\n'
        line += '|\n'
        line += '|                        typ   min   max\n'
        line += '[Temperature Range]       25   125   -40\n'
        line += '|Note: Junction Temperature\n'
        line += '[Voltage Range]          3.3   2.7   3.6\n'
        line += '|\n'
        line += self._line_sep

        self._f_wr(file_name=file_name, line=line)


    def _iv(self,file_name, dt_type, dt_file_name):
        '''construct iv curve for resistor pull up/down mode
        '''
        dt_note = '|Note: Vtable = Vcc - Voutput\n' if dt_type in [
            'Pullup', 'POWER_clamp'] else ''
        line = '|\n' + '[%s]\n' % dt_type + \
            '%s' % dt_note + '|\n' + '|\n' + self._line_iv
        self._f_wr(file_name=file_name, line=line)

        tbl_2_wr = pd.read_csv(dt_file_name)
        self._tbl_fmt(tbl_2_wr)

        index_ = tbl_2_wr.index
        if   dt_type == 'GND_clamp':
            end_pnt = tbl_2_wr[tbl_2_wr['PAD']==3.3].index[0]
            index_  = np.arange(0,end_pnt+1)
        elif dt_type == 'POWER_clamp':
            end_pnt = tbl_2_wr[tbl_2_wr['PAD']==0.0].index[0]
            index_  = np.arange(0,end_pnt+1)

        for i in index_:
            pad_ = tbl_2_wr.loc[i]['PAD']
            line = '%s' % (pad_) + ' ' * 3 if pad_ < 0 else '%s' % (pad_) + ' ' * 4
            for col_ in ['typ', 'min', 'max']:
                i_ = tbl_2_wr.loc[i][col_]
                l_i = ' ' * 3 + \
                    '%s' % (i_) if i_.startswith('-') else ' ' * 4 + '%s' % (i_)
                line += l_i
            self._f_wr(file_name=file_name, line=line + '\n')

        self._f_wr(file_name=file_name, line='|\n')


    def _ramp(self,file_name, dt_file_name, d0=0, d1=0):
        '''construct ramp data for resistor pull up/down mode
        '''
        d0 = 0.0 if d0 == 0 else 1.1
        d1 = 0.0 if d1 == 0 else 1.1

        dt_f_n_splt = dt_file_name.split('_')
        if 'rpud' in dt_f_n_splt:
            r_load = dt_f_n_splt[-1][:-4].upper()
            tbl_sep = ' '
        else:
            r_load = 50
            tbl_sep = ' '

        dt_note = '|Note: 20% to 80% voltage swing / time it takes to swing the above voltage\n'
        line = '|\n' + '[Ramp]\n' + '%s' % dt_note + \
            'R_load = %s\n' % r_load + '|\n' + self._line_rmp
        self._f_wr(file_name=file_name, line=line)

        tbl_2_wr = pd.read_csv(dt_file_name, sep=tbl_sep)
        if 'otpt' in dt_f_n_splt:
            tbl_2_wr_g = tbl_2_wr.groupby(by=['DRV_0', 'DRV_1'])
            tbl_2_wr = tbl_2_wr_g.get_group((d0, d1))
        for i in tbl_2_wr.index:
            type_ = tbl_2_wr.loc[i]['TYPE']
            t_2_wr = 'dV/dt_r' if type_.endswith('r') else 'dV/dt_f'

            line = '%s' % (t_2_wr) + ' '
            for col_ in ['typ', 'min', 'max']:
                i_ = tbl_2_wr.loc[i][col_]
                if i_.startswith('-'):
                    i_ = i_[1:]
                l_i = ' ' * 3 + '%s' % (i_)
                line += l_i
            self._f_wr(file_name=file_name, line=line + '\n')

        self._f_wr(file_name=file_name, line='|\n')


    def _vt(self,file_name, dt_file_name, pu=True, tbl_sep=','):
        '''construct vt curve for pull up & pull down waveform
        '''
        r_or_f = 'Rising' if '_r_' in dt_file_name else 'Falling'
        line = '|\n' + '[%s Waveform]\n' % r_or_f
        line += 'R_fixture     = 50\n'
        if not pu:
            line += 'V_fixture     = 3.3\n'
            line += 'V_fixture_min = 2.7\n'
            line += 'V_fixture_max = 3.6\n'
        else:
            line += 'V_fixture     = 0\n'
            line += 'V_fixture_min = 0\n'
            line += 'V_fixture_max = 0\n'
        line += self._line_vt
        self._f_wr(file_name=file_name, line=line)

        #tbl_2_wr = pd.read_csv(dt_file_name, sep=tbl_sep)
        # self._tbl_fmt_vt(tbl_2_wr,dt_file_name)
        tbl_2_wr = self._tbl_fmt_vt(dt_file_name)
        for i in tbl_2_wr.index:
            time_ = tbl_2_wr.loc[i]['TIME']
            line = '%s' % (time_) + ' ' * 3
            for col_ in ['typ', 'min', 'max']:
                i_ = tbl_2_wr.loc[i][col_]
                l_i = ' ' * 3 + \
                    '%s' % (i_) if i_.startswith('-') else ' ' * 4 + '%s' % (i_)
                line += l_i
            self._f_wr(file_name=file_name, line=line + '\n')

        self._f_wr(file_name=file_name, line='|\n')


    def main(self,f_2_e='esp32_gpio.ibs',f_header='esp32_head.ibs',f_adr = './ESP32_IBIS_GPIO/CorrectData/'):
        '''script to construct IBIS file based on simulation data
        
        - :param f_2_e   : file name to be used for IBIS model      
        - :param f_header: header file required to contruct IBIS model, modify before use
        - :param f_adr   : simulation data file location
        - :note: vinh, vinl & c_comp values are not picked from data file, but manually typed, see line 73,78,79
        '''
        shutil.copyfile(f_header, f_2_e)

        ### use below lines to construct io_pud
        f_head    = 'ibis_iv_rpud'
        iv_type_l = ['Pulldown', 'Pullup', 'POWER_clamp', 'GND_clamp']
        iv_t_n_l  = ['pd', 'pu', 'pc', 'gc']

        '''model header'''
        self._model_h_e(file_name=f_2_e, model_name='io_pud', model_head=True)
        '''model definition'''
        self._model_def(file_name=f_2_e, model_name='io_pud')

        '''construct i-v table'''
        for d_i, d_v in enumerate(iv_type_l):
            dt_file_name = f_adr + f_head + '_' + iv_t_n_l[d_i] + '.csv'
            self._iv(file_name=f_2_e, dt_type=d_v, dt_file_name=dt_file_name)

        '''construct ramp table'''
        dt_file_name = f_adr + 'ibis_vt_rpud_ramp_10k.csv' # define file name here

        self._ramp(file_name=f_2_e, dt_file_name=dt_file_name)
        '''model footer'''
        self._model_h_e(file_name=f_2_e, model_name='io_pud', model_head=False)
        ### end of io_pud construct

        ### below lines to contruct io_drv
        drv_stp_l         = collections.OrderedDict()
        drv_stp_l['STR']  = range(4)
        drv_stp_l['DRV0'] = [0, 1, 0, 1]
        drv_stp_l['DRV1'] = [0, 0, 1, 1]
        drv_l             = pd.DataFrame(drv_stp_l)

        f_head    = 'ibis_iv_otpt'
        iv_type_l = ['Pulldown', 'Pullup','POWER_clamp','GND_clamp']
        iv_t_n_l  = ['pd', 'pu','pc','gc']
        vt_type_l = ['Rising Waveform', 'Falling Waveform']

        for s_i in range(4):
            '''model header'''
            self._model_h_e(file_name=f_2_e, model_name='io_drv_%s' %
                       s_i, model_head=True)
            '''model definition'''
            self._model_def(file_name=f_2_e, model_name='io_drv_%s' % s_i)
            _d0 = drv_l['DRV0'][drv_l['STR'] == s_i].values[0]
            _d1 = drv_l['DRV1'][drv_l['STR'] == s_i].values[0]

            # _d0 = 0.0 if _d0 == 0 else 1.1
            # _d1 = 0.0 if _d1 == 0 else 1.1

            '''contruct i-v table'''
            for d_i, d_v in enumerate(iv_type_l):
                dt_file_name = f_adr + f_head + '_' + \
                    iv_t_n_l[d_i] + '_' + 'D1_%s_D0_%s' % (_d1, _d0) + '.csv'
                print 'IV USE file: %s' % dt_file_name
                # iv_t_n_l[d_i] + '_' +'D0_%s_D1_%s' % (_d0, _d1) + '.csv'
                self._iv(file_name=f_2_e, dt_type=d_v, dt_file_name=dt_file_name)

            '''construct ramp table'''
            dt_file_name = f_adr + 'ibis_vt_otpt_ramp.csv' # define file name here

            print 'VT RAMP USE file: %s' % dt_file_name
            self._ramp(file_name=f_2_e, dt_file_name=dt_file_name, d0=_d0, d1=_d1)

            '''construct v-t table'''
            # define file name here
            for p_t in ['pd_r', 'pd_f', 'pu_r', 'pu_f']:
                # dt_file_name = f_adr + 'ibis_vt_otpt_'+p_t+'_%d_%d'%(_d0,_d1)+'.csv'
                dt_file_name = f_adr + 'ibis_vt_otpt_' + \
                    p_t + '_d1_%d_d0_%d' % (_d1, _d0) + '.csv'
                print 'VT USE file: %s' % dt_file_name
                pu_j = True if 'pu' in p_t else False
                self._vt(file_name=f_2_e, dt_file_name=dt_file_name, pu=pu_j)

            '''model footer'''
            self._model_h_e(file_name=f_2_e, model_name='io_drv_%s' %
                       s_i, model_head=False)
        ### end of io_drv model 

        self._f_wr(file_name=f_2_e, line='[End]\n|\n')
        ### end of entire ibis model
