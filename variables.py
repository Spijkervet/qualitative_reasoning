from enum import IntEnum

class MagnitudeValues(IntEnum):
    ZERO = 0
    PLUS = 1
    MAX = 999

class DerivativeValues(IntEnum):
    MIN = -1
    ZERO = 0
    MAX = 1

class Magnitude():

    def __init__(self, val, maximum=MagnitudeValues.MAX):
        self.val = MagnitudeValues(val)
        self.maximum = maximum

class Derivative():

    def __init__(self, val, maximum=DerivativeValues.MAX):
        self.val = DerivativeValues(val)
        self.maximum = maximum
