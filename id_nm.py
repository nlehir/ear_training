def id_nm(index):
    """
        return the string name of the note
        as a function of the index
    """
    offset_to_a4 = index - 9
    if offset_to_a4 == 0:
        return "A4"
    elif offset_to_a4 == 1:
        return "Bb4"
    elif offset_to_a4 == 2:
        return "B4"
    elif offset_to_a4 == 3:
        return "C5"
    elif offset_to_a4 == -1:
        return "Ab4"
    elif offset_to_a4 == -2:
        return "G4"
    elif offset_to_a4 == -3:
        return "Gb4"
    elif offset_to_a4 == -4:
        return "F4"
    elif offset_to_a4 == -5:
        return "E4"
    elif offset_to_a4 == -6:
        return "Eb4"
    elif offset_to_a4 == -7:
        return "D4"
    elif offset_to_a4 == -8:
        return "Db4"
    elif offset_to_a4 == -9:
        return "C4"
    else:
        return "error"
