from collections import defaultdict
from collections import namedtuple
import functools

recipes = {'Бутерброд с ветчиной': {'Хлеб': 50, 'Ветчина': 20, 'Сыр': 20},
           'Салат Витаминный': {'Помидоры': 50, 'Огурцы': 20, 'Лук': 20, 'Майонез': 50, 'Зелень': 20}}

store = {'Хлеб': 250, 'Ветчина': 120, 'Сыр': 120,
         'Помидоры': 50, 'Огурцы': 20, 'Лук': 20,
         'Майонез': 50, 'Зелень': 20}


statistics = defaultdict(list)
Order = namedtuple('Order', ['success', 'portions'])

def collect_statistics(statistics):
    def decorator(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            result = func(*args, *kwargs)
            if result[0] == 0:
                statistics.setdefault(args[0], [])
                statistics[args[0]].append(Order(result[0], args[1]-result[1]))       
            else:
                statistics[args[0]].append(Order(result[0], result[1]))    
            return result
        return wrapped
    return decorator
        

@collect_statistics(statistics)
def check_portions(food, count, recipes=recipes, store=store):
    max_food_count = 10000 #  ^_^
    for product, cost in recipes[food].items():
        if product not in store:
            return (0, 0)
        
        max_food_count = min(max_food_count, store[product] // cost)
        
    if(max_food_count >= count):
        return(1, count)
    return(0, max_food_count)

def main():
    print(check_portions('Бутерброд с ветчиной', 20))
    print(statistics)
    print(check_portions('Салат Витаминный', 1))
    print(statistics)
    print(check_portions('Бутерброд с ветчиной', 2))
    print(statistics)
    
main();
    