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
    AllFileListPath_Main.clear();
    filetool->QfileListAll(CurrentDirPath);    
    AllFileListPath_Main=filetool->GetAllFileListPath();

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

    AllFileListPath_Main.values().clear();
    filetool->QfileListAll(CurrentDirPath);
    AllFileListPath_Main=filetool->GetAllFileListPath();

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

    string CurrentFilepath_s=CurrentFilepath.toStdString();
    string Source_s=ui->Edit_Source->text().toStdString();
    string Target_s=ui->Edit_Target->text().toStdString();
    int int_Suffix=ui->ComboBox_Suffix->currentIndex();
    string classname;
    string classfuns;
    try
    {
    string pyFilePath = "/script";
    int ret = CplusUsePython::instance()->init(pyFilePath,"fileOperation");
    if(ret != 0)
    {
        cout << "init failure!" << endl;
    }

    switch(int_Suffix)
    {
        case 2:
             classname="RemoteWord";
             classfuns="word_replace";
             qDebug()<<"11111";

     qDebug()<< AllFileListPath_Main.value("docx")<<"ss"<<endl;
             ret = CplusUsePython::instance()->CCallClassFunc(classname,classfuns,CurrentFilepath_s,Source_s,Target_s);

        case 5:
             classname="RemoteExcel";
             classfuns="re_Excel";

             ret = CplusUsePython::instance()->CCallClassFunc(classname,classfuns,CurrentFilepath_s,Source_s,Target_s);

    }

    }
    catch(...){
        qDebug()<< "调用外部工具出错";
    }

}

//void MainWindow::on_progressBar_valueChanged(int value)
//{

//}

void MainWindow::showMsg(const QString &msg)
{
    qDebug()<< msg;
}
