"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from thinkbayes import Pmf

class Bowl(object):
    def __init__(self, cookies):
        self.cookies = cookies
        self.normalize()


    def Update(self, cookie):
        # remove a cookie
        try:
            if self.cookies[cookie] == 0:
                raise IndexError
            self.cookies[cookie] -= 1
        except IndexError:
            raise


    def normalize(self):
        total = sum(self.cookies.values())
        cookies = self.cookies.copy()
        for flavor in cookies.keys():
            cookies[flavor] = 1.0 * cookies[flavor] / total

        return cookies


class Cookie(Pmf):
    """A map from string bowl ID to probablity."""

    mixes = {
        'Bowl 1':dict(vanilla=0.75, chocolate=0.25),
        'Bowl 2':dict(vanilla=0.5, chocolate=0.5),
        }

    def __init__(self, hypos):
        """Initialize self.

        hypos: sequence of string bowl IDs
        """
        Pmf.__init__(self)
        for hypo in hypos:
            self.Set(hypo, 1)
        self.Normalize()

    def Update(self, data):
        """Updates the PMF with new data.

        data: string cookie type
        """
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            self.Mult(hypo, like)
        self.Normalize()


    def Likelihood(self, data, hypo):
        """The likelihood of the data under the hypothesis.

        data: string cookie type
        hypo: string bowl ID
        """
        mix = self.mixes[hypo]
        like = mix[data]
        return like


def main():
    hypos = ['Bowl 1', 'Bowl 2']

    pmf = Cookie(hypos)

    # we're saying that this is the data
    pmf.Update('vanilla')

    for hypo, prob in pmf.Items():
        print hypo, prob


if __name__ == '__main__':
    main()
