from PyQt6.QtCore import QEasingCurve, QMarginsF, QRectF, QSize, QVariantAnimation, Qt
from PyQt6.QtWidgets import QSizePolicy, QWidget
from PyQt6.QtGui import QColorConstants, QPaintEvent, QPainter, QBrush, QPen, QColor
from math import pi

class QSpinningProgressIndicator(QWidget):
    def __init__(self, parent=None, color: QColor = None, indeterminate: bool = True):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        self.__color = QColor(80, 160, 255) if color is None else color

        self.__pen = QPen(self.__color, 5, style = Qt.PenStyle.CustomDashLine, cap = Qt.PenCapStyle.RoundCap, join = Qt.PenJoinStyle.RoundJoin)
        self.__brush = QBrush(self.__color)

        self.__offset = 0

        self.__progress: int = 0
        self.__maxValue: int = 100

        self.__anim = QVariantAnimation(
            self,
            startValue = 0.0,
            endValue = 1.0,
            duration = 1000,
            valueChanged = self.__setOffset,
            easingCurve = QEasingCurve.Type.Linear
        )
        self.__anim.setLoopCount(-1)

        self.setIndeterminate(indeterminate)

    def setProgress(self, progress: int):
        self.__progress = progress
        self.update()

    def setMaxValue(self, value: int):
        self.__maxValue = value
        self.update()

    def setColor(self, color: QColor):
        self.__color = color
        self.__pen.setColor(self.__color)
        self.__brush.setColor(self.__color)


    def setIndeterminate(self, value: bool):
        self.__indeterminate = value
        if self.__indeterminate:
            self.__anim.start()
        else:
            self.__anim.stop()

        self.update()

    def __setOffset(self, offset: float):
        self.__offset = offset
        self.update()

    def sizeHint(self) -> QSize:
        hint = QSize(15, 15)
        print(f'size hint is {hint}')
        return hint

    def paintEvent(self, a0: QPaintEvent) -> None:
        with QPainter(self) as p:
            p: QPainter
            p.setRenderHint(QPainter.RenderHint.Antialiasing, True)
            
            self.__diameter = min(self.rect().width(), self.rect().height())
            self.__radius = self.__diameter / 2
            self.__circumference = 2 * pi * self.__radius
            self.__rect = QRectF(-self.__radius, -self.__radius, self.__diameter, self.__diameter)

            # Calculate pen width
            widthRatio = 0.1
            width = self.__diameter * widthRatio
            self.__pen.setWidthF(width)

            self.__rect = self.__rect.marginsRemoved(QMarginsF(width, width, width, width))
            p.translate(self.__radius, self.__radius)
            
            if self.__indeterminate: self.paintIndeterminate(p)
            else: self.paintDeterminate(p)


    def paintDeterminate(self, p: QPainter):
        p.setBrush(QColorConstants.Red)
        angle = -16 * (360.0 * float(self.__progress) / float(self.__maxValue))
        p.setPen(Qt.PenStyle.NoPen)
        p.setBrush(self.__brush)
        p.drawPie(self.__rect, 16 * 90, angle)


    def paintIndeterminate(self, p: QPainter):
        fillToSpaceRatio = 0.65
        fill = self.__circumference * fillToSpaceRatio / self.__pen.widthF()
        space = self.__circumference * (1 - fillToSpaceRatio) / self.__pen.widthF()
        self.__pen.setDashPattern([fill, space])

        p.rotate(360.0 * self.__offset)
        p.setPen(self.__pen)
        p.setBrush(Qt.BrushStyle.NoBrush)
        p.drawEllipse(self.__rect)