#include "mainwindow.h"
MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)

{
    ui->setupUi(this);
    connect(ui->FileButton, SIGNAL(clicked()), this, SLOT(on_FileButton_clicked()),Qt::UniqueConnection);
    connect(ui->Button_FilePath, SIGNAL(clicked()), this, SLOT(on_Button_FilePath_clicked()),Qt::UniqueConnection);
    connect(ui->MianButton, SIGNAL(clicked()), this, SLOT(on_MianButton_clicked()),Qt::UniqueConnection);
    connect(&myThread,SIGNAL(requestMsg(const QString&)),this,SLOT(showMsg(const QString&)));

    filetool=new DocumentOperation();
    filetool->QfileListAll("DirPath");
    AllFileListPath_Main=filetool->GetAllFileListPath();
    qDebug()<<0<<AllFileListPath_Main.values();

}

MainWindow::~MainWindow()
{
    delete ui;
}
void MainWindow::on_Button_FilePath_clicked()
{
    QFileInfo fi;
    CurrentFilepath = QFileDialog::getOpenFileName(this);
    fi = QFileInfo(CurrentFilepath);
    if(ui->ComboBox_Suffix->findText(fi.completeSuffix()) == -1) // 针对addItem方法可避免重复添加
    {
       ui->ComboBox_Suffix->setCurrentText("*.*");
    }
    else
    {

       ui->ComboBox_Suffix->setCurrentText(fi.completeSuffix());
    }

    CurrentDirPath=fi.path()+"/";
    ui->Edit_Path->setText(CurrentDirPath);

    ui->ComboBox_Suffix->setEditable(false);
    CurrentSuffix=ui->ComboBox_Suffix->currentText();

    //获取全部文件路径
    this->_init_DocumentOperation();
    qDebug()<<1<<AllFileListPath_Main.values();

}

void MainWindow::on_FileButton_clicked()
{
    CurrentDirPath=ui->Edit_Path->text();
    CurrentSuffix=ui->ComboBox_Suffix->currentText();
    Source=ui->Edit_Source->text();
    Target=ui->Edit_Target->text();

    if(CurrentSuffix=="*.*")
    {
        int size=AllFileListPath_Main.keys().count();

        for(int i = 0; i<size; ++i)
        {
            QString Suffix_L=AllFileListPath_Main.keys()[i];
            filetool->QfileRename(Suffix_L,Source,Target);

        }

    }
    else{

        filetool->QfileRename(CurrentSuffix,Source,Target);

    }
    this->_init_DocumentOperation();

    qDebug()<<3<<AllFileListPath_Main.values();

//    AllFileListPath_Main.values().clear();
//    filetool->QfileListAll(CurrentDirPath);
//    AllFileListPath_Main=filetool->GetAllFileListPath();

//    DocumentOperation *filetool= new DocumentOperation(Path,Suffix,Source,Target,false);
//    this->FileNamePath=filetool->fileNameList;
//    int int_Suffix=ui->ComboBox_Suffix->currentIndex();
//    cout<<int_Suffix<<endl;
//    switch(int_Suffix)
//    {
//        case 1:
//            WordFileNamePath_docx=filetool->file_operator();
//        case 2:
//            ExcelFileNamePath_xlsx=filetool->file_operator();
//        default:
//            this->FileNamePath=filetool->file_operator();

//    }

}



void MainWindow::on_MianButton_clicked()
{

//        myThread.setdata(classname,classfuns,Sourcex,Targetx);
//        MyThread.setvector(WordFileNamePath_docx);
        myThread.start();
}

void MainWindow::on_ContextButton_clicked()
{

//   string CurrentFilepath_s=CurrentFilepath.toStdString();
//    string Source_s=ui->Edit_Source->text().toLocal8Bit().toStdString();
//    string Target_s=ui->Edit_Target->text().toLocal8Bit().toStdString();
//    int int_Suffix=ui->ComboBox_Suffix->currentIndex();

//    string classname_Word="RemoteWord";
//    string classfuns_Word="word_replace";


//    string classname_Excel="RemoteExcel";
//    string classfuns_Excel="re_Excel";


//    try
//    {
//    string pyFilePath = "/script";
//    int ret = CplusUsePython::instance()->init(pyFilePath,"fileOperation");
//    if(ret != 0)
//        {
//        cout << "init failure!" << endl;
//        }

//    if(int_Suffix==2)
//        {
//            QVector <QString> docx_value=AllFileListPath_Main.value("docx");
//             for(int j=0;j<docx_value.count();j++)
//             {
//                 QString path2=docx_value[j];
//                 CplusUsePython::instance()->CCallClassFunc(classname_Word,classfuns_Word,path2.toStdString(),Source_s,Target_s);
//             }
//        }
//    else if( int_Suffix==5)
//        {
//            QVector <QString> xlsx_value=AllFileListPath_Main.value("xlsx");
//             for(int j=0;j<xlsx_value.count();j++)
//             {
//                 QString path5=xlsx_value[j];
//                  CplusUsePython::instance()->CCallClassFunc(classname_Excel,classfuns_Excel,path5.toStdString(),Source_s,Target_s);
//             }
//        }
//    else if( int_Suffix==0)
//        {
//         QVector <QString> docx_value1=AllFileListPath_Main.value("docx");
//            for(int j=0;j<docx_value1.count();j++)
//           {
//                    string path20=docx_value1[j].toLocal8Bit().toStdString();;
//                 CplusUsePython::instance()->CCallClassFunc(classname_Word,classfuns_Word,path20,Source_s,Target_s);
//            }

//              QVector <QString> xlsx_value1=AllFileListPath_Main.value("xlsx");
//             for(int j=0;j<xlsx_value1.count();j++)
//             {
//                   QString x = xlsx_value1[0];
//                   string path50=x.toLocal8Bit().toStdString();;
//                    cout<<path50<<endl;
//                    cout<<Source_s<<endl;
//                    cout<<Target_s<<endl;
//                    cout<<classname_Excel<<endl;
//                    cout<<classfuns_Excel<<endl;

//                  CplusUsePython::instance()->CCallClassFunc(classname_Excel,classfuns_Excel,path50,Source_s,Target_s);
//             }
//        }
//    else
//        {
//           // 当上面条件都不为真时执行
//        }

//    }
//    catch(...){
//        qDebug()<< "调用外部工具出错";
//    }


    string Sourcex=ui->Edit_Source->text().toStdString();
       string Targetx=ui->Edit_Target->text().toStdString();
       int int_Suffix=ui->ComboBox_Suffix->currentIndex();
       cout<<int_Suffix<<endl;
       string pyFilePath = "/script";
       int ret = CplusUsePython::instance()->init(pyFilePath,"fileOperation");
       if(ret != 0)
       {
           cout << "init failure!" << endl;
       }

       switch(int_Suffix)
       {
           case 2:
                ret = CplusUsePython::instance()->CCallClassFunc("RemoteWord","word_replace",CurrentFilepath.toLocal8Bit().toStdString(),Sourcex,Targetx);

           case 5:
                ret = CplusUsePython::instance()->CCallClassFunc("RemoteExcel","re_Excel",CurrentFilepath.toLocal8Bit().toStdString(),Sourcex,Targetx);

       }
}

//void MainWindow::on_progressBar_valueChanged(int value)
//{

//}

void MainWindow::showMsg(const QString &msg)
{
    qDebug()<< msg;
}

void MainWindow::_init_DocumentOperation()
{
    AllFileListPath_Main.clear();
    AllFileListPath_Main=filetool->GetAllFileListPath();
}
