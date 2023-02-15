class Page:
    """класс страница"""

    def __init__(self, text=None, max_sign=2000):
        self._text = '' if text is None else text
        self.max_sign = max_sign

    def __str__(self):
        return self._text
    # напишите вашу реализацию методов здесь   
    
    def __add__(self, text):
        if isinstance(text, Page) == 1:
            raise TypeError
        return self._text + text

class Book:
    """класс книга"""

    def __init__(self, title, content=None):
        self.title = title
        self._content = [] if content is None else content

    # напишите вашу реализацию методов здесь
    

def main():
    page = Page('text')
    page += '_new_text'
    print(page)
   # s = 'string_' + page
  #  print(type(s))
   # print(s)
  #  new_page = page + 123
  #  print(id(page) == id(new_page))
    
    

main()