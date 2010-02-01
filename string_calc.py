def add(string):
  string = _convert_delimiters(string)
  if string:
    return _add_string_elements(string)
  else:
    return 0

def _add_string_elements(string):
  numbers = map(int, string.split(','))
  numbers = _eliminate_numbers_over_limit(numbers)
  if any(number < 0 for number in numbers):
    raise ValueError
  return sum(numbers)

def _convert_delimiters(string):
  string = _convert_custom_delimiter(string)
  return string.replace('\n', ',')

def _convert_custom_delimiter(string):
  if string.startswith('//'):
    delimiters, string = string.split('\n', 1)
    delimiters = _parse_multiple_delimiters(delimiters)
    for delimiter in delimiters:
      string = string.replace(delimiter, ',')
  return string

def _parse_multiple_delimiters(delimiters):
  delimiters = delimiters[2:]
  if delimiters.startswith('['):
    delimiters = delimiters[1:].replace('[', ',').replace(']', '')
  return delimiters.split(',')

def _eliminate_numbers_over_limit(numbers):
  for number in numbers:
    if number > 1000:
      numbers.remove(number)
  return numbers
