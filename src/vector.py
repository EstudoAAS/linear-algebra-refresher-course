from math import sqrt, acos, pi
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'
    NO_UNIQUE_PARALLEL_COMPONENT_MSG= 'There is not a unique parallel component to the zero vector'
    NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG = 'There is not a unique orthogonal component to the zero vector'
    ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG = 'Only defined in tow or three dimensions'

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

    def dot(self, v):
            return sum([x * y for x,y in zip(self.coordinates, v.coordinates)])


    def angle_with(self,v, in_degrees = False):
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            # print(u2)
            # print(u1.dot(u2))
            angle_in_radians = acos(u1.dot(u2))

            if in_degrees:
                degrees_per_radian = 180. / pi
                return angle_in_radians * degrees_per_radian #return degrees(acos((self.dot(v))/Decimal(self.magnitude() * v.magnitude())))
            else:
                return angle_in_radians #return acos((self.dot(v))/Decimal(self.magnitude() * v.magnitude()))

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with the zero vector')
            else:
                raise e

    def plus(self,v):
        new_coordinates =[x + y for x,y in zip(self.coordinates, v.coordinates)]
        return new_coordinates

    def minus(self,v):
        return [x - y for x,y in zip(self.coordinates, v.coordinates)]

    def times_scalar(self,c):
        return Vector([Decimal(c) * x for x in self.coordinates])

    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        #return Decimal(sqrt(sum(coordinates_squared))) <<<<<<<<<<<<<<<<<<<<<<<<<< Precision problem causes acos < -1, but: -1<=acos<=1
        return Decimal(sum(coordinates_squared)).sqrt()

    def normalized(self):
        try:
            return self.times_scalar(Decimal('1.0') / Decimal(self.magnitude()))
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    def isParallel_aas(self, v):
        l1 = []
        l2 = []
        for i in range(len(self.coordinates)):
            l1.append(Decimal(self.coordinates[i].__abs__()))
            l2.append(Decimal(v.coordinates[i].__abs__()))

        if (sum(l1) == 0) or (sum(l2) == 0):
            return True
        try:
            u1 = self.normalized()
            u2 = v.normalized()
        except ZeroDivisionError:
            return True
        l1.clear()
        l2.clear()
        for i in range(len(u1.coordinates)):
            l1.append(Decimal(u1.coordinates[i].__abs__()))
            l2.append(Decimal(u2.coordinates[i].__abs__()))

        print("l1= ",l1)
        print("l2= ", l2)
        return Vector(l1).__eq__(Vector(l2))

    def isOrthogonal_aas(self, v):
        if self.dot(v) == 0:
            return True
        else:
            return False

    def is_orthogonal_to(self, v, tolerance=1e-10):
        return abs(self.dot(v)) < tolerance

    def is_parallel_to(self, v):
        return ( self.is_zero() or v.is_zero() or self.angle_with(v) == 0 or self.angle_with(v) == pi)

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    def component_parallel_to(self, basis):
        try:
            u = basis.normalized()
            weight = self.dot(u)
            return u.times_scalar(weight)
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e

    def component_orthogonal_to(self, basis):
        try:
            projection = self.component_parallel_to(basis)
            return Vector(self.minus(projection))
        except Exception as e:
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(self.NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG)
            else:
                raise e

    def decomposition(self, b):
        return str(self.component_parallel_to(b)) + " + " + str(self.component_orthogonal_to(b))

    def cross(self, v):
        try:
            x_1, y_1, z_1 = self.coordinates
            x_2, y_2, z_2 = v.coordinates

            new_coordinates = [ Decimal((y_1*z_2)-(y_2*z_1)),
                                Decimal(-((x_1*z_2) - (x_2*z_1))),
                                Decimal((x_1*y_2) - (x_2*y_1)) ]
            return Vector(new_coordinates)

        except ValueError as e:
            msg = str(e)
            if msg == 'not enough values to unpack (expected 3, got 2)': #if msg == 'need more than 2 values to unpack':
                self_embedded_in_R3 = Vector(self.coordinates + ('0',))
                v_embedded_in_R3 = Vector(v.coordinates + ('0',))
                return self_embedded_in_R3.cross(v_embedded_in_R3)
            elif (msg == 'too many values to unpack' or msg == 'Need at least 2 coordinates'):
                raise Exception(self.ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG)
            else:
                raise e


    def area_of_parallelogram_with(self, v):
        cross_product = self.cross(v)
        return cross_product.magnitude()#return Decimal(r.coordinates[0]**2 + r.coordinates[1]**2 + r.coordinates[2]**2).sqrt()

    def area_of_triangle_with(self, v):
        return Decimal( self.area_of_parallelogram_with(v) / Decimal('2.0'))

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
