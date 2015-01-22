__author__ = 'hatice'

import concatenate
import unittest

class TestKnownValues(unittest.TestCase):

    def setUp(self):
        self.list = ['User_sample1_file1_R1.gz', 'User_sampl1_file2_R1.gz',
                     'User_sampl1_file2_R2.gz', 'User_sampl1_file2_R2.gz']

    def test_clean_folder(self):
       """test if the screening of a folder gives the right list of files"""
       self.assertEqual(self.list, concatenate.clean_folder(files_list=self.list, readtype='R1'))

suite = unittest.TestLoader().loadTestsFromTestCase(TestKnownValues)
unittest.TextTestRunner(verbosity=2).run(suite)

