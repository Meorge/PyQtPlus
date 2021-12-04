from typing import Callable, Union
from PyQt6.QtCore import pyqtBoundSignal

# this is defined in QtCore but I can't import it :(
PYQT_SLOT = Union[Callable[..., None], pyqtBoundSignal]