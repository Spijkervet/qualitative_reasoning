from variables import Magnitude, MagnitudeValues, Derivative, DerivativeValues

class Quantity():

    def __init__(self, magnitude, derivative):
        self.magnitude = magnitude
        self.derivative = derivative

    def __repr__(self):
        return '({}, {})'.format(self.magnitude.val, self.derivative.val)
