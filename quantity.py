from variables import Magnitude, MagnitudeValues, Derivative, DerivativeValues

class Quantity():

    def __init__(self, magnitude, derivative):
        self.magnitude = magnitude
        self.derivative = derivative

    def __repr__(self):
        return '({}, {})'.format(self.magnitude.val, self.derivative.val)

    def is_equal(self, quantity):
        if self.magnitude.val == quantity.magnitude.val and self.derivative.val == quantity.derivative.val:
            return True
        return False
