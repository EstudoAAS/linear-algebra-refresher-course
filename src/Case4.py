import vector


def main():

    """v1 = vector.Vector([1, 1, 1])
    v2 = vector.Vector([-10, -10, -10])
    v3 = vector.Vector([3,0])
    v4 = vector.Vector([0,1])
    print("É paralelo? ",v1.isParallel(v2))
    print("É ortogonal? ", v3.isOrthogonal(v4))"""

    v1 = vector.Vector([-7.579,-7.88])
    w1 = vector.Vector([22.737,23.64])
    v2 = vector.Vector([-2.029,9.97,4.172])
    w2 = vector.Vector([-9.231,-6.639,-7.245])
    v3 = vector.Vector([-2.328,-7.284,-1.214])
    w3 = vector.Vector([-1.821,1.072,-2.94])
    v4 = vector.Vector([2.118,4.827])
    w4 = vector.Vector([0,0])

    """print("v1.w1 É paralelo? ", v1.isParallel(w1))
    print("v1.w1 É ortogonal? ", v1.isOrthogonal(w1))
    print("v2.w2 É paralelo? ", v2.isParallel(w2))
    print("v2.w2 É ortogonal? ", v2.isOrthogonal(w2))
    print("v3.w3 É paralelo? ", v3.isParallel(w3))
    print("v3.w3 É ortogonal? ", v3.isOrthogonal(w3))
    print("v4.w4 É paralelo? ", v4.isParallel(w4))
    print("v4.w4 É ortogonal? ", v4.isOrthogonal(w4))"""

    print("v1.w1 É paralelo? ", v1.is_parallel_to(w1))
    print("v1.w1 É ortogonal? ", v1.is_orthogonal_to(w1))
    print("v2.w2 É paralelo? ", v2.is_parallel_to(w2))
    print("v2.w2 É ortogonal? ", v2.is_orthogonal_to(w2))
    print("v3.w3 É paralelo? ", v3.is_parallel_to(w3))
    print("v3.w3 É ortogonal? ", v3.is_orthogonal_to(w3))
    print("v4.w4 É paralelo? ", v4.is_parallel_to(w4))
    print("v4.w4 É ortogonal? ", v4.is_orthogonal_to(w4))

main()