/****************************************************************************
** Meta object code from reading C++ file 'phraseview.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.7.0)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../phraseview.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'phraseview.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.7.0. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
struct qt_meta_stringdata_GuessShortcut_t {
    QByteArrayData data[5];
    char stringdata0[43];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_GuessShortcut_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_GuessShortcut_t qt_meta_stringdata_GuessShortcut = {
    {
QT_MOC_LITERAL(0, 0, 13), // "GuessShortcut"
QT_MOC_LITERAL(1, 14, 9), // "activated"
QT_MOC_LITERAL(2, 24, 0), // ""
QT_MOC_LITERAL(3, 25, 4), // "nkey"
QT_MOC_LITERAL(4, 30, 12) // "keyActivated"

    },
    "GuessShortcut\0activated\0\0nkey\0"
    "keyActivated"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_GuessShortcut[] = {

 // content:
       7,       // revision
       0,       // classname
       0,    0, // classinfo
       2,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       1,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    1,   24,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
       4,    0,   27,    2, 0x08 /* Private */,

 // signals: parameters
    QMetaType::Void, QMetaType::Int,    3,

 // slots: parameters
    QMetaType::Void,

       0        // eod
};

void GuessShortcut::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        GuessShortcut *_t = static_cast<GuessShortcut *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->activated((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 1: _t->keyActivated(); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        void **func = reinterpret_cast<void **>(_a[1]);
        {
            typedef void (GuessShortcut::*_t)(int );
            if (*reinterpret_cast<_t *>(func) == static_cast<_t>(&GuessShortcut::activated)) {
                *result = 0;
                return;
            }
        }
    }
}

const QMetaObject GuessShortcut::staticMetaObject = {
    { &QShortcut::staticMetaObject, qt_meta_stringdata_GuessShortcut.data,
      qt_meta_data_GuessShortcut,  qt_static_metacall, Q_NULLPTR, Q_NULLPTR}
};


const QMetaObject *GuessShortcut::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *GuessShortcut::qt_metacast(const char *_clname)
{
    if (!_clname) return Q_NULLPTR;
    if (!strcmp(_clname, qt_meta_stringdata_GuessShortcut.stringdata0))
        return static_cast<void*>(const_cast< GuessShortcut*>(this));
    return QShortcut::qt_metacast(_clname);
}

int GuessShortcut::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QShortcut::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 2)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 2;
    }
    return _id;
}

// SIGNAL 0
void GuessShortcut::activated(int _t1)
{
    void *_a[] = { Q_NULLPTR, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}
struct qt_meta_stringdata_PhraseView_t {
    QByteArrayData data[15];
    char stringdata0[150];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_PhraseView_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_PhraseView_t qt_meta_stringdata_PhraseView = {
    {
QT_MOC_LITERAL(0, 0, 10), // "PhraseView"
QT_MOC_LITERAL(1, 11, 14), // "phraseSelected"
QT_MOC_LITERAL(2, 26, 0), // ""
QT_MOC_LITERAL(3, 27, 12), // "languageCode"
QT_MOC_LITERAL(4, 40, 6), // "source"
QT_MOC_LITERAL(5, 47, 6), // "phrase"
QT_MOC_LITERAL(6, 54, 13), // "setSourceText"
QT_MOC_LITERAL(7, 68, 10), // "sourceText"
QT_MOC_LITERAL(8, 79, 14), // "toggleGuessing"
QT_MOC_LITERAL(9, 94, 6), // "update"
QT_MOC_LITERAL(10, 101, 13), // "guessShortcut"
QT_MOC_LITERAL(11, 115, 4), // "nkey"
QT_MOC_LITERAL(12, 120, 12), // "selectPhrase"
QT_MOC_LITERAL(13, 133, 5), // "index"
QT_MOC_LITERAL(14, 139, 10) // "editPhrase"

    },
    "PhraseView\0phraseSelected\0\0languageCode\0"
    "source\0phrase\0setSourceText\0sourceText\0"
    "toggleGuessing\0update\0guessShortcut\0"
    "nkey\0selectPhrase\0index\0editPhrase"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_PhraseView[] = {

 // content:
       7,       // revision
       0,       // classname
       0,    0, // classinfo
       8,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       1,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    3,   54,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
       6,    2,   61,    2, 0x0a /* Public */,
       8,    0,   66,    2, 0x0a /* Public */,
       9,    0,   67,    2, 0x0a /* Public */,
      10,    1,   68,    2, 0x08 /* Private */,
      12,    1,   71,    2, 0x08 /* Private */,
      12,    0,   74,    2, 0x08 /* Private */,
      14,    0,   75,    2, 0x08 /* Private */,

 // signals: parameters
    QMetaType::Void, QMetaType::QString, QMetaType::QString, QMetaType::QString,    3,    4,    5,

 // slots: parameters
    QMetaType::Void, QMetaType::QString, QMetaType::QString,    3,    7,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, QMetaType::Int,   11,
    QMetaType::Void, QMetaType::QModelIndex,   13,
    QMetaType::Void,
    QMetaType::Void,

       0        // eod
};

void PhraseView::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        PhraseView *_t = static_cast<PhraseView *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->phraseSelected((*reinterpret_cast< const QString(*)>(_a[1])),(*reinterpret_cast< const QString(*)>(_a[2])),(*reinterpret_cast< const QString(*)>(_a[3]))); break;
        case 1: _t->setSourceText((*reinterpret_cast< const QString(*)>(_a[1])),(*reinterpret_cast< const QString(*)>(_a[2]))); break;
        case 2: _t->toggleGuessing(); break;
        case 3: _t->update(); break;
        case 4: _t->guessShortcut((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 5: _t->selectPhrase((*reinterpret_cast< const QModelIndex(*)>(_a[1]))); break;
        case 6: _t->selectPhrase(); break;
        case 7: _t->editPhrase(); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        void **func = reinterpret_cast<void **>(_a[1]);
        {
            typedef void (PhraseView::*_t)(const QString & , const QString & , const QString & );
            if (*reinterpret_cast<_t *>(func) == static_cast<_t>(&PhraseView::phraseSelected)) {
                *result = 0;
                return;
            }
        }
    }
}

const QMetaObject PhraseView::staticMetaObject = {
    { &QTreeView::staticMetaObject, qt_meta_stringdata_PhraseView.data,
      qt_meta_data_PhraseView,  qt_static_metacall, Q_NULLPTR, Q_NULLPTR}
};


const QMetaObject *PhraseView::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *PhraseView::qt_metacast(const char *_clname)
{
    if (!_clname) return Q_NULLPTR;
    if (!strcmp(_clname, qt_meta_stringdata_PhraseView.stringdata0))
        return static_cast<void*>(const_cast< PhraseView*>(this));
    return QTreeView::qt_metacast(_clname);
}

int PhraseView::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QTreeView::qt_metacall(_c, _id, _a);
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

// SIGNAL 0
void PhraseView::phraseSelected(const QString & _t1, const QString & _t2, const QString & _t3)
{
    void *_a[] = { Q_NULLPTR, const_cast<void*>(reinterpret_cast<const void*>(&_t1)), const_cast<void*>(reinterpret_cast<const void*>(&_t2)), const_cast<void*>(reinterpret_cast<const void*>(&_t3)) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}
QT_END_MOC_NAMESPACE
