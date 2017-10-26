# freesurfer_scripts
#### _A variety of useful scripts developed for use with open-source brain MRI software Freesurfer_

[Freesurfer](https://surfer.nmr.mgh.harvard.edu/) is an open source software suite for processing and analyzing (human) brain MRI images.  These scripts were developed for use in academic research and are made public in the hopes of further improving upon the usefulness of Freesurfer and its related programs.  

- anonymize_freesurfer.py  
..This script works on a folder containing post-processing files from Freesurfer.
 It replaces the subject ID in the folder of freesurfer data with a randomly-
 generated number, and copies each anonymized file into the appropriate subfolder 
 of the anonymized subject ID.  The original subject ID and new anonymized ID are 
 stored in a single text file for later decoding.  Additionally, all MRI images that
 contain the skull are defaced to prevent identification through 3D reconstruction.
 Defacing of each MRI takes ~1 hour, so each subject should be expected to take ~7 hours.

- make_ctable.py
..This file contains several functions that facilitate the creation of a user-defined colortable.  Colors can be defined for a given region or set of regions (current code assigns colors randomly on a blue-white-red colormap).  

- capture_image.tcl
..This script creates images of the brain given a subject, hemisphere, surface, and a specified colortable.

- capture_images.sh
..This is a bash script that creates images of the brain in batches, using capture_image.tcl

  

If you find any errors or omissions or have suggestions for ways I could improve this resource, please contact me by [email](maria-holl@nd.edu).