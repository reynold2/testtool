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
    int int_Suffix=ui->ComboBox_Suffix->currentIndex();
    cout<<int_Suffix<<endl;
    switch(int_Suffix)
    {
        case 1:
            WordFileNamePath_docx=filetool.file_operator();
            break;
        case 2:
            ExcelFileNamePath_xlsx=filetool.file_operator();
            break;
        case 0:
            FileNamePath=filetool.file_operator();
            break;

    }

}

void MainWindow::on_Button_FilePath_clicked()
{
    QFileInfo fi;
    QString file_full;
    file_full = QFileDialog::getOpenFileName(this);
    fi = QFileInfo(file_full);
    ui->Edit_Path->setText(fi.path()+"/");
    ui->Edit_Path->setDisabled(true);
}

void MainWindow::on_MianButton_clicked()
{
        myThread.start();
}

void MainWindow::on_ContextButton_clicked()
{

}

//void MainWindow::on_progressBar_valueChanged(int value)
//{

//}

void MainWindow::showMsg(const QString &msg)
{
    qDebug()<< msg;
}
