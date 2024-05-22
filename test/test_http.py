import unittest
from ddt import ddt, data, unpack, file_data
from requests import get
from ..tools.http import HTTPClient

@ddt
class TestHTTP(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass

  @classmethod
  def setUpClass():
    pass
  
  @classmethod
  def tearDownClass():
    pass

  def setUpModule():
    pass

  def tearDownModule():
    pass

  @unittest.skip(reason='')
  def test_request(self):
    pass
  
  @data([], [], [])
  @unpack
  @unittest.skipIf(condition=True, reason='')
  def test_get(self, url, query):
    pass

  @unittest.skipUnless(condition=True, reason='')
  def test_post(self):
    """  """
    self.assertFalse()
    self.assertTrue()
    self.assertIn()
    self.assertEqual()
    self.assertNotEqual()
