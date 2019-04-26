#include "myrunable.h"
#include <QDebug>
#include <QThread>
MyRunnable::MyRunnable(QObject *parent)
    : QRunnable()
{
    mParent = parent;


}

MyRunnable::~MyRunnable()
{
    runnableID = 0;
//    filenamepath->clear();

}

void MyRunnable::setID(const int &id)
{
    runnableID = id;

}

void MyRunnable::requestMsg(const QString &msg)
{
    QMetaObject::invokeMethod(mParent, "requestMsg", Qt::QueuedConnection, Q_ARG(QString, msg));
}

void MyRunnable::setfilepathvector(const vector<string>& pvec)
{

}

void MyRunnable::setdefault(const string &x, const string &y, const string &z, const string &m)
{
     Sourcex=z;
     Targetx=m;
     classname=x;
     classfuns=y;
}



void MyRunnable::run()
{

        requestMsg(QString("this is a MyRunnable %1").arg(runnableID));
        QThread::sleep(1);

//        string pyFilePath = "/script";
//        int ret = CplusUsePython::instance()->init(pyFilePath,"fileOperation");

//        if(ret != 0)
//        {
//            cout << "init failure!" << endl;
//        }

//        int count = filenamepath.size();
//        for (int i = 0; i < count;i++)
//        {
//            string vector_filename = (*iter);
//            ret = CplusUsePython::instance()->CCallClassFunc(classname,classfuns,vector_filename,Sourcex,Targetx);
//        }


}


