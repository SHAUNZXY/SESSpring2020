# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 15:04:01 2020

@author: Xiaoyang Zou
"""

import unittest
import numpy as np
from midterm_project import *

class TestCircle(unittest.TestCase):
    def SetUp(self):
        self.c1 = Circle(0.5,0.5,0.5)
        self.c2 = Circle(0.5,-0.5,0.5)
        self.c3 = Circle(0.5,0.5,-0.5)
        self.c4 = Circle(0.5,-0.5,-0.5)
        self.cl = [self.c1,self.c2,self.c3,self.c4]

    def PointJudgeTest(self):
        self.assertTrue(self.c1.PointJudge)
        
    def RSquareTest(self):
        r1 = RSquare(self.cl)
        r2 = 4*0.5**2
        self.assertEqual(r1,r2)
        
if __name__ == '__main__':
    unittest.main()