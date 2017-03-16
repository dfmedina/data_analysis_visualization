class Matrix(object):

    def sum_matrix(self, m1, m2):
        result = [[0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]]
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m2)):
                    result[i][j] += m1[i][k] + m2[k][j]
        return result

    def mult_matrix(self, m1, m2):
        result = [[0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]]
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m2)):
                    result[i][j] += m1[i][k] * m2[k][j]
        return result

    def scalar_product(self, m, value):
        for i in range(len(m[0])):
            for j in range(len(m)):
                m[i][j] *= value
        return m


if __name__ == '__main__':

    # 3x3 matrix
    X = [[12,7,3],
        [4 ,5,6],
        [7 ,8,9]]
    # 3x4 matrix
    Y = [[5,8,1,2],
        [6,7,3,0],
        [4,5,9,1]]

    matrix_operation = Matrix()
    print matrix_operation.sum_matrix(X, Y)
    print matrix_operation.mult_matrix(X, Y)
    print matrix_operation.scalar_product(X, 2)
