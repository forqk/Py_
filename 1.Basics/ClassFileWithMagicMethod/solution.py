import os.path
import tempfile

base_path = tempfile.gettempdir()

class File:
    def __init__(self, pathname):
        self.pathname = pathname
        self.current_position = 0;
        
        if not os.path.exists(pathname):
            with open(os.path.join(pathname), 'a+'):
                pass
            
    def __str__(self): 
        return self.pathname

    def __add__(self, obj):
        new_file = File(os.path.join(base_path, tempfile.NamedTemporaryFile().name))
        new_file.write(self.read() + obj.read())
        return new_file

    def __iter__(self):
        return self
            
    def __next__(self):
        with open(self.pathname, 'r') as file:
            file.seek(self.current_position)
            line = file.readline()
            if not line:
                self.current_position = 0;
                raise StopIteration
            self.current_position = file.tell()
            return line
                
    def __str__(self):
        return self.pathname

    def read(self):
        with open(self.pathname, 'r') as file:
            return file.read()

    def write(self, line):
        with open(self.pathname, 'w') as file:
            return file.write(line)


def main():
    path_to_file = 'some_filename'
    print(os.path.exists(path_to_file))
    file_obj = File(path_to_file)
    print(os.path.exists(path_to_file))
    print(file_obj)
    print(file_obj.read())
    print(file_obj.write('some text'))
    print(file_obj.read())
    print(file_obj.write('other text'))
    print(file_obj.read())
    file_obj_1 = File(path_to_file + '_1')
    file_obj_2 = File(path_to_file + '_2')
    print(file_obj_1.write('line 1\n'))
    print(file_obj_2.write('line 2\n'))
    new_file_obj = file_obj_1 + file_obj_2
    print(isinstance(new_file_obj, File))
    print(new_file_obj)
    for line in new_file_obj:
        print(ascii(line))
        
    new_path_to_file = str(new_file_obj)
    print(os.path.exists(new_path_to_file))
    file_obj_3 = File(new_path_to_file)
    print(file_obj_3)
    with open('some_file.txt', 'w') as file:
        file.write('1\n2\n3\n')
    print('файл существует? -', os.path.exists('some_file.txt'))
    file = File('some_file.txt')
    print('содержание файла -', ascii(file.read()))
    print('содержание файла -')
    for row in file:
        print('строка -', ascii(row))
main()
