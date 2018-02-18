# Author: Christian Seely

import time

# This class holds utility methods to be used in any of the algorithms.

class Utils(object):

    @staticmethod
    def timeit(func):
        def timed(*args, **kw):
            iStart = time.time()
            func(*args, **kw)
            iEnd = time.time()
            print("\nTime: {0}".format(iEnd-iStart))
        return timed