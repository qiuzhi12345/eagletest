====================
Quick Start Guide
====================


Project Introduction 
=============== 

	RFAPI:
		* In eagletest/py_script/hal
		* it is to store software interface APIs.

	RFLIB:
		* In eagletest/py_script/rftest/rflib
		* it is to store common RF test functions.

	TestCase:
		* In eagletest/py_script/rftest/testcase
		* it is to store RF test cases.

	RFDATA:
		* In eagletest/py_script/rftest/rfdata
		* it is to store RF test data.

	DOCS:
		* In eagletest/py_script/rftest/docs
		* it is to store document and testreport.



Start rftest 
=============== 

	In "eagletest/py_script/" run commands:
    
        	ipython -i autotest.py rftest

        	chip=RFTCS(com(6))   # 6 should change to your com port number


Common test commands
=========================
	
	1. write/read memory

		chip.mem.wrm(0x600060a0, 11, 8, 0x0)

		chip.mem.rdm(0x600060a0, 11, 8)


	2. write/read i2c

		 chip.i2c.rfrx.dtest = 0

		 chip.i2c.rfrx.dtest


	3. write/read PBUS

		chip.pbus.pbus_debugmode()

		chip.pbus.pbus_wr('rfrx1', 'en1', 0x184)
	
		chip.pbus.pbus_rd('rfrx1', 'en1')

		chip.pbus.pbus_workmode()


	4. select RF channel

		chip.wifi.rfchsel(1)  # 1~14


	5. TX Tone

	    * Debug mode TX tone

		chip.pbus.pbus_debugmode()

 		chip.pbus.open_tx(pa=0x5f, bb=0x120)  # set PA and BB gain

		chip.rfcal.tos()    # calibrate TX DC

		chip.wifi.txtone(1, 2, 40)   #enable, frequency(mHz), digital attenuation(0.24db)


	    * Debug mode stop TX tone

		chip.wifi.stoptone()   #stop TX tone

		chip.pbus.pbus_workmode()  # exit PBUS debug mode


		
	    * Work mode TX tone

		chip.wifi.force_txon(1)

		chip.wifi.txtone(1, 2, 40)   #enable, frequency(mHz), digital attenuation(0.24db)


	    * Work mode stop TX tone
	
		chip.wifi.stoptone()

		chip.wifi.force_txon(0)



	6. RX dump test

		chip.adc_dump.adcdumptest(dump_num=1024, plot_en=1)



Basic functions test cases
===========================

	1. Write and read test 

		basic=BasicTest(chip.comport, chip.chipv)

		basic.mem_test()

		basic.i2c_test()

		basic.pbus_test()


	2. RFPLL CAP Sweep

		basic=BasicTest(chip.comport, chip.chipv)

		basic.rfpll_sweep()


