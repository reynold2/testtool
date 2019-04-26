#include "mythread.h"
#include <QThreadPool>
#include "myrunable.h"
#include <QDebug>
MyThread::MyThread(QObject *parent) :
    QThread(parent)
{
}

void MyThread::run()
{
    QThreadPool myPool;
    myPool.setMaxThreadCount(4);
    for(int i = 0;i < 4;i++)
    {
        MyRunnable *subThread = new MyRunnable(this);
        subThread->setID(i);
//        subThread->setdefault(classname,classfuns,Sourcex,Targetx);
//        subThread->setfilepathvector(filenamepath);
        myPool.start(subThread);
    }

    myPool.waitForDone();
}


//void MyThread::setvector(const vector<string> *pvec)
//{
//    filenamepath=pvec;
//}

//void MyThread::setdata(const string &x, const string &y, const string &z, const string &m)
//{
//     Sourcex=z;
//     Targetx=m;
//     classname=x;
//     classfuns=y;
//}
