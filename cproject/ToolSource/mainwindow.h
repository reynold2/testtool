#ifndef MAINWINDOW_H
#define MAINWINDOW_H
#include<qfiledialog.h>
#include<QMessageBox.h>
#include <QDateTime>
#include <QThreadPool>
#include <QMainWindow>
#include "ui_mainwindow.h"
#include"documentoperation.h"
#include "myrunable.h"
#include "mythread.h"
#include "math.h"
#include <Python.h>
#include <iostream>
#include <string>
#include "extension_python.h"


//vector<vector<string>> ALLFILEPATHLIST;


namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:
    void on_FileButton_clicked();

    void on_Button_FilePath_clicked();

    void on_MianButton_clicked();

    void on_ContextButton_clicked();

//    void on_progressBar_valueChanged(int value);

    void showMsg(const QString &msg);

private:
    Ui::MainWindow *ui;
    MyThread myThread;
    DocumentOperation *filetool;
    void stringSpilt();
    string exepath;

private:
   QMap< QString,QVector< QString >> AllFileListPath_Main;
   QString CurrentDirPath;
   QString CurrentFilepath ;
   QString CurrentSuffix;

   QString Source;
   QString Target;
   int ret;

public:
    vector<string> WordFileNamePath_docx;
    vector<string> ExcelFileNamePath_xlsx;
    vector<string> FileNamePath;







};

#endif // MAINWINDOW_H
