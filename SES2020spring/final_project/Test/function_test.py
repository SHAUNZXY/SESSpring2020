import unittest
import numpy as np
import final_project_NBA
from final_project_NBA import NBA_Analysis
import filecmp
import warnings

class test_func(unittest.TestCase):
    
    def setUp(self):
        self.pathtest=NBA_Analysis("test_player_regular_season_career.txt")
        warnings.simplefilter("ignore", ResourceWarning)

    def test_Save(self):
        self.pathtest.Save('efficiency')
        result = filecmp.cmp("top50_efficiency.txt", "standard_result.txt")
        print('The result of the comparison is {}'.format(result))
        self.assertTrue(result)
    

if __name__ == '__main__':

    unittest.main(verbosity=2)
