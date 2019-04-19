#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QDebug>
#include <QDateTime>
#include <QThreadPool>
#include <myrunable.h>
MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    connect(&myThread,SIGNAL(requestMsg(const QString&)),this,SLOT(showMsg(const QString&)));


}

void MainWindow::showMsg(const QString &msg)
{
    qDebug()<< msg;
}
MainWindow::~MainWindow()
{
    delete ui;
}






void MainWindow::on_pushButton_clicked()
{
        myThread.start();
}
