from PyQt6.QtCore import QPointF, Qt
from PyQt6.QtGui import QColor, QColorConstants, QGradient, QLinearGradient
from PyQt6.QtWidgets import QCheckBox, QGridLayout, QHBoxLayout, QLabel, QMainWindow, QApplication, QPushButton, QSlider, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget
from PyQtPlus.QtWidgetsPlus import QSpinningProgressIndicator
import sys

class SpinnerTest(QMainWindow):
    def __init__(self):
        super().__init__()

        self.p = QSpinningProgressIndicator(color = QColor(80, 160, 255))
        self.p2 = QSpinningProgressIndicator(color = QColor(80, 160, 255))

        # self.a = QSlider()
        # self.a.setOrientation(Qt.Orientation.Horizontal)
        # self.a.setMinimum(0)
        # self.a.setMaximum(100)
        # self.a.valueChanged.connect(self.p.setProgress)

        # self.c = QCheckBox('Indeterminate', toggled=self.p.setIndeterminate)



        self.group = QWidget()
        self.groupLy = QHBoxLayout(self.group)
        self.groupLy.addWidget(self.p, alignment=Qt.AlignmentFlag.AlignVCenter)
        self.groupLy.addWidget(QLabel('Processing'))
        self.groupLy.addStretch()
        self.groupLy.setSpacing(5)
        self.groupLy.setContentsMargins(0,0,0,0)

        self.w = QTreeWidget()

        self.item1 = QTreeWidgetItem(self.w)
        self.w.setItemWidget(self.item1, 0, self.group)


        self.bw = QWidget()

        self.ly = QGridLayout(self.bw)
        self.ly.addWidget(self.w, 0, 0)
        self.ly.addWidget(self.p2, 1, 0)

        self.setCentralWidget(self.bw)

if __name__ == "__main__":
    app = QApplication([])
    window = SpinnerTest()
    window.show()
    sys.exit(app.exec())