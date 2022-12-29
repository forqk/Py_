import sys
import json
import functools

def to_json(func):
  @functools.wraps(func)
  def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)
  return wrapped

@to_json
def some_funtion(dict_):
    return dict_
  
def main():  
  result = some_funtion({'a': 1, 'b': 2})
  assert isinstance(result, str)
  assert result == '{"a": 1, "b": 2}'
  assert json.loads(result) == {'a': 1, 'b': 2}
  assert some_funtion.__name__ == 'some_funtion'
  print('All tests passed!')
   
main()
