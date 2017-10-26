# https://github.com/mholla/freesurfer_scripts

# This script creates images of a reconstructed brain surface, 
# using the script capture_image.tcl
  
# Subject names, hemipsheres, and surfaces are set in the code below.
# Surfaces are specified as: 
# - inf = inflated
# - wh = white matter
# - pl = pial

# run in freesurfer/subjects folder as "bash capture_images.sh"

# ---------------------------------------------------------

function onehemi() {
  sbjid=$1
  hemi=$2
  surf=$3

  subjectdir=$sbjid

  tksurfer $sbjid $hemi $surf -tcl "capture_image.tcl"
}

# list desired subjects, hemispheres, and surfaces here
onehemi subject_name lh pl
onehemi subject_name rh inf 

