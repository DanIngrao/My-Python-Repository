import unittest
import text_changer

class TryTextChanger(unittest.TestCase):

    def test_uppercase(self):
        word = 'good morning'
        res = text_changer.textuppercase(word)
        self.assertEqual(res, 'Good Morning')

if __name__ == '__main__':
    unittest.main()

# Traceback (most recent call last):
#   File "c:\Users\danin\Desktop\Python Repositories\Python Proyects\My-Python-Repository\Practices\Practice 8\try.py", line 9, in test_uppercase
#     self.assertEqual(res, 'Good Morning')
# AssertionError: 'GOOD MORNING' != 'Good Morning'
# - GOOD MORNING
# + Good Morning
# 
# 
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
# 
# FAILED (failures=1)