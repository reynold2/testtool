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
    // C++调用python函数
//    int CCallFunction(const string pyFuncName, const string message);
    // C++调用python类中的函数
    int CCallClassFunc(const string pyFuncName, const string name, const int age);

private:
    PyObject *pName;
    PyObject *pModule;
    PyObject *pFunc;
    PyObject *pArgs;
    PyObject *pClass;
    PyObject *pInstance;
};

#endif // CPLUSUSEPYTHON_H
