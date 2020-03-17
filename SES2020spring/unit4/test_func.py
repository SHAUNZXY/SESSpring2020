# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 15:04:01 2020

@author: Xiaoyang Zou
"""

import unittest
import numpy as np
from midterm_project import Circle
from midterm_project import RSquare, MaxAreaCircles

class TestCircle(unittest.TestCase):
    def setUp(self):
        self.c1 = Circle(0.5,0.5,0.5)
        self.c2 = Circle(0.5,-0.5,0.5)
        self.c3 = Circle(0.5,0.5,-0.5)
        self.c4 = Circle(0.5,-0.5,-0.5)
        self.cl = []
        self.cl.append(self.c3)
        self.cl.append(self.c4)

    def test_PointJudge(self):
        self.assertTrue(self.c1.PointJudge(self.cl))
        
    def test_RSquare(self):
        r1 = RSquare(self.cl)
        r2 = 2*0.5**2
        self.assertEqual(r1,r2)
        
    def test_distance(self):
        d1=self.c1.distance(self.c2)
        d2=np.linalg.norm([self.c1.x-self.c2.x,self.c1.y-self.c2.y])      
        self.assertEqual(d1, d2)
        
    def test_MaxAreaCircles(self):
        m = 4
        cl = MaxAreaCircles(m,False)
        result = RSquare(cl)
        self.assertGreaterEqual(result,1)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)