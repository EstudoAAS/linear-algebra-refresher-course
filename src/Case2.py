import vector

def main():
    print(vector.Vector([-0.221,7.437]).magnitude())
    print(vector.Vector([5.581,-2.136]).normalized())

    print(vector.Vector([8.813,-1.331,-6.247]).magnitude())
    print(vector.Vector([1.996,3.108,-4.554]).normalized())

main()