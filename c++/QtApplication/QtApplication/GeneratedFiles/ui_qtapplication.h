/********************************************************************************
** Form generated from reading UI file 'qtapplication.ui'
**
** Created by: Qt User Interface Compiler version 5.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_QTAPPLICATION_H
#define UI_QTAPPLICATION_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_QtApplicationClass
{
public:
    QWidget *centralWidget;
    QPushButton *clickbutton;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *QtApplicationClass)
    {
        if (QtApplicationClass->objectName().isEmpty())
            QtApplicationClass->setObjectName(QStringLiteral("QtApplicationClass"));
        QtApplicationClass->resize(600, 400);
        centralWidget = new QWidget(QtApplicationClass);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        clickbutton = new QPushButton(centralWidget);
        clickbutton->setObjectName(QStringLiteral("clickbutton"));
        clickbutton->setGeometry(QRect(180, 140, 75, 23));
        QtApplicationClass->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(QtApplicationClass);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 600, 23));
        QtApplicationClass->setMenuBar(menuBar);
        mainToolBar = new QToolBar(QtApplicationClass);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        QtApplicationClass->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(QtApplicationClass);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        QtApplicationClass->setStatusBar(statusBar);

        retranslateUi(QtApplicationClass);

        QMetaObject::connectSlotsByName(QtApplicationClass);
    } // setupUi

    void retranslateUi(QMainWindow *QtApplicationClass)
    {
        QtApplicationClass->setWindowTitle(QApplication::translate("QtApplicationClass", "QtApplication", Q_NULLPTR));
        clickbutton->setText(QApplication::translate("QtApplicationClass", "PushButton", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class QtApplicationClass: public Ui_QtApplicationClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_QTAPPLICATION_H
