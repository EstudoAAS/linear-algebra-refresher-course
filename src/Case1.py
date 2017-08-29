import vector

def main():
    vetor1 = vector.Vector([8.218,-9.341])
    print(vetor1.plus(vector.Vector([-1.129,2.111])))

    vetor2 = vector.Vector([7.119,8.215])
    print(vetor2.minus(vector.Vector([-8.223,0.878])))

    vetor3 = vector.Vector([1.671,-1.012,-0.318])
    print(vetor3.times_scalar(7.41))

main()