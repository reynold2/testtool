/****************************************************************************
** Meta object code from reading C++ file 'phrasebookbox.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.7.0)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../phrasebookbox.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'phrasebookbox.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.7.0. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
struct qt_meta_stringdata_PhraseBookBox_t {
    QByteArrayData data[13];
    char stringdata0[140];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_PhraseBookBox_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_PhraseBookBox_t qt_meta_stringdata_PhraseBookBox = {
    {
QT_MOC_LITERAL(0, 0, 13), // "PhraseBookBox"
QT_MOC_LITERAL(1, 14, 9), // "newPhrase"
QT_MOC_LITERAL(2, 24, 0), // ""
QT_MOC_LITERAL(3, 25, 12), // "removePhrase"
QT_MOC_LITERAL(4, 38, 8), // "settings"
QT_MOC_LITERAL(5, 47, 4), // "save"
QT_MOC_LITERAL(6, 52, 13), // "sourceChanged"
QT_MOC_LITERAL(7, 66, 6), // "source"
QT_MOC_LITERAL(8, 73, 13), // "targetChanged"
QT_MOC_LITERAL(9, 87, 6), // "target"
QT_MOC_LITERAL(10, 94, 17), // "definitionChanged"
QT_MOC_LITERAL(11, 112, 10), // "definition"
QT_MOC_LITERAL(12, 123, 16) // "selectionChanged"

    },
    "PhraseBookBox\0newPhrase\0\0removePhrase\0"
    "settings\0save\0sourceChanged\0source\0"
    "targetChanged\0target\0definitionChanged\0"
    "definition\0selectionChanged"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_PhraseBookBox[] = {

 // content:
       7,       // revision
       0,       // classname
       0,    0, // classinfo
       8,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    0,   54,    2, 0x08 /* Private */,
       3,    0,   55,    2, 0x08 /* Private */,
       4,    0,   56,    2, 0x08 /* Private */,
       5,    0,   57,    2, 0x08 /* Private */,
       6,    1,   58,    2, 0x08 /* Private */,
       8,    1,   61,    2, 0x08 /* Private */,
      10,    1,   64,    2, 0x08 /* Private */,
      12,    0,   67,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, QMetaType::QString,    7,
    QMetaType::Void, QMetaType::QString,    9,
    QMetaType::Void, QMetaType::QString,   11,
    QMetaType::Void,

       0        // eod
};

void PhraseBookBox::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        PhraseBookBox *_t = static_cast<PhraseBookBox *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->newPhrase(); break;
        case 1: _t->removePhrase(); break;
        case 2: _t->settings(); break;
        case 3: _t->save(); break;
        case 4: _t->sourceChanged((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 5: _t->targetChanged((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 6: _t->definitionChanged((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 7: _t->selectionChanged(); break;
        default: ;
        }
    }
}

const QMetaObject PhraseBookBox::staticMetaObject = {
    { &QDialog::staticMetaObject, qt_meta_stringdata_PhraseBookBox.data,
      qt_meta_data_PhraseBookBox,  qt_static_metacall, Q_NULLPTR, Q_NULLPTR}
};


const QMetaObject *PhraseBookBox::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *PhraseBookBox::qt_metacast(const char *_clname)
{
    if (!_clname) return Q_NULLPTR;
    if (!strcmp(_clname, qt_meta_stringdata_PhraseBookBox.stringdata0))
        return static_cast<void*>(const_cast< PhraseBookBox*>(this));
    if (!strcmp(_clname, "Ui::PhraseBookBox"))
        return static_cast< Ui::PhraseBookBox*>(const_cast< PhraseBookBox*>(this));
    return QDialog::qt_metacast(_clname);
}

int PhraseBookBox::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QDialog::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 8)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 8;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 8)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 8;
    }
    return _id;
}
QT_END_MOC_NAMESPACE
