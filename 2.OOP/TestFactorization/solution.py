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
    def test_usage(self):
        self.assertEqual(2+2, 4)
        
    def test_wrong_types_raise_exception(self):
        pass
        # with self.subTest(i=1):
        #     self.assertRaises(TypeError, factorize, 'string')
        # with self.subTest(i=1):
        #     self.assertRaises(TypeError, factorize, 1.5)
            
    def est_zero_and_one_cases(self):
        a = (0, )
        b = (1, )
        with self.subTest(i = 2):
            
        
        
        
            
            
    
        
        
def main():
   # factorize(4)
    
    unittest.main()
    
main()