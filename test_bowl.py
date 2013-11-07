from unittest import TestCase, TextTestRunner, TestLoader
from cookie3 import Bowl
from pdb import set_trace

__author__ = 'idris'


class TestBowl(TestCase):
    def test_remove_cookie(self):
        cookies = dict(chocolate=10, vanilla=10)
        bowl = Bowl(cookies)
        bowl.Update('chocolate')
        self.assertEquals(9, bowl.cookies['chocolate'])


    def test_remove_zero_cookie(self):
        bowl = Bowl(dict(chocolate=0, vanilla=10))
        self.assertRaises(IndexError,  bowl.Update, 'chocolate')


    def test_normalize(self):
        cookies = dict(chocolate=10, vanilla=10)
        bowl = Bowl(cookies)
        self.assertEquals(0.5, bowl.normalize()['chocolate'])

if __name__ == '__main__':
    suite = TestLoader().loadTestsFromTestCase(TestBowl)
    TextTestRunner(verbosity=2).run(suite)
