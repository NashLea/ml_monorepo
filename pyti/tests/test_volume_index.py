from __future__ import absolute_import
import unittest
import numpy as np

from tests.sample_data import SampleData
from pyti import volume_index


class TestVolumeIndex(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.close_data = SampleData().get_sample_close_data()
        self.volume = SampleData().get_sample_volume()

        self.pvi_expected = [1.0, 1.0131617136727868, 1.0152943403369297, 
        1.0220581740172878, 1.0220581740172878, 1.0244368189382491, 
        1.0244368189382491, 1.028220752029624, 1.028220752029624, 
        1.0248545154752871, 1.0248545154752871, 1.0276690488102527, 
        1.0244650041655374, 1.0151167327315447, 1.0151167327315447, 
        0.9972084407513031, 0.99256833708695491, 0.99256833708695491, 
        0.99517706110413839, 0.97758096185097998, 0.97758096185097998, 
        0.97758096185097998, 0.99466607532561435, 0.99006720628561307, 
        0.99006720628561307, 0.9885444164271886, 0.99615836571931071, 
        0.99615836571931071, 0.98495031479002748, 0.99788463403910965, 
        0.99788463403910965, 0.99171806061919043, 0.99171806061919043, 
        1.0161153624211521, 1.027359450785359, 1.027359450785359, 
        1.0355085426193171, 1.0228194246619016, 0.99612764186303671, 
        0.99612764186303671, 1.0040616159726605, 1.0257877152198811, 
        1.0257877152198811, 1.0257877152198811, 1.0230216079786347, 
        1.0289668610989608, 1.0289668610989608, 1.0289668610989608, 
        1.0289668610989608, 1.0259326287949169, 1.0259326287949169, 
        1.0189863197822924, 1.0189863197822924, 1.0189863197822924, 
        1.0183277653623486, 1.0280667720726715, 1.0280667720726715, 
        1.0339082770092849, 1.0168155256078024, 1.0168155256078024, 
        1.0168155256078024, 1.0187952720226248, 1.0187952720226248, 
        1.0187952720226248, 1.016996041509638, 1.0263976544718645, 
        1.0263976544718645, 1.0263976544718645, 1.0421392044955968, 
        1.0421392044955968, 1.0281920752436917, 1.0214867246418142, 
        1.0214867246418142, 1.0248001127276287, 1.0248001127276287, 
        1.0110249205679784, 1.0110249205679784, 1.0110249205679784, 
        0.99793812043944774, 1.0161128254535388, 1.0161128254535388, 
        1.0161128254535388, 1.0020913185554337, 1.0020913185554337, 
        1.0001286681336989, 1.0027497561162737, 1.0076880378225743, 
        1.0043958500183741, 1.0043958500183741, 1.0073152364142319, 
        1.011110438728847, 1.0115673861647203, 1.0115673861647203, 
        1.0154889254595501, 1.0154889254595501, 1.0154889254595501, 
        1.0215347849615932, 1.0215347849615932, 1.0229904134885814, 
        1.0233574850301697, 1.0220790634542931, 1.0220790634542931, 
        1.0242368747726398, 1.0242368747726398, 1.0242368747726398, 
        1.0257753069682629, 1.0257753069682629, 1.0134804497418848, 
        1.0134804497418848, 1.0083590544889585, 1.0026421481601104, 
        1.0026421481601104, 1.0049716578506291, 0.99852579865015956, 
        0.99852579865015956, 0.99368537269643453, 0.99368537269643453, 
        0.99368537269643453, 0.99368537269643453, 0.98515032029708494, 
        0.98924228371006429, 0.98207121911504114, 0.96934966949449142, 
        0.96934966949449142, 0.97169334499548909, 0.97169334499548909, 
        0.97908212385343263]

        self.nvi_expected = [1.0, 1.0, 1.0, 1.0, 0.99737014309878635,
        0.99737014309878635, 1.0004742987659747, 1.0004742987659747,
        0.99716065719744162, 0.99716065719744162, 1.0043145436667653,
        1.0043145436667653, 1.0043145436667653, 1.0043145436667653,
        1.0062413756294879, 1.0062413756294879, 1.0062413756294879,
        0.98680231838995269, 0.98680231838995269, 0.98680231838995269,
        0.98663450803834407, 1.001543812354337, 1.001543812354337,
        1.001543812354337, 0.9944189699523458, 0.9944189699523458,
        0.9944189699523458, 0.99416561480076548, 0.99416561480076548,
        0.99416561480076548, 0.98635048365765376, 0.98635048365765376,
        0.95843298325586723, 0.95843298325586723, 0.95843298325586723,
        0.98950906327275012, 0.98950906327275012, 0.98950906327275012,
        0.98950906327275012, 0.99088989143683581, 0.99088989143683581,
        0.99088989143683581, 0.99632731175782552, 1.0082109045860519,
        1.0082109045860519, 1.0082109045860519, 1.0161210862361918,
        1.024938792602782, 1.0106146186998928, 1.0106146186998928,
        1.0173304832838312, 1.0173304832838312, 0.99918797201758558,
        0.99641396346902655, 0.99641396346902655, 0.99641396346902655,
        0.99371355483156543, 0.99371355483156543, 0.99371355483156543,
        0.99665482086415003, 0.99435889590200588, 0.99435889590200588,
        0.99137380024919031, 0.99593195460701656, 0.99593195460701656,
        0.99593195460701656, 0.99675568915703361, 0.98682169637474004,
        0.98682169637474004, 0.9880204711359688, 0.9880204711359688,
        0.9880204711359688, 0.98259721740583439, 0.98259721740583439,
        0.98661148727656012, 0.98661148727656012, 0.98443970883380372,
        0.99704600899003337, 0.99704600899003337, 0.99704600899003337,
        1.0034417876586332, 1.0034790446217512, 1.0034790446217512,
        0.99659080642219422, 0.99659080642219422, 0.99659080642219422,
        0.99659080642219422, 0.99659080642219422, 0.99417854456756283,
        0.99417854456756283, 0.99417854456756283, 0.99417854456756283,
        0.9975467383944433, 0.9975467383944433, 1.000864645328748,
        0.99560818602833268, 0.99560818602833268, 0.99695467086972778,
        0.99695467086972778, 0.99695467086972778, 0.99695467086972778,
        0.994176709793965, 0.994176709793965, 0.98225048254896785,
        0.98430800315838363, 0.98430800315838363, 0.98531676754696274,
        0.98531676754696274, 0.9535660945461697, 0.9535660945461697,
        0.9535660945461697, 0.95340247863870453, 0.95340247863870453,
        0.95340247863870453, 0.95677675074268698, 0.95677675074268698,
        0.956510065780109, 0.93419742391107474, 0.93441331173792364,
        0.93441331173792364, 0.93441331173792364, 0.93441331173792364,
        0.93441331173792364, 0.92071826863351425, 0.92071826863351425,
        0.91541969388983713, 0.91541969388983713]

    def test_pvi(self):
        pvi = volume_index.positive_volume_index(self.close_data, self.volume)
        print(list(pvi))
        np.testing.assert_array_equal(pvi, self.pvi_expected)

    def test_pvi_invalid_data(self):
        self.close_data.append(1)
        with self.assertRaises(Exception) as cm:
            volume_index.positive_volume_index(self.close_data, self.volume)
        expected = ("Error: mismatched data lengths, check to ensure that all input data is the same length and valid")
        self.assertEqual(str(cm.exception), expected)

    def test_nvi(self):
        nvi = volume_index.negative_volume_index(self.close_data, self.volume)
        np.testing.assert_array_equal(nvi, self.nvi_expected)

    def test_nvi_invalid_data(self):
        self.close_data.append(1)
        with self.assertRaises(Exception) as cm:
            volume_index.negative_volume_index(self.close_data, self.volume)
        expected = ("Error: mismatched data lengths, check to ensure that all input data is the same length and valid")
        self.assertEqual(str(cm.exception), expected)
