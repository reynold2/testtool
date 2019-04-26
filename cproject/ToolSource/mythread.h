#ifndef MYTHREAD_H
#define MYTHREAD_H

#include <QThread>

class MyThread : public QThread
{
    Q_OBJECT
public:
    explicit MyThread(QObject *parent = 0);

protected:
    void run();

signals:
    void requestMsg(const QString &msg);

public slots:
public:
//    void setvector(const vector<string>* pvec);
//    void setdata(const string &x, const string &y, const string &z, const string &m);

private:
    //父对象

//    vector<string>* filenamepath;
    int runnableID;

//    string Sourcex;
//    string Targetx;
//    string classname;
//    string classfuns;

};

#endif // MYTHREAD_H
