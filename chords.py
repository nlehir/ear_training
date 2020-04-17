import random

m7b5 = "\N{LATIN CAPITAL LETTER O WITH STROKE}"
M7 = "\N{GREEK CAPITAL LETTER DELTA}"+'7'
mM7 = '-'+"\N{GREEK CAPITAL LETTER DELTA}"+'7'
m7 = "-7"
c7 = "7"
d7 = "°7"
c7b5 = "7b5"
M7d5 = M7+"#5"
M7b5 = M7+"b5"
M7p = M7+"+"
M7d11 = M7+"#11"
M7d9 = M7+"#9"

chords = [c7, m7, M7, m7b5]
t3_chords = chords+[mM7, d7, M7d5, M7b5, c7b5]

intervals = dict()
intervals[M7] = [4, 3, 4]
intervals[m7] = [3, 4, 3]
intervals[c7] = [4, 3, 3]
intervals[m7b5] = [3, 3, 4]

intervals[mM7] = [3, 4, 4]
intervals[d7] = [3, 3, 3]
intervals[M7d5] = [4, 4, 3]
intervals[c7b5] = [4, 2, 4]
intervals[M7b5] = [4, 2, 5]


class Chord:
    """
        generate chords,
        inversions,
        direction,
        text
    """

    def __init__(self, t3):
        if t3:
            self.nature = random.choice(t3_chords)
        else:
            self.nature = random.choice(chords)
        self.up = random.randint(0, 1)
        self.inversion = random.randint(0, 3)
        text_up = set_text_up(self.up)
        text_inv = text_inversion(self.inversion)
        self.intvls = get_intervals(self.nature, self.inversion, self.up)
        self.text = text_up + self.nature + text_inv


def text_inversion(inversion):
    if inversion == 0:
        text_inv = "PF"
    elif inversion == 1:
        text_inv = "R1"
    elif inversion == 2:
        text_inv = "R2"
    elif inversion == 3:
        text_inv = "R3"
    return text_inv


def set_text_up(up):
    if up:
        text_up = u"\u2191"
    else:
        text_up = u"\u2193"
    return text_up


def get_intervals(nature, inversion, up):
    """
        intervals in the chords in semitones
    """
    chd_itvs = intervals[nature]
    for inv in range(inversion):
        interval_0 = chd_itvs[1]
        interval_1 = chd_itvs[2]
        interval_2 = 12-sum(chd_itvs)
        chd_itvs = [interval_0, interval_1, interval_2]
    if not up:
        chd_itvs = reverse_chord(chd_itvs)
    return chd_itvs


def reverse_chord(chd_itvs):
    intv0 = - chd_itvs[2]
    intv1 = - chd_itvs[1]
    intv2 = - chd_itvs[0]
    return [intv0, intv1, intv2]
