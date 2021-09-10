#!/usr/bin/env python


import numpy as np

from six import string_types


# obspy basis convention
OBSPY = [
    'NED',# 	North, East, Down 	Jost and Herrmann 1989
    'USE',# 	Up, South, East 	Global CMT Catalog, Larson et al. 2010
    'XYZ',# 	East, North, Up 	General formulation, Jost and Herrmann 1989
    'RT', # 	Radial, Transverse, Tangential 	psmeca (GMT), Wessel and Smith 1999
    'NWU',# 	North, West, Up 	Stein and Wysession 2003
     ]


# compearth basis conventions
COMPEARTH = [
    1, # USE
    2, # NED  Jost and Herrmann 1989, Aki and Richards 1980
    3, # NWU  Stein and Wysession 2003, Tape and Tape 2012
    4, # ENU
    5, # SEU  Tape and Tape 2013
    ]


mapping = {
    'NED': 2,
    'USE': 1,
    'XYZ': 4,
    'NWU': 3,
    'ENU': 4,
    'SEU': 5,
    }


def _parse_basis(code):

    if not isinstance(code, six.string_types):
        raise ValueError
    code = code.upper()

    if code=='RT':
        raise NotImplementedError

    if code not in COMPEARTH and\
       code not in mapping:
        raise ValueError

    if code in COMPEARTH:
        return code

    elif code in mapping:
        return mapping[code]


