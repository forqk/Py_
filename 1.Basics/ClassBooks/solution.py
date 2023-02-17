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
        if(len(self._text + other) > self.max_sign):
            raise TooLongTextError
        
        self._text += other;
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
        if len(self._content) <  item or item <= 0:
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
    
                
# def main():
#     page = Page('text')
#     page += '_new_text'
#     assert(str(page) == 'text_new_text')
#     s = 'string_' + page
#     assert(isinstance(s, str))
#     assert(str(s) == 'string_text_new_text')
#     try :
#         new_page = page + 123 
#     except TypeError:
#         print('TypeError ok')
#     new_page = page + '123'
#     assert(id(page) == id(new_page))
#     page1 = Page('text')
#     assert(len(page1) == 4)
   
#     assert((page1 > page) == False)
#     try:
#         page += 's' * 3000 #TooLongTextError
#     except TooLongTextError:
#         print('TooLongTextError Ok')
        
#     content = [Page('Page {}'.format(str(num))) for num in range(1,10)]
#     book = Book('my_book', content)
#     assert(len(book) == 9)
#     assert(str(book[1]) == 'Page 1')
    
#     book[9] = 'Last page'
    
#     assert(str(book[9])== 'Last page')
   
#     try:
#         print(book[10])
#     except PageNotFoundError:
#         print('PageNotFoundError Ok')
#     book[9] += '\nnew_string'
#     assert(str(book[9]) == 'Last page\nnew_string')
#     assert(isinstance(book[9], Page))
    
#     book2 = Book('book2')
    
#     assert(book2 != book)
#     line = 'test'
#     try:
#         assert(book2 != line)
#     except TypeError:
#         print('TypeError Ok')
    
    
#     page3 = Page('text')
#     page4 = Page('Texta')
    
#     assert(page3 < page4)
    
    
# main()