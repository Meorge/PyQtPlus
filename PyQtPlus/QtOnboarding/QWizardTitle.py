from typing import Optional
from PyQt6.QtCore import QAbstractAnimation, QEasingCurve, QParallelAnimationGroup, QPoint, QPropertyAnimation, QTimer, Qt
from PyQt6.QtGui import QColorConstants, QFont, QPaintEvent, QPainter, QPixmap
from PyQt6.QtWidgets import QSizePolicy, QVBoxLayout, QWidget, QLabel

class QWizardTitle(QWidget):
    def __init__(self, parent=None, title=None, subtitle=None, icon=None, iconSize=None):
        super().__init__(parent)

        self.icon = QLabel(self)

        self.title = QLabel(self)
        self.titleFont = QFont()
        self.titleFont.setBold(True)
        self.titleFont.setPointSizeF(self.titleFont.pointSizeF() * 2.0)
        self.title.setFont(self.titleFont)
        self.title.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)

        self.subtitle = QLabel(self)
        self.subtitle.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)

        self.ly = QVBoxLayout(self)
        self.ly.setSpacing(0)
        self.ly.addWidget(self.icon, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.ly.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.ly.addWidget(self.subtitle, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
    
        self.setLayout(self.ly)



        self.__iconPath = icon
        self.setTitle(title)
        self.setSubtitle(subtitle)
        self.setIcon(icon)
        self.setIconSize(iconSize)
        
    def setTitle(self, value: Optional[str]):
        if value == '' or value is None:
            self.title.clear()
            self.title.setVisible(False)
        else:
            self.title.setText(value)
            self.title.setVisible(True)

    def setSubtitle(self, value: Optional[str]):
        if value == '' or value is None:
            self.subtitle.clear()
            self.subtitle.setVisible(False)
        else:
            self.subtitle.setText(value)
            self.subtitle.setVisible(True)

    def setIcon(self, iconPath: Optional[str]):
        self.__iconPath = iconPath
        if iconPath is None:
            self.icon.clear()
            self.icon.setVisible(False)
            self.__iconPath = None
        else:
            self.icon.setPixmap(QPixmap(iconPath).scaledToHeight(self.icon.height(), Qt.TransformationMode.SmoothTransformation))
            self.icon.setVisible(True)

    def setIconSize(self, size: Optional[int]):
        self.icon.setFixedHeight(70 if size is None else size)
        self.setIcon(self.__iconPath)


    def animateIn(self):
        QTimer.singleShot(200, self.__actuallyAnimateIn)

    def __actuallyAnimateIn(self):
        globalPos = self.mapToParent(self.pos())

        self.__moveAnim = QPropertyAnimation(
            self,
            b'pos',
            duration=800,
            easingCurve=QEasingCurve.Type.OutCubic,
            startValue=self.mapFromParent(globalPos + QPoint(0, 100)),
            endValue=self.mapFromParent(globalPos)
        )


        animGroup = QParallelAnimationGroup(self)
        animGroup.addAnimation(self.__moveAnim)
        animGroup.start(QAbstractAnimation.DeletionPolicy.DeleteWhenStopped)