def gen_ticket_number(count, series, length=6):
    """
    генератор номеров билетов, входные параметры: count - количество билетов,
    series - номер серии, необязательный аргумент length - количество цифр
    в номере, по умолчанию равен 6, выход - строка вида: <номер билета> <серия билета>
    """
    # напишите вашу реализацию здесь
    number_ = gen_number(length)
    series_ = gen_series(series)
    
    current_series = next(series_)
    current_number = 1;
    
    for i in range(1, count+1):
        if current_number > int("9"*length):
            number_ = gen_number(length)
            current_series = next(series_)
            current_number = 0
            
        current_number += 1
        yield next(number_) + ' ' + current_series
    
def gen_series(series):
    """
    генератор серий лотерейных билетов начиная с series по "ZZ" включительно, входные 
    параметры: series -  - номер серии, выход - строка, состоящая из двух заглавных 
    букв латинского алфавита
    """
    # напишите вашу реализацию здесь
    first = series[0].upper()
    last = series[1].upper()
    
    yield str(first + last)
    
    while True:
        if first == 'Z' and last == 'Z':
            break
        if last == 'Z':
            last = 'A'
            first = chr(ord(first) + 1)
        else :
            last = chr(ord(last)+ 1)
        
        yield str(first + last)

def gen_number(length=6):
    """
    генератор номеров лотерейных билетов в одной серии, входные параметры: 
    необязательный аргумент length - количество цифр в номере, по умолчанию равен 6
    
    """
    lst = [[] for x in range(0, int("9"*length)+1)]
    for i in range(1, len(lst)):
        f = "0" + str(length)
        lst[i] = format(i, f)
        yield lst[i]
        