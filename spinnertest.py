from PyQt6.QtCore import QPointF, Qt
from PyQt6.QtGui import QColor, QColorConstants, QGradient, QLinearGradient
from PyQt6.QtWidgets import QCheckBox, QGridLayout, QMainWindow, QApplication, QSlider, QVBoxLayout, QWidget
from PyQtPlus.QtWidgetsPlus import QSpinningProgressIndicator
import sys

class SpinnerTest(QMainWindow):
    def __init__(self):
        super().__init__()

        self.p = QSpinningProgressIndicator(color = QColor(250, 100, 120))

        self.a = QSlider()
        self.a.setOrientation(Qt.Orientation.Horizontal)
        self.a.setMinimum(0)
        self.a.setMaximum(100)
        self.a.valueChanged.connect(self.p.setProgress)

        self.c = QCheckBox('Indeterminate', toggled=self.p.setIndeterminate)

        self.ly = QGridLayout()
        self.ly.addWidget(self.p, 0, 0)
        self.ly.addWidget(self.a, 1, 0)
        self.ly.addWidget(self.c, 2, 0)

        self.w = QWidget()
        self.w.setLayout(self.ly)
        self.setCentralWidget(self.w)

if __name__ == "__main__":
    app = QApplication([])
    window = SpinnerTest()
    window.show()
    sys.exit(app.exec())