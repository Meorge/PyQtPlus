from PyQt6.QtCore import QPointF, Qt
from PyQt6.QtGui import QColor, QColorConstants, QGradient, QLinearGradient
from PyQt6.QtWidgets import QGridLayout, QMainWindow, QApplication, QVBoxLayout, QWidget
from PyQtPlus.QtWidgetsPlus import QColorPicker, QMonochromeGraphicLabel
from PyQtPlus.QtOnboarding import QOnboardingItem, QWizardTitle
import sys

class OnboardingView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.header = QWizardTitle(parent=self, title='Genni', icon='genni_logo.png', iconSize=150)
        self.item1 = QOnboardingItem(title='Live Training', body='Watch a graph of your model\'s loss as\nit progresses.')
        self.item2 = QOnboardingItem(title='Easy Datasets', body='Upload your own datasets, or easily\ncreate one from a Twitter search query.')
        self.item3 = QOnboardingItem(title='Check Output', body='Check your generated text against\nyour datasets, or a custom blocklist.')

        self.__ly = QVBoxLayout()
        self.__ly.setSpacing(5)
        self.__ly.addWidget(self.header)
        self.__ly.addWidget(self.item1)
        self.__ly.addWidget(self.item2)
        self.__ly.addWidget(self.item3)
        self.__ly.addStretch()

        self.__w = QWidget()
        self.__w.setLayout(self.__ly)
        self.setCentralWidget(self.__w)

        self.header.animateIn()

class SvgIconView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.a = QMonochromeGraphicLabel(svgPath='thumbup.svg', tintColor=QColorConstants.Red, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
        self.b = QMonochromeGraphicLabel(svgPath='thumbup.svg', tintColor=QColorConstants.Green)
        self.c = QMonochromeGraphicLabel(svgPath='thumbup.svg', tintColor=QColorConstants.Blue)

        self.aP = QColorPicker(colorSet=self.a.setTintColor)
        self.bP = QColorPicker(colorSet=self.b.setTintColor)
        self.cP = QColorPicker(colorSet=self.c.setTintColor)

        self.ly = QGridLayout()
        self.ly.addWidget(self.a, 0, 0)
        self.ly.addWidget(self.b, 0, 1)
        self.ly.addWidget(self.c, 0, 2)
        self.ly.addWidget(self.aP, 1, 0)
        self.ly.addWidget(self.bP, 1, 1)
        self.ly.addWidget(self.cP, 1, 2)

        self.gradient = QLinearGradient(QPointF(0, 0), QPointF(1, 1))
        self.gradient.setCoordinateMode(QGradient.CoordinateMode.ObjectMode)
        self.gradient.setColorAt(1, QColor(150, 30, 230))
        self.gradient.setColorAt(0, QColor(30, 80, 255))
        self.g = QMonochromeGraphicLabel(svgPath='thumbup.svg', tintColor=self.gradient)

        self.ly.addWidget(self.g, 2, 0)

        self.w = QWidget()
        self.w.setLayout(self.ly)
        self.setCentralWidget(self.w)


if __name__ == "__main__":
    app = QApplication([])
    window = SvgIconView()
    window.show()
    sys.exit(app.exec())
