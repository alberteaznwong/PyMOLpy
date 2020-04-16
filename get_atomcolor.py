#This script is to get the color name and RGB value of an atom in PyMOL.
#first, cp get_atomcolor.py to your pwd;
#secod, "Ctrl + Middle Mouse Button " to get "pk1", i.e., the atom of interest;
#last, input 'run get_atomcolor.py' and Enter.
stored.color = []
cmd.iterate("pk1", "stored.color.append(color)")
color_dict = dict(cmd.get_color_indices())
key_list = list(color_dict.keys())
if (stored.color[0] in key_list):
    val_list = list(color_dict.values())
    tuple_pml = cmd.get_color_tuple(stored.color[0])
    tuple_cst = [255, 255, 255]
    tuple_RGB = tuple(ele1 * ele2 for ele1, ele2 in zip(tuple_pml, tuple_cst))

    print ('The color number and name of selected atom are:\n{number}, {name}.'.format(
    number = stored.color[0], name = key_list[val_list.index(stored.color[0])]))
    for i in range(0, 177):
        stored.color = []
        cmd.iterate("pk1", "stored.color.append(color)" )
        color_indices = cmd.get_color_indices()
        color_dict = dict(cmd.get_color_indices())
        key_list = list(color_dict.keys())
        val_list = list(color_dict.values())
        number_current = stored.color[0]
        number_temp = color_indices[i][1]
        name_current = key_list[val_list.index(stored.color[0])]
        name_temp = color_indices[i][0]
        tuple_current = cmd.get_color_tuple(stored.color[0])
        tuple_temp = cmd.get_color_tuple(number_temp)
        if (tuple_temp == tuple_current and name_temp != name_current):
            color_nick = color_indices[i][0]
            print ('This color is also called as: {nick}.'.format(nick = color_nick))
        else:
            i += 1
    print ('The pymol tuple and RGB tuple of this color are:\n{pml}\n{rgb}.'.format(
    pml = tuple_pml,rgb = tuple_RGB))
else:
    color_dict = dict(cmd.get_color_indices(5387))
    key_list = list(color_dict.keys())
    val_list = list(color_dict.values())
    tuple_pml = cmd.get_color_tuple(stored.color[0])
    tuple_cst = [255, 255, 255]
    tuple_RGB = tuple(ele1 * ele2 for ele1, ele2 in zip(tuple_pml, tuple_cst))

    print ('The color number and name of selected atom are:\n{number}, {name}.'.format(
    number = stored.color[0], name = key_list[val_list.index(stored.color[0])]))
    for i in range(0, 177): #use 5387 instead of 177 to get a thorough search, slowly.
        stored.color = []
        cmd.iterate("pk1", "stored.color.append(color)" )
        color_indices = cmd.get_color_indices(5387)
        color_dict = dict(cmd.get_color_indices(5387))
        key_list = list(color_dict.keys())
        val_list = list(color_dict.values())
        number_current = stored.color[0]
        number_temp = color_indices[i][1]
        name_current = key_list[val_list.index(stored.color[0])]
        name_temp = color_indices[i][0]
        tuple_current = cmd.get_color_tuple(stored.color[0])
        tuple_temp = cmd.get_color_tuple(number_temp)
        if (tuple_temp == tuple_current and name_temp != name_current):
            color_nick = color_indices[i][0]
            print ('This color is also called as: {nick}.'.format(nick = color_nick))
        else:
            i += 1
    print ('The pymol tuple and RGB tuple of this color are:\n{pml}\n{rgb}.'.format(
    pml = tuple_pml,rgb = tuple_RGB))
