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
}

void MyRunnable::setID(const int &id)
{
    runnableID = id;
}

void MyRunnable::requestMsg(const QString &msg)
{
    QMetaObject::invokeMethod(mParent, "requestMsg", Qt::QueuedConnection, Q_ARG(QString, msg));
}

void MyRunnable::run()
{
    for(int i = 0;i < 10;i++)
    {
        requestMsg(QString("this is a MyRunnable %1").arg(runnableID));
        QThread::sleep(1);
    }
}
