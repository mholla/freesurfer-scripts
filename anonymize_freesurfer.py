'''
https://github.com/mholla/freesurfer_scripts

This script works on a folder containing post-processing files from Freesurfer.
It replaces the subject ID in the folder of freesurfer data with a randomly-
generated number, and copies each anonymized file into the appropriate subfolder 
of the anonymized subject ID.  The original subject ID and new anonymized ID are 
stored in a single text file for later decoding.  Additionally, all MRI images that
contain the skull are defaced to prevent identification through 3D reconstruction.
Defacing of each MRI takes ~1 hour, so each subject should be expected to take ~7 hours.

To use:
1. place this file in the freesurfer/subjects folder (or any folder containing the 
   desired subjects)
2. download mri_deface tools from https://surfer.nmr.mgh.harvard.edu/fswiki/mri_deface 
   and follow instructions to decompress downloads
3. place resulting files (mri_deface, talairach_mixed_with_skull.gca, and face.gca)
   in the same subject folder
4. populate list of subjects if not the entire folder
4. run (python anonymize_freesurfer.py)

Besides subject name, identifying dates or other information may remain which may be 
considered Personal Health Information (PHI).  This script is not guaranteed to remove 
all PHI.  All responsibility rests with the end user to ensure confidentiality.  
'''

# ---------------------------------------------------------

import os
import random
from shutil import copyfile

def anonymize_file(subject,ID,path):

    orig_filename = '%s/%s' %(subject,path)
    anon_filename = '%s/%s' %(ID,path)

    # create anonymized file
    anon_file = open(anon_filename,'w')
    
    # search for subject name and replace it with subject ID
    contents = open(orig_filename).read()
    contents_anon = contents.replace(subject, ID)
    anon_file.write(contents_anon)
    anon_file.close()


def copy_file(subject,ID,path):
    
    orig_filename = '%s/%s' %(subject,path)
    anon_filename = '%s/%s' %(ID,path)

    copyfile(orig_filename,anon_filename)


def anonymize_mgz(subject,ID,path):

    orig_filename = '%s/%s' %(subject,path)
    anon_filename = '%s/%s' %(ID,path)

    # https://surfer.nmr.mgh.harvard.edu/fswiki/mri_deface
    command_string = 'mri_deface %s talairach_mixed_with_skull.gca face.gca %s' %(orig_filename,anon_filename)
    print command_string
    os.system(command_string)


def anonymize_folder(subject,ID,path):

    extensions = ['.label','.stats','.touch','.log','.bak','.old','.lta','recon-all']
    mgzs = ['nu_noneck.mgz','nu.mgz','001.mgz','orig_nu.mgz','orig.mgz','rawavg.mgz','T1.mgz']

    items = os.listdir('%s/%s' %(subject,path))
    for item in items:

        fullpath = '%s/%s' %(path,item)
        
        if os.path.isdir('%s/%s' %(subject,fullpath)):
            print '%s/%s is a directory' %(subject,fullpath)
            anonymize_folder(subject,ID,fullpath)
        else:
            if any(x in item for x in extensions):
                anonymize_file(subject,ID,fullpath)
                print '%s/%s has been anonymized' %(subject,fullpath)
            elif any(y in item for y in mgzs):
                anonymize_mgz(subject,ID,fullpath)
                print '%s/%s has been anonymized' %(subject,fullpath)
            else:
                copy_file(subject,ID,fullpath)
                print '%s/%s has been copied' %(subject,fullpath)


def anonymize_subject(subject):

    # generate anonymous subject ID
    ID = '%04d' %random.randint(0,9999)
    print subject, ID

    code = open('anonymization.txt','a')
    code.write('%s %s \n' %(subject, ID))
    code.close()

    # set up anonymous file structure
    os.mkdir(ID)

    folders = ['label','mri','scripts','stats','surf','touch','mri/transforms','mri/orig']

    for folder in folders:
        os.mkdir('%s/%s' %(ID,folder))

    # copy anonymous data to new directory
    folders = os.listdir(subject)
    for folder in folders:

        anonymize_folder(subject,ID,folder)


if __name__ == '__main__':

    subjects = os.listdir(os.getcwd())
    # subjects = ['subject1','subject2']

    for subject in subjects:
        anonymize_subject(subject)
