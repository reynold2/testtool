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


}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_FileButton_clicked()
{

    QString Path=ui->Edit_Path->text();
    QString Suffix=ui->ComboBox_Suffix->currentText();
    QString Source=ui->Edit_Source->text();
    QString Target=ui->Edit_Target->text();
    DocumentOperation filetool(Path,Suffix,Source,Target,false);
//    for (size_t i =0; i < filetool.fileNameList.size(); i ++)
//    {

//            cout<< filetool.fileNameList[i]<<endl;

//     }

    int int_Suffix=ui->ComboBox_Suffix->currentIndex();
    cout<<int_Suffix<<endl;
    switch(int_Suffix)
    {
        case 1:
            WordFileNamePath_docx=filetool.file_operator();
        case 2:
            ExcelFileNamePath_xlsx=filetool.file_operator();
        case 0:
            FileNamePath=filetool.file_operator();
    }

}

void MainWindow::on_Button_FilePath_clicked()
{
    QFileInfo fi;
    QString file_full;
    file_full = QFileDialog::getOpenFileName(this);
    fi = QFileInfo(file_full);
    this->CurrentFilepath=file_full.toStdString();
    ui->Edit_Path->setText(fi.path()+"/");

}

void MainWindow::on_MianButton_clicked()
{
        myThread.start();
}

void MainWindow::on_ContextButton_clicked()
{
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
             ret = CplusUsePython::instance()->CCallClassFunc("RemoteWord","word_replace",this->CurrentFilepath,Sourcex,Targetx);

        case 5:
             ret = CplusUsePython::instance()->CCallClassFunc("RemoteExcel","re_Excel",this->CurrentFilepath,Sourcex,Targetx);

    }


}

//void MainWindow::on_progressBar_valueChanged(int value)
//{

//}

void MainWindow::showMsg(const QString &msg)
{
    qDebug()<< msg;
}
