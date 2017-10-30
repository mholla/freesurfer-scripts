'''
https://github.com/mholla/freesurfer_scripts

This file contains several functions that facilitate the creation of a user-defined colortable

Colors can be defined for a given region or set of regions in make_colortable 
(current code assigns colors randomly on a blue-white-red colormap)

list_regions creates the required ordered list of regions in the Destrieux atlas; 
if another atlas is desired (i.e., Desikan-Killiany), this list should be recreated accordingly

define_color is a helper function that tranforms a number into a color given a colormap and a range

write_ctab_entry writes a single line of the ctab file, defining region i to be a given color
the function name_to_rgb requires the package webcolors (https://pypi.python.org/pypi/webcolors/)
'''


import string
import numpy
import matplotlib
import matplotlib.pyplot as plt
import random
from webcolors import *

def make_colortable(filename):
    ''' 
    make_colortable(filename): writes a complete ctab to the file specified
    '''

    regions = list_regions()

    f = open(filename,'w')

    for i in range(len(regions)):
        color = define_color(random.randint(0,99),0,100)
        write_ctab_entry(f,regions,i,color)
    
    f.close()


def list_regions():
    ''' 
    list_regions(): lists regions of the Destrieux atlas along with the required ordering in the ctab file

    2nd column is ordering for ctab file
    3rd column matches numbering in Destriuex 2010 paper
    '''

    regions = [
        ['Unknown',                       0,  0],
        ['G_and_S_frontomargin',          1,  1],
        ['G_and_S_occipital_inf',         2,  2],
        ['G_and_S_paracentral',           3,  3],
        ['G_and_S_subcentral',            4,  4], 
        ['G_and_S_transv_frontopol',      5,  5],
        ['G_and_S_cingul-Ant',            6,  6],
        ['G_and_S_cingul-Mid-Ant',        7,  7],
        ['G_and_S_cingul-Mid-Post',       8,  8],
        ['G_cingul_Post_dorsal',          9,  9],
        ['G_cingul_Post_ventral',        10, 10],
        ['G_cuneus',                     11, 11],
        ['G_front_inf_Opercular',        12, 12],
        ['G_front_inf_Orbital',          13, 13],
        ['G_front_inf_Triangul',         14, 14],
        ['G_front_middle',               15, 15],
        ['G_front_sup',                  16, 16],
        ['G_Ins_lg_and_S_cent_ins',      17, 17],
        ['G_insular_short',              18, 18],
        ['G_occipital_middle',           19, 19], 
        ['G_occipital_sup',              20, 20],
        ['G_oc_temp_lat_fusifor',        21, 21], 
        ['G_oc_temp_med_Lingual',        22, 22], 
        ['G_oc_temp_med_Parahip',        23, 23], 
        ['G_orbital',                    24, 24],
        ['G_pariet_inf_Angular',         25, 25],
        ['G_pariet_inf_Supramar',        26, 26],
        ['G_parietal_sup',               27, 27],
        ['G_postcentral',                28, 28],
        ['G_precentral',                 29, 29],
        ['G_precuneus',                  30, 30],
        ['G_rectus',                     31, 31],
        ['G_subcallosal',                32, 32],
        ['G_temp_sup_G_T_transv',        33, 33],
        ['G_temp_sup_Lateral',           34, 34], 
        ['G_temp_sup_Plan_polar',        35, 35],
        ['G_temp_sup_Plan_tempo',        36, 36],
        ['G_temporal_inf',               37, 37],
        ['G_temporal_middle',            38, 38],
        ['Lat_Fis-ant-Horizont',         39, 39],
        ['Lat_Fis-ant-Vertical',         40, 40],
        ['Lat_Fis-post',                 41, 41],
        ['Medial_wall',                  42, 75],
        ['Pole_occipital',               43, 42],
        ['Pole_temporal',                44, 43],
        ['S_calcarine',                  45, 44],
        ['S_central',                    46, 45],
        ['S_cingul_Marginalis',          47, 46],
        ['S_circular_insula_ant',        48, 47],
        ['S_circular_insula_inf',        49, 48],
        ['S_circular_insula_sup',        50, 49],
        ['S_collat_transv_ant',          51, 50],
        ['S_collat_transv_post',         52, 51],
        ['S_front_inf',                  53, 52],
        ['S_front_middle',               54, 53],
        ['S_front_sup',                  55, 54],
        ['S_interm_prim_Jensen',         56, 55],
        ['S_intrapariet_and_P_trans',    57, 56],
        ['S_oc_middle_and_Lunatus',      58, 57],
        ['S_oc_sup_and_transversal',     59, 58],
        ['S_occipital_ant',              60, 59],
        ['S_oc_temp_lat',                61, 60],
        ['S_oc_temp_med_and_Lingual',    62, 61],
        ['S_orbital_lateral',            63, 62],
        ['S_orbital_med_olfact',         64, 63],
        ['S_orbital_H_Shaped',           65, 64],
        ['S_parieto_occipital',          66, 65],
        ['S_pericallosal',               67, 66],
        ['S_postcentral',                68, 67],
        ['S_precentral_inf_part',        69, 68],
        ['S_precentral_sup_part',        70, 69],
        ['S_suborbital',                 71, 70],
        ['S_subparietal',                72, 71],
        ['S_temporal_inf',               73, 72],
        ['S_temporal_sup',               74, 73],
        ['S_temporal_transverse',        75, 74]
        ]

    return regions


def define_color(x,a,b):
    ''' 
    define_color(x,a,b): turns a number x between a and b into a colormap representation 
    '''

    colormap = plt.get_cmap('bwr')
    norm = matplotlib.colors.Normalize(vmin=a, vmax=b)

    color = colormap(norm(x))
    return color


def write_ctab_entry(f,regions,i,color):
    ''' 
    write_ctab_entry(f,regions,i,color): writes entry in colortable file f, defining region i to be a given color 
    '''

    n = str(regions[i][1]).ljust(2)
    name = str(regions[i][0]).ljust(32)
    if type(color) is str:
        color_rgb = name_to_rgb(color)
        r = str(color_rgb[0]).ljust(3)
        g = str(color_rgb[1]).ljust(3)
        b = str(color_rgb[2]).ljust(3)
    else: 
        color_rgb = color
        r = str(int(color_rgb[0]*255.)).ljust(3)
        g = str(int(color_rgb[1]*255.)).ljust(3)
        b = str(int(color_rgb[2]*255.)).ljust(3)

    f.write('%s %s %s %s %s    0\n' %(n, name, r, g, b))


if __name__ == '__main__':
    make_colortable('my_colortable.ctab')



