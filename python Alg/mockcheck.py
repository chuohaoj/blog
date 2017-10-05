import unittest
import mock

class TestStringMethod(unittest.TestCase):
    def TestUpper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def testIsUpper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

class Count():
    def add(self, a, b):
        return a + b

    def mutiple(self, a, b):
        ans = a
        for _ in range(b):
            ans = self.add(ans, a)
        return ans 

class TestAdd(unittest.TestCase):
    def test_add(self):
        count = Count()
        count.add = mock.Mock(return_value=10)
        result = count.add(8, 2)
        self.assertEqual(result, 10)

    def test_addnotEqual(self):
        count = Count()
        count.add = mock.Mock(return_value=10, side_effect=count.add)
        result = count.add(8, 8)
        print(result)
        count.add.assert_called_with(8, 8)
        self.assertEqual(result, 16)

if __name__ == '__main__':
    unittest.main()

