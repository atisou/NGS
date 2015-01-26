__author__ = 'hatice'

import concatenate
import cProfile
import os

os.chdir("/path2wd/here")
cProfile.run('concatenate.function_concatenate("sample_folder_name", "R1_outfile", "R2_outfile"), "timing.stats"')
