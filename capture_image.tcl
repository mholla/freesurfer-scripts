# https://github.com/mholla/freesurfer_scripts

# This script creates images of a reconstructed brain surface using a specified colortable.  

# Subject name and hemipshere are defined in the command (or, for batch mode, in capture_images.sh).  
# Color tables should be set in the code below.
# Multiple surfaces can be specified in the code below by the numbers.
# 0  Main
# 1  Inflated
# 2  White
# 3  Pial
# 4  Original
# Main and Original appear to both refer to the surface specified in the command.

# to run for an individual subject:
# "tksurfer subject hemi surface -tcl capture_image.tcl"

# to run for a batch of subjects: use capture_images.sh

# some code courtesy of:
# https://surfer.nmr.mgh.harvard.edu/fswiki/QaImageScripts

# ---------------------------------------------------------

# before running, make sure folders are declared correctly.
# $home refers to freesurfer's subject folder and does not appear to be changeable
# to change folder, type "setenv SUBJECT_DIR "path/to/subject/directory/" " in the terminal
set subjectsdir $home
set  subjectdir "$home/$subject"
set    imagedir "$home/images"

puts "Subject Dir: $subjectdir"
puts "Hemi: $hemi"

# choose atlas (note: this command wants side (lh/rh) omitted)
labl_import_annotation "aparc.a2009s.annot" ;# Destrieux atlas
# labl_import_annotation "aparc.annot" ;# Desikan-Killiany atlas

# choose color table
labl_load_color_table "$subjectsdir/colortable.ctab"

# align hemisphere to capture lateral surface
set rotmult 1
if {$hemi == "rh"} {
  set rotmult -1
}

# if specifying surfaces in this file, update switch and foreach commands 
foreach surfix {0} {
  set surfname "ERROR"

  switch -exact -- $surfix {
    0 { set surfname main; set zoom 1.00}
    1 { set surfname inf ; set zoom 0.75}
    2 { set surfname wh  ; set zoom 1.25}
    3 { set surfname pl  ; set zoom 1.25}
    4 { set surfname orig; set zoom 1.00}
  }

  scale_brain $zoom
  set_current_vertex_set $surfix

  redraw

  # save image, using braces to avoid tcl's utterly brain-dead catenation inadequacies...
  set imagepath "${imagedir}/${subject}_${surfname}.tif"
  save_tiff $imagepath
}

exit 0
