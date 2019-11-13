# coding: utf-8
import sys
# import simpleaudio as sa
import sounddevice as sd
import soundfile as sf
from PIL import ImageFont
import random
if sys.version_info < (3, 0):
    import Tkinter as tk
else:
    import tkinter as tk

# m7b5 = u"\N{LATIN CAPITAL LETTER O WITH STROKE}"
m7b5 = u"\u2205"
# M7 = u"\N{GREEK CAPITAL LETTER DELTA}"+u"7"
M7 = u"\u0394"+u"7"
mM7 = u"-"+u"\u0394"+u"7"
# M9 = u"\N{GREEK CAPITAL LETTER DELTA}"+u"9"
m7 = u"-7"
c7 = u"7"
d7 = u"\u00BA"+"7"
M7p = M7+u"+"
# M7d11 = M7+u"\u266F"+u"11"
# M7d9 = M7+u"\u266F"+u"9"

font_choice_1 = "./Bebas-Regular.ttf"
font_choice_2 = "./Roboto-Condensed.ttf"
font_choice_3 = "./BebasNeue-Regular.ttf"
font = ImageFont.truetype(font_choice_2, 15)

positions = ["RP", "R1", "R2", "R3"]


notes = ['C', 'C#', 'Db', 'D', 'D#',
         'Eb', 'E', 'F', 'F#', 'Gb',
         'G', 'G#', 'Ab', 'A', 'A#',
         'Bb', 'B']

colors_note = ["#74b8cc"]

colors_chord = ["#ce7feb",
                "#bc84d1",
                "#de7c91",
                "#db8489",
                "#d69a9e",
                "#bc7dd4"]

colors_chord = ["#68baa8",
                "#7ac4b4",
                "#84d1c0",
                "#6bbfad",
                "#56b39f",
                "#35b095",
                "#2fc4a4",
                "#3bd4b3",
                "#36b59a",
                "#23c2a0"]


arrows = [u"\u2191",
          u"\u2193"]

config_text = (
    "enter : next note & chords     "
    "n : change note     "
    "c : change chords     "
    "a : play note"
)


class Interface(tk.Frame):
    def __init__(self, fenetre):
        tk.Frame.__init__(self, fenetre)
        # self.grid_propagate(0)
        self.pack(fill=tk.BOTH)
        # self.notes_buffer = notes.copy()
        if sys.version_info < (3, 0):
            self.notes_buffer = notes[:]
        else:
            self.notes_buffer = notes.copy()
        self.current_note = "C"
        self.hardcore = False
        self.chords = [c7, m7, M7, m7b5]
        self.hardcore_chords = self.chords+[mM7, d7, M7p]

        fontsize = 50
        width = 10

        # pan 1
        # --------------
        # --------------
        self.pan_1 = tk.Label(self)
        self.pan_1.pack(fill=tk.BOTH)

        self.note = tk.Label(
            self.pan_1,
            width=width,
            height=3,
            bg=random.choice(colors_note),
            font=(font, fontsize),
            text="Appuyer")
        self.note.pack(side="left")

        self.chord_1 = tk.Label(
            self.pan_1,
            width=width,
            height=3,
            bg=random.choice(colors_chord),
            font=(font, fontsize),
            text="sur")
        self.chord_1.pack(side="left")

        self.chord_2 = tk.Label(
            self.pan_1,
            width=width,
            height=3,
            bg=random.choice(colors_chord),
            font=(font, fontsize),
            text="entrée")
        self.chord_2.pack(side="left")

        self.chord_3 = tk.Label(
            self.pan_1,
            width=width,
            height=3,
            bg=random.choice(colors_chord),
            font=(font, fontsize),
            text="!")
        self.chord_3.pack(side="left")
        # --------------
        # --------------

        # pan 2
        # --------------
        # --------------
        self.options = tk.Label(self, bg="#73abf5", width="60")
        self.options.pack(fill="both")

        self.config = tk.Label(
            self.options,
            width=70,
            height=3,
            bg="#73abf5",
            font=(font, 22),
            text=config_text)
        self.config.pack(side="left", fill="both")

        self.h_button = tk.Checkbutton(
            self.options,
            text="hardcore mode (h)",
            bg="#ba9027",
            font=(font, 16),
            command=self.toggle_h_mode)
        self.h_button.pack(side=tk.LEFT, fill="both")
        # --------------
        # --------------

    def next_note(self):
        if len(self.notes_buffer) == 0:
            # self.notes_buffer = notes.copy()
            if sys.version_info < (3, 0):
                self.notes_buffer = notes[:]
            else:
                self.notes_buffer = notes.copy()
        next_note = random.choice(self.notes_buffer)
        self.current_note = next_note
        self.notes_buffer.remove(next_note)
        self.note["text"] = self.current_note
        self.note["bg"] = random.choice(colors_note)

    def get_filename(self):
        if self.current_note == "C#":
            parsed_note_name = "Db"
        elif self.current_note == "D#":
            parsed_note_name = "Eb"
        elif self.current_note == "F#":
            parsed_note_name = "Gb"
        elif self.current_note == "G#":
            parsed_note_name = "Ab"
        elif self.current_note == "A#":
            parsed_note_name = "Bb"
        else:
            parsed_note_name = self.current_note
        filename = "./"+parsed_note_name+".wav"
        return filename

    def play_note(self):
        filename = self.get_filename()
        # Extract data and sampling rate from file
        data, fs = sf.read(filename, dtype='float32')
        sd.play(data, fs)
        # status = sd.wait()  # Wait until file is done playing
        # wave_obj = sa.WaveObject.from_wave_file(filename)
        # play_obj = wave_obj.play()
        # play_obj.wait_done()

    def next_chords(self):
        if self.hardcore:
            available_chords = self.hardcore_chords
        else:
            available_chords = self.chords
        # chord 1
        text1 = random.choice(arrows)+random.choice(available_chords)
        text1 += " "+random.choice(positions)
        self.chord_1["text"] = text1
        self.chord_1["bg"] = random.choice(colors_chord)

        # chord 2
        text2 = random.choice(arrows)+random.choice(available_chords)
        text2 += " "+random.choice(positions)
        self.chord_2["text"] = text2
        self.chord_2["bg"] = random.choice(colors_chord)

        # chord 3
        text3 = random.choice(arrows)+random.choice(available_chords)
        text3 += " "+random.choice(positions)
        self.chord_3["text"] = text3
        self.chord_3["bg"] = random.choice(colors_chord)

    def toggle_h_mode(self):
        self.hardcore = not self.hardcore
        self.h_button.toggle()


def next_note(event):
    interface.next_note()
    interface.play_note()


def play_note(event):
    interface.play_note()


def next_chords(event):
    interface.next_chords()


def next_all(event):
    interface.next_note()
    interface.next_chords()
    interface.play_note()


def switch_h_mode(event):
    interface.toggle_h_mode()


def quit_ex(event):
    interface.quit()


fenetre = tk.Tk()
interface = Interface(fenetre)
fenetre.bind('<Return>', next_all)
fenetre.bind('<n>', next_note)
fenetre.bind('<c>', next_chords)
fenetre.bind('<h>', switch_h_mode)
fenetre.bind('<a>', play_note)
fenetre.bind('<q>', quit_ex)
interface.mainloop()
