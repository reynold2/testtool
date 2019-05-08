#include<extension_python.h>

CplusUsePython::CplusUsePython()
{

}

CplusUsePython::~CplusUsePython()
{
    if (Py_IsInitialized()) {
        if (pName) Py_DECREF(pName);
        if (pArgsinit) Py_DECREF(pArgsinit);
        if (pArgsfunc) Py_DECREF(pArgsfunc);
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
// 修改记录：
//************************************
int CplusUsePython::init(const string pyFilePath, const string pyFileNameNoSuffix)
{
    int ret = 0;
    if (pyFilePath.empty() || pyFileNameNoSuffix.empty())
        return -1;
    Py_Initialize();
    pDict=NULL;
    pName = NULL;
    pModule = NULL;
    pFunc = NULL;
    pArgsinit = NULL;
    pArgsfunc = NULL;
    pClass = NULL;
    pInstance = NULL;
    result = NULL;


     //判断初始化是否成功
    if (!Py_IsInitialized())
        return -2;
    // 调用python中需要使用的模块
    ret = PyRun_SimpleString("import sys");
    if (ret != 0)
    {
        // 导入失败，关闭python调用
        Py_Finalize();
        return -3;
    }

    // 导入python文件的相关操作
    ret = PyRun_SimpleString(pyFilePath.c_str());
    if (ret != 0)
    {
        ret = PyRun_SimpleString("sys.path.append('./')");
        cout<<"Find alternate script paths"<<endl;
        if (ret != 0)
        {
            Py_Finalize();
            return -4;
        }
    }

      pModule = PyImport_ImportModule(pyFileNameNoSuffix.c_str());
 //   pModule = PyImport_Import(pyFileNameNoSuffix.c_str());
    if (!pModule)
    {
        cout <<  pyFileNameNoSuffix << endl;
        Py_Finalize();
        return -5;
    }

    return 0;
}
//************************************
// 函数名称: CCallClassFunc
// 函数说明：c++函数调用
// 返 回 值: int
// 参    数: const string filepath
// 参    数: const string oldname
// 参    数: const string newname
// 修改记录：
//************************************

int CplusUsePython::CCallClassFunc(const string pyclassName,const string pyFuncName,const string filepath, const string oldname, const string newname)
{
//    if (pyFuncName.empty() || pyclassName.empty())
//    {
//        return -1;
//    }


//    // 向Python传参数是以元组（tuple）的方式传递的
////    pArgsinit = PyTuple_New(1);
//    //  PyObject* Py_BuildValue(char *format, ...) 将C++的变量转换成一个Python对象
//    //  s 表示字符串，i 表示整型变量，f 表示浮点数
////    PyTuple_SetItem(pArgsinit, 0, Py_BuildValue("s", ));

//    // 增加支持调用类中方法的操作

//    pDict = PyModule_GetDict(pModule);
//    pClass = PyDict_GetItemString(pDict, "RemoteWord");
////    pClass = PyObject_GetAttrString(pModule,""); // pyclassName为类的名字
//    if(!pClass)
//    {
//      cout<<"查找类名出错"<<endl;
//        return -2;
//    }

//    // 传入python构造函数中的两个参数
//    pInstance = PyInstanceMethod_New(pClass);
////   pInstance = PyObject_CallObject(pClass,pArgsinit);

//    if(!pInstance)
//    {
//        cout<<"Class instantiation error"<<endl;
//        return -3;
//    }
//    // 调用类中的函数
////    pArgsfunc = PyTuple_New(2);
////    //  PyObject* Py_BuildValue(char *format, ...) 将C++的变量转换成一个Python对象
////    //  s 表示字符串，i 表示整型变量，f 表示浮点数
////    PyTuple_SetItem(pArgsfunc, 0, Py_BuildValue("s", oldname.c_str()));
////    PyTuple_SetItem(pArgsfunc, 1, Py_BuildValue("s", newname.c_str()));
////    pFunc = PyObject_CallMethod(pInstance,(char*)pyFuncName.c_str(),pArgsfunc);

//        pFunc = PyObject_CallMethod(pInstance,"word_replace","(s,s,s)","E:\\test\\wz.docx","av","ww");
////    pFunc = PyObject_CallMethod(pInstance,(char*)pyFuncName.c_str(),"(s,s,s)",(char*)filepath.c_str(),(char*)oldname.c_str(),(char*)newname.c_str() );
//    if(!pFunc)
//    {
//         cout<<"An error occurred calling the real column method"<<endl;
//        return -4;
//    }

        pArgsfunc = Py_BuildValue("(s,s,s)", (char*)filepath.c_str(),(char*)oldname.c_str(),(char*)newname.c_str());
        pFunc = PyObject_GetAttrString(pModule, "mianfile");
        if(!pFunc)
        {
             qDebug()<<"Error calling method"<<endl;
            return -4;
        }

        result=PyEval_CallObject(pFunc, pArgsfunc);
        int c=0 ;
           // 将 python 类型的返回值转换为 C/C++类型
        PyArg_Parse(result, "i", &c);
        qDebug() << "status code:" << c << endl;

        return 0;
}
//string转char数组c_str用来替换方法避免可能出现的中文乱码
char *CplusUsePython::zhuanhuan(string src)
{
        char *dst = new char[255];
        int i;
        for(i=0;i <=src.length();i++)
            dst[i]=src[i];
        dst[i] = '\0';
        return dst;
}




