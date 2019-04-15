#include "mainwindow.h"
#include "ui_mainwindow.h"
#include"fileoperation.h"
#include"documentoperation.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{


    ui->setupUi(this);
    connect(ui->FileButton, SIGNAL(clicked()), this, SLOT(on_FileButton_clicked()),Qt::UniqueConnection);
    connect(ui->Button_FilePath, SIGNAL(clicked()), this, SLOT(on_Button_FilePath_clicked()),Qt::UniqueConnection);

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
    qDebug()<<Suffix<<endl;

    DocumentOperation filetool(Path,Suffix,Source,Target,false);

    bool x=filetool.file_operator();
    cout<<x<<endl;
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
