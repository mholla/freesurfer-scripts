# https://github.com/mholla/freesurfer_scripts

# This script creates images of a reconstructed brain surface 
# using a specified colortable.  Subject name, hemipshere, and 
# surface are set in the command. Surfaces are specified as: 
# - inf = inflated
# - wh = white matter
# - pl = pial

# to run for an individual subject:
# "tksurfer subject hemi surface -tcl capture_image.tcl"

# to run for a batch of subjects:
# use capture_images.sh

# some code courtesy of:
# https://surfer.nmr.mgh.harvard.edu/fswiki/QaImageScripts

# ---------------------------------------------------------

# before running, make sure folders are declared correctly.
# $home refers to the current working directory
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

# Iterate surfaces
foreach surfix {1 3} {
  set surfname "ERROR"

  switch -exact -- $surfix {
    1 { set surfname inf ; set zoom 0.75}
    2 { set surfname wh  ; set zoom 1.25}
    3 { set surfname pl  ; set zoom 1.25}
  }

  scale_brain $zoom
  set_current_vertex_set $surfix

  redraw

  # save image, using braces to avoid tcl's utterly brain-dead catenation inadequacies...
  set imagepath "${imagedir}/${subject}_${surfname}.tif"
  save_tiff $imagepath
}

exit 0
