from unittest import TestCase, TextTestRunner, TestLoader
from cookie3 import Cookie
from bowl import Bowl
from pdb import set_trace

__author__ = 'idris'


class TestBowl(TestCase):
    '''
    def test_remove_cookie(self):
        cookies = dict(chocolate=10, vanilla=10)
        bowl = Bowl(cookies)
        bowl.Update('chocolate')
        self.assertEquals(9, bowl.cookies['chocolate'])


    def test_remove_zero_cookie(self):
        bowl = Bowl(dict(chocolate=0, vanilla=10))
        self.assertRaises(IndexError,  bowl.Update, 'chocolate')
    '''

    def test_remove2(self):
        """ simplifies to book example
        """
        mixes = {
            'Bowl 1':Bowl(dict(Vanilla=1, Chocolate=10)),
            'Bowl 2':Bowl(dict(Vanilla=2, Chocolate=20)),
            }

        hypos = ['Bowl 1', 'Bowl 2']
        pmf = Cookie(hypos, mixes)

        # remove two vanilla cookies
        pmf.Update('Vanilla')
        pmf.Update('Vanilla')

        # This is saying that if you pick two vanilla cookies from one bowl, it must be Bowl2.
        # This is different than saying that you pick two cookies from unknown bowls, they're both vanilla,
        # and they both came from bowl 2
        self.assertAlmostEquals(pmf.d['Bowl 1'], 0)
        self.assertAlmostEquals(pmf.d['Bowl 2'], 1)


    def test_book_example(self):
        mixes = {
            'Bowl 1':Bowl(dict(Vanilla=30, Chocolate=10)),
            'Bowl 2':Bowl(dict(Vanilla=20, Chocolate=20)),
            }

        hypos = ['Bowl 1', 'Bowl 2']
        pmf = Cookie(hypos, mixes)

        # we're saying that this is the data
        pmf.Update('Vanilla')
        self.assertAlmostEquals(pmf.d['Bowl 1'], 0.6)
        self.assertAlmostEquals(pmf.d['Bowl 2'], 0.4)


    def test_zero_vanilla(self):
        mixes = {
            'Bowl 1':Bowl(dict(Vanilla=0, Chocolate=10)),
            'Bowl 2':Bowl(dict(Vanilla=20, Chocolate=20)),
            }

        hypos = ['Bowl 1', 'Bowl 2']
        pmf = Cookie(hypos, mixes)

        # we're saying that this is the data
        pmf.Update('Vanilla')
        self.assertAlmostEquals(pmf.d['Bowl 1'], 0.0)
        self.assertAlmostEquals(pmf.d['Bowl 2'], 1)





if __name__ == '__main__':
    suite = TestLoader().loadTestsFromTestCase(TestBowl)
    TextTestRunner(verbosity=5).run(suite)