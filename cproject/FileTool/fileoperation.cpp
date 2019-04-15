#include <typeinfo>
#include"fileoperation.h"
using namespace std;
bool testfile(QString dirpath,QString suffixs,QString soures,QString target, bool x)
{
//将文件名列表放入vector容器中进行储存
    _finddata_t file;
    string s_dirpath;
    string s_suffixs;
    string s_soures;
    string s_target;
    s_dirpath=dirpath.toStdString();
    s_suffixs=suffixs.toStdString();
    s_soures = string((const char *)soures.toLocal8Bit());
    s_target = string((const char *)target.toLocal8Bit());
    long handle;
    vector<string> fileNameList;
    if ((handle = _findfirst((s_dirpath+s_suffixs).c_str(), &file)) ==-1l)
    {
        cout<<"File not found!\n"<<s_dirpath<<endl;
    }
    else
    {
        do {
            string str(file.name);
            fileNameList.push_back(str);
        }while(_findnext(handle, &file) == 0);
    }
    _findclose(handle);
//遍历文件名向量，并进行修改
    for (vector<string>::iterator iter = fileNameList.begin(); iter != fileNameList.end(); ++iter)
    {
        string vector_filename = (*iter);
        string oldName = s_dirpath+vector_filename;
        string newfilename=replace_all(vector_filename,s_soures,s_target);
        string newName = s_dirpath+newfilename;
        int c=rename(oldName.c_str(), newName.c_str());
        if ( c == 0 )
            puts ( "File  renamed" );
        else
            perror( "Error renaming file" );
    }
    return true;
}

//字符串替换的函数
std::string& replace_all(std::string& str, const std::string& old_value, const std::string& new_value)
{
    try
    {
        for (std::string::size_type pos(0); pos != std::string::npos; pos += new_value.length())
        {

            if ((pos = str.find(old_value, pos)) != std::string::npos)
            {
                str.replace(pos, old_value.length(), new_value);

            }
            else {
                break;
            }
        }
    }
    catch (std::exception e)
    {
        qDebug()<<"进入异常";
    }
    return  str;
}
