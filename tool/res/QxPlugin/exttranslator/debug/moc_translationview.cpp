/****************************************************************************
** Meta object code from reading C++ file 'translationview.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.7.0)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../translationview.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'translationview.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.7.0. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
struct qt_meta_stringdata_TranslationView_t {
    QByteArrayData data[14];
    char stringdata0[167];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_TranslationView_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_TranslationView_t qt_meta_stringdata_TranslationView = {
    {
QT_MOC_LITERAL(0, 0, 15), // "TranslationView"
QT_MOC_LITERAL(1, 16, 23), // "currentTransItemChanged"
QT_MOC_LITERAL(2, 40, 0), // ""
QT_MOC_LITERAL(3, 41, 4), // "code"
QT_MOC_LITERAL(4, 46, 6), // "source"
QT_MOC_LITERAL(5, 53, 16), // "onSelectedSource"
QT_MOC_LITERAL(6, 70, 8), // "selected"
QT_MOC_LITERAL(7, 79, 13), // "onCurLineEdit"
QT_MOC_LITERAL(8, 93, 10), // "QLineEdit*"
QT_MOC_LITERAL(9, 104, 15), // "currentLineEdit"
QT_MOC_LITERAL(10, 120, 16), // "onPhraseSelected"
QT_MOC_LITERAL(11, 137, 8), // "langCode"
QT_MOC_LITERAL(12, 146, 10), // "sourceText"
QT_MOC_LITERAL(13, 157, 9) // "transText"

    },
    "TranslationView\0currentTransItemChanged\0"
    "\0code\0source\0onSelectedSource\0selected\0"
    "onCurLineEdit\0QLineEdit*\0currentLineEdit\0"
    "onPhraseSelected\0langCode\0sourceText\0"
    "transText"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_TranslationView[] = {

 // content:
       7,       // revision
       0,       // classname
       0,    0, // classinfo
       4,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       1,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    2,   34,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
       5,    1,   39,    2, 0x0a /* Public */,
       7,    1,   42,    2, 0x0a /* Public */,
      10,    3,   45,    2, 0x0a /* Public */,

 // signals: parameters
    QMetaType::Void, QMetaType::QString, QMetaType::QString,    3,    4,

 // slots: parameters
    QMetaType::Void, QMetaType::QString,    6,
    QMetaType::Void, 0x80000000 | 8,    9,
    QMetaType::Void, QMetaType::QString, QMetaType::QString, QMetaType::QString,   11,   12,   13,

       0        // eod
};

void TranslationView::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        TranslationView *_t = static_cast<TranslationView *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->currentTransItemChanged((*reinterpret_cast< const QString(*)>(_a[1])),(*reinterpret_cast< const QString(*)>(_a[2]))); break;
        case 1: _t->onSelectedSource((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 2: _t->onCurLineEdit((*reinterpret_cast< QLineEdit*(*)>(_a[1]))); break;
        case 3: _t->onPhraseSelected((*reinterpret_cast< const QString(*)>(_a[1])),(*reinterpret_cast< const QString(*)>(_a[2])),(*reinterpret_cast< const QString(*)>(_a[3]))); break;
        default: ;
        }
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        switch (_id) {
        default: *reinterpret_cast<int*>(_a[0]) = -1; break;
        case 2:
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
            typedef void (TranslationView::*_t)(const QString & , const QString & );
            if (*reinterpret_cast<_t *>(func) == static_cast<_t>(&TranslationView::currentTransItemChanged)) {
                *result = 0;
                return;
            }
        }
    }
}

const QMetaObject TranslationView::staticMetaObject = {
    { &QWidget::staticMetaObject, qt_meta_stringdata_TranslationView.data,
      qt_meta_data_TranslationView,  qt_static_metacall, Q_NULLPTR, Q_NULLPTR}
};


const QMetaObject *TranslationView::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *TranslationView::qt_metacast(const char *_clname)
{
    if (!_clname) return Q_NULLPTR;
    if (!strcmp(_clname, qt_meta_stringdata_TranslationView.stringdata0))
        return static_cast<void*>(const_cast< TranslationView*>(this));
    return QWidget::qt_metacast(_clname);
}

int TranslationView::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 4)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 4;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 4)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 4;
    }
    return _id;
}

// SIGNAL 0
void TranslationView::currentTransItemChanged(const QString & _t1, const QString & _t2)
{
    void *_a[] = { Q_NULLPTR, const_cast<void*>(reinterpret_cast<const void*>(&_t1)), const_cast<void*>(reinterpret_cast<const void*>(&_t2)) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}
QT_END_MOC_NAMESPACE
