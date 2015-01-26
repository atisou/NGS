#!/usr/bin/python

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
        self.assertEqual(self.list, concatenate.clean_folder(files_list=self.list, concatenated_file='my_R1.gz'))


        # Create case where a concatenated file already exists
        l2 = self.list[:]
        l2.append('my_R1.gz')

        # Check that the method detects an already existing zip output file of same name
        self.assertNotEqual(l2, concatenate.clean_folder(files_list=self.list, concatenated_file='my_R1.gz'))

        # Check that the method removes the pre-existing zip output file of same name
        self.assertEqual(self.list, concatenate.clean_folder(files_list=l2, concatenated_file='my_R1.gz'))


    def test_make_reads_file(self):
        # Test if make_reads_file() method produces the expected output
         self.assertEqual(['User_sample1_file2_R2.gz', 'User_sample1_file2_R2.gz'], concatenate.make_reads_list(files_list= self.list, read_type='R2'))
         self.assertNotEqual(['User_sample1_file2_R2.gz', 'User_sample1_file2_R2.gz'], concatenate.make_reads_list(files_list= self.list, read_type='R1'))


suite = unittest.TestLoader().loadTestsFromTestCase(TestKnownValues)
unittest.TextTestRunner(verbosity=2).run(suite)


