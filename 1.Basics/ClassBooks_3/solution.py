import calendar
from collections import OrderedDict


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


class Page:
    """класс страница"""

    def __init__(self, text=None, max_sign=2000):
        self._text = '' if text is None else text
        self.max_sign = max_sign

    # напишите вашу реализацию методов здесь
    def __str__(self):
        return str(self._text)

    def __add__(self, other):
        if not isinstance(other, str) and not isinstance(other, Page):
            raise TypeError
        if len(self._text + other) > self.max_sign:
            raise TooLongTextError

        self._text += other
        return self

    def __radd__(self, other):
        return other + self._text

    def __len__(self):
        return len(self._text)

    def __gt__(self, other):
        return len(self) > len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __eq__(self, other):
        return len(self) == len(other)


class Book:
    """класс книга"""

    def __init__(self, title, content=None):
        self.title = title
        self._content = [] if content is None else content

    def __len__(self):
        return len(self._content)

    def __getitem__(self, item):
        if len(self._content) < item or item <= 0:
            raise PageNotFoundError
        return (self._content[item-1])

    def __setitem__(self, item, value):
        self._content[item-1] = Page(value)

    def __eq__(self, other):
        if not isinstance(self, Book) or not isinstance(other, Book):
            raise TypeError
        return len(self._content) == len(other._content)

    def __ge__(self, other):
        return len(self._content) >= len(other._content)

    def __gt__(self, other):
        return len(self._content) >= len(other._content)


class CalendarBookmark:
    """класс дескриптор - закладка для ежедневника"""

    page_number = 0

    def __set__(self, obj, value):
        if (value <= 0 or value > len(obj._content)):
            raise PageNotFoundError

        self.page_number = value

    def __get__(self, obj, obj_type):
        return self.page_number


class Person:
    """класс описывающий человека"""

    def __init__(self, name):
        self.name = name

    def set_bookmark(self, *args, **kwargs):
        raise NotImplementedError

    def get_bookmark(self, *args, **kwargs):
        raise NotImplementedError

    def del_bookmark(self, *args, **kwargs):
        raise NotImplementedError


class Reader:
    def read(self, book, num_page):
        if num_page < 0 or num_page >= len(book._content):
            raise PageNotFoundError
        return book._content[num_page-1]


class Writer:
    def write(self, book, num_page, text):
        if num_page < 0 or num_page >= len(book._content):
            raise PageNotFoundError
        if len(book._content[num_page-1]) + len(text) > book._content[num_page].max_sign:
            raise TooLongTextError
        book._content[num_page-1] +=text


class AdvancedPerson(Person, Reader, Writer):
    """класс человека умеющего читать, писать, пользоваться закладками"""

    def set_bookmark(self, book, num_page):
        if hasattr(book, 'set_bookmark'):
            book.set_bookmark(self, num_page)
            return
        raise NotExistingExtensionError

    def get_bookmark(self, book):
        if hasattr(book, 'get_bookmark'):
            return book.get_bookmark(self)
        raise NotExistingExtensionError

    def del_bookmark(self, book, person):
        if hasattr(book, 'get_bookmark'):
            book.del_bookmark(self)
            return
        raise NotExistingExtensionError

    def search(self, book, page):
        last_page = book[len(book)]
        if page not in last_page._table:
            raise PageNotFoundError
        return last_page._table[page]
        

    def read(self, book, page):
        if isinstance(page, str):
            return Reader().read(book, self.search(book, page)-1)
        return Reader().read(book, page-1)

    def write(self, book, page, text):
        if isinstance(page, str):
            Writer().write(book, self.search(book, page)-1, text)
        Writer().write(book, page-1, text)

class PageTableContents(Page):
    _table = OrderedDict()
    _start = 'TABLE OF CONTENT\n'

    def __init__(self, text=None, max_sign=2000):
        if text is not None:
            self._table = text
            super().__init__(str(self._table))

    def search(self, chapter):
        if chapter not in self._table:
            raise PageNotFoundError
        return self._table[chapter]

    def __str__(self):
        line = ''
        if isinstance(self._table, str) :   
            line += self._table
        else:
            line = self._start
            for key, value in self._table.items():
                line += str(key) + ':' + str(value) + '\n'
                
        return line
    
    def __add__(self, other):
        raise PermissionDeniedError

class CalendarBook(Book):
    """класс книги - ежедневник с закладкой"""
    bookmark = CalendarBookmark()

    def __init__(self, title, content=None):
        tc = calendar.TextCalendar(firstweekday=0)
        self.title = title

        all_calendar_dates = []
        month_pages = OrderedDict()

        for i in range(1, 13):
            all_calendar_dates.append(Page(str(tc.formatmonth(int(title), i))))

            main_list = tc.itermonthdates(int(title), i)

            for date_ in list(main_list):
                if date_.month == i:
                    all_calendar_dates.append(Page(str(date_)))

            month_pages[calendar.month_name[i]] = len(
                all_calendar_dates) - calendar.monthrange(int(title), i)[1]

        all_calendar_dates.append(PageTableContents(month_pages))

        super().__init__(title, all_calendar_dates)


def main():
    note = CalendarBook('2018')
    print(note[1])
    print(note[2])
    print(len(note))
    print(note[378])
    print(note[378].search('August'))
  #  print(note[400]) #pagenotfounderror
  #  print(note['August']) #typeerror # check late
   
    person = AdvancedPerson('Adam') 
    print(person.search(note, 'May'))
    
    print(person.read(note, 125))
    person.write(note, 2, '\nHappy New Year!!!')  
    print(note[2])
    #person.write(note, 2, 'too_long_string' * 1000) #toolongtexterror
    text = 'TABLE OF CONTENT\nJanuary:1\nFebruary:33\n'
    
    page = PageTableContents(text, 300)
    print(page)
    content = [Page('page 1'), Page('page 2'), Page('page 3'), Page('page 4'), Page('page 5')]
    book = Book('title', content)
    reader = Reader()
    page = reader.read(book, 1)
    print(str(page))    
    
    # book = CalendarBook('1980')
    # person = AdvancedPerson('Sasha')
    # print(person.read(book, 'January'))
    
    # content = [Page('num: {}.'.format(str(num))) for num in range(1 ,11)]
    # book = Book('title', content)
    # print('содержимое страницы до добавления: ', book[1], sep ='\n')
    # writer = Writer()
    # writer.write(book, 1, 'some_text')
    # print('Содержимое страницы после добавления:', book[1], sep='\n')
    
   # text = 'TABLE OF CONTENT\nJanuary:1\n'
  #  page = PageTableContents(text, 300)
 #   page += "some_string"
    
main()

# # tc= calendar.TextCalendar(firstweekday=0)
# print(tc.formatmonth(2018, 1))
# days = (tc.itermonthdates(2018, 1))
# for i in list(days):
#     if i.month == 1:
#         print(i)
