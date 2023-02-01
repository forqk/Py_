import os.path
import tempfile
import sys

base_path = tempfile.gettempdir()

class File:
    def __init__(self, pathname):
        self.pathname = pathname
        
        with open(os.path.join(base_path, pathname), 'a+'):
            pass
        
    def __str__(self):
        return self.pathname
    
    def __add__(self, obj):
        pass
        
    
    def read(self):
        with open(os.path.join(base_path, self.pathname), 'r') as file:
            return file.read()
    
    def write(self, line):
        with open(os.path.join(base_path, self.pathname), 'w+') as file:
            return file.write(line)
        
            
def main():
    path_to_file = 'some_filename'
    print(os.path.exists(os.path.join(base_path, path_to_file)))
    file_obj = File(path_to_file)
    print(os.path.exists(os.path.join(base_path, path_to_file)))
    print(file_obj)
    print(file_obj.read())
    print(file_obj.write('some text'))
    print(file_obj.read())
    print(file_obj.write('other text'))
    print(file_obj.read())
    file_obj_1 = File(path_to_file + '_1')
    file_obj_2 = File(path_to_file + '_2')
    print(file_obj_1.write('line 1\n'))
    print(file_obj_2.write('line 2\n'));
    
    
main()