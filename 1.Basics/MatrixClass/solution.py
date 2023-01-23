class Matrix:
    MAX_SIZE = 1000

    def __init__(self, max_size=None):
        # MAX_SIZE = max_size or MAX_SIZE #check late
        if max_size:
            MAX_SIZE = max_size
        self._matrix = [None for _ in range(1)]

    def append(self, element=None):
        # если добавляемый элемент - None, возвращаем матрицу
        if element is None:
            return
        # узнаем индекс первого "нулевого" элемента
        idx = self._matrix.index(None)
        # добавляем элемент
        self._matrix[idx] = element
        # определяем размер матрицы
        size = int(len(self._matrix) ** 0.5)

        # print("size", len(self._matrix))
        # проверяем нужно ли увеличивать размер матрицы

        if idx == size * (size - 1):
            # увеличиваем размер матрицы
            self._matrix.extend(
                [None, ] * ((size + 1) ** 2 - len(self._matrix)))
        # возвращаем матрицу
        # return matrix

    def pop(self): 
        if len(self._matrix) == 1:  # check later, maybe it single element will be None
            raise IndexError

        idx = self._matrix.index(None) - 1
        return_val = self._matrix[idx]
        self._matrix[idx] = None

        matrix_side_size = int(len(self._matrix) ** 0.5)
        size_of_reduced_matrix = len(self._matrix) - 2 * matrix_side_size + 1
        one_side_reduced_mtrx = int(size_of_reduced_matrix ** 0.5)
        
        if size_of_reduced_matrix - idx >= one_side_reduced_mtrx:
            del self._matrix[-size_of_reduced_matrix]
        else:
            pass

        return return_val

    def __str__(self):
        result = ''
        size = int(len(self._matrix) ** 0.5)
        for row in range(size):
            result += ' '.join([str(i)
                               for i in self._matrix[size * row:size * (row + 1)]]) + '\n'
        return result  # check last space later

    @classmethod
    def from_iter(cls, iter_obj, max_size=None):
        pass


def main():
    matrix = Matrix()
    print(type(matrix))
    print(matrix)

    for i in range(1, 14):
        matrix.append(i)
        print(matrix)
        print('*' * 10)

    print('matrix_pop', matrix.pop())
    print(matrix)


main()
