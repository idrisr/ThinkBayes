"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from thinkbayes import Pmf
from bowl import Bowl


class Cookie(Pmf):
    """A map from string bowl ID to probablity."""


    def __init__(self, hypos, bowls):
        """Initialize self.

        hypos: sequence of string bowl IDs
        """
        self.bowls = bowls
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
        mix = self.bowls[hypo]
        like = mix[data] / self.bowls[hypo].total()
        if mix[data] > 0:
            self.bowls[hypo].Remove(data)
        return like


def main():
    hypos = ['Bowl 1', 'Bowl 2']
    bowls = {
        'Bowl 1':Bowl(dict(Vanilla=30, Chocolate=10)),
        'Bowl 2':Bowl(dict(Vanilla=20, Chocolate=20)),
        }

    pmf = Cookie(hypos, bowls)

    # we're saying that this is the data
    pmf.Update('Vanilla')

    for hypo, prob in pmf.Items():
        print hypo, prob

    print pmf.bowls['Bowl 1'];
    print pmf.bowls['Bowl 2'];


if __name__ == '__main__':
    main()
