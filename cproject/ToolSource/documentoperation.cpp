#include "documentoperation.h"



DocumentOperation::DocumentOperation(QString dirpath, QString  suffixs, QString soures, QString target, bool x)
{
    this->dirpath=dirpath;
    this->suffixs=suffixs;
    this->soures=soures;
    this->target=target;
    this->state =x;
    this->setvector();
}

DocumentOperation::~DocumentOperation()
{

}

string &DocumentOperation::replace_all(string &str, const string &old_value, const string &new_value)
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
            printf("exception:String substitution exception");
        }
        return  str;
}


void DocumentOperation::setvector()
{
   //将文件名列表放入vector容器中进行储存
        _finddata_t file;
        s_dirpath=this->dirpath.toStdString();
        s_suffixs=this->suffixs.toStdString();
        s_soures = string((const char *)soures.toLocal8Bit());
        s_target = string((const char *)target.toLocal8Bit());
        long handle;

        if ((handle = _findfirst((s_dirpath+s_suffixs).c_str(), &file)) ==-1l)
        {
            cout<<"File not found!\n"<<s_dirpath<<endl;
        }
        else
        {
            do {
                string str(file.name);

                this->fileNameList.push_back(str);
            }while(_findnext(handle, &file) == 0);
        }
        _findclose(handle);
}

vector<string>  DocumentOperation::file_operator()
{
    //遍历文件名向量，并进行修改
    vector<string> file_operator1;
    for (vector<string>::iterator iter = this->fileNameList.begin(); iter != this->fileNameList.end(); ++iter)
    {
        string vector_filename = (*iter);
        string oldName = s_dirpath+vector_filename;
        string newfilename=this->replace_all(vector_filename,s_soures,s_target);
        string newName = s_dirpath+newfilename;
        int c=rename(oldName.c_str(), newName.c_str());
        file_operator1.push_back(newName);
        if ( c == 0 )
//            puts ( "File  renamed" );
           qDebug()<<"修改成功："<<QString::fromLocal8Bit(newfilename.c_str())<<endl;
        else
            perror( "Error renaming file" );
    }
    return file_operator1;
}
