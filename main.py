import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.tetnoBar.valueChanged.connect(self.bar_changed)
        self.ui.wiekBar.valueChanged.connect(self.bar_changed)
        self.ui.cholBar.valueChanged.connect(self.bar_changed)
        self.ui.tetnoBox.valueChanged.connect(self.box_changed)
        self.ui.wiekBox.valueChanged.connect(self.box_changed)
        self.ui.cholBox.valueChanged.connect(self.box_changed)
        self.show()

    def bar_changed(self):
        self.ui.tetnoBox.setValue(self.ui.tetnoBar.value())
        self.ui.cholBox.setValue(self.ui.cholBar.value())
        self.ui.wiekBox.setValue(self.ui.wiekBar.value())

    def box_changed(self):
        self.ui.tetnoBar.setValue(self.ui.tetnoBox.value())
        self.ui.cholBar.setValue(self.ui.cholBox.value())
        self.ui.wiekBar.setValue(self.ui.wiekBox.value())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())
