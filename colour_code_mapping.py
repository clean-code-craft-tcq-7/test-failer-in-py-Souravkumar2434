major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]

def get_pair_number(majorcolor, minorcolor):
     return major_colors.index(majorcolor) * 5 + minor_colors.index(minorcolor)
     

def print_color_map():
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f' {get_pair_number(major, minor)} | {major} | {minor}')
    return len(major_colors) * len(minor_colors)
