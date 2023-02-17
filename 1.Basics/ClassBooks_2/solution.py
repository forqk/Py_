import calendar


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
        if (len(self._text + other) > self.max_sign):
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


class CalendarBook(Book):
    """класс книги - ежедневник с закладкой"""
    bookmark = CalendarBookmark()

    def __init__(self, title, content=None):
        tc = calendar.TextCalendar(firstweekday=0)
        self.title = title

        all_calendar_dates = []
        for i in range(1, 13):
            all_calendar_dates.append(tc.formatmonth(int(title), i))

            main_list = tc.itermonthdates(int(title), i)

            for date_ in list(main_list):
                if date_.month == i:
                    all_calendar_dates.append(date_)

        super().__init__(title, all_calendar_dates)


def main():

    book = CalendarBook('2018')
    print(len(book))
    print(book.title)
    print(book[1])
    print(book[2])
    print(book[32])
    print(book[33])
    print(book[0])


main()

# tc= calendar.TextCalendar(firstweekday=0)
# print(tc.formatmonth(2018, 1))
# days = (tc.itermonthdates(2018, 1))
# for i in list(days):
#     if i.month == 1:
#         print(i)
