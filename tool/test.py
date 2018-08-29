from PyQt5.QtCore import QObject, pyqtSignal

class NewSignal(QObject):

    # 一个valueChanged的信号，该信号没有参数.
    valueChanged = pyqtSignal()

    def connect_and_emit_valueChanged(self):
        # 绑定信号和槽函数
        self.valueChanged.connect(self.handle_valueChanged)

        # 发射信号.
        self.trigger.emit()

    def handle_valueChanged(self):
        print("trigger signal received")
x=NewSignal()
x.connect_and_emit_valueChanged()