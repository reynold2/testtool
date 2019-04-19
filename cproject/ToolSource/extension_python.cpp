#include<extension_python.h>

CplusUsePython::CplusUsePython()
{

}

CplusUsePython::~CplusUsePython()
{
    if (Py_IsInitialized()) {
        if (pName) Py_DECREF(pName);
        if (pArgs) Py_DECREF(pArgs);
        if (pModule) Py_DECREF(pModule);
        if (pFunc) Py_DECREF(pFunc);
        if (pClass) Py_DECREF(pClass);
        if (pInstance) Py_DECREF(pInstance);
        Py_Finalize();
    }
}

//************************************
// 函数名称: init
// 函数说明：初始化相关操作
// 返 回 值: int
// 参    数: const string pyFilePath
// 参    数: const string pyFileNameNoSuffix
// 作    者：ISmileLi
// 作成日期：2018/11/25
// 修改记录：
//************************************
int CplusUsePython::init(const string pyFilePath, const string pyFileNameNoSuffix)
{
    int ret = 0;
    if (pyFilePath.empty() || pyFileNameNoSuffix.empty())
        return -1;
    Py_Initialize();
    pName = NULL;
    pModule = NULL;
    pFunc = NULL;
    pArgs = NULL;
    pClass = NULL;
    pInstance = NULL;
    // 判断初始化是否成功
//    if (!Py_IsInitialized())
//        return -2;
//    // 调用python中需要使用的模块
//    ret = PyRun_SimpleString("import sys");
//    if (ret != 0)
//    {
//        // 导入失败，关闭python调用
//        Py_Finalize();
//        return -3;
//    }
//    // 导入python文件的相关操作
//    if (ret == 0)
//    {
//        ret = PyRun_SimpleString("sys.path.append('./')");
//    }
//    if (ret != 0)
//    {
//        Py_Finalize();
//        return -4;
//    }
//    pModule = PyImport_Import(pyFileNameNoSuffix.c_str());
//    if (!pModule)
//    {
//        Py_Finalize();
//        return -5;
//    }

    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('./')");
    pModule = PyImport_ImportModule("pythontest");
    if (!pModule)
    {
        cout << "Import Module Failed" << endl;
        system("pause");
        return 0;
    }
    return 0;
}

//************************************
// 函数名称: CCallClassFunc
// 函数说明：C++调用python类中的函数
// 返 回 值: int
// 参    数: const string pyFuncName
// 参    数: const string name
// 参    数: const string age
// 作    者：ISmileLi
// 作成日期：2018/11/25
// 修改记录：
//************************************
int CplusUsePython::CCallClassFunc(const string pyFuncName,const string name, const int age)
{
    if (pyFuncName.empty() || name.empty() || age <= 0)
    {
        return -1;
    }


    // 向Python传参数是以元组（tuple）的方式传递的
    pArgs = PyTuple_New(2);
    //  PyObject* Py_BuildValue(char *format, ...) 将C++的变量转换成一个Python对象
    //  s 表示字符串，i 表示整型变量，f 表示浮点数
    PyTuple_SetItem(pArgs, 0, Py_BuildValue("s", name.c_str()));
    PyTuple_SetItem(pArgs, 1, Py_BuildValue("i", age));

    // 增加支持调用类中方法的操作
    pClass = PyObject_GetAttrString(pModule,"ISmileLi"); // DrawPic为类的名字
    if(!pClass)
    {
        return -2;
    }

    // 传入python构造函数中的两个参数
  //  pInstance = PyInstance_New(pClass,pArgs,NULL);
    pInstance = PyEval_CallObject(pClass,pArgs);

    if(!pInstance)
    {
        return -3;
    }
    // 调用类中的函数
    pFunc = PyObject_CallMethod(pInstance,(char*)pyFuncName.c_str(),NULL,NULL);
    if(!pFunc)
    {
        return -4;
    }

    return 0;
}
