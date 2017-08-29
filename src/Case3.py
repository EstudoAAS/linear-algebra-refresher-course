import vector


def main():
    print(vector.Vector([7.887,4.138]).dot(vector.Vector([-8.802,6.776])))
    print(vector.Vector([-5.955,-4.904,-1.874]).dot(vector.Vector([-4.496,-8.755,7.103])))

    print(vector.Vector([3.183,-7.627]).angle_with(vector.Vector([-2.668,5.319])))
    print(vector.Vector([7.35,0.221,5.188]).angle_with(vector.Vector([2.751,8.259,3.985]),True))


main()