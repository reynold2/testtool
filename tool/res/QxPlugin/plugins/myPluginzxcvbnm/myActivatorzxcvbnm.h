#ifndef MYPLUGINZXCVBNM_H
#define MYPLUGINZXCVBNM_H

#include "ipluginactivator.h"

using namespace ExtensionSystem;
using namespace Internal;

class myActivatorzxcvbnm : public QObject
        , public IPluginActivator
{
    Q_OBJECT
    Q_INTERFACES(ExtensionSystem::IPluginActivator)
    Q_PLUGIN_METADATA(IID "corelib.pluginframework.PluginActivator/1.0")

public:

    myActivatorzxcvbnm(QObject* parent = 0);
    ~myActivatorzxcvbnm();

public:

    void start(PluginContext *context);
    void stop(PluginContext *context);
};
#endif // MYPLUGINZXCVBNM_H
