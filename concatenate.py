#!/usr/bin/python

__author__ = 'hatice'

# This is a script, which aims to concatenate the sequencing files of sample based on their reads types. There are 2 types of reads: R1 and R2. The idea is to merge all the R1 sequencing files of a sample together, and do the same for the R2 sequencing files of the same sample. Finally, apply this to all the sequencing samples of the experiment. This script assumes that the sample folder contains only sequencing files.

#########
# Usage:#
#########
# cd in working directory, where the samples folders are located.
# type:
# python </path/2/concatenate.py/>   <folder_name_containing_files>  <output_R1.gz> <output_R2.gz>



import os
import re

os.chdir('/home/hatice/Documents/Projects/Unifr/test')

def screen_folder(folder_name):
    """ Function that lists the content/file_names/subfolders_names of a folder"""

    content_list = os.listdir(folder_name)
    return content_list  #this is not full path file/foldernames list but only file/foldernames


def clean_folder(files_list, concatenated_file):
    """ Function to remove concatenated files that could exist already in sample folder. This would be the case if re-run this script."""

    l1 = concatenated_file.split('/')
    concatenated_file_wo_path = l1[-1]
    while concatenated_file_wo_path in files_list:
        s = "echo Found pre-existing concatenated file with same name %s: deleting it..." % concatenated_file_wo_path
        os.system(s)
        s2 = 'rm %s' % concatenated_file
        os.system(s2)
        files_list.remove(concatenated_file_wo_path)

    for name in files_list:
        if re.search('R1|R2', name) == None:
            print "found a non seq file %s: skipping it..." % name
            files_list.remove(name)

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


def zip_merge(infile, outfile):
    """Function that calls the cat bash function from the terminal. The advantage of cat is that it can be used directly on gz files without decompressing them. The disadvantage of cat is that it concatenates without zipping, therefore if the input files are not zipped, the output file won't be neither. The alternative would be gzip -c."""

    # Use cat instead of gzip -c, since sequencing files could be gz or not
    s = 'cat %s >> %s' % (infile, outfile)
    print s
    os.system(s)



def concatenate_sample_files_per_read_type(folder_name, concatenated_file,read_type):
    """Main function that loops through each sample folder and applies the gzip by reads type. R1.gz and R2.gz files are created for each sample."""

    # List all the files within a given sample folder
    files_list = screen_folder(folder_name)


    # Remove from the files list the previously concatenated zip files if exist.
    reads_files_per_sample = clean_folder(files_list, concatenated_file)

    # List files of a given sample folder ranged by read type
    reads_list = make_reads_list(reads_files_per_sample, read_type)

    # Do the zip of the R1 or R2 files, within a given folder of sample
    for typespe_file in reads_list:
        infile = folder_name + typespe_file
        zip_merge(infile, concatenated_file)



def function_concatenate(folder_name, r1_concatenated_file, r2_concatenated_file):

    path = os.getcwd()
    full_folder_name = path + '/' + folder_name + '/'
    full_r1_concatenated_file = full_folder_name + r1_concatenated_file
    full_r2_concatenated_file = full_folder_name + r2_concatenated_file

    concatenate_sample_files_per_read_type(full_folder_name, full_r1_concatenated_file, 'R1')
    concatenate_sample_files_per_read_type(full_folder_name, full_r2_concatenated_file, 'R2')



#These lines of code allow the python script to be called directly from bash with the arguments of the main function. For this, need to define what the main function of the script is.
# if __name__ == "__main__":
#     import sys
#     function_concatenate(str(sys.argv[1]), str(sys.argv[2]),  str(sys.argv[3]))



function_concatenate('sample1', 'R1.gz', 'R2.gz')

