import unittest
from primes import is_prime

class PrimesTestCase(unittest.TestCase):
    def test_is_five_prime(self):
        lst = []
        for i in range(1,10):
            if i > 1:
                for j in range(2,i):
                    if(i % j==0):
                        break
                else:
                    lst.append(i)
        print(lst)
        self.assertEqual(lst,[2, 3, 5, 7])

if __name__ == '__main__':
    unittest.main()
