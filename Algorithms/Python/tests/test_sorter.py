# Author: Christian Seely

import unittest
import random
from itertools import chain


from .context import sorter
from .context import quick_sorter


class TestQuickSorter(unittest.TestCase):

    def genRandIntArr(self, t_iN, t_iK):
        return list(chain.from_iterable([random.sample(range(1, t_iK), t_iK - 1) for _ in range(t_iN)]))

    def genRandFloatArr(self, t_iN, t_iK):
        pass

    def genRandStringArr(self, t_iN, t_iK):
        pass

    def testDirectSort(self):
        aInput = self.genRandIntArr(t_iN=10,  t_iK=100)
        self.assertEquals(quick_sorter.sort(t_aInput=aInput), sorted(aInput))

    def testIndirectSort(self):
        aInput = self.genRandIntArr(t_iN=10,  t_iK=100)
        self.assertEquals(sorter.mySort(t_oAlg=sorter.SortingAlgo.QUICK_SORT, t_aInput=aInput), sorted(aInput))


if __name__ == '__main__':
    unittest.main()

