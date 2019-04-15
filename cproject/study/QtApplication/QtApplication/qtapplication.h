#ifndef QTAPPLICATION_H
#define QTAPPLICATION_H

#include <QtWidgets/QMainWindow>
#include "ui_qtapplication.h"

class QtApplication : public QMainWindow
{
	Q_OBJECT

public:
	QtApplication(QWidget *parent = 0);
	~QtApplication();

private:
	Ui::QtApplicationClass ui;

};

#endif // QTAPPLICATION_H