Performance oprimization cases
===============================

	1. Sweep I2C Register 

		i2c_sweep = I2C_SWEEP(chip.comport, chip.chipv)

		i2c_sweep.i2c_EVM_MASK(cable_lose=2, channel=[1], sheetnamelist=['rftx'], curr_en=0, mask_en=0,  num=10, iqv_no=2)

		i2c_sweep.combi2c_EVM_MASK(cable_lose=2, channel=[1], sheetnamelist=['rftx'], curr_en=0, mask_en=0, target_pwr_dis=1, num=10, iqv_no=2)

		i2c_sweep.read_i2creg_all_loop(loop=1,i2c_table_out="d:/chip/eagletest/rfdata/i2c_table.xlsm") # read all i2c register	value	

	2. Sweep TX GAIN 

		test = Sweep_TX_Gain(chip.comport, chip.chipv)

		test.sweep_tx_gain_tone(cable_lose=2, target_pwr_dis=0, board_no='') #use spectrum analyzer

		test.sweep_tx_gain_EVM(cable_lose=2, channel=[1], data_rate=['mcs7'], num=10, target_pwr_dis=0, iqv_no=2, board_no='') #use WIFI Insturment
		
		test.sweep_dig_gain(cable_lose=2,channel=[1], data_rate=['mcs7'], num=10, iqv_no=2, board_no='')#use WIFI Insturment

	3. Power detector Test	

		pwrdet = PwrDet(chip.comport, chip.chipv)

		pwrdet.tone_power_detector(backoff=-80,cable_lose=0) # use spectrum analyzer

		pwrdet.packet_power_detector(cable_lose=2, channel=[1], data_rate=['mcs7'], num=10, iqv_no=2)# use WIFI insturment

	4. PA performance test

		pa_test = PA_OutPwr(chip.comport, chip.chipv)
		
		pa_test.Chip_Test()

		- then input:

			0, sweeping I2C to test Power;              #use spectrum analyzer

			1, setting I2C register to test P1dB;       #use spectrum analyzer

			2, EVM and P1dB test on diffrent Matching;  #use spectrum analyzer and WIFI Insturment

			3, MASK and IM3  test on different Matching;#use spectrum analyzer and WIFI Insturment

	5. Force Tx Gain Test 

		test = Sweep_TX_Gain(chip.comport, chip.chipv)

		test.fixed_tx_gain_EVM(cable_lose=2, channel=[1], data_rate=['mcs7'], num=10, target_pwr_dis=1,iqv_no=2, board_no='')

	6. Filter Test

		FT = filter_test(chip.comport, chip.chipv)

		FT.filter_tx(cfreq=2437, bw=60, att=0, bt_en=0, device_spa='E4404B')

		FT.test_rxfilter_bt(force_gain=34, chan=1,bw=4, est_len=4096)

	
	7. RX gain and dco sweep

	    * rx gain table test

		test=Sweep_RX_Gain(chip.comport,chip.chipv)

		test.sweep_rx_table(cable_att=3, tx_chan=14, iqv_no=2)

	    * force rfrx gain test

		test.sweep_rxgain_force(cable_att=3, tx_chan=14, iq_no=2)

	    * rx dco scale test

		test.sweep_rxdc(14)

		

TX/RX performance test
=========================

	1. open instrument server

 		instru_server('iqx')  #input: 'iqv', 'iqx', 'wt'


	2. TX Power & EVM & MASK Test

		test=WIFI_TXRX_TEST(chip.comport, chip.chipv)

		test.WIFI_TX_PWR_EVM(cable_lose=2, channel=[14], data_rate=['mcs7'], iqv_no=2, iqv_num=10)


	3. RX Sensitivity Test

		test.WIFI_RX_sens(cable_lose=2, chan_in=[14], data_rate=['mcs7'],iqv_no=1)


	4. RX Maximum input level Test

		test.WIFI_RX_maxlevel(cable_lose=2, chan_in=[14], data_rate=['mcs7'], iqv_no=1)


	5. RX Dynamic Range Test

		test.WIFI_RX_range(cable_lose=2, chan_in=[14], data_rate=['mcs7'], rx_range=['[-75, 0]'], iqv_no=1)


RX ACPR Test
=========================

	acpr = RF_ACPR(chip.comport, chip.chipv)

	acpr.rx_acpr(iq_signal='iqxel',iq_interfere='wt200',lost_list=[11.5],iq_mode=['11b'], pwr_interfere_step=1, packnum=100, iqv_signal_no=1,iqv_interfere_no=1,Module_Name='ESP32_Testboard',Module_Num='')


RX Frequency offset Test
=========================

	test = RxFreqTol(chip.comport, chip.chipv)

	test.rf_freq_tol_test(instru_name='wt208c',lost_list=[11.5],tx_chan=[14],tx_pwr =-50,iq_mode=['11b'],packnum=100,iqv_no=1,comment='ESP32_Testboard')
		

	
Current test
=========================

	1. RF TX RX current Test

		test = RF_Curr(chip.comport, chip.chipv)

		test.txrate_curr(channel=[1,6,11], data_rate=['mcs0','mcs7'], cable_lose=1, rf_en =0, iqv_no=1)

		test.rxrate_curr(channel=[1,6,11],data_rate=['1m','mcs7_40'])
	
CSV Report Write Usage 
=========================

	from rftest.rflib.csv_report import csvreport

	title = 'data1, data2, data3\n'

        fname = self.wifi.get_filename('store_folder', 'file_name')

        fw1=csvreport(fname, title)

	fw1.write_data([data1, data2, data3])



Generate docomments 
======================== 

	In "eagletest/py_script/rftest/docs" run commands:

        	ipython doc_gen.py rftest










