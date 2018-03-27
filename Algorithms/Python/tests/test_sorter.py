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
            self.genRandIntArr(t_iN=10, t_iK=100),
            self.genRandFloatArr(t_iN=10, t_iK=100, t_fStep=0.25),
            self.genRandStringArr(t_iN=10, t_iK=100)
        ]

    def genSample(self, t_iN, aPool):
        return list(chain.from_iterable([random.sample(aPool, len(aPool) - 1) for _ in range(t_iN)]))

    def genRandIntArr(self, t_iN, t_iK):
        aPool = range(t_iK)
        return self.genSample(t_iN=t_iN, aPool=aPool)

    def genRandFloatArr(self, t_iN, t_iK, t_fStep):
        aPool = list((x / (1/t_fStep) for x in range(t_iK)))
        return self.genSample(t_iN=t_iN, aPool=aPool)

    def genRandStringArr(self, t_iN, t_iK):
        sPool = string.ascii_letters + string.digits
        aPool = [''.join(random.choice(sPool) for _ in range(10)) for _ in range(t_iK)]
        return self.genSample(t_iN=t_iN, aPool=aPool)

    def testDirectSort(self):
        for aSample in self.generateSamples():
            self.assertEquals(quick_sorter.sort(t_aInput=aSample), sorted(aSample))

    def testIndirectSort(self):
        for aSample in self.generateSamples():
            print(len(aSample))
            self.assertEquals(sorter.mySort(t_oAlg=sorter.SortingAlgo.QUICK_SORT, t_aInput=aSample), sorted(aSample))

    def testCustomComparator(self):
        for aSample in self.generateSamples():
            self.assertEquals(quick_sorter.sort(t_aInput=aSample, t_fComparator=lambda x,y: x>=y), sorted(aSample, reverse=True))

if __name__ == '__main__':
    unittest.main()

