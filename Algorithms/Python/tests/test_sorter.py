# Author: Christian Seely

import unittest
import random
import string
from itertools import chain


from context import sorter
from context import quick_sorter


class TestQuickSorter(unittest.TestCase):

    def generateSamples(self):
        return [
            self.genRandIntArr(iN=10, iK=100),
            self.genRandFloatArr(iN=10, iK=100, fStep=0.25),
            self.genRandStringArr(iN=10, iK=100)
        ]

    def genSample(self, iN, aPool):
        return list(chain.from_iterable([random.sample(aPool, len(aPool) - 1) for _ in range(iN)]))

    def genRandIntArr(self, iN, iK):
        aPool = range(iK)
        return self.genSample(iN=iN, aPool=aPool)

    def genRandFloatArr(self, iN, iK, fStep):
        aPool = list((x / (1/fStep) for x in range(iK)))
        return self.genSample(iN=iN, aPool=aPool)

    def genRandStringArr(self, iN, iK):
        sPool = string.ascii_letters + string.digits
        aPool = [''.join(random.choice(sPool) for _ in range(10)) for _ in range(iK)]
        return self.genSample(iN=iN, aPool=aPool)

    def testDirectSort(self):
        for aSample in self.generateSamples():
            self.assertEquals(quick_sorter.sort(aInput=aSample), sorted(aSample))

    def testIndirectSort(self):
        for aSample in self.generateSamples():
            self.assertEquals(sorter.mySort(oAlg=sorter.SortingAlgo.QUICK_SORT, aInput=aSample), sorted(aSample))

    def testCustomComparator(self):
        for aSample in self.generateSamples():
            self.assertEquals(quick_sorter.sort(aInput=aSample, fComparator=lambda x,y: x>=y), sorted(aSample, reverse=True))

if __name__ == '__main__':
    unittest.main()

