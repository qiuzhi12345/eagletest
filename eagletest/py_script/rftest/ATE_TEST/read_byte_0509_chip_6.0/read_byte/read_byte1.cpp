/*

#include "iostream"
#include "ate_test_result_check.h"
#include <string>

using namespace std;

int main()
{ char list[512];
for(int j=0;j<512;j++)
{
	list[j]=2;
}
char a;
a=1;

ate_check(list ,1);
	int i=0;
	cout<<"test...."<<endl;
	cin>>i;
	return 0;

}*/

#define CONVERT_EN




#include <stdlib.h>
#include "ate_test_result_check.h"

#include <windows.h>
#include   <iostream>  
#include <fstream>
 #include   <io.h>  
 #include   <direct.h>  
 #include   <string>  
 #include   <vector>  
 #include   <iomanip>  
 #include   <ctime>  
 using   namespace   std;  
 
 void getFiles( string, vector<string>& );
 unsigned char get_0x_num(char h,char l);
 int get_0x(char s);
void process_byte(string source,string foldername,string targetname );


double DVDD_testV_1[2];
double VDD_RTC_testV_1[2];
double DVDD_testV_2[2];
double VDD_RTC_testV_2[2];
double LightSleep_IDD_VBAT[2];
double LightSleep_IDD_DVDD_IO[2];
double Chip_PD_IDD_VBAT[2];
double Chip_PD_IDD_DVDD_IO[2];
double DeepSleep_IDD_VBAT[2];
double DeepSleep_IDD_DVDD_IO[2];
double DynamicIDD_VBAT[2];
double DynamicIDD_DVDD_IO[2];



const char* log_name;



int   main()  
{  

	int pos=0;
	int fnum=0;
	int aaa=0;
	//int file_cnt=0;
	string fname;
	string path;


    vector<string>   files;  
	string ntmp;
	//cout<<"Please enter the folder path: "<<endl;
	//cin>>path;
	path=".";
    //getFiles( ".", files );
	getFiles(path,files);


     // print the files get
    for   (int   j=0;   j<files.size();   ++j) 
	{
        //cout   <<   files[j] << endl; 
		ntmp=files[j];


		//if(ntmp=="./Capdata_01.txt")
		if((ntmp.find(".txt",0)<ntmp.length())||(ntmp.find(".log",0)<ntmp.length()) )
		{
			//cout<<"tttttttttttttttttt"<<endl;
			pos=ntmp.find_last_of("/");
			////cout<<"files[j];   "<<ntmp<<endl;
			fname=ntmp.substr(pos,ntmp.length()-pos);
			//cout<<"fname:   "<<fname<<endl;

			process_byte(ntmp,"./ReadByteLog","./ReadByteLog"+fname);
			//cout<<"test after ate.h"<<endl;
			fnum++;
		}

    }
	cout<<fnum<<" files read..."<<endl;
	cout<<"continue..."<<endl;
	cout<<"Press any key to exit..."<<endl;		
	 cin.get();
	 cin.get();
		return   0;  
}
	



void process_byte(string source,string foldername,string targetname )
{
//string s="./Capdata_01.txt";
	//char* fpath="./Capdata_01.txt";
const char* fpath=source.data();
const char* folder=foldername.data();
const char* target=targetname.data();
	string lines;
	ifstream in(fpath);
	const int data_num=2000;
	const int float_data_num=10;

	int st_flg=1;//  1:start with the beginning ; 0:start when meeting the flg;
	int cnt=0;



	unsigned char data_list[data_num]={0};  //begin with 0
	float fdata[float_data_num]={0.0};
    



	const int LEN=100;
	char str[LEN];
	while(in.getline(str,LEN))


	{//cout<<"read from line:"<<str<<endl;
		//cout<<"test st_flg : "<<st_flg<<endl;
		 if(str[0]=='0'&& st_flg==0) 
			 {st_flg=1;
			 }
		 else if((st_flg==1) &&( cnt<data_num))
			 {   //cout<<"data_list assign.."<<endl;
				 data_list[cnt]=get_0x_num(str[0],str[1]);
				 
				 cnt++;
			 }
		 else if((st_flg==1)&&(cnt>=data_num)&&(cnt<data_num+float_data_num))
			 {
				 fdata[cnt-data_num]=atof(str);
				 //cout<<"fdata["<<cnt-data_num<<"]"<<fdata[cnt-data_num]<<endl;
				 cnt++;
			 }
		 else
			 { //cout<<"finished....cnt:"<<cnt<<endl;
			 }

	}
	in.close();

	DVDD_testV_1[1]=fdata[0];
    VDD_RTC_testV_1[1]=fdata[1];
    DVDD_testV_2[1]=fdata[2];
    VDD_RTC_testV_2[1]=fdata[3];
    LightSleep_IDD_VBAT[1]=fdata[4];
    LightSleep_IDD_DVDD_IO[1]=fdata[5];
	Chip_PD_IDD_VBAT[1]=fdata[6];
	Chip_PD_IDD_DVDD_IO[1]=fdata[7];

   // DeepSleep_IDD_VBAT[1]=fdata[6];
    //DeepSleep_IDD_DVDD_IO[1]=fdata[7];
    DynamicIDD_VBAT[1]=fdata[8];
    DynamicIDD_DVDD_IO[1]=fdata[9];
	/*
	unsigned char data_list[512]={0};
	for(int k=0;k<512;k++)
		data_list[k]=0xff;
		*/
    //ofstream fout("test2.txt");
	log_name=target;
CreateDirectory(folder,NULL);
	ate_check(data_list,1);
	//fout.close();
}
       



unsigned char get_0x_num(char h,char l)
{ 
	int high,low;
	unsigned char num;
  high=get_0x(h);
  low=get_0x(l);
  num=(high<<4)| low;
  return num;




}
int get_0x(char s)
{
	switch(s)
	{
	case ' ': return 0x0;
	case '0': return 0x0;
	case '1': return 0x1;
	case '2': return 0x2;
	case '3': return 0x3;
	case '4': return 0x4;
	case '5': return 0x5;
	case '6': return 0x6;
	case '7': return 0x7;
	case '8': return 0x8;
	case '9': return 0x9;
	case 'a': return 0xa;
	case 'b': return 0xb;
	case 'c': return 0xc;
	case 'd': return 0xd;
	case 'e': return 0xe;
	case 'f': return 0xf;
	case 'A': return 0xa;
	case 'B': return 0xb;
	case 'C': return 0xc;
	case 'D': return 0xd;
	case 'E': return 0xe;
	case 'F': return 0xf;
	default: cout<<"read error when get 0x..."<<" :  ["<<s<<"]"<<endl;
	}
}

void getFiles( string path, vector<string>& files ) {
    //文件句柄  
    long   hFile   =   0;  
    //文件信息  
    struct _finddata_t fileinfo;  

    string p;

    if   ((hFile   =   _findfirst(p.assign(path).append("/*").c_str(),&fileinfo))   !=   -1)  {  

        do  {  
            //如果是目录,迭代之
            //如果不是,加入列表
            if   ((fileinfo.attrib   &   _A_SUBDIR)) {  
                if   (strcmp(fileinfo.name,".")   !=   0   &&   strcmp(fileinfo.name,"..")   !=   0)  
                    getFiles(   p.assign(path).append("/").append(fileinfo.name), files   );  
					  //不读取子目录
            }  else  {  
                files.push_back(   p.assign(path).append("/").append(fileinfo.name)  );
            }  
        }   while   (_findnext(   hFile,   &fileinfo   )   ==   0);  

        _findclose(hFile);  
    }
}
