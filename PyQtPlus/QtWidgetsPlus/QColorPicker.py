from typing import Optional
from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QColorDialog
from .. import PYQT_SLOT

class QColorPicker(QWidget):
    colorSet = pyqtSignal(QColor)

    def __init__(self, parent: QObject = None, color: QColor = None, colorSet: Optional[PYQT_SLOT] = None):
        super().__init__(parent)
        self.preview = QPushButton(clicked=self.showPicker)
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.preview)
        self.layout().setContentsMargins(0,0,0,0)

        if colorSet is not None:
            self.colorSet.connect(colorSet)

        self.setColor(QColor() if color is None else color)

    def setColor(self, color: QColor, emitSignal: bool = True):
        self._color = color
        self.preview.setStyleSheet(f'background-color: rgb({self._color.red()}, {self._color.green()}, {self._color.blue()});')
        if emitSignal: self.colorSet.emit(self._color)
        
    def showPicker(self):
        self.setColor(QColorDialog.getColor(self._color))