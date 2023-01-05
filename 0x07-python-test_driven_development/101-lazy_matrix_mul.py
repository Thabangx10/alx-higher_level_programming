#!/usr/bin/python3
"""Defines a matrix multiplication function using NUMPY"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """The multiplication of 2 matrices.

       Arguments:
                m_a (list of lists containing ints/floats):
                m_b (list of lists containing ints/floats):
    """

    return(np.matmul(m_a, m_b))
