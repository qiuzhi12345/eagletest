#include<Python.h>//前面所做的一切配置都是为了调用这个头文件和相关库
#include<iostream>
using namespace std;

int main()
{
    Py_Initialize();//使用python之前，要调用Py_Initialize();这个函数进行初始化
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('./')");

    PyObject * pModule = NULL, * first = NULL, * second = NULL;//声明变量

    pModule =PyImport_ImportModule("add_item");//这里是要调用的文件名

	//无参数调用
	second= PyObject_GetAttrString(pModule, "show");//这里是要调用的函数名
	PyEval_CallObject(second, NULL);//调用函数
	
	//有参数函数调用
	//PyObject* pDict = PyModule_GetDict(pModule);
	first= PyObject_GetAttrString(pModule, "add_item");//这里是要调用的函数名

	
	PyObject * pArgs = NULL, * pList = NULL;
	//构造列表
	pList = PyList_New(2);
	PyList_SetItem(pList, 0, Py_BuildValue("s",x_name));
	PyList_SetItem(pList, 1, Py_BuildValue("s",y_name));
	PyList_Append(pList, Py_BuildValue("s", "the third"));
	//构造字典
	PyObject* pDict = PyDict_New();
	PyDict_SetItemString(pDict, "first", Py_BuildValue("i", 1));
	PyDict_SetItemString(pDict, "second", Py_BuildValue("i", 1));
	//设置参数，用元组封装
	pArgs = PyTuple_New(2);
	PyTuple_SetItem(pArgs, 0, pList);
	PyTuple_SetItem(pArgs, 1, pDict);
	
    PyEval_CallObject(first, pArgs);//调用函数

	//PyEval_CallObject(first,NULL);
    Py_Finalize();//调用Py_Finalize，这个根Py_Initialize相对应的。
	system("pause");
    return 0;
}