#ifndef EXTENSION_PYTHON_H
#define EXTENSION_PYTHON_H
#include "math.h"
#include <Python.h>
#include <iostream>
#include<direct.h>
#include <iomanip>
#include<QDebug>
#include<QTime>
using namespace std;
class CplusUsePython
{
public:
    CplusUsePython();
    ~CplusUsePython();

    static CplusUsePython* instance()
    {
        static CplusUsePython instance;
        return &instance;
    }

    // 初始化相关操作
    int init(const string pyFilePath, const string pyFileNameNoSuffix);
    // C++调用python类中的函数
    int CCallClassFunc(const string pyclassName,const string pyFuncName,const string filepath, const string oldname, const string newname);


    char* zhuanhuan(string src);



private:
    PyObject *pName;
    PyObject *pModule;
    PyObject *pFunc;
    PyObject *pArgsinit;
    PyObject *pArgsfunc;
    PyObject *pClass;
    PyObject *pInstance;
    PyObject *result;
    PyObject *pDict;
public:
    bool stuate;
    double timeall;

};

#endif // CPLUSUSEPYTHON_H
