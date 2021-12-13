from typing import Union
from PyQt6.QtCore import QObject, QRect, QRectF, Qt
from PyQt6.QtGui import QColor, QColorConstants, QGradient, QPaintEvent, QPainter, QPixmap
from PyQt6.QtWidgets import QWidget
from PyQt6.QtSvg import QSvgRenderer

class QMonochromeGraphicLabel(QWidget):
    def __init__(self,
        parent: QObject = None,
        svgPath: str = None,
        tintColor: Union[QColor, QGradient] = None,
        aspectRatioMode: Qt.AspectRatioMode = Qt.AspectRatioMode.IgnoreAspectRatio
        ):
        super().__init__(parent)
        self.__tintColor: Union[QColor, QGradient] = None
        self.__svgPath: str = ''
        self.__aspectRatioMode = Qt.AspectRatioMode.IgnoreAspectRatio

        self.setTintColor(tintColor)
        self.setSvgPath(svgPath)
        self.setAspectRatioMode(aspectRatioMode)

    def tintColor(self) -> Union[QColor, QGradient]: return self.__tintColor
    def setTintColor(self, color: Union[QColor, QGradient]): self.__tintColor = color

    def svgPath(self) -> str: return self.__svgPath
    def setSvgPath(self, path: str):
        self.__svgPath = path
        self.__svgRenderer = QSvgRenderer(self.__svgPath)
        self.__svgRenderer.setAspectRatioMode(self.__aspectRatioMode)

    def aspectRatioMode(self) -> Qt.AspectRatioMode: return self.__aspectRatioMode
    def setAspectRatioMode(self, mode: Qt.AspectRatioMode):
        self.__aspectRatioMode = mode
        self.__svgRenderer.setAspectRatioMode(self.__aspectRatioMode)

    def paintEvent(self, event: QPaintEvent) -> None:
        self.__img = QPixmap(self.width(), self.height())
        self.__img.fill(QColorConstants.Transparent)
        with QPainter(self) as p:
            p: QPainter
            with QPainter(self.__img) as qp:
                qp: QPainter
                if self.__svgPath:
                    self.__svgRenderer.render(qp, QRectF(self.__img.rect()))
                    qp.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
                    qp.fillRect(self.__img.rect(), QColorConstants.Black if self.__tintColor is None else self.__tintColor)

            p.drawPixmap(self.rect(), self.__img, self.__img.rect())
