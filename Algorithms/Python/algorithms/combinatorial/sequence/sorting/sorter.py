# Author: Christian Seely

from enum import Enum

from sorters import quick_sorter

class SortingAlgo(Enum):
    QUICK_SORT = 1


oRunner = {
    SortingAlgo.QUICK_SORT : quick_sorter.sort
}

def mySort(oAlg, aInput):
    if not isinstance(oAlg, SortingAlgo):
        raise TypeError('t_oAlg must be an instance of SortingAlgo Enum')
    fSortingAlgo = oRunner.get(oAlg)
    return fSortingAlgo(aInput=aInput)




