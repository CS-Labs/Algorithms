# Author: Christian Seely

class Settings(object):
    fComparator = None

def sort(aInput, fComparator=lambda x,y: x <= y):
    Settings.fComparator = fComparator
    return quicksort(aArr=aInput, iLo=0, iHi=len(aInput) - 1)

def quicksort(aArr, iLo, iHi):
    if iLo < iHi:
        iPart = partition(aArr=aArr, iLo=iLo, iHi=iHi)
        quicksort(aArr=aArr, iLo=iLo, iHi=(iPart - 1))
        quicksort(aArr=aArr, iLo=(iPart + 1), iHi=iHi)
    return aArr

def partition(aArr, iLo, iHi):
    iPivot = aArr[iHi]
    iI = iLo - 1
    for iJ in range(iLo, iHi):
        if Settings.fComparator(aArr[iJ], iPivot):
            iI += 1
            aArr[iI], aArr[iJ] = aArr[iJ], aArr[iI] # Optimal swapping speed.
    aArr[iI+1],aArr[iHi] = aArr[iHi], aArr[iI+1] # Optimal swapping speed.
    return iI + 1


