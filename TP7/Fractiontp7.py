import math


class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : November 2020
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : num and den must be int
        POST : initialize a new Fraction object with the num and den that the user
        entered or the default ones
        RAISES : ZeroDivisionError if self.__den == 0
        """
        assert isinstance(num, int)
        assert isinstance(den, int)
        self.__num = int(num)
        self.__den = int(den)
        if self.__den == 0:
            raise ZeroDivisionError("den cannot equals 0")

    @property
    def numerator(self):
        return self.__num

    @property
    def denominator(self):
        return self.__den

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : none
        POST : returns textual representation of the reduced fraction
        """
        gcd = self.__greatest_common_divisor()
        new_str = str(int(self.__num / gcd)) + " / " + str(int(self.__den / gcd))
        return new_str

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : none
        POST : returns textual representation of the reduced form of the fraction as mixed numbers
        """
        if self.__num % self.__den == 0:
            return str(int(self.__num / self.__den))
        if self.__num == -1:
            return str(self)
        if self.__num < -1:
            new_str = str(math.ceil(self.__num / self.__den)) + " - " + str(self.__num % self.__den) + " / " + str(
                self.__den)
        else:
            new_str = str(self.__num // self.__den) + " + " + str(self.__num % self.__den) + " / " + str(self.__den)
        return new_str

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : none
         POST : returns new Fraction whcih the value is the sum of the two fractions
        RAISES : TypeError if other is not int or Fraction
         """
        if not isinstance(other, int) and not isinstance(other, Fraction):
            raise TypeError("Invalid arg type, other must be int or Fraction")
        if isinstance(other, int):
            return self + Fraction(other, 1)  # recursion to have other as a fraction
        elif isinstance(other, Fraction):
            num1 = self.__num
            den1 = self.__den
            num2 = other.numerator
            den2 = other.denominator

            num1 *= den2
            den1 *= den2

            num2 *= self.__den

            num_res = num1 + num2

            return Fraction(num_res, den1)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : none
        POST : returns a new fraction of the subtraction of the two fractions
        RAISES : TypeError if other is not int or Fraction
        """
        if not isinstance(other, int) and not isinstance(other, Fraction):
            raise TypeError("Invalid arg type, other must be int or Fraction")
        if isinstance(other, int):
            return self - Fraction(other, 1)
        elif isinstance(other, Fraction):
            num1 = self.__num
            den1 = self.__den
            num2 = other.numerator
            den2 = other.denominator

            num1 *= den2
            den1 *= den2

            num2 *= self.__den
            num_res = num1 - num2

            return Fraction(num_res, den1)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : none
        POST : returns a new fraction containing the multiplication of the two fractions
        RAISES : TypeError if other is not int or Fraction
        """
        if not isinstance(other, int) and not isinstance(other, Fraction):
            raise TypeError("Invalid arg type, other must be int or Fraction")
        if isinstance(other, int):
            return self * Fraction(other, 1)
        elif isinstance(other, Fraction):
            return Fraction(self.__num * other.numerator, self.__den * other.denominator)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : none
        POST : returns a new fraction containing the division of the two fractions
        RAISES : TypeError if other is not int or Fraction
        """
        if not isinstance(other, int) and not isinstance(other, Fraction):
            raise TypeError("Invalid arg type, other must be int or Fraction")
        if other.numerator == 0:
            raise ZeroDivisionError
        if isinstance(other, int):
            return self.__truediv__(Fraction(other, 1))
        elif isinstance(other, Fraction):
            return self * Fraction(other.denominator, other.numerator)

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : other must be int
        POST : returns a new Fraction containing initial fraction to the power of the other's value
        """
        if not isinstance(other, int):
            raise TypeError("Invalid arg type, other must be int")
        return Fraction(int(pow(self.__num, other)), int(pow(self.__den, other)))

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE: none
        POST: returns if the two reduced fractions are the same or not
        RAISES : TypeError if other is not int or Fraction
        """
        if not isinstance(other, int) and not isinstance(other, Fraction):
            raise TypeError("Invalid arg type, other must be int or Fraction")
        if isinstance(other, int):
            return self == Fraction(other, 1)

        gcd1 = self.__greatest_common_divisor()
        gcd2 = other.__greatest_common_divisor()
        return self.__num / gcd1 == other.numerator / gcd2 and self.__den / gcd1 == other.denominator / gcd2

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : none
        POST : returns if a fraction value is 0 or not
        """
        return self.__num == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : none
        POST : returns if a fraction is an integer or not
        """
        return self.__num % self.__den == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : none
        POST : returns if the absolute value of the fraction is under 1
        """

        return abs(self.__num / self.__den) < 1

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : none
        POST : returns if the fraction's numerator equals one in reduced form
        """
        gcd = self.__greatest_common_divisor()
        return self.__num / gcd == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacent if the absolute value of the difference them is a unit fraction

        PRE : other must be int or Fraction
        POST : returns if the two fractions are adjacent or not
        RAISES : TypeError if other is not int or Fraction
        """
        if not isinstance(other, int) and not isinstance(other, Fraction):
            raise TypeError("Invalid arg type, other must be int or Fraction")
        if isinstance(other, int):
            return self.is_adjacent_to(Fraction(other, 1))
        res = self - other
        return abs(res.numerator) == 1 and res.denominator > 0

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : none
        POST : returns the decimal value of the fraction
        """
        return float(self.__num / self.__den)

    def __greatest_common_divisor(self):
        """Returns the greatest common divisor

        PRE: none
        POST: returns the greatest common divisor of the numerator and denominator

        """

        num = self.__num
        den = self.__den
        while den != 0:
            temp = den
            den = num % den
            num = temp
        return num


if __name__ == "__main__":
    a = Fraction(1, 4)  # 5/20 - 4/20
    b = Fraction(1, 5)
    c = Fraction(5, 2)
    print(b.is_adjacent_to(a))
    print(c.as_mixed_number())
