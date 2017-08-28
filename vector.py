from math import sqrt, acos, degrees
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)
            if self.dimension == 1:
                raise ValueError

        except ValueError:
            if self.dimension == 1:
                raise ValueError('Need at least 2 coordinates')
            else:
                raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def plus(self,v):
        new_coordinates =[x + y for x,y in zip(self.coordinates, v.coordinates)]
        return new_coordinates

    def minus(self,v):
        return [x - y for x,y in zip(self.coordinates, v.coordinates)]

    def times_scalar(self,c):
        return [Decimal(c) * x for x in self.coordinates]

    def magnitude(self):
        return sqrt(sum([x**2 for x in self.coordinates]))

    def normalized(self):
        try:
            return self.times_scalar(Decimal('1.0') / self.magnitude())
        except ZeroDivisionError:
            raise Exception(CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    def dot(self, v):
            return sum([x * y for x,y in zip(self.coordinates, v.coordinates)])

    def angle_with(self,v, in_degrees = False):
        try:
            if in_degrees:
                return degrees(acos((self.dot(v))/Decimal(self.magnitude() * v.magnitude())))
            else:
                return acos((self.dot(v))/Decimal(self.magnitude() * v.magnitude()))
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with the zero vector')
            else:
                raise e

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
