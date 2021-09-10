#!/usr/bin/env python


import unittest
import numpy as np

from mtpar import cmt2tt, cmt2tt15, tt2cmt, tt152cmt
from mtpar.basis import cast
from mtpar.util import PI, DEG

try:
    from mtuq.grid import FullMomentTensorGridRandom, FullMomentTensorGridRegular,\
        DoubleCoupleGridRandom
    from mtuq.util.lune import to_mij

except ImportError:
    raise Exception("MTUQ not installed")


EPSVAL = 1.e-3
NSAMPLES = 50

def isclose(a, b):
    return np.all(np.isclose(a, b, rtol=EPSVAL))


class TestMomentTensor(unittest.TestCase):
    def test_DoubleCoupleGridRandom(self):
        for _ in range(NSAMPLES):
             grid = DoubleCoupleGridRandom(magnitude=1., npts=1)
             M1 = grid.get(0)

             args = []
             for val in grid.vals:
                 args += [val[0]]
             M2 = tt152cmt(*args)

             e = np.linalg.norm(M1-M2)/np.linalg.norm(M1)
             if e > EPSVAL:
                 print('||M1 - M2|| = %e' % e)
                 raise Exception


    def test_FullMomentTensorGridRandom(self):
        for _ in range(NSAMPLES):
             grid = FullMomentTensorGridRandom(magnitude=1., npts=1)

             dict1 = grid.get_dict(0)
             keys1 = list(dict1.keys())
             vals1 = np.array(list(dict1.values()))
             vals2 = cmt2tt15(grid.get(0))

             print()
             if not isclose(vals1, vals2):
                 for _i in range(6):
                     print('%10s: %9.2e %9.2e' % (keys1[_i], vals1[_i], vals2[_i]))
                 raise Exception

         


    def test_FullMomentTensorGridRandom2(self):
         grid = FullMomentTensorGridRandom(magnitude=1., npts=1)
         M1 = grid.get(0)

         args = []
         for val in grid.vals:
             args += [val[0]]
         M2 = tt152cmt(*args)

         e = np.linalg.norm(M1-M2)/np.linalg.norm(M1)
         if e > EPSVAL:
             print('||M1 - M2|| = %e' % e)
             raise Exception


    def test_grid_callback(self):
         grid1 = FullMomentTensorGridRegular(
             magnitude=1., npts_per_axis=10)

         grid2 = FullMomentTensorGridRegular(
             magnitude=1., npts_per_axis=10, callback=tt152cmt)

         M1 = grid1.get(333)
         M2 = grid2.get(333)

         e = np.linalg.norm(M1-M2)/np.linalg.norm(M1)
         if e > EPSVAL:
             print('||M1 - M2|| = %e' % e)
             raise Exception




if __name__ == '__main__':
    unittest.main()

