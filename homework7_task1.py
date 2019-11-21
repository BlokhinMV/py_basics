class Matrix:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        return str("\n".join(["\t".join([str(j) for j in i]) for i in self.list]))

    def __add__(self, other):
        if (len(self.list) != len(other.list)) or (len(self.list[0]) != len(other.list[0])):
            print('Складывать можно только матрицы одинакового размера')
            return

        return Matrix([[(self.list[i][j] + other.list[i][j]) for j in range(len(self.list[0]))] for i in range(len(self.list))])




m = Matrix([[1,2,3], [4,5,6], [7,8,9]])
print(m)
n = Matrix([[4,-6,9],[8,2,-1], [0,-5,-9]])
print(m + n)