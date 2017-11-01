# https://github.com/mholla/freesurfer_scripts

# This script creates images of a reconstructed brain surface, 
# using the script capture_image.tcl
  
# Subject names and hemisperes are set in the code below.
# Single surfaces can be specified here, or multiple surfaces in capture_image.tcl
# Color tables should be specified in capture_image.tcl

# run in subjects folder as "bash capture_images.sh"
# to change subjects folder, type "setenv SUBJECT_DIR "path/to/subject/directory/" " in the terminal

# ---------------------------------------------------------

function onehemi() {
  sbjid=$1
  hemi=$2
  surf=$3

  tksurfer $sbjid $hemi $surf -tcl "capture_image.tcl"
}

# list desired subjects, hemispheres, and surfaces here
onehemi subject_name lh pial
onehemi subject_name rh inflated

