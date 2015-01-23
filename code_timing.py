__author__ = 'hatice'

import concatenate
import cProfile
import os

os.chdir("/path2wd/here")
cProfile.run('concatenate.function_concatenate("sample3", "R1.gz", "R2.gz")')
