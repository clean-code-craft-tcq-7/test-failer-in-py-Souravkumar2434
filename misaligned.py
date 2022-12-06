from colour_code_mapping import print_color_map, get_pair_number

result = print_color_map()
assert(result == 25)
assert get_pair_number("Red","Blue") == 6
assert get_pair_number("Black","Blue") == 11
