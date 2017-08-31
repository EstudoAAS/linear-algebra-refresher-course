import vector


def main():

    v1 = vector.Vector([3.039,1.879])
    b1 = vector.Vector([0.825,2.036])
    print(v1.component_parallel_to(b1))

    v2 = vector.Vector([-9.88,-3.264,-8.159])
    b2 = vector.Vector([-2.155,-9.353,-9.473])
    print(v2.component_orthogonal_to(b2))

    v3 = vector.Vector([3.009,-6.172,3.692,-2.51])
    b3 = vector.Vector([6.404,-9.144,2.759,8.718])
    print(v3.decomposition(b3))


main()