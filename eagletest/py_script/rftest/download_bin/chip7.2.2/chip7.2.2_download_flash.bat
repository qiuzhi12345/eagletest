cd D:\chip\eagletest\py_script\rftest\download_bin\chip7.2.2
esptool.py --no-stub --chip esp32c -b 115200 -p com%1 write_flash --flash_mode dio --flash_fre 20m 0x1000 CHIP722_RFTest_20190516.bin
