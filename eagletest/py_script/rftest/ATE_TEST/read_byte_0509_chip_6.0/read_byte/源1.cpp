#include<Python.h>//ǰ��������һ�����ö���Ϊ�˵������ͷ�ļ�����ؿ�
#include<iostream>
using namespace std;

int main()
{
    Py_Initialize();//ʹ��python֮ǰ��Ҫ����Py_Initialize();����������г�ʼ��
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('./')");

    PyObject * pModule = NULL, * first = NULL, * second = NULL;//��������

    pModule =PyImport_ImportModule("add_item");//������Ҫ���õ��ļ���

	//�޲�������
	second= PyObject_GetAttrString(pModule, "show");//������Ҫ���õĺ�����
	PyEval_CallObject(second, NULL);//���ú���
	
	//�в�����������
	//PyObject* pDict = PyModule_GetDict(pModule);
	first= PyObject_GetAttrString(pModule, "add_item");//������Ҫ���õĺ�����

	
	PyObject * pArgs = NULL, * pList = NULL;
	//�����б�
	pList = PyList_New(2);
	PyList_SetItem(pList, 0, Py_BuildValue("s",x_name));
	PyList_SetItem(pList, 1, Py_BuildValue("s",y_name));
	PyList_Append(pList, Py_BuildValue("s", "the third"));
	//�����ֵ�
	PyObject* pDict = PyDict_New();
	PyDict_SetItemString(pDict, "first", Py_BuildValue("i", 1));
	PyDict_SetItemString(pDict, "second", Py_BuildValue("i", 1));
	//���ò�������Ԫ���װ
	pArgs = PyTuple_New(2);
	PyTuple_SetItem(pArgs, 0, pList);
	PyTuple_SetItem(pArgs, 1, pDict);
	
    PyEval_CallObject(first, pArgs);//���ú���

	//PyEval_CallObject(first,NULL);
    Py_Finalize();//����Py_Finalize�������Py_Initialize���Ӧ�ġ�
	system("pause");
    return 0;
}