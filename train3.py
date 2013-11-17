"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import thinkbayes
import thinkplot
import numpy as np

from thinkbayes import Pmf, Percentile, Suite
from dice import Dice


class Train(Dice):
    """Represents hypotheses about how many trains the company has."""


class Train2(Dice):
    """Represents hypotheses about how many trains the company has."""

    def __init__(self, hypos, alpha=1.0):
        """Initializes the hypotheses with a power law distribution.

        hypos: sequence of hypotheses
        alpha: parameter of the power law prior
        """
        Pmf.__init__(self)
        for hypo in hypos:
            self.Set(hypo, hypo**(-alpha))
        self.Normalize()


class Train3(Suite):
    def Likelihood(self, data, hypo):
        """Exercise 3
        Assumes a power law distribution of the size of companies.
        For example, if there were 5 companies A-E, A would have 1 car, B has 2 ... etc
        Therefore there are 5 cars labeled 1, 4 labeled 2, ... and one 1 labeled 5.
        For the hypothesis there are 5 total cars and we observe a car labeled 5,
        The likelihood is (1/5) / (1 + 1/2 + 1/3 + 1/4 + 1/5)
        which would require fractional cars, since if there were 5 cars total, a power law
        distribution does not allow discrete number of cars per company.
        """
        if hypo < data:
            return 0
        else:
            denom = np.arange(1, hypo)
            return hypo**-1.0 / sum(denom**-1.0)


def MakePosterior(high, dataset, constructor):
    """Makes and updates a Suite.

    high: upper bound on the range of hypotheses
    dataset: observed data to use for the update
    constructor: function that makes a new suite

    Returns: posterior Suite
    """
    hypos = xrange(1, high+1)
    suite = constructor(hypos)
    suite.name = str(high)

    for data in dataset:
        suite.Update(data)

    return suite


def ComparePriors():
    """Runs the analysis with two different priors and compares them."""
    dataset = [60]
    high = 1000

    thinkplot.Clf()
    thinkplot.PrePlot(num=2)

    constructors = [Train, Train2, Train3]
    labels = ['uniform', 'power law', 'many companies']

    for constructor, label in zip(constructors, labels):
        suite = MakePosterior(high, dataset, constructor)
        suite.name = label
        thinkplot.Pmf(suite)

    thinkplot.Save(root='train4',
                xlabel='Number of trains',
                ylabel='Probability')

def main():
    ComparePriors()

    dataset = [30, 60, 90]

    thinkplot.Clf()
    thinkplot.PrePlot(num=3)

    for high in [500, 1000, 2000]:
        suite = MakePosterior(high, dataset, Train2)
        print high, suite.Mean()

    thinkplot.Save(root='train3',
                   xlabel='Number of trains',
                   ylabel='Probability')

    interval = Percentile(suite, 5), Percentile(suite, 95)
    print interval

    cdf = thinkbayes.MakeCdfFromPmf(suite)
    interval = cdf.Percentile(5), cdf.Percentile(95)
    print interval


if __name__ == '__main__':
    main()
