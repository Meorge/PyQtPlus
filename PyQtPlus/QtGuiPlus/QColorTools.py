from PyQt6.QtGui import QColor
from PyQtPlus.QtCorePlus import QInterpolationTools

class QColorTools:
    @classmethod
    def lerp(cls, a: QColor, b: QColor, t: float) -> QColor:
        col = QColor()
        col.setRedF(QInterpolationTools.lerp(a.redF(), b.redF(), t))
        col.setGreenF(QInterpolationTools.lerp(a.greenF(), b.greenF(), t))
        col.setBlueF(QInterpolationTools.lerp(a.blueF(), b.blueF(), t))
        return col
