__author__ = 'hatice'

import concatenate
import unittest


class TestKnownValues(unittest.TestCase):
    def setUp(self):
        self.list = ['User_sample1_file1_R1.gz', 'User_sample1_file2_R1.gz',
                     'User_sample1_file2_R2.gz', 'User_sample1_file2_R2.gz']

    def test_clean_folder(self):
        """test if the screening of a folder gives the right list of files"""

        # Best case scenario: no pre-existing concatenated file, clean_folder does nothing
        self.assertEqual(self.list, concatenate.clean_folder(files_list=self.list, readtype='R1'))


        # A concatenated file already exists: check if clean_folder() removes it correctly
        l2 = self.list.append('R1.gz')
        self.assertNotEqual(l2, concatenate.clean_folder(files_list=self.list, readtype='R1'))


suite = unittest.TestLoader().loadTestsFromTestCase(TestKnownValues)
unittest.TextTestRunner(verbosity=2).run(suite)
