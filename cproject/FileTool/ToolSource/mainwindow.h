#ifndef MAINWINDOW_H
#define MAINWINDOW_H
#include<QMessageBox.h>
#include <QMainWindow>
#include"qdebug.h"
#include<qfiledialog.h>


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

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
