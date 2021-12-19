from typing import Union

class QInterpolationTools:
    @classmethod
    def lerp(cls, a: Union[float, int], b: Union[float, int], t: float) -> float:
        return a + (b - a) * t