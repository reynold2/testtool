#ifndef MYRUNNABLE_H
#define MYRUNNABLE_H

#include <QRunnable>
#include <QMetaObject>
#include<documentoperation.h>
#include<extension_python.h>

class MyRunnable : public QRunnable
{
public:
    MyRunnable(QObject *parent = 0);
    ~MyRunnable();

    void run();

    void setID(const int &id);
    //向外传送消息
    void requestMsg(const QString &msg);
    //向函数中传递路径
    void setfilepathvector(const vector<string> &pvec);
    void setdefault(const string &x, const string &y, const string &z, const string &m);

private:
    //父对象
    QObject *mParent;
    vector<string>*filenamepath;
    int runnableID;

    string Sourcex;
    string Targetx;
    string classname;
    string classfuns;
};

#endif // MYRUNNABLE_H
