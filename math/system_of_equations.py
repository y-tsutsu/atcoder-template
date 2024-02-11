from math import lcm

import numpy as np


def system_of_equations(a, b, c, d, u, v):
    '''ax + by = u
       cx + dy = v'''
    lac = lcm(a, c)
    _, b_, _, d_, u_, v_ = lac, b * lac // a, lac, d * lac // c, u * lac // a, v * lac // c
    y = (u_ - v_) / (b_ - d_)
    x = (u - b * y) / a
    return x, y


def system_of_equations_np(a, b, c, d, u, v):
    '''ax + by = u
       cx + dy = v'''
    m = np.array([[a, b], [c, d]])
    n = np.array([u, v])
    return np.linalg.solve(m, n)
