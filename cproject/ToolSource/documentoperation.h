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
public:
    QMap< QString,QVector< QString >> AllFileListPath;
    void QfileListAll(QString path);
    void QfileRename(QString suffixs,QString soures,QString target);
};

#endif // DOCUMENTOPERATION_H
