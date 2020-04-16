#This script is to get the color of an atom in PyMOL.
#first, cp get_atomcolor.py to your pwd;
#secod, Ctrl+Middle to get "pk1", i.e., the atom of interest;
#last, input 'run get_atomcolor.py' and Enter.

stored.color = []

cmd.iterate ("pk1", "stored.color.append(color)" )
color_indices=cmd.get_color_indices()
tuple_pml=cmd.get_color_tuple(stored.color[0])
tuple_cst=[255, 255, 255]
tuple_RGB=tuple(ele1 * ele2 for ele1, ele2 in zip(tuple_pml, tuple_cst)) 

print 'The color number and name of selected atom are:\n{number}, {name}.'.format(
number=color_indices[stored.color[0]][1], name=color_indices[stored.color[0]][0])

print 'The pymol tuple and RGB tuple of this color are:\n{pml}\n{rgb}.'.format(
pml=tuple_pml,rgb=tuple_RGB)
