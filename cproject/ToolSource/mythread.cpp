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

