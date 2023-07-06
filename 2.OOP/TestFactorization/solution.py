from contracts import contract
import unittest


@contract
def factorize(x):
    """ 
    Factorize positive integer and return its factors.
    :type x: int,>=0
    :rtype: tuple[N],N>0
    """
    
    a = (x, )
    return a


class TestFactorize(unittest.TestCase):        
    def test_wrong_types_raise_exception(self):
        cases = ["string", 1.5]   
        for case in cases:
            with self.subTest(x=case):
                self.assertRaises(TypeError, factorize, case)
    
        
    def test_negative(self):
        cases = [-1, -10, -100]
        for case in cases:
                with self.subTest(x=case):
                    self.assertRaises(ValueError, factorize, case)

    def test_zero_and_one_cases(self):
        cases = [0, 1]
        for case in cases:
            with self.subTest(x=case):
                self.assertEqual(factorize(case), (case,))
                    
    
    def test_simple_numbers(self):
        cases = [3, 13, 29]
        for case in cases:
            with self.subTest(x=case):
                self.assertEqual(factorize(case), (case,))
                
    def test_two_simple_multipliers(self):
        cases = [6, 26, 121]
        expected =[(2,3), (2,13), (11, 11)] 
        for case, exp in zip(cases, expected):
             with self.subTest(x=case):
                 self.assertEqual(factorize(case), exp)
            
    
    def test_many_multipliers(self):
        cases = [1001, 9699690]
        expected = [(7, 11, 13), (2, 3, 5, 7, 11, 13, 17, 19)]
        for case, exp in zip(cases, expected):
            with self.subTest(x=case):
                self.assertEqual(factorize(case), exp)
        
 
              
def main():
   # print(factorize("line"))    
    unittest.main()
    

    
    
main()