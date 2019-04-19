#ifndef MYRUNNABLE_H
#define MYRUNNABLE_H

#include <QRunnable>
#include <QMetaObject>

class MyRunnable : public QRunnable
{
public:
    MyRunnable(QObject *parent = 0);
    ~MyRunnable();

    void run();

    void setID(const int &id);
    //向外传送消息
    void requestMsg(const QString &msg);
private:
    //父对象
    QObject *mParent;

    int runnableID;
};

#endif // MYRUNNABLE_H
