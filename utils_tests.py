from utils import utils
import unittest

class utils_tests(unittest.TestCase):
    def test_reversed(self):
        self.assertEqual(utils.reversed(418),814)
        self.assertEqual(utils.reversed(-418),-814)

        with self.assertRaises(AssertionError) as ctx:
            utils.reversed("String")    
        self.assertEqual(str(ctx.exception), 'input not an integer')

        with self.assertRaises(AssertionError) as ctx:
            utils.reversed(418.5)
        self.assertEqual(str(ctx.exception),'input not an integer')

    def test_formatter(self):
        with self.assertRaises(AssertionError) as ctx:
            utils.formatter(418.5)
        self.assertEqual(str(ctx.exception),'input not an integer')

        with self.assertRaises(AssertionError) as ctx:
            utils.formatter("String")
        self.assertEqual(str(ctx.exception),'input not an integer')
       
        self.assertEqual(utils.formatter(418),('0b110100010','0o642'))
      

if __name__ == '__main__':
    unittest.main()
