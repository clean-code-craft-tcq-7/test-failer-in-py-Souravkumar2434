def size(cms):
    if cms < 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    elif cms == 38:
        print("No information available for size 38cms!")
        return ' '
    else:
        return 'L'
