# Author: Christian Seely

from enum import Enum

from sorters import quick_sorter

class SortingAlgo(Enum):
    QUICK_SORT = 1


m_Runner = {
    SortingAlgo.QUICK_SORT : quick_sorter.sort
}

def mySort(t_oAlg, t_aInput):
    if not isinstance(t_oAlg, SortingAlgo):
        raise TypeError('t_oAlg must be an instance of SortingAlgo Enum')
    fSortingAlgo = m_Runner.get(t_oAlg)
    return fSortingAlgo(t_aInput=t_aInput)




