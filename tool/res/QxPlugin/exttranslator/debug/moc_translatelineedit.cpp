/****************************************************************************
** Meta object code from reading C++ file 'translatelineedit.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.7.0)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../translatelineedit.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'translatelineedit.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.7.0. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
struct qt_meta_stringdata_TranslateLineEdit_t {
    QByteArrayData data[11];
    char stringdata0[98];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_TranslateLineEdit_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_TranslateLineEdit_t qt_meta_stringdata_TranslateLineEdit = {
    {
QT_MOC_LITERAL(0, 0, 17), // "TranslateLineEdit"
QT_MOC_LITERAL(1, 18, 12), // "souceChanged"
QT_MOC_LITERAL(2, 31, 0), // ""
QT_MOC_LITERAL(3, 32, 6), // "source"
QT_MOC_LITERAL(4, 39, 11), // "curLineEdit"
QT_MOC_LITERAL(5, 51, 10), // "QLineEdit*"
QT_MOC_LITERAL(6, 62, 8), // "lineEidt"
QT_MOC_LITERAL(7, 71, 6), // "isDone"
QT_MOC_LITERAL(8, 78, 4), // "done"
QT_MOC_LITERAL(9, 83, 7), // "refresh"
QT_MOC_LITERAL(10, 91, 6) // "onEdit"

    },
    "TranslateLineEdit\0souceChanged\0\0source\0"
    "curLineEdit\0QLineEdit*\0lineEidt\0isDone\0"
    "done\0refresh\0onEdit"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_TranslateLineEdit[] = {

 // content:
       7,       // revision
       0,       // classname
       0,    0, // classinfo
       5,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       4,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    1,   39,    2, 0x06 /* Public */,
       4,    1,   42,    2, 0x06 /* Public */,
       7,    1,   45,    2, 0x06 /* Public */,
       9,    0,   48,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
      10,    0,   49,    2, 0x08 /* Private */,

 // signals: parameters
    QMetaType::Void, QMetaType::QString,    3,
    QMetaType::Void, 0x80000000 | 5,    6,
    QMetaType::Void, QMetaType::Bool,    8,
    QMetaType::Void,

 // slots: parameters
    QMetaType::Void,

       0        // eod
};

void TranslateLineEdit::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        TranslateLineEdit *_t = static_cast<TranslateLineEdit *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->souceChanged((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 1: _t->curLineEdit((*reinterpret_cast< QLineEdit*(*)>(_a[1]))); break;
        case 2: _t->isDone((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 3: _t->refresh(); break;
        case 4: _t->onEdit(); break;
        default: ;
        }
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        switch (_id) {
        default: *reinterpret_cast<int*>(_a[0]) = -1; break;
        case 1:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<int*>(_a[0]) = -1; break;
            case 0:
                *reinterpret_cast<int*>(_a[0]) = qRegisterMetaType< QLineEdit* >(); break;
            }
            break;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        void **func = reinterpret_cast<void **>(_a[1]);
        {
            typedef void (TranslateLineEdit::*_t)(const QString & );
            if (*reinterpret_cast<_t *>(func) == static_cast<_t>(&TranslateLineEdit::souceChanged)) {
                *result = 0;
                return;
            }
        }
        {
            typedef void (TranslateLineEdit::*_t)(QLineEdit * );
            if (*reinterpret_cast<_t *>(func) == static_cast<_t>(&TranslateLineEdit::curLineEdit)) {
                *result = 1;
                return;
            }
        }
        {
            typedef void (TranslateLineEdit::*_t)(bool );
            if (*reinterpret_cast<_t *>(func) == static_cast<_t>(&TranslateLineEdit::isDone)) {
                *result = 2;
                return;
            }
        }
        {
            typedef void (TranslateLineEdit::*_t)();
            if (*reinterpret_cast<_t *>(func) == static_cast<_t>(&TranslateLineEdit::refresh)) {
                *result = 3;
                return;
            }
        }
    }
}

const QMetaObject TranslateLineEdit::staticMetaObject = {
    { &QLineEdit::staticMetaObject, qt_meta_stringdata_TranslateLineEdit.data,
      qt_meta_data_TranslateLineEdit,  qt_static_metacall, Q_NULLPTR, Q_NULLPTR}
};


const QMetaObject *TranslateLineEdit::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *TranslateLineEdit::qt_metacast(const char *_clname)
{
    if (!_clname) return Q_NULLPTR;
    if (!strcmp(_clname, qt_meta_stringdata_TranslateLineEdit.stringdata0))
        return static_cast<void*>(const_cast< TranslateLineEdit*>(this));
    return QLineEdit::qt_metacast(_clname);
}

int TranslateLineEdit::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QLineEdit::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 5)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 5;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 5)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 5;
    }
    return _id;
}

// SIGNAL 0
void TranslateLineEdit::souceChanged(const QString & _t1)
{
    void *_a[] = { Q_NULLPTR, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}

// SIGNAL 1
void TranslateLineEdit::curLineEdit(QLineEdit * _t1)
{
    void *_a[] = { Q_NULLPTR, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 1, _a);
}

// SIGNAL 2
void TranslateLineEdit::isDone(bool _t1)
{
    void *_a[] = { Q_NULLPTR, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 2, _a);
}

// SIGNAL 3
void TranslateLineEdit::refresh()
{
    QMetaObject::activate(this, &staticMetaObject, 3, Q_NULLPTR);
}
QT_END_MOC_NAMESPACE
