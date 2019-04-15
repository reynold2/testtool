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

#include"msword.h"
using namespace std;
class DocumentOperation
{
public:

     DocumentOperation(QString dirpath,QString suffixs,QString soures,QString target,bool x);

    ~DocumentOperation();

     std::string& replace_all(std::string& str, const std::string& old_value, const std::string& new_value);

private:
    QString dirpath;
    QString suffixs;
    QString soures;
    QString target;
    bool state ;
    vector<string> fileNameList;

    string s_dirpath;
    string s_suffixs;
    string s_soures;
    string s_target;
private :
    void setvector();

public:
    bool file_operator();


};

#endif // DOCUMENTOPERATION_H
