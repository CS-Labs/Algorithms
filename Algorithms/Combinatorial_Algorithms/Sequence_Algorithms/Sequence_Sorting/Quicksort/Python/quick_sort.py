# Author: Christian Seely

import random
from itertools import chain
import utils # See utils.py in the Utilities folder.

class QuickSort(object):

    @staticmethod
    @utils.Utils.timeit
    def run(aRandArry, bPrintResults = False, bIterative = False, bConcurrent = False):
        if(bPrintResults):
            print("\nStart Array: {0}".format(aRandArry))
        aResult = QuickSort._quickSort(aArr=aRandArry,iLo=0,iHi=len(aRandArry)-1)
        if(bPrintResults):
            print("\nEnd Array: {0}".format(aResult))
        return aResult

    @staticmethod
    def _quickSort(aArr, iLo, iHi):
        if iLo < iHi:
            iPart = QuickSort._partition(aArr=aArr,iLo=iLo,iHi=iHi)
            QuickSort._quickSort(aArr=aArr,iLo=iLo,iHi=(iPart - 1))
            QuickSort._quickSort(aArr=aArr, iLo=(iPart + 1),iHi=iHi)
        return aArr

    @staticmethod
    def _partition(aArr, iLo, iHi):
        iPivot = aArr[iHi]
        iI = iLo - 1
        for iJ in range(iLo, iHi):
            if aArr[iJ] <= iPivot:
                iI += 1
                aArr[iI], aArr[iJ] = aArr[iJ], aArr[iI] # Optimal swapping speed.
        aArr[iI+1],aArr[iHi] = aArr[iHi], aArr[iI+1] # Optimal swapping speed.
        return iI + 1


def main():
    # Create a random list of size n*k.
    N = 100
    K = 1000
    aInput = list(chain.from_iterable([random.sample(range(1,K),K-1) for _ in range(N)]))
    QuickSort.run(aRandArry=aInput)



if __name__ == "__main__":
    main()