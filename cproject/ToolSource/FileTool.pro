#-------------------------------------------------
#
# Project created by QtCreator 2019-04-10T13:46:55
#
#-------------------------------------------------

QT       += core gui concurrent

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = FileTool
TEMPLATE = app

# The following define makes your compiler emit warnings if you use
# any feature of Qt which has been marked as deprecated (the exact warnings
# depend on your compiler). Please consult the documentation of the
# deprecated API in order to know how to port your code away from it.
DEFINES += QT_DEPRECATED_WARNINGS

# You can also make your code fail to compile if you use deprecated APIs.
# In order to do so, uncomment the following line.
# You can also select to disable deprecated APIs only up to a certain version of Qt.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0


SOURCES += \
        main.cpp \
        mainwindow.cpp \
    documentoperation.cpp \
    myrunable.cpp \
    mythread.cpp \
    extension_python.cpp \



HEADERS += \
        mainwindow.h \
    documentoperation.h \
    mythread.h \
    myrunable.h \
    extension_python.h \




FORMS += \
        mainwindow.ui

DISTFILES += \
    fileOperation.py
############# python enviroment
#home

#INCLUDEPATH +=C:\Users\Administrator\AppData\Local\Programs\Python\Python37\include
#LIBS += -LC:\Users\Administrator\AppData\Local\Programs\Python\Python37\libs\ -lPython37

#company
INCLUDEPATH +=C:\Users\Administrator\AppData\Local\Programs\Python\Python36\include
LIBS += -LC:\Users\Administrator\AppData\Local\Programs\Python\Python36\libs\ -lPython36
