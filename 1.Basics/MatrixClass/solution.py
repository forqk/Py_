class Matrix:
    MAX_SIZE = 1000
    def __init__(self, max_size=None):
        self.MAX_SIZE = max_size or self.MAX_SIZE #check late
        
        self._matrix = [None for _ in range(1)]

    def append(self, element=None):
        if element is None: # если добавляемый элемент - None, возвращаем матрицу
            return
        
        idx = None
        
        try:
            idx = self._matrix.index(None)  # узнаем индекс первого "нулевого" элемента
        except:
            raise IndexError
     
        self._matrix[idx] = element    # добавляем элемент
        
        size = int(len(self._matrix) ** 0.5) # определяем размер матрицы
        
        if(size < self.MAX_SIZE) :
            if idx == size * (size - 1):  # проверяем нужно ли увеличивать размер матрицы
                self._matrix.extend([None, ] * ((size + 1) ** 2 - len(self._matrix)))  # увеличиваем размер матрицы
      

    def pop(self): 
        print(len(self._matrix))
        if len(self._matrix) == 1:  # check later, maybe it single element will be None
            raise IndexError
        
        
        try:
            idx = self._matrix.index(None) - 1
        except:
            idx = len(self._matrix)-1;
            
        return_val = self._matrix[idx]
        self._matrix[idx] = None

        matrix_side_size = int(len(self._matrix) ** 0.5)
        size_of_reduced_matrix = len(self._matrix) - 2 * matrix_side_size + 1
        one_side_reduced_mtrx = int(size_of_reduced_matrix ** 0.5)
        
      
        if size_of_reduced_matrix - idx >= one_side_reduced_mtrx:
            print('ужимаем нахой')
            self._matrix = self._matrix[:-size_of_reduced_matrix + idx -1]
            print(self._matrix)
            
        return return_val

    def __str__(self):
        result = ''
        size = int(len(self._matrix) ** 0.5)
        for row in range(size):
            result += ' '.join([str(i)
                               for i in self._matrix[size * row:size * (row + 1)]]) + '\n'
        return result.strip('\n')  # check last space later

    @classmethod
    def from_iter(cls, iter_obj, max_size=None):
        matrix = Matrix(max_size)
        
        try:
            lst = [i for i in iter_obj if  i != None]
            for i in lst:
                matrix.append(i)
        except IndexError:
            raise IndexError
        except TypeError:
            raise TypeError
            
        
        return matrix
            
        

def main():
#     matrix = Matrix()
#     print(type(matrix))
#     print(matrix)

#     for i in range(1, 4):
#         matrix.append(i)
#         print(matrix)
#         print('*' * 10)

#     print(matrix.pop())
#     print(matrix)
    
#     matrix.append(None)
#     print(matrix)
    
#     matrix = Matrix(max_size=2)
#     for i in range(1, 5):
#         matrix.append(i)
#     print(matrix)
#    # matrix.append(5)
    
#     matrix = Matrix.from_iter([1,2,3])
#     print(matrix)
    
#     matrix = Matrix.from_iter(range(3))
#     print(matrix)
    
#     matrix = Matrix.from_iter(range(9), max_size=3)
#     print(matrix)
    
   # matrix = Matrix.from_iter(range(30), max_size=3)
    
  #  matrix = Matrix.from_iter([None,1,2,None,None,3,None,4,None,None,None])
  #  print(matrix)
    matrix = Matrix(max_size=3)
    # for i in range(1, 10):
    #     matrix.append(i)
    # print(matrix)
    # print(matrix.pop())
    # print(matrix)
    for i in range(1, 10):
        matrix.append(i)
        print(matrix)
        
    for i in range(9, 0, -1):
        item = matrix.pop()
        print('удаляемый елемент', item)
        print(matrix)
        print('\n')


main()
