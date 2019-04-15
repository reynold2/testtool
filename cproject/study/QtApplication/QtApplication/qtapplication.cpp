#include "qtapplication.h"

QtApplication::QtApplication(QWidget *parent)
	: QMainWindow(parent)
{
	ui.setupUi(this);
}

QtApplication::~QtApplication()
{

}
