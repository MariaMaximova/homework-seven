#!usr/bin/python3
# -*- coding: utf-8 -*-


def gcd(numerator, denominator):
    """greatest common factor"""
    while denominator != 0:
        t = denominator
        denominator = numerator % denominator
        numerator = t
    return numerator


class Fraction:

    def __init__(self, numerator, denominator):
        """initiate fraction"""
        self.numerator, self.denominator = numerator, denominator

    def __add__(self, other):
        """initiate add"""
        top, bottom = self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator
        smallest = gcd(top, bottom)
        return Fraction(top // smallest, bottom // smallest)

    def __mul__(self, other):
        """initiate multiply"""
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __sub__(self, other):
        """initiate subvision"""
        top, bottom = self.numerator * other.denominator - other.numerator * self.denominator, self.denominator * other.denominator
        smallest = gcd(top, bottom)
        return Fraction(top // smallest, bottom // smallest)

    def __truediv__(self, other):
        """initiate division"""
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
    
    def __pow__(self, power):
        """initiate a power"""
        return Fraction(self.numerator ** power, self.denominator ** power)

    def __str__(self):
        """return all results"""
        return '{}/{}'.format(self.numerator, self.denominator)


if __name__ == "__main__":

    fraction1 = Fraction(4, 5)
    print(fraction1 + Fraction(1, 8))
    print(Fraction(5, 7) / 10)
    print(Fraction(40, 70))
    print(Fraction(1, 6) + Fraction(1, 3))
    print(Fraction(1, 2) + Fraction(3, 4) + Fraction(1, 9) * Fraction(3, 5))
    print(Fraction(5, 7)**2)
