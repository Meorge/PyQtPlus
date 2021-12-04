from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPaintEvent, QPainter, QPixmap
from PyQt6.QtWidgets import QGridLayout, QHBoxLayout, QLabel, QSizePolicy, QVBoxLayout, QWidget

class QOnboardingItem(QWidget):
    def __init__(self, parent=None, title=None, body=None):
        super().__init__(parent)

        self.__leftIcon = QLabel()
        self.__leftIcon.setPixmap(QPixmap('New.svg').scaledToHeight(40, Qt.TransformationMode.SmoothTransformation))
        self.__headerLabel = QLabel('' if title is None else title)

        self.__headerFont = self.__headerLabel.font()
        self.__headerFont.setBold(True)
        self.__headerLabel.setFont(self.__headerFont)

        self.__bodyLabel = QLabel('' if body is None else body)
        self.__bodyLabel.setWordWrap(False)

        self.__bodyLabel.setWindowOpacity(0.5)

        self.__bodyFont = self.__bodyLabel.font()
        # self.__bodyFont.seta

        self.__topLy = QHBoxLayout(self)
        self.__topLy.addWidget(self.__leftIcon, stretch=0)
    
        self.__textLy = QVBoxLayout()
        self.__textLy.setSpacing(0)
        self.__textLy.addWidget(self.__headerLabel, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeading)
        self.__textLy.addWidget(self.__bodyLabel, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeading)
        self.__topLy.addLayout(self.__textLy, stretch=1)

        self.__sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.__headerLabel.setSizePolicy(self.__sizePolicy)
        self.__bodyLabel.setSizePolicy(self.__sizePolicy)
        self.setSizePolicy(self.__sizePolicy)

    def title(self) -> str: return self.__headerLabel.text()
    def setTitle(self, value: str): self.__headerLabel.setText(value)

    def body(self) -> str: return self.__bodyLabel.text()
    def setBody(self, value: str): self.__bodyLabel.setText(value)

    def paintEvent(self, a0: QPaintEvent) -> None:
        QPainter(self).drawRect(self.rect())

