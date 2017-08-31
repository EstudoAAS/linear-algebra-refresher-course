import vector


def main():

    v1 = vector.Vector([8.462,7.893,-8.187])
    w1 = vector.Vector([6.984,-5.975,4.778])
    print(v1.cross_product(w1))

    v2 = vector.Vector([-8.987,-9.838,5.031])
    w2 = vector.Vector([-4.268,-1.861,-8.866])
    print(v2.area_of_parallelogram(w2))

    v3 = vector.Vector([1.5,9.547,3.691])
    w3 = vector.Vector([-6.007,0.124,5.772])
    print(v3.area_of_triangle(w3))






main()