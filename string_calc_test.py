from string_calc import add
import nose.tools

def test_empty_string_is_0():
  assert 0 == add('')

def test_single_item_return_self():
  assert 2 == add('2')
  assert 1 == add('1')

def test_multiple_items_return_sum():
  assert 3 == add('1,2')
  assert 4 == add('1,3')
  assert 6 == add('1,2,3')

def test_delimiter_can_be_return():
  assert 3 == add('1\n2')
  assert 6 == add('1\n2,3')

def test_delimiter_can_be_custom():
  assert 3 == add('//*\n1*2')
  assert 6 == add('//+\n1+2+3')
  assert 6 == add('//abc\n1abc2abc3')
  assert 4 == add('//*12\n1*121*122')

def test_delimiter_can_be_minus():
  assert 6 == add('//-\n1-2-3')
  assert 3 == add('//-\n1-2')

def test_values_cannot_be_negative():
  nose.tools.assert_raises(ValueError, add, '1,-2')
  nose.tools.assert_raises(ValueError, add, '//*12\n1*123*12-1')

def test_can_have_multiple_delimiters():
  assert 6 == add('//[*][#]\n1*2#3')
  assert 6 == add('//[**][abc]\n1**2abc3')

def test_ignores_values_over_1000():
  assert 6 == add('1,2,3,1001')
  assert 6 == add('//[*][++]\n1*2++1002*3++1009')
