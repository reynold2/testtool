#ifndef EXTENSION_PYTHON_H
#define EXTENSION_PYTHON_H
#include "math.h"
#include <Python.h>
#include <iostream>
#include<QDebug>
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
};

#endif // CPLUSUSEPYTHON_H
