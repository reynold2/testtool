/*
 #include "mainwindow.h"
#include <QApplication>
#include <extension_python.h>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.show();

//    Extension_Python test=new Extension_Python();


    return a.exec();
}

*/
#include "math.h"
#include <Python.h>
#include <iostream>
#include <string>
#include "extension_python.h"

using namespace std;

int main ()
{
    // C++和python相互调用的相关接口查询https://docs.python.org/2/index.html
    string pyFilePath = "/work/test/testC++/test_C_use_Python";
    int ret = CplusUsePython::instance()->init(pyFilePath,"ISmileLi");
    if(ret != 0)
    {
        cout << "init failure!" << endl;
    }

//    ret = CplusUsePython::instance()->CCallFunction("print_message","this is test C++ use python!");

//    ret = CplusUsePython::instance()->CCallClassFunc("print_name","LiSa",18);
//    ret = CplusUsePython::instance()->CCallClassFunc("print_age","LiSa",18);
//    ret = CplusUsePython::instance()->CCallClassFunc("print_name_age","LiSa",18);

    return 0;
}
