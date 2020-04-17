import random


def frequency_from_id(index):
    """
        get frequency from index
    """
    offset_to_a4 = index - 9
    frequency = pow(2, offset_to_a4/12)*440
    return frequency


def generate_one_frequency(center_offset_to_a4, ambitus):
    """
        ambitus is in semi tones
        n_note is in semitones
    """
    if ambitus % 2 == 0:
        p = ambitus // 2
        offset_to_center = random.randint(-p, p)
    else:
        p = (ambitus - 1) // 2
        offset_to_center = random.randint(-p, p+1)
    n_note = center_offset_to_a4 + offset_to_center
    frequency = pow(2, n_note/12)*440
    return frequency


def ids_chord(chord, note_id):
    """
        ids of notes in chord
        note_id is the first note
    """
    note_2 = note_id + chord.intvls[0]
    note_3 = note_2 + chord.intvls[1]
    note_4 = note_3 + chord.intvls[2]
    return note_id, note_2, note_3, note_4


def frequencies_seq(note_id, c1, c2, c3):
    """
        center_offset_to_a4: int
        nb_notes: int
        ambitus: int (tons)
    """
    id_sequence = list()
    ids_c1 = ids_chord(c1, note_id)
    id_sequence += ids_c1

    if c1.up:
        if c2.up:
            ids_c2 = ids_chord(c2, ids_c1[0])
        else:
            ids_c2 = ids_chord(c2, ids_c1[-1])
    else:
        if c2.up:
            ids_c2 = ids_chord(c2, ids_c1[-1])
        else:
            ids_c2 = ids_chord(c2, ids_c1[0])
    id_sequence += ids_c2

    if c2.up:
        if c3.up:
            ids_c3 = ids_chord(c3, ids_c2[0])
        else:
            ids_c3 = ids_chord(c3, ids_c2[-1])
    else:
        if c3.up:
            ids_c3 = ids_chord(c3, ids_c2[-1])
        else:
            ids_c3 = ids_chord(c3, ids_c2[0])
    id_sequence += ids_c3

    freq_sequence = [frequency_from_id(idn) for idn in id_sequence]
    return freq_sequence
