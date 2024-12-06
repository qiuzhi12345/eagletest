//Copyright (c) 2010 Espressif System
// 
// Generate flash bin files
//
// ------------------------------------------------------------------------
// flash bin file layout is as the following
//  
//   header {
//     uint8 magic = 0xE9
//      uint8 block_number (how many blocks in the bin file)
//   }
//   block_header {
//      uint32  load_addr (the address to be loaded)
//      uint32  data_len
//  }
//  [actual data ...]
//  [next block...]
//  [pad, align to 16B, include 1B checksum]
//  [uint8 checksum, result of xor all data]
//
//  NB: on-chip unpack routine may encounter problem if data_len of certain
//      block is less than 16B (minimum flash_data_line)
// ----------------------------------------------------------------------
//

#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdlib>

using namespace std;

#define FLASH_DATA_LINE 16
#define DATA_LINE_BITS 0xf
#define TEXT_ADDRESS 0x40100000
#define TEXT_END     0x40120000
#define DATA_ADDRESS 0x3ffb0000
#define DATA_END 0x3fff8160
#define BIN_MAGIC 0xE9
#define APP_ENTRY 0  //don't overwirte the start point specified in ld script
#define CHECKSUM_INIT	0xEF

ifstream::pos_type text_size;
ifstream::pos_type rodata_size;
ifstream::pos_type data_size;
unsigned int text_size4 = 0;

char * text_seg;
char * rodata_seg;
char * data_seg;
char * pad_buf;

#pragma pack(1)
struct header {
    unsigned char magic;
    unsigned char blocks;
    //unsigned int checksum;  //xor the entire file
    unsigned char pad[2];  //pad 2 bytes, since iram can't be access in byte-wise
    unsigned int entry;
};

struct header bin_header;
#pragma pack()

struct block_header {
    unsigned int load_address;
    unsigned int data_length;
};

struct block_header text_header, rodata_header, data_header;

