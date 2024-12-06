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

		# Debug mode TX tone

		chip.pbus.pbus_debugmode()

 		chip.pbus.open_tx(pa=0x5f, bb=0x120)  # set PA and BB gain

		chip.rfcal.tos()    # calibrate TX DC

		chip.wifi.txtone(1, 2, 40)   #enable, frequency(mHz), digital attenuation(0.24db)


		# Debug mode stop TX tone

		chip.wifi.stoptone()   #stop TX tone

		chip.pbus.pbus_workmode()  # exit PBUS debug mode


		
		# Work mode TX tone

		chip.wifi.force_txon(1)

		chip.wifi.txtone(1, 2, 40)   #enable, frequency(mHz), digital attenuation(0.24db)


		# Work mode stop TX tone
	
		chip.wifi.stoptone()

		chip.wifi.force_txon(0)



	6. RX dump test

		chip.dump.adcdumptest(dump_num=1024, plot_en=1)



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


	
Current test
=========================




Generate docomments 
======================== 

	In "eagletest/py_script/rftest/docs" run commands:

        	ipython doc_gen.py rftest










