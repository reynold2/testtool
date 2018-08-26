QT += core

TARGET = myPluginzxcvbnm

include(../../../include/global.prf)
include($$INCLUDE_DIR/pluginframework.prf)
include($$INCLUDE_DIR/dynamiclayout.prf)
include($$INCLUDE_DIR/eventadmin.prf)
include($$INCLUDE_DIR/configureadmin.prf)
include($$INCLUDE_DIR/mainwindow.prf)
include($$INCLUDE_DIR/testinterface.prf)
include($$INCLUDE_DIR/undomanager.prf)
include($$INCLUDE_DIR/propertybrowser.prf)

TEMPLATE = lib

SOURCES += myActivatorzxcvbnm.cpp
HEADERS += myActivatorzxcvbnm.h

RESOURCES += resource.qrc

DISTFILES += META.INF \
             extension.xml \
    extension.xml

TRANSLATIONS += zh_CN.ts

resource.files += $$PWD/images/*
resource.path = $$PLUGINS_DIR/$$TARGET/images/

target.path = $$PLUGINS_DIR/$$TARGET/

extension.files += extension.xml
extension.path = $$PLUGINS_DIR/$$TARGET/

language.files += $$PWD/*.qm
language.path = $$PLUGINS_DIR/$$TARGET/languages/

INSTALLS += target extension resource language