int main(int argc, char const *  argv[]) 
{
    ifstream textfile;
    ifstream rodatafile;
    ifstream datafile;
    ofstream binfile;
    int pad, blocks = 0;
    unsigned int text_entry_address, data_start_address, rodata_start_address;

    if (argc < 6) {
        cout << "usage: genflashbin text.bin text_entry_addr data.bin data_start_address rodata.bin rodata_start_address" << endl;
        return 0;
    }

    if (1) {
        sscanf(argv[2], "%08x", &text_entry_address);
        cout << "text start_addr 0x" << hex << text_entry_address << endl;
        if ((text_entry_address < TEXT_ADDRESS) || (text_entry_address > TEXT_END)) {
            cout << "!!! Wrong entry address !!!  Use default" << endl;
            cout << "start_addr is in hex format but no 0x prefix" << endl;
        } else {
            //text seg load_address always be 0x40100000, a.k.a. iram start point
            //text_entry_address is where the user_start(), assign to bin_header->entry
            text_header.load_address = TEXT_ADDRESS;
        }

        sscanf(argv[4], "%08x", &data_start_address);
        cout << "data start_addr 0x" << hex << data_start_address << endl;
        if (data_start_address == 0) {
            cout << " no data segment " << endl;
        } else if ((data_start_address < DATA_ADDRESS) || (data_start_address > DATA_END)) {
            cout << "!!! Wrong data start address !!!  Use default" << endl;
            cout << "data_start_addr is in hex format but no 0x prefix" << endl;
        } else {
            data_header.load_address = data_start_address;
        }

        sscanf(argv[6], "%08x", &rodata_start_address);
        cout << "rodata start_addr 0x" << hex << rodata_start_address << endl;
        if ((rodata_start_address < DATA_ADDRESS) || (rodata_start_address > DATA_END)) {
            cout << "!!! Wrong rodata start address !!!  Use default" << endl;
            cout << "rodata_start_addr is in hex format but no 0x prefix" << endl;
        } else {
            rodata_header.load_address = rodata_start_address;
        }
    }

    textfile.open(argv[1], ios::in | ios::binary | ios::ate);
    if (textfile.is_open()) {
        unsigned int tmp;
        text_size = textfile.tellg();
        tmp = text_size;
        if (tmp & 0x3) {
            cout << "ERROR: text seg len is " << text_size <<" is NOT 4-byte aligned!! Need to pad" << endl;
        }
        text_size4 = (tmp + 3) & (~3); //roundup to 4
		
        text_header.data_length = text_size4;
        text_seg = new char [text_size4];
        memset(text_seg, 0, text_size4);
        textfile.seekg (0, ios::beg);
        textfile.read(text_seg, text_size);
        textfile.close();

        blocks++;
    } else {
        cout << "unable to open text bin file" << endl;
        return 0;
    }
	cout << "text size" << text_size4 << endl;

    //It's possible that there is no data segment...
    if (data_header.load_address) { 
        datafile.open (argv[3], ios::in | ios::binary | ios::ate);
        if (datafile.is_open())
        {
            data_size = datafile.tellg();
            data_header.data_length = data_size;
            data_seg = new char [data_size];
            datafile.seekg (0, ios::beg);
            datafile.read(data_seg, data_size);
            datafile.close();
            if (data_size) blocks++;
        } else {
            cout << "unable to open data bin file or there is no data segment!" << endl;
            //delete[] text_seg;
            //return 0;
        }
    }
	cout << "data size" << data_size << endl;

    rodatafile.open (argv[5], ios::in | ios::binary | ios::ate);
    if (rodatafile.is_open()) {
        rodata_size = rodatafile.tellg();
        rodata_header.data_length = rodata_size;
        rodata_seg = new char [rodata_size];
        rodatafile.seekg (0, ios::beg);
        rodatafile.read(rodata_seg, rodata_size);
        rodatafile.close();
        if (rodata_size) blocks++;
    } else {
        cout << "unable to open rodata bin file or there is no rodata segment!" << endl;
        //delete[] text_seg;
        //delete[] data_seg;
        //return 0;
    }
	cout << "rodata size" << rodata_size << endl;

    if (text_size) {
        binfile.open("eagle.app.flash.bin", ios::out | ios::binary);
        if (binfile.is_open()) {
            unsigned char checksum = CHECKSUM_INIT;
            bin_header.magic = BIN_MAGIC;
            bin_header.blocks = blocks;
            bin_header.entry = text_entry_address; //where is user_start()

            int total_size = sizeof(struct header) + bin_header.blocks * sizeof(struct block_header) +
                text_size4 + data_size + rodata_size + 1;  //last one is checksum
            pad = FLASH_DATA_LINE - (total_size & DATA_LINE_BITS);
			cout << "header size is " << sizeof(struct header) << " block header size " << (bin_header.blocks * sizeof(struct block_header)) << " total size is " << total_size << " pad is 0x" << pad << " blocks " << bin_header.blocks << endl;
            if (pad > 0) {
                pad_buf = new char [pad];
            }
            memset(pad_buf, 0, pad);

            unsigned char *seg_ptr = (unsigned char *)text_seg;
            for (int i=0; i < text_size4; i++) 
            {
                //how about text_seg is not 4byte aligned...
                checksum ^= *seg_ptr++;
            }

            unsigned int tempCHK = checksum;
            cout << "chksum text " << tempCHK << endl;
            if (data_size) {
                unsigned char *seg_ptr = (unsigned char *)data_seg;
                for (int i=0; i<data_size; i++) 
                {
                    //how about text_seg is not 4byte aligned...
                    checksum ^= *seg_ptr++;
                }
                tempCHK = checksum;
                cout << "chksum data " << tempCHK << endl;
            }
            if (rodata_size) {
                seg_ptr = (unsigned char *)rodata_seg;
                for (int i=0; i<rodata_size; i++) 
                {
                    //how about rodata_seg is not 4byte aligned...
                    checksum ^= *seg_ptr++;
                }
                tempCHK = checksum;
                cout << "chksum all " << tempCHK << endl;
            }

            binfile.write((const char *)&bin_header, sizeof(struct header));
            binfile.write((const char *)&text_header, sizeof(struct block_header));
            binfile.write(text_seg, text_header.data_length);
            cout << "text load_addr 0x" << text_header.load_address << " len 0x" << text_header.data_length << endl;
            if (data_size) {
                binfile.write((const char *)&data_header, sizeof(struct block_header));
                binfile.write(data_seg, data_size);
                cout << "data load_addr 0x" << data_header.load_address << " len 0x" << data_header.data_length << endl;
            }
            if (rodata_size) {
                binfile.write((const char *)&rodata_header, sizeof(struct block_header));
                binfile.write(rodata_seg, rodata_size);
                cout << "rodata load_addr 0x" << rodata_header.load_address << " len 0x" << rodata_header.data_length << endl;
            }
            if (pad) {
                binfile.write(pad_buf, pad);
            }
            binfile.write((const char *)&checksum, sizeof(char));

            binfile.close();
        } else {
            cout << "write failed" << endl;
        }
    }
    delete[] text_seg;
    delete[] data_seg;
    delete[] rodata_seg;
    if (pad > 0)
        delete[] pad_buf;

    return 0;
}


