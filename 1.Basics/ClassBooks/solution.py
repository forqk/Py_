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
        return self._text
        
    def __add__(self, other):
        if not isinstance(other, str) and not isinstance(other, Page):
            raise TypeError    
        if( len(self._text + other) > self.max_sign):
            raise TooLongTextError
        
        self._text += other;
        return self   
        
    def __radd__(self, other):
        return other + self._text  
    
    def __len__(self):
        return len(self._text)
    
    def __gt__(self, other):
        return len(self) > len(other)
    

class Book:
    """класс книга"""

    def __init__(self, title, content=None):
        self.title = title
        self._content = [] if content is None else content

    def __len__(self):
        return len(self._content)
    
    def __getitem__(self, item):
        return self._content[item-1]
    
    def __setitem__(self, item, value):
        self._content[item-1] = value
    
def main():
    page = Page('text')
    page += '_new_text'
    print(page)
    s = 'string_' + page
    print(s)
    #new_page = page + 123 #TypeError
    new_page = page + '123'
    print(id(page) == id(new_page))
    page1 = Page('text')
    print(len(page1))
    print(page1 > page)
   # page += 's' * 3000 #TooLongTextError
    content = [Page('Page {}'.format(str(num))) for num in range(1,10)]
    book = Book('my_book',content)
    print(len(book))
    print(book[1])
    book[9] = 'Last page'
    print(book[9])
    #print(book[10]) #PAge not found error!
    book[9] += '\nnew_string'
    print(book[9])
    print(type(book[9])) #wrong type 
    
    
    
main()