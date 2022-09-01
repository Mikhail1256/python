class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    def __str__(self):
        str = ['','','']
        for matrix1 in range(len(self.matrix)):
            for matrix2 in range(len(self.matrix[matrix1])):
                for matrix3 in self.matrix[matrix1][matrix2]:
                    str[matrix2] += f'{matrix3} '
                str[matrix2] += '\t\t'
        return f'{str[0]}\n{str[1]}\n{str[2]}'

    def __add__(self,target):
        new_matrix = []
        for width in range(len(self.matrix[0])):
            new_matrix.append([])
            for length in range(len(self.matrix[0][0])):
                new_matrix[width].append(self.matrix[0][width][length]+target.matrix[0][width][length])

        return new_matrix
            


matrix = Matrix([[[31,32],[37,43],[51,86]],[[3,5,32],[2,4,6],[-1,64,-8]],[[3,5,8,3],[8,3,7,1]]])
matrix2 = Matrix([[[31,32],[37,43],[51,86]],[[3,5,32],[2,4,6],[-1,64,-8]],[[3,5,8,3],[8,3,7,1]]])
print(matrix)
print(matrix+matrix2)

#немного накосячил с пониманием ТЗ, не стал переделывать полностью