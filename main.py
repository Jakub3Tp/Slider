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
        self.death()

    def box_changed(self):
        self.ui.tetnoBar.setValue(self.ui.tetnoBox.value())
        self.ui.cholBar.setValue(self.ui.cholBox.value())
        self.ui.wiekBar.setValue(self.ui.wiekBox.value())
        self.death()

    def death(self):
        age_death = 0
        age_death = (1/130*self.ui.wiekBar.value())*100
        chol_death = 0
        chol_death = (1/100*self.ui.cholBar.value()-200)*100
        if chol_death < 0:
            chol_death = 0
        hearth_death = 0
        if self.ui.tetnoBox.value() < 50:
            hearth_death = 1/50*(50-self.ui.tetnoBar.value())*100
        elif self.ui.tetnoBox.value() > 100:
            hearth_death = 1/100*(self.ui.tetnoBox.value()-100)*100

        death = (hearth_death + chol_death + age_death)/3
        self.ui.progressBar.setValue(int(100-death))

        if death < 33:
            self.ui.progress.setText("Dobrze jest")
        elif death < 66:
            self.ui.progress.setText("Lepiej odwiedz doktora")
        else:
            self.ui.progress.setText("Widzimi się przyszłym życiu")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())
