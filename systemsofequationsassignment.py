#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 17:40:00 2023

@author: djhoannapiolo
"""
import numpy as np
import numpy.linalg as nl


A = np.array([ [2,-1,3],
               [-1,3,-1],
               [4,-4,3]])

b = np.array([[10],
              [-1],
              [3]])

# I need A-inverse

Ainv = nl.inv(A)

print(Ainv @ A)

x = Ainv @ b
print(x)

print(A@x - b)