import unittest
from cal.py import *

def is_int(val):
  if type(val) == int:
      return True
  else :
      return False

class TestStringMethods(unittest.TestCase):
  def test_negative(self):
    testvalue = False
    message = "test value is not true"
    self.assertTrue( testvalue, message)

if __name__ == '__main__':
  unittest.main()
