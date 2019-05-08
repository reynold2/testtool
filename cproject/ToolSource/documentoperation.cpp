#include "documentoperation.h"

DocumentOperation::DocumentOperation()
{

}
void DocumentOperation::QfileListAll(QString path1)
{
if (!AllFileListPath.isEmpty())
{
    AllFileListPath.clear();
}
this->path=path1;
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
                qDebug()<<"File replacement failed:" <<it.value().at(j)<<endl;
            }
            else
            {

                qDebug()<<"File replaced successfully:" <<oldfilenamepath.replace(soures,target)<<endl;

            }
            }
        }

    else
        {
            qDebug()<< it.value();
        }
    }
    AllFileListPath.clear();
    this->QfileListAll(this->path);
//    qDebug()<<7<<AllFileListPath.values();

}

QMap<QString, QVector<QString> > DocumentOperation::GetAllFileListPath()
{
    return AllFileListPath;
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

