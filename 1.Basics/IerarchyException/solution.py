from string import ascii_lowercase as alphabet

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

    def _write_read_checker(self, page, text = None):
        if page > self.size:
            raise PageNotFoundError()
        if isinstance(self, Novel) and text is not None:
            raise PermissionDeniedError()
        if text is not None and len(text) > self.max_sign: 
            raise TooLongTextError()
        
    def read(self, page):        
        self._write_read_checker(page)
        return self.content[page]
     
    def write(self, page, text):
        self._write_read_checker(page, text)
        self.content[page] += text

class Novel(Book):
    """класс описывающий книгу и методы работы с ней"""
    bookmark = dict()
    def __init__(self, author, year, title, content = None):
        """конструктор"""
        self.author = author 
        self.year = year 
        super().__init__(title, content)
        
    def read(self, page):
        """возвращает страницу"""
        super().read(page)
        

    def set_bookmark(self, person, page):
        """устанавливает закладку в книгу book"""
        self.bookmark = {person: page}

    def get_bookmark(self, person):
        """получает номер страницы установленной закладки в книге book"""
        if not self.bookmark[person]:
            raise PageNotFoundError
        return self.bookmark[person]

    def del_bookmark(self, person):
        """удаляет закладку читателя person, если она установлена"""
        if person in self.bookmark and self.bookmark[person] != None:
            self.bookmark[person] = None;

    def write(self, page, text):
        """делает запись текста text на страницу page """
        super().write(page, text)
        

class Notebook(Book):
    """класс описывающий тетрадь и методы работы с ней"""

    def __init__(self, title, size = 12, max_sign = 2000, content = None):
        """конструктор"""
        self.max_sign = max_sign
        self.size = size   
        
        content = content or ['' for i in range(self.size)]
        
        if content is not None:
            self.size = len(content)
           
        super().__init__(title, content)

    def read(self, page):
        """возвращает страницу с номером page"""
        return super().read(page)
    
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
        return book.read(page)

    def write(self, book, page, text):
        """пишем на страницу с номером page в книге book"""
        return book.write(page, text)

    def set_bookmark(self, book, page):
        """устанавливаем закладку в книгу book на страницу с номером page"""
        if (isinstance(book, Notebook)):
            raise NotExistingExtensionError
        
        book.set_bookmark(self, page) #self_name or Class self?

    def get_bookmark(self, book):
        """получаем номер страницы установленной закладки в книге book"""
        if (isinstance(book, Notebook)):
            raise NotExistingExtensionError
        return book.get_bookmark(self)

    def del_bookmark(self, book):
        """удаляет закладку из книги book"""
        if (isinstance(book, Notebook)):
            raise NotExistingExtensionError
        book.del_bookmark(self)
        

# def main():
#     person = Person('Igor')
#     assert(person.name == 'Igor')
#     content = [sign for sign in alphabet]
#     notebook = Notebook('note', 24, 100, content)
#     assert(notebook.title == 'note')
#     assert(notebook.max_sign == 100)
#     assert(notebook.size == 26)
#     assert([sign for sign in alphabet] == notebook.content)
#     novel = Novel('Grin', 1925, 'Gold chain')
#     assert(novel.size == 0)
#     assert(novel.author == 'Grin')
#     assert(novel.year == 1925)
#     assert(novel.title == 'Gold chain')
#     assert(person.read(notebook, 10) == 'k')
#     person.write(notebook, 10, '+new_value')
#     assert(person.read(notebook, 10) == 'k+new_value')
#     ''' exception '''
#     #person.read(notebook, 100) 
#     #too_long_text = alphabet * 1000
#     #person.write(notebook, 0, too_long_text)
#     novel = Novel('Grin', 1925, 'Gold chain', content)
#     #person.write(novel, 10, 'new_value')
#     person.set_bookmark(novel, 10)
#     assert(person.get_bookmark(novel) == 10)
#     # person.del_bookmark(novel) 
#     # print(person.get_bookmark(novel))
    
#     person = Person('Sasha')
#     content =['page_1', 'page_2']
#     notebook = Notebook('note', 2, 100, content)
#     notebook.write(1, '+add_text')
#     assert(notebook.read(1) == 'page_2+add_text')

# main()