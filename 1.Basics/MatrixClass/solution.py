class Matrix:
    MAX_SIZE = 1000
    
    def __init__(self, max_size=None):
        #MAX_SIZE = max_size or MAX_SIZE #check late
        if max_size:
            MAX_SIZE = max_size
        self._matrix =[None for _ in range(1)]

    
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
       
        
        #print("size", len(self._matrix))
        # проверяем нужно ли увеличивать размер матрицы

        if idx == size * (size - 1):
        # увеличиваем размер матрицы
            self._matrix.extend([None, ] * ((size + 1) ** 2 - len(self._matrix)))
        # возвращаем матрицу
        # return matrix

    def pop(self):
        pass # 1. найди индекс 2. сделать квадрантную матрицу меньше на одну сторону и столбец.
   

    def __str__(self):
        result = ''
        size = int(len(self._matrix) ** 0.5)
        for row in range(size):
            result += ' '.join([str(i) for i in self._matrix[size * row:size * (row + 1)]]) + '\n'
        return result #check last space later
        

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
main()