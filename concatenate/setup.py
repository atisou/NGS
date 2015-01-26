__author__ = 'hatice'

from setuptools import setup

setup(name='concatenate',
      #py_modules=['concatenate_reads'],
      version='0.1',
      description='Merge NGS sequencing files by reads types (R1/R2)',
      classifiers=['Licence :: Freeware',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Scientific/Engineering :: Bio-Informatics'],
      keywords='concatenate reads file NGS',
      url='https://github.com/atisou/NGS',
      author='Hatice Akarsu Egger',
      author_email='atisou@hotmail.co.uk',
      license='Freeware',
      package_dir={'': 'concatenate_reads'},
      packages=[''],
      #install_requires=[''],
      include_package_data=True,
      zip_safe=False,

      # Setup the command line function call from the terminal
      #scripts=['bin/run-concatenate'],
      entry_points={
          'console_scripts': ['run-concatenate=concatenate.run_concatenate:command_line_fun'],
      },

      # Setup the unittests calls
      test_suite='nose.collector',
      tests_require=['nose'])