def cast(mt, old=None, new=None):
    """ Converts from one basis convention to another
    """

    i1 = _parse_basis(old)
    i2 = _parse_basis(new)

    if  mt.shape != (6,)
       raise ValueError

    mtnew = np.empty(6)
    mtnew[:] = np.nan


    #
    # From now on, we closely follow compearth's implementation
    #

    if i1==i2:
        mtnew = mt

    elif (i1,i2) == (1,2):
        # up-south-east to north-east-down
        mtnew[0] = mt[1]
        mtnew[1] = mt[2]
        mtnew[2] = mt[0]
        mtnew[3] =-mt[5]
        mtnew[4] = mt[3]
        mtnew[5] =-mt[4]
    elif (i1,i2) == (1,3):
        # up-south-east to north-west-up
        mtnew[0] = mt[1]
        mtnew[1] = mt[2]
        mtnew[2] = mt[0]
        mtnew[3] = mt[5]
        mtnew[4] =-mt[3]
        mtnew[5] =-mt[4]
    elif (i1,i2) == (1,4):
        # up-south-east to east-north-up
        mtnew[0] = mt[2]
        mtnew[1] = mt[1]
        mtnew[2] = mt[0]
        mtnew[3] =-mt[5]
        mtnew[4] = mt[4]
        mtnew[5] =-mt[3]
    elif (i1,i2) == (1,5):
        # up-south-east to south-east-up
        mtnew[0] = mt[1]
        mtnew[1] = mt[2]
        mtnew[2] = mt[0]
        mtnew[3] = mt[5]
        mtnew[4] = mt[3]
        mtnew[5] = mt[4]  

    elif (i1,i2) == (2,1):
        # north-east-down to up-south-east
        mtnew[0] = mt[2]
        mtnew[1] = mt[0]
        mtnew[2] = mt[1]
        mtnew[3] = mt[4]
        mtnew[4] =-mt[5]
        mtnew[5] =-mt[3]
    elif (i1,i2) == (2,3):
        # north-east-down to north-west-up
        mtnew[0] = mt[0]
        mtnew[1] = mt[1]
        mtnew[2] = mt[2]
        mtnew[3] =-mt[3]
        mtnew[4] =-mt[4]
        mtnew[5] = mt[5]   
    elif (i1,i2) == (2,4):
        # north-east-down to east-north-up
        mtnew[0] = mt[1]
        mtnew[1] = mt[0]
        mtnew[2] = mt[2]
        mtnew[3] = mt[3]
        mtnew[4] =-mt[5]
        mtnew[5] =-mt[4]
    elif (i1,i2) == (2,5):
        # north-east-down to south-east-up
        mtnew[0] = mt[0]
        mtnew[1] = mt[1]
        mtnew[2] = mt[2]
        mtnew[3] =-mt[3]
        mtnew[4] = mt[4]
        mtnew[5] =-mt[5]   

    elif (i1,i2)==(3,1):
        # north-west-up to up-south-east
        mtnew[0] = mt[2]
        mtnew[1] = mt[0]
        mtnew[2] = mt[1]
        mtnew[3] =-mt[4]
        mtnew[4] =-mt[5]
        mtnew[5] = mt[3]
    elif (i1,i2)==(3,2):
        # north-west-up to north-east-down
        mtnew[0] = mt[0]
        mtnew[1] = mt[1]
        mtnew[2] = mt[2]
        mtnew[3] =-mt[3]
        mtnew[4] =-mt[4]
        mtnew[5] = mt[5] 
    elif (i1,i2)==(3,4):
        # north-west-up to east-north-up
        mtnew[0] = mt[1]
        mtnew[1] = mt[0]
        mtnew[2] = mt[2]
        mtnew[3] =-mt[3]
        mtnew[4] =-mt[5]
        mtnew[5] = mt[4] 
    elif (i1,i2)==(3,5):
        # north-west-up to south-east-up
        mtnew[0] = mt[0]
        mtnew[1] = mt[1]
        mtnew[2] = mt[2]
        mtnew[3] = mt[3]
        mtnew[4] =-mt[4]
        mtnew[5] =-mt[5] 

    elif (i1,i2)==(4,1):
        # east-north-up to up-south-east
        mtnew[0] = mt[2]
        mtnew[1] = mt[1]
        mtnew[2] = mt[0]
        mtnew[3] =-mt[5]
        mtnew[4] = mt[4]
        mtnew[5] =-mt[3]
    elif (i1,i2)==(4,2):
        # east-north-up to north-east-down
        mtnew[0] = mt[1]
        mtnew[1] = mt[0]
        mtnew[2] = mt[2]
        mtnew[3] = mt[3]
        mtnew[4] =-mt[5]
        mtnew[5] =-mt[4]
    elif (i1,i2)==(4,3):
        # east-north-up to north-west-up
        mtnew[0] = mt[1]
        mtnew[1] = mt[0]
        mtnew[2] = mt[2]
        mtnew[3] =-mt[3]
        mtnew[4] = mt[5]
        mtnew[5] =-mt[4] 
    elif (i1,i2)==(4,5):
        # east-north-up to south-east-up
        mtnew[0] = mt[1]
        mtnew[1] = mt[0]
        mtnew[2] = mt[2]
        mtnew[3] =-mt[3]
        mtnew[4] =-mt[5]
        mtnew[5] = mt[4] 

    elif (i1,i2)==(5,1):
        # south-east-up to up-south-east
        mtnew[0] = mt[2]
        mtnew[1] = mt[0]
        mtnew[2] = mt[1]
        mtnew[3] = mt[4]
        mtnew[4] = mt[5]
        mtnew[5] = mt[3]
    elif (i1,i2)==(5,2):
        # south-east-up to north-east-down
        mtnew[0] = mt[0]
        mtnew[1] = mt[1]
        mtnew[2] = mt[2]
        mtnew[3] =-mt[3]
        mtnew[4] = mt[4]
        mtnew[5] =-mt[5]
    elif (i1,i2)==(5,3):
        # south-east-up to north-west-up
        mtnew[0] = mt[0]
        mtnew[1] = mt[1]
        mtnew[2] = mt[2]
        mtnew[3] = mt[3]
        mtnew[4] =-mt[4]
        mtnew[5] =-mt[5]
    elif (i1,i2)==(5,4):
        # south-east-up to east-north-up
        mtnew[0] = mt[1]
        mtnew[1] = mt[0]
        mtnew[2] = mt[2]
        mtnew[3] =-mt[3]
        mtnew[4] = mt[5]
        mtnew[5] =-mt[4] 

    return mtnew

