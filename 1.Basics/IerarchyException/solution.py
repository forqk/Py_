class BookIOErrors (Exception):
    def error(self, err):
        raise err;

class PageNotFoundError(BookIOErrors):
    def __init__(self):
        super().__init__('PageNotFoundError')
        
class TooLongTextError(BookIOErrors):
    def __init__(self):
        super().__init__('TooLongTextError')
    
class PermissionDeniedError(BookIOErrors):
    def __init__(self):
        super().__init__('PermissionDeniedError')

class NotExistingExtensionError(BookIOErrors):
    def __init__(self):
        super().__init__('NotExistingExtensionError')

class Book:
    def __init__(self, title, content=None):
        self.title = title
        self.content = content or []
        self.size = len(self.content)

    def read(self, page):
        print('type(self)_readMethod', type(self))
       # raise NotImplementedError

    def write(self, page, text):
        print('type(self)_writeMethod', type(self))
       # raise NotImplementedError


class Novel(Book):
    """класс описывающий книгу и методы работы с ней"""
    def __init__(self, author, year, title, content):
        """конструктор"""
        self.author = author #строка
        self.year = year #целое
        super.__init__(title, content)
        
    def read(self, page):
        """возвращает страницу"""
        super().read(self.content[self.PersonPage[page]])
        

    def set_bookmark(self, person, page):
        """устанавливает закладку в книгу book"""
        self.PersonPage = {person: page}

    def get_bookmark(self, person):
        """получает номер страницы установленной закладки в книге book"""
        try:
            return self.PersonPage[person]
        except:
            PageNotFoundError()
    
    def del_bookmark(self, person):
        """удаляет закладку читателя person, если она установлена"""
        del self.PersonPage[person]

    def write(self, page, text):
        """делает запись текста text на страницу page """
        super().write(page, text)
        


class Notebook(Book):
    """класс описывающий тетрадь и методы работы с ней"""
    max_sign = 2000
    size = 12
    
    def __init__(self, title, size, max_sign, content):
        """конструктор"""
        self.max_sign = max_sign # or 2000 ?
        self.size = size    
        
        if len(content) != 0:
            self.size = len(content)
        else:
            content = ['' for i in range(self.size)] #если контент не задан список пустых строк разхмером сайз.
            
        super.__init__(title, content)

    def read(self, page):
        """возвращает страницу с номером page"""
        super().read(page)
    
    def write(self, page, text):
        """делает запись текста text на страницу с номером page """
        super().write(page, text)


class Person:
    """класс описывающий человека и методы работы с книгой"""

    def __init__(self, name):
        """конструктор"""
        self.name = name;
        
    def read(self, book, page):
        """читаем страницу с номером page в книге book"""
        book.read(page)

    def write(self, book, page, text):
        """пишем на страницу с номером page в книге book"""
        book.write(page, text)

    def set_bookmark(self, book, page):
        """устанавливаем закладку в книгу book на страницу с номером page"""
        book.set_bookmark(page)

    def get_bookmark(self, book):
        """получаем номер страницы установленной закладки в книге book"""
        book.getbookmark(self.name)

    def del_bookmark(self, book):
        """удаляет закладку из книги book"""
        book.delbookrmark(self.name)
        

def main():
    pass

main()