def create_matrix(size):
    """
    Функция принимает на вход размер квадратной матрицы. Возвращает 'пустую' матрицу
    размером size x size, (все элементы матрицы имеют значение равное None).
    :param size: int > 0
    :return: list 
    """
    lst = [[None]*size for i in range(0, size)]
    return lst

def ExpandMatrix(matrix, element):
    for row in matrix:
        row.append(None)
    matrix.append([None]*len(matrix[0]))
    
    lst = []
    for row in matrix:
        for col in row:
            if col != None:
                lst.append(col)
    lst.append(element)
  
    pos = 0;
    
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if pos >= len(lst):
                matrix[row][col] = None
            else:
                matrix[row][col] = lst[pos]
            pos += 1;
    return matrix
 
def add_element(element, matrix):
    if element == None: #Добавление нулевого игнорируется
        return
    """
    Функция добавляет element в матрицу matrix и при необходимости изменяет размер
    матрицы. Возвращает полученную матрицу.
    :param element: string
    :param matrix: list
    :return: list
    """
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == None:
                if i == len(matrix)-1 and j == 0:
                    ExpandMatrix(matrix, element)           
                    return matrix
                matrix[i][j] = element;
                return matrix

def matrix_to_string(matrix):
    """
    Функция создает строковое представление matrix - строку, в которой строки матрицы 
    разделены переносом строки, а элементы строки разделены пробелами.
    :param matrix: list
    :return: string
    """
    # вставьте вашу реализацию функции здесь
    line = ''
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            line += str(matrix[i][j])
            if(j != len(matrix[0])-1):
                line += ' '
            else:
                line +='\n'

    return line

def main():
    matrix = create_matrix(4)
    for i in range(13):
        matrix = add_element(i, matrix)        
        print('ваш вывод')
        print(matrix_to_string(matrix))
    
    matrix = create_matrix(2)
    print(matrix_to_string(matrix))
    matrix = add_element(5, matrix)
    matrix = add_element(7, matrix)
    print(matrix_to_string(matrix))
    matrix = add_element(9, matrix)
    print(matrix_to_string(matrix))
        
main()