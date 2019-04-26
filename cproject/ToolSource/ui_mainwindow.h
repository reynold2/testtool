/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QProgressBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QTabWidget *tabWidget;
    QWidget *FileTable;
    QLineEdit *Edit_Path;
    QLineEdit *Edit_Source;
    QLineEdit *Edit_Target;
    QLabel *label;
    QLabel *label_2;
    QLabel *label_3;
    QPushButton *Button_FilePath;
    QLabel *label_5;
    QComboBox *ComboBox_Suffix;
    QProgressBar *progressBar;
    QWidget *layoutWidget;
    QVBoxLayout *verticalLayout_2;
    QVBoxLayout *verticalLayout;
    QPushButton *MianButton;
    QPushButton *FileButton;
    QPushButton *ContextButton;
    QWidget *ContentTable;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(600, 400);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        tabWidget = new QTabWidget(centralWidget);
        tabWidget->setObjectName(QStringLiteral("tabWidget"));
        tabWidget->setGeometry(QRect(0, 0, 601, 341));
        FileTable = new QWidget();
        FileTable->setObjectName(QStringLiteral("FileTable"));
        Edit_Path = new QLineEdit(FileTable);
        Edit_Path->setObjectName(QStringLiteral("Edit_Path"));
        Edit_Path->setGeometry(QRect(130, 20, 113, 20));
        Edit_Source = new QLineEdit(FileTable);
        Edit_Source->setObjectName(QStringLiteral("Edit_Source"));
        Edit_Source->setGeometry(QRect(130, 50, 113, 20));
        Edit_Target = new QLineEdit(FileTable);
        Edit_Target->setObjectName(QStringLiteral("Edit_Target"));
        Edit_Target->setGeometry(QRect(130, 80, 111, 20));
        label = new QLabel(FileTable);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(10, 20, 111, 16));
        label_2 = new QLabel(FileTable);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(10, 50, 91, 16));
        label_3 = new QLabel(FileTable);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setGeometry(QRect(10, 80, 54, 12));
        Button_FilePath = new QPushButton(FileTable);
        Button_FilePath->setObjectName(QStringLiteral("Button_FilePath"));
        Button_FilePath->setGeometry(QRect(240, 20, 31, 21));
        QFont font;
        font.setFamily(QStringLiteral("Agency FB"));
        font.setPointSize(7);
        Button_FilePath->setFont(font);
        label_5 = new QLabel(FileTable);
        label_5->setObjectName(QStringLiteral("label_5"));
        label_5->setGeometry(QRect(350, 20, 54, 20));
        ComboBox_Suffix = new QComboBox(FileTable);
        ComboBox_Suffix->setObjectName(QStringLiteral("ComboBox_Suffix"));
        ComboBox_Suffix->setGeometry(QRect(410, 20, 72, 22));
        ComboBox_Suffix->setCurrentText(QStringLiteral("*.*"));
        progressBar = new QProgressBar(FileTable);
        progressBar->setObjectName(QStringLiteral("progressBar"));
        progressBar->setGeometry(QRect(0, 290, 118, 23));
        progressBar->setValue(24);
        layoutWidget = new QWidget(FileTable);
        layoutWidget->setObjectName(QStringLiteral("layoutWidget"));
        layoutWidget->setGeometry(QRect(510, 220, 84, 85));
        verticalLayout_2 = new QVBoxLayout(layoutWidget);
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setContentsMargins(11, 11, 11, 11);
        verticalLayout_2->setObjectName(QStringLiteral("verticalLayout_2"));
        verticalLayout_2->setContentsMargins(0, 0, 0, 0);
        verticalLayout = new QVBoxLayout();
        verticalLayout->setSpacing(6);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        MianButton = new QPushButton(layoutWidget);
        MianButton->setObjectName(QStringLiteral("MianButton"));

        verticalLayout->addWidget(MianButton);

        FileButton = new QPushButton(layoutWidget);
        FileButton->setObjectName(QStringLiteral("FileButton"));

        verticalLayout->addWidget(FileButton);


        verticalLayout_2->addLayout(verticalLayout);

        ContextButton = new QPushButton(layoutWidget);
        ContextButton->setObjectName(QStringLiteral("ContextButton"));

        verticalLayout_2->addWidget(ContextButton);

        tabWidget->addTab(FileTable, QString());
        ContentTable = new QWidget();
        ContentTable->setObjectName(QStringLiteral("ContentTable"));
        tabWidget->addTab(ContentTable, QString());
        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 600, 23));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);

        retranslateUi(MainWindow);

        tabWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "\346\226\207\346\241\243\346\223\215\344\275\234\345\267\245\345\205\267", Q_NULLPTR));
        Edit_Path->setText(QApplication::translate("MainWindow", "DirPath", Q_NULLPTR));
        label->setText(QApplication::translate("MainWindow", "\346\226\207\344\273\266\345\244\271\346\211\200\345\234\250\350\267\257\345\276\204", Q_NULLPTR));
        label_2->setText(QApplication::translate("MainWindow", "\346\272\220\346\225\260\346\215\256", Q_NULLPTR));
        label_3->setText(QApplication::translate("MainWindow", "\347\233\256\346\240\207\346\225\260\346\215\256", Q_NULLPTR));
#ifndef QT_NO_TOOLTIP
        Button_FilePath->setToolTip(QApplication::translate("MainWindow", "\350\257\267\351\200\211\346\213\251\346\226\207\344\273\266\346\211\200\345\234\250\350\267\257\345\276\204\344\270\213\344\273\273\346\204\217\344\270\200\344\270\252\346\226\207\344\273\266\344\273\245\344\276\277\346\210\221\344\273\254\350\203\275\351\241\272\345\210\251\346\211\276\345\210\260\345\256\203\344\273\254", Q_NULLPTR));
#endif // QT_NO_TOOLTIP
        Button_FilePath->setText(QApplication::translate("MainWindow", "\346\265\217\350\247\210", Q_NULLPTR));
        label_5->setText(QApplication::translate("MainWindow", "\346\226\207\344\273\266\345\220\216\347\274\200", Q_NULLPTR));
        ComboBox_Suffix->clear();
        ComboBox_Suffix->insertItems(0, QStringList()
         << QApplication::translate("MainWindow", "*.*", Q_NULLPTR)
         << QApplication::translate("MainWindow", "doc", Q_NULLPTR)
         << QApplication::translate("MainWindow", "docx", Q_NULLPTR)
         << QApplication::translate("MainWindow", "rtf", Q_NULLPTR)
         << QApplication::translate("MainWindow", "xls", Q_NULLPTR)
         << QApplication::translate("MainWindow", "xlsx", Q_NULLPTR)
         << QApplication::translate("MainWindow", "txt", Q_NULLPTR)
        );
        MianButton->setText(QApplication::translate("MainWindow", "\345\205\250\351\203\250\346\233\277\346\215\242", Q_NULLPTR));
        FileButton->setText(QApplication::translate("MainWindow", "\346\226\207\344\273\266\345\220\215\346\233\277\346\215\242", Q_NULLPTR));
        ContextButton->setText(QApplication::translate("MainWindow", "\346\226\207\344\273\266\345\206\205\345\256\271\346\233\277\346\215\242", Q_NULLPTR));
        tabWidget->setTabText(tabWidget->indexOf(FileTable), QApplication::translate("MainWindow", "\346\226\207\344\273\266\346\223\215\344\275\234", Q_NULLPTR));
        tabWidget->setTabText(tabWidget->indexOf(ContentTable), QApplication::translate("MainWindow", "\345\267\245\345\205\267", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
