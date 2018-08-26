/****************************************************************************
** Meta object code from reading C++ file 'tablemodel.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.7.0)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../tablemodel.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#include <QtCore/QList>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'tablemodel.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.7.0. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
struct qt_meta_stringdata_TableModel_t {
    QByteArrayData data[17];
    char stringdata0[202];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_TableModel_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_TableModel_t qt_meta_stringdata_TableModel = {
    {
QT_MOC_LITERAL(0, 0, 10), // "TableModel"
QT_MOC_LITERAL(1, 11, 17), // "currentRowChanged"
QT_MOC_LITERAL(2, 29, 0), // ""
QT_MOC_LITERAL(3, 30, 10), // "currentRow"
QT_MOC_LITERAL(4, 41, 13), // "setCurrentRow"
QT_MOC_LITERAL(5, 55, 5), // "clear"
QT_MOC_LITERAL(6, 61, 10), // "appendData"
QT_MOC_LITERAL(7, 72, 4), // "data"
QT_MOC_LITERAL(8, 77, 10), // "insertData"
QT_MOC_LITERAL(9, 88, 5), // "index"
QT_MOC_LITERAL(10, 94, 9), // "removeRow"
QT_MOC_LITERAL(11, 104, 3), // "row"
QT_MOC_LITERAL(12, 108, 10), // "updateData"
QT_MOC_LITERAL(13, 119, 19), // "QList<QVariantHash>"
QT_MOC_LITERAL(14, 139, 14), // "updateEditData"
QT_MOC_LITERAL(15, 154, 16), // "updateHeaderData"
QT_MOC_LITERAL(16, 171, 30) // "QList<QPair<QString,QString> >"

    },
    "TableModel\0currentRowChanged\0\0currentRow\0"
    "setCurrentRow\0clear\0appendData\0data\0"
    "insertData\0index\0removeRow\0row\0"
    "updateData\0QList<QVariantHash>\0"
    "updateEditData\0updateHeaderData\0"
    "QList<QPair<QString,QString> >"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_TableModel[] = {

 // content:
       7,       // revision
       0,       // classname
       0,    0, // classinfo
      10,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       1,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    1,   64,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
       4,    1,   67,    2, 0x0a /* Public */,
       5,    0,   70,    2, 0x0a /* Public */,
       6,    1,   71,    2, 0x0a /* Public */,
       8,    2,   74,    2, 0x0a /* Public */,
      10,    1,   79,    2, 0x0a /* Public */,
      12,    1,   82,    2, 0x0a /* Public */,
      14,    1,   85,    2, 0x0a /* Public */,
      15,    1,   88,    2, 0x0a /* Public */,
      12,    2,   91,    2, 0x0a /* Public */,

 // signals: parameters
    QMetaType::Void, QMetaType::Int,    3,

 // slots: parameters
    QMetaType::Void, QMetaType::Int,    3,
    QMetaType::Void,
    QMetaType::Void, QMetaType::QVariantHash,    7,
    QMetaType::Void, QMetaType::Int, QMetaType::QVariantHash,    9,    7,
    QMetaType::Void, QMetaType::Int,   11,
    QMetaType::Void, 0x80000000 | 13,    7,
    QMetaType::Void, QMetaType::QVariantHash,    7,
    QMetaType::Void, 0x80000000 | 16,    7,
    QMetaType::Void, QMetaType::Int, QMetaType::QVariantMap,   11,    7,

       0        // eod
};

void TableModel::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        TableModel *_t = static_cast<TableModel *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->currentRowChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 1: _t->setCurrentRow((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 2: _t->clear(); break;
        case 3: _t->appendData((*reinterpret_cast< const QVariantHash(*)>(_a[1]))); break;
        case 4: _t->insertData((*reinterpret_cast< int(*)>(_a[1])),(*reinterpret_cast< const QVariantHash(*)>(_a[2]))); break;
        case 5: _t->removeRow((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 6: _t->updateData((*reinterpret_cast< const QList<QVariantHash>(*)>(_a[1]))); break;
        case 7: _t->updateEditData((*reinterpret_cast< const QVariantHash(*)>(_a[1]))); break;
        case 8: _t->updateHeaderData((*reinterpret_cast< const QList<QPair<QString,QString> >(*)>(_a[1]))); break;
        case 9: _t->updateData((*reinterpret_cast< int(*)>(_a[1])),(*reinterpret_cast< const QVariantMap(*)>(_a[2]))); break;
        default: ;
        }
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        switch (_id) {
        default: *reinterpret_cast<int*>(_a[0]) = -1; break;
        case 6:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<int*>(_a[0]) = -1; break;
            case 0:
                *reinterpret_cast<int*>(_a[0]) = qRegisterMetaType< QList<QVariantHash> >(); break;
            }
            break;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        void **func = reinterpret_cast<void **>(_a[1]);
        {
            typedef void (TableModel::*_t)(int );
            if (*reinterpret_cast<_t *>(func) == static_cast<_t>(&TableModel::currentRowChanged)) {
                *result = 0;
                return;
            }
        }
    }
}

const QMetaObject TableModel::staticMetaObject = {
    { &QAbstractTableModel::staticMetaObject, qt_meta_stringdata_TableModel.data,
      qt_meta_data_TableModel,  qt_static_metacall, Q_NULLPTR, Q_NULLPTR}
};


const QMetaObject *TableModel::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *TableModel::qt_metacast(const char *_clname)
{
    if (!_clname) return Q_NULLPTR;
    if (!strcmp(_clname, qt_meta_stringdata_TableModel.stringdata0))
        return static_cast<void*>(const_cast< TableModel*>(this));
    return QAbstractTableModel::qt_metacast(_clname);
}

int TableModel::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QAbstractTableModel::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 10)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 10;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 10)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 10;
    }
    return _id;
}

// SIGNAL 0
void TableModel::currentRowChanged(int _t1)
{
    void *_a[] = { Q_NULLPTR, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}
QT_END_MOC_NAMESPACE
