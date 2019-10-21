#!/usr/bin/env python


import unittest
import numpy as np

from mtpar import cmt2tt, cmt2tt15, tt2cmt, tt152cmt
from mtpar.basis import change_basis
from mtpar.util import PI, DEG

try:
    from mtuq.grid import FullMomentTensorGridRandom
except ImportError:
    raise Exception("MTUQ not installed")


EPSVAL = 1.e-3


class TestMomentTensor(unittest.TestCase):
    def test_RandomFullMomentTensor(self):
         grid = FullMomentTensorGridRandom(magnitude=1., npts=1)
         M1 = grid.get(0)

         args = []
         for val in grid.vals:
             args += [val[0]]
         M2 = tt152cmt(*args)

         e = np.linalg.norm(M1-M2)/np.linalg.norm(M1)
         if e > EPSVAL:
             for val in M1: print(val)
             print()
             for val in M2: print(val)
             print()

             print('||M1 - M2|| = %e' % e)
             raise Exception



if __name__ == '__main__':
    unittest.main()

