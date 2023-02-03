import os.path
import tempfile
import sys

base_path = tempfile.gettempdir()


class File:
    line_count = 0
    iter_count = 0

    def __init__(self, pathname):
        self.pathname = pathname

        with open(os.path.join(base_path, pathname), 'a+'):
            pass

    def __str__(self):
        return self.pathname

    def __add__(self, obj):
        new_file = File(os.path.join(base_path, "new_file"))
        new_file.write(self.read() + obj.read())
        return new_file

    def __iter__(self):
        return self

    def __next__(self):
        if self.iter_count > self.line_count:
            raise StopIteration 

        with open(os.path.join(base_path, self.pathname), 'r') as file:
            for num_line, line in enumerate(file):
                if num_line == self.iter_count:
                    self.iter_count += 1
                    return line

    def read(self):
        with open(os.path.join(base_path, self.pathname), 'r') as file:
            return file.read()

    def write(self, line):
        with open(os.path.join(base_path, self.pathname), 'w+') as file:
            self.line_count += 1
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
    print(file_obj_2.write('line 2\n'))
    new_file_obj = file_obj_1 + file_obj_2
    print(isinstance(new_file_obj, File))
    print(new_file_obj)
    for line in new_file_obj:
        print(ascii(line))


main()
