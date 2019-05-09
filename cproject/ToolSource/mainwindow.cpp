#include "mainwindow.h"
MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)

{
    ui->setupUi(this);
    ui->ComboBox_Suffix->setEnabled(false);
    connect(ui->FileButton, SIGNAL(clicked()), this, SLOT(on_FileButton_clicked()),Qt::UniqueConnection);
    connect(ui->Button_FilePath, SIGNAL(clicked()), this, SLOT(on_Button_FilePath_clicked()),Qt::UniqueConnection);
    connect(ui->MianButton, SIGNAL(clicked()), this, SLOT(on_MianButton_clicked()),Qt::UniqueConnection);
    connect(&myThread,SIGNAL(requestMsg(const QString&)),this,SLOT(showMsg(const QString&)));

    MainWindow::stringSpilt();
    filetool=new DocumentOperation();
    int ret = usepython->instance()->init(exepath,"fileOperation");
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
    ui->ComboBox_Suffix->setEnabled(true);
//    qDebug()<<AllFileListPath_Main.values();
}

void MainWindow::on_FileButton_clicked()
{
    ui->FileButton->setEnabled(false);
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
     // qDebug()<<8<<AllFileListPath_Main.values();

    ui->FileButton->setEnabled(true);
}



void MainWindow::on_MianButton_clicked()
{
    this->on_FileButton_clicked();
    string Source_s=ui->Edit_Source->text().toStdString();
    string Target_s=ui->Edit_Target->text().toStdString();
    try
    {
    QMap<QString,QVector< QString >>::Iterator  it_mian;
        for(it_mian = AllFileListPath_Main.begin();it_mian != AllFileListPath_Main.end();++it_mian)
        {
            for(int j=0;j<it_mian.value().count();j++)
            {
                string CurrentFilepath_local= it_mian.value().at(j).toStdString();
                QFuture<void> future= QtConcurrent::run(this, &MainWindow::thread_context,CurrentFilepath_local,Source_s,Target_s);
            }

        }

    }
    catch(...){
        qDebug()<< "Error calling external tool";
    }
}

void MainWindow::on_ContextButton_clicked()
{
    ui->ContextButton->setDisabled(true);
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
                QThread::sleep(1);
                    do
                     {
                          qDebug()<<1<<usepython->stuate;
                         if(usepython->stuate)
                         {
                            qDebug()<<2<<usepython->stuate;
                            int ret = usepython->instance()->CCallClassFunc("classname","classfuns",CurrentFilepath_local,Source_s,Target_s);
                            qDebug()<<3<<usepython->timeall;

                         }
                         qDebug()<<4<<usepython->stuate;
                         continue;
                         qDebug()<<5<<usepython->stuate;
                     }while(!usepython->stuate);
                qDebug()<<6<<usepython->stuate;

            }

        }
    }
    else{
            qDebug()<<usepython->stuate;
        int ret = CplusUsePython::instance()->CCallClassFunc("classname","classfuns",CurrentFilepath_s,Source_s,Target_s);
        qDebug()<<usepython->stuate;
    }

    }
    catch(...){
        qDebug()<< "Error calling external tool";
    }

    ui->ContextButton->setDisabled(false);
}

void MainWindow::on_progressBar_valueChanged(int value)
{

}

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

void MainWindow::thread_context(string CurrentFilepath_s,string Source_s,string Target_s)
{
    CplusUsePython::instance()->CCallClassFunc("classname","classfuns",CurrentFilepath_s,Source_s,Target_s);
}
