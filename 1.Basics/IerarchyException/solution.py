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


class Book:
    def __init__(self, title, content=None):
        self.title = title
        self.content = content or []
        self.size = len(self.content)

    def _write_read_checker(self, page, text=None):
        if page > self.size or page < 0:
            raise PageNotFoundError()
        if isinstance(self, Novel) and text:
            raise PermissionDeniedError()
        if text and (self.size + len(text) > self.max_sign):
            raise TooLongTextError()

    def read(self, page):
        self._write_read_checker(page)
        return self.content[page]

    def write(self, page, text):
        self._write_read_checker(page, text)
        self.content[page] += text


class Novel(Book):
    bookmark = dict()

    def __init__(self, author, year, title, content=None):
        self.author = author
        self.year = year
        super().__init__(title, content)

    def read(self, page):
        return super().read(page)

    def set_bookmark(self, person, page):
        self.bookmark[person] = page

    def get_bookmark(self, person):
        if not self.bookmark[person]:
            raise PageNotFoundError
        return self.bookmark[person]

    def del_bookmark(self, person):
        if person in self.bookmark and self.bookmark[person] != None:
            self.bookmark[person] = None

    def write(self, page, text):
        super().write(page, text)


class Notebook(Book):
    def __init__(self, title, size=12, max_sign=2000, content=None):
        self.max_sign = max_sign
        self.size = size

        content = content or ['' for i in range(self.size)]

        if content is not None:
            self.size = len(content)

        super().__init__(title, content)

    def read(self, page):
        return super().read(page)

    def write(self, page, text):
        super().write(page, text)


class Person:
    def __init__(self, name):
        self.name = name

    def read(self, book, page):
        return book.read(page)

    def write(self, book, page, text):
        return book.write(page, text)

    def set_bookmark(self, book, page):
        if (isinstance(book, Notebook)):
            raise NotExistingExtensionError
        book.set_bookmark(self, page)

    def get_bookmark(self, book):
        if (isinstance(book, Notebook)):
            raise NotExistingExtensionError
        return book.get_bookmark(self)

    def del_bookmark(self, book):
        if (isinstance(book, Notebook)):
            raise NotExistingExtensionError
        book.del_bookmark(self)


# def Test():
#     TestOk = True

#     person = Person('Igor')
#     assert (person.name == 'Igor')
#     content = [sign for sign in alphabet]
#     notebook = Notebook('note', 24, 100, content)
#     assert (notebook.title == 'note')
#     assert (notebook.max_sign == 100)
#     assert (notebook.size == 26)
#     assert ([sign for sign in alphabet] == notebook.content)
#     novel = Novel('Grin', 1925, 'Gold chain')
#     assert (novel.size == 0)
#     assert (novel.author == 'Grin')
#     assert (novel.year == 1925)
#     assert (novel.title == 'Gold chain')
#     assert (person.read(notebook, 10) == 'k')
#     person.write(notebook, 10, '+new_value')
#     assert (person.read(notebook, 10) == 'k+new_value')

#     notebook = Notebook('note', 24, 100)
#     try:
#         notebook.write(1000, 'new_text')
#         print('1. Не выброшено PageNotFoundError - ошибка')
#         TestOk = False
#     except PageNotFoundError:
#            # print('1. Выброшено PageNotFounderror - OK!')
#             pass
#     try:
#         notebook.write(-1, 'new_text')
#         print('1. Не выброшено PageNotFoundError - ошибка')
#         TestOk = False
#     except PageNotFoundError:
#         #print('2. Выброшено PageNotFoundError - ОК!')
#         pass


#     person = Person('Igor')
#     content = [sign for sign in alphabet]
#     novel = Novel('Grin', 1925, 'Gold chain', content)
#     novel.set_bookmark(person, 18)
#     bookmark  = novel.get_bookmark(person)
#     assert(bookmark == 18)
#     novel.del_bookmark(person)
#     try:
#         bookmark = novel.get_bookmark(person)
#         print('1. Не выброшено PageNotFoundError - ошибка')
#         TestOk = False
#     except PageNotFoundError:
#         pass

#     content = ['1', '2']

#     notebook = Notebook('note', 2, 100, content)
#     assert(notebook.read(1) == '2')

#     novel = Novel('Grin', 1925, 'Gold chain', content)
#     assert(novel.read(1) == '2')

#     if TestOk:
#         print("Tests ok!")
#     else:
#         print("Tests failed!")


# def main():
#     Test()
# main()
