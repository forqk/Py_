class Matrix:
    MAX_SIZE = 1000

    def __init__(self, max_size=None):
        self.MAX_SIZE = max_size or self.MAX_SIZE
        self._matrix = [None for _ in range(1)]

    def append(self, element=None):
        if element is None:
            return
        try:
            idx = self._matrix.index(None)
        except:
            raise IndexError

        self._matrix[idx] = element
        size = int(len(self._matrix) ** 0.5)

        if size < self.MAX_SIZE and idx == size * (size - 1):
            self._matrix.extend(
                [None, ] * ((size + 1) ** 2 - len(self._matrix)))

    def pop(self):
        if len(self._matrix) == 1:
            raise IndexError
        try:
            idx = self._matrix.index(None) - 1
        except:
            idx = len(self._matrix)-1

        return_val = self._matrix[idx]
        self._matrix[idx] = None

        matrix_side_size = int(len(self._matrix) ** 0.5)
        size_of_reduced_matrix = len(self._matrix) - 2 * matrix_side_size + 1

        if size_of_reduced_matrix - idx >= int(size_of_reduced_matrix ** 0.5):
            self._matrix = self._matrix[:-matrix_side_size]
        return return_val

    def __str__(self):
        result = ''
        size = int(len(self._matrix) ** 0.5)
        for row in range(size):
            result += ' '.join([str(i)
                               for i in self._matrix[size * row:size * (row + 1)]]) + '\n'
        return result.strip('\n')

    @classmethod
    def from_iter(cls, iter_obj, max_size=None):
        matrix = Matrix(max_size)

        lst = [i for i in iter_obj if i != None]
        for i in lst:
            matrix.append(i)

        return matrix
