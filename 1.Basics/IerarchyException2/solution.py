from string import ascii_lowercase as alphabet


class BookIOErrors (Exception):
    pass


class PageNotFoundError(BookIOErrors):
    pass


class TooLongTextError(BookIOErrors):
    pass


class PermissionDeniedError(BookIOErrors):
    pass


class NotExistingExtensionError(BookIOErrors):
    pass

class Person:
    """класс описывающий человека"""
    def __init__(self, name):
        self.name = name

    @staticmethod
    def read(book, page):
        """читаем страницу page в книге book"""
        return book.read(page)

    @staticmethod
    def write(book, page, text):
        """пишем на страницу page в книге book"""
        book.write(page, text)

    def set_bookmark(self, book, page):
        """устанавливает закладку в книгу book"""
        if hasattr(book, 'set_bookmark'):
            book.set_bookmark(self, page)
            return
        raise NotExistingExtensionError

    def get_bookmark(self, book):
        """получает номер страницы установленной закладки в книге book"""
        if hasattr(book, 'get_bookmark'):
            return book.get_bookmark(self)
        raise NotExistingExtensionError

    def del_bookmark(self, book):
        """удаляет закладку читателя person, если она установлена"""
        if hasattr(book, 'get_bookmark'):
            book.del_bookmark(self)
            return
        raise NotExistingExtensionError


class Book:
    def __init__(self, title, content=None):
        self.title = title
        self.content = content or []
        self.size = len(self.content)

    def read(self, *args, **kwargs):
        raise NotImplementedError

    def write(self, *args, **kwargs):
        raise NotImplementedError


class Novel(Book):
    def __init__(self, author, year, title, content=None):
        super().__init__(title, content)
        self.author = author  # автор
        self.year = year  # год издания
        self.bookmark = {}  # словарь: ключ-читатель,значение-номер страницы

    def read(self, page):
        """возвращает страницу"""
        if page < 0 or page >= len(self.content):
            raise PageNotFoundError
        return self.content[page]

    def write(self, *args, **kwargs):
        raise PermissionDeniedError

    def set_bookmark(self, person, page):
        """устанавливает закладку в книгу book"""
        if page < 0 or page >= len(self.content):
            raise PageNotFoundError
        self.bookmark[person] = page

    def get_bookmark(self, person):
        """получает номер страницы установленной закладки в книге book"""
        if person in self.bookmark:
            return self.bookmark[person]
        raise PageNotFoundError

    def del_bookmark(self, person):
        if person in self.bookmark:
            del self.bookmark[person]


class Notebook(Book):
    def __init__(self, title, size=12, max_sign=2000, content=None):
        content = content if content else ['', ] * size
        super().__init__(title, content)
        self.max_sign = max_sign  # максимальное количество символов на странице

    def read(self, page):
        """возвращает страницу"""
        if page < 0 or page >= len(self.content):
            raise PageNotFoundError
        return self.content[page]

    def write(self, page, text):
        if page < 0 or page >= len(self.content):
            raise PageNotFoundError
        if len(self.content[page]) + len(text) > self.max_sign:
            raise TooLongTextError
        self.content[page] += text

class NovelWithTable(Novel):
    def __init__(self, author, year, title, content = None, table = None):
        self.table =  table or dict()
        super().__init__(author, year, title, content)
       
    def add_chapter(self, chapter, page):
        self.table[chapter] = page
        
    def search(self, chapter):
        if chapter not in self.table:
            raise PageNotFoundError
        return self.table[chapter]
    
    def remove_chapter(self, chapter):
        if chapter not in self.table:
            raise PageNotFoundError
        del self.table[chapter]

class AdvancedPerson(Person):
    @staticmethod
    def search(book, name_page):
        return book.search(name_page)
    
    def read(self, book, page):
        if isinstance(page, int) :
            return book.read(page)
        if isinstance(page, str):
            return (book.read(book.search(page)))
    
    def write(self, book, page, text):
        if isinstance(book, Novel):
            raise PermissionDeniedError
      
        
            
def Test():
    
    person  = AdvancedPerson('Ivan')

    content = [sign for sign in alphabet]
    table = {'start_page': 0}
    novel = NovelWithTable('Grin', 1925, 'Gold chain', content, table)
    print(novel.table)
    print(person.search(novel, 'start_page'))
   # print(person.search(novel, 'non-exist_page'))
    novel.add_chapter('last_page', 26)
    print(person.search(novel, 'last_page'))
    novel.remove_chapter('start_page')
    print(novel.table)
    
    person.write(novel, 'random_page', '+new_value')

    

def main():
    Test()
main()