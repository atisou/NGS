#!/usr/bin/python

__author__ = 'hatice'

# This is a script, which aims to concatenate the sequencing files of sample based on their reads types. There are 2 types of reads: R1 and R2. The idea is to merge all the R1 sequencing files of a sample together, and do the same for the R2 sequencing files of the same sample. Finally, apply this to all the sequencing samples of the experiment. This script assumes that the sample folder contains only sequencing files.

import os
import re


def screen_folder(path, folder_name):
    """ Function that lists the content/file_names of a folder"""

    folder = path + folder_name + '/'
    files_list = os.listdir(folder)
    return files_list


def clean_folder(files_list, readtype):
    """ Function to remove concatenated files that could exist already in sample folder. This would be the case if re-run this script."""

    concatenated_file = str(readtype) + '.gz'

    while concatenated_file in files_list:
        s = 'echo Found pre-existing concatenated file: deleting it...'
        os.system(s)
        files_list.remove(concatenated_file)

    return files_list



def make_reads_list(files_list, read_type):
    """Function that separates the files by read type (R1 or R2), within a given sample folder"""

    # Prepare the lists that will hold reads type specific files, for a given sample folder
    list_per_read = []

    # Loop through files of a sample folder:
    pattern = str(read_type)
    for file in files_list:
        # Do pattern matching for R1 or R2
        matched_file = re.search(pattern, file)
        if matched_file:
            # Append found R1 file to R1 files list (same with R2)
            list_per_read.append(file)


    # Sort the files lists to make sure the R1 and R2 files are ordered in exactly same way in both lists; i.e same file has R1 and R2 data at the same index position in both lists
    list_per_read = sorted(list_per_read)

    return list_per_read


def zip_merge(path, read_type, filename):
    """Function that calls a bash function from the terminal. This bash function is gzip that can concatenate directly the gz files into a merged gz file"""

    infile = path + filename
    outfile = path + read_type + '.gz'
    # Use cat instead of gzip -c, since sequencing files could be gz or not
    s = 'cat %s >> %s' % (infile, outfile)
    print s
    os.system(s)


def apply_zip(path, read_type, type_list):
    """Loop function: apply the zip function to each file in the read type container, i.e R1 and R2 files lists"""

    for type_file in type_list:
        zip_merge(path, read_type, type_file)



def concatenate_sample_files_per_read_type(experiment_path, experiment_name, read_type):
    """Main function that loops through each sample folder and applies the gzip by reads type. R1.gz and R2.gz files are created for each sample."""

    samples_names = screen_folder(experiment_path, experiment_name)
    sample_path = experiment_path + experiment_name + '/'
    for sample in samples_names:
        # List all the files within a given sample folder
        reads_files_per_sample = screen_folder(sample_path, sample)

        # Remove from the files list the previously concatenated zip files if exist.
        reads_files_per_sample = clean_folder(reads_files_per_sample, read_type)

        # List files of a given sample folder ranged by read type
        reads_list = make_reads_list(reads_files_per_sample, read_type)

        # Do the zip of the R1 or R2 files, within a given folder of sample
        path = sample_path + sample + '/'
        apply_zip(path, read_type, reads_list)



def function_concatenate(experiment_path, experiment_name):

    for read_type in ('R1', 'R2'):
        concatenate_sample_files_per_read_type(experiment_path, experiment_name, read_type)



#These lines of code allow the python script to be called directly from bash with the arguments of the main function. For this, need to define what the main function of the script is.
if __name__ == "__main__":
    import sys
    function_concatenate(str(sys.argv[1]), str(sys.argv[2]))



# function_concatenate(experiment_path='/home/hatice/Documents/Projects/Unifr/', experiment_name='test')

