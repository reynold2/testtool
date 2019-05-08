#ifndef DOCUMENTOPERATION_H
#define DOCUMENTOPERATION_H
#include <QString>
#include"QDebug"
#include <iostream>
#include <QString>
#include <io.h>
#include <stdlib.h>
#include <vector>
#include <iostream>
#include <QVector>
#include <QMap>
#include <QString>
#include <QDir>
#include <QFileInfoList>
#include <QStringList>
#include <QFileInfo>
#include <QFile>
#include <QDebug>


using namespace std;
class DocumentOperation
{
public:

     DocumentOperation();

    ~DocumentOperation();

private:

    QString oldfilenamepath;
    QString newfilenamepath;
    QMap< QString,QVector< QString >> AllFileListPath;
    QString path;
public:
    static std::string& replace_all(std::string& str, const std::string& old_value, const std::string& new_value);
    void QfileListAll(QString path1);
    void QfileRename(QString suffixs,QString soures,QString target);


    QMap< QString,QVector< QString >> GetAllFileListPath();
};

#endif // DOCUMENTOPERATION_H
