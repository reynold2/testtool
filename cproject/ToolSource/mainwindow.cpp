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

    MainWindow::stringSpilt();
    filetool=new DocumentOperation();
    int ret = CplusUsePython::instance()->init(exepath,"fileOperation");
    if(ret != 0)
    {
        qDebug() << "script init failure!" << endl;
    }

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

    //获取全部文件路径判断是否AllFileListPath_Main是否初始化
    filetool->QfileListAll(CurrentDirPath);
    AllFileListPath_Main=filetool->GetAllFileListPath();

//    qDebug()<<AllFileListPath_Main.values();
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
      AllFileListPath_Main=filetool->GetAllFileListPath();
      qDebug()<<8<<AllFileListPath_Main.values();


}



void MainWindow::on_MianButton_clicked()
{

        myThread.start();
}

void MainWindow::on_ContextButton_clicked()
{

    string CurrentFilepath_s=CurrentFilepath.toStdString();
    string Source_s=ui->Edit_Source->text().toStdString();
    string Target_s=ui->Edit_Target->text().toStdString();
    string Standby_Mode=ui->ComboBox_Suffix->currentText().toStdString();
    try
    {
        if(Standby_Mode=="*.*")
    {
    QMap<QString,QVector< QString >>::Iterator  it;
        for(it = AllFileListPath_Main.begin();it != AllFileListPath_Main.end();++it)
        {
            for(int j=0;j<it.value().count();j++)
            {
                string CurrentFilepath_local= it.value().at(j).toStdString();
                QThread::sleep(3);
                int ret = CplusUsePython::instance()->CCallClassFunc("classname","classfuns",CurrentFilepath_local,Source_s,Target_s);

            }

        }
    }
    else{
        int ret = CplusUsePython::instance()->CCallClassFunc("classname","classfuns",CurrentFilepath_s,Source_s,Target_s);
    }

    }
    catch(...){
        qDebug()<< "Error calling external tool";
    }

}

//void MainWindow::on_progressBar_valueChanged(int value)
//{

//}

void MainWindow::showMsg(const QString &msg)
{
    qDebug()<< msg;
}

void MainWindow::stringSpilt()
{
    char buffer[_MAX_PATH];
    _getcwd(buffer,_MAX_PATH);
    string m=buffer;
    DocumentOperation::replace_all(m,"\\","/");
    QString z=QString::fromStdString(m);
    QString str1=QString("sys.path.append('%1')").arg(z);
    exepath=str1.toStdString();
}
