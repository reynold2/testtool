#include "documentoperation.h"



DocumentOperation::DocumentOperation()
{

}
void DocumentOperation::QfileListAll(QString path)
{
QDir dir(path);
    if(!dir.exists())
    {
        qDebug()<<"error:dirpath not exists";
        return;
    }
    dir.setFilter(QDir::Files | QDir::NoSymLinks);
    QFileInfoList list = dir.entryInfoList();
    //前面都是判断路径是否ok
    int file_count = list.count();
    if(file_count <= 0)
    {
         qDebug()<<"error:file is empty";//文件名字
        return;
    }
    for(int i=0; i<file_count; i++)//获取当前路径的文件
    {
        QFileInfo file_info = list.at(i);
       // qDebug()<<file_info.fileName();//文件名字
        QString suffix = file_info.suffix();//类型名字
       // qDebug()<<suffix;
        QString absolute_file_path = file_info.absoluteFilePath();//文件路径加名字
        QVector < QString >m_vector = AllFileListPath.value(suffix);
       //m_vector.push_back(file_info.fileName());//传入的是文件名字如果要是全路径见下面注释代码
        m_vector.push_back(absolute_file_path);
        AllFileListPath.insert(suffix,m_vector);//主键值为类型名字，里面value为里面所有的同类型名字
    }
}

void DocumentOperation::QfileRename(QString suffixs,QString soures,QString target)
{
    QMap<QString,QVector< QString >>::Iterator  it;
    for(it = AllFileListPath.begin();it != AllFileListPath.end();++it)//迭代器遍历
    {
//    qDebug()<<(*it);
//    qDebug()<<it.key();
    if(QString::compare(it.key(),suffixs)==0)
        {
        for(int j=0;j<it.value().count();j++)//C语言写法遍历
            {    

            oldfilenamepath =it.value().at(j);//at取出来的值为const，不可更改，迭代器可以更改

//            string oldname=string((const char *)(it.value().at(j)).toLocal8Bit());
//            string newname=string((const char *)(oldfilenamepath.replace(soures,target)).toLocal8Bit());
//            int c=rename(oldname.c_str(), newname.c_str());
           int c=QFile::rename(it.value().at(j),oldfilenamepath.replace(soures,target));

            if( c==0)
            {
                qDebug()<<"文件替换失败:" <<it.value().at(j)<<endl;
            }
            else
            {
                qDebug()<<"文件替换成功:" <<oldfilenamepath.replace(soures,target)<<endl;

            }
            }
        }
    else
        {
            qDebug()<< it.value();
        }
    }
}

QMap<QString, QVector<QString> > DocumentOperation::GetAllFileListPath()
{
    return AllFileListPath;
}
DocumentOperation::~DocumentOperation()
{

}

//string &DocumentOperation::replace_all(string &str, const string &old_value, const string &new_value)
//{
//        try
//        {
//            for (std::string::size_type pos(0); pos != std::string::npos; pos += new_value.length())
//            {

//                if ((pos = str.find(old_value, pos)) != std::string::npos)
//                {
//                    str.replace(pos, old_value.length(), new_value);

//                }
//                else {
//                    break;
//                }
//            }
//        }
//        catch (std::exception e)
//        {
//            printf("exception:String substitution exception");
//        }
//        return  str;
//}


//void DocumentOperation::setvector()
//{
//   //将文件名列表放入vector容器中进行储存
//        _finddata_t file;
//        s_dirpath=this->dirpath.toStdString();
//        s_suffixs=this->suffixs.toStdString();
//        s_soures = string((const char *)soures.toLocal8Bit());
//        s_target = string((const char *)target.toLocal8Bit());
//        long handle;

//        if ((handle = _findfirst((s_dirpath+s_suffixs).c_str(), &file)) ==-1l)
//        {
//            cout<<"File not found!\n"<<s_dirpath<<endl;
//        }
//        else
//        {
//            do {
//                string str(file.name);

//                this->fileNameList.push_back(str);
//            }while(_findnext(handle, &file) == 0);
//        }
//        _findclose(handle);
//}

//vector<string>  DocumentOperation::file_operator()
//{
//    //遍历文件名向量，并进行修改
//    vector<string> file_operator1;
//    for (vector<string>::iterator iter = this->fileNameList.begin(); iter != this->fileNameList.end(); ++iter)
//    {
//        string vector_filename = (*iter);
//        string oldName = s_dirpath+vector_filename;
//        string newfilename=DocumentOperation::replace_all(vector_filename,s_soures,s_target);
//        string newName = s_dirpath+newfilename;
//        int c=rename(oldName.c_str(), newName.c_str());
//        file_operator1.push_back(newName);
//        if ( c == 0 )
//           puts ( "File  renamed" );
//            qDebug()<<QString::fromLocal8Bit(newfilename.c_str())<<endl;

//        else
//            perror( "Error renaming file" );
//    }
//    return file_operator1;
//}
