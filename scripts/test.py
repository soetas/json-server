import unittest
from test.test_http import TestHTTP

if __name__ == '__main__':
  unittest.defaultTestLoader.discover(start_dir='', pattern='test_*.py')
  runner = unittest.TextTestRunner()

  suite = unittest.TestSuite()

  suite.addTest(TestHTTP(''))
  suite.addTest()
  suite.addTests([])

  # runner.run(suite)

  unittest.main(module='__main__', defaultTest='suite', verbosity=1)

