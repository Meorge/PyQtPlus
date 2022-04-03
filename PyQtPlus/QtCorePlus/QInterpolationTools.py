from typing import Union

class QInterpolationTools:
    @classmethod
    def lerp(cls, a: Union[float, int], b: Union[float, int], t: float) -> float:
        return a + (b - a) * t

    @classmethod
    def invLerp(cls, v: Union[float, int], a: Union[float, int], b: Union[float, int]) -> float:
        return (v - a) / (b - a)

    @classmethod
    def remap(cls, inMin: Union[float, int], inMax: Union[float, int], outMin: Union[float, int], outMax: Union[float, int], v: Union[float, int]):
        t = cls.invLerp(v, inMin, inMax)
        return cls.lerp(outMin, outMax, t)