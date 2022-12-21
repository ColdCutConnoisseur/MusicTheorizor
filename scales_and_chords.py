"""Keys, scales, and chords, yay!"""


class AccidentalsDisplay:
    SHARPS = "sharps"
    FLATS = "flats"

class ScalesAndChords:
    def __init__(self):

        self.notes = ["A", "A#/Bb", "B", "C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab"]
        self.num_notes = len(self.notes)
        self.accidentals_display = AccidentalsDisplay.SHARPS

        self.ionian_recipe = [2, 2, 2, 1, 2, 2, 2, 1]
        self.dorian_recipe = []
        self.phrygian_recipe = []
        self.lydian_recipe = []
        self.mixolydian_recipe = []
        self.aeolian_recipe = []
        self.locrian_recipe = []


    
    def _format_and_return_note(self, note):
        """accidentals_display --> switch for determining if #/b note returned"""
        accidental_search = '/'

        if accidental_search in note:
            note_split = note.split('/')

            if self.accidentals_display is AccidentalsDisplay.SHARPS:
                note = note_split[0]

            elif self.accidentals_display is AccidentalsDisplay.FLATS:
                note = note_split[1]

        return note

    def _return_note_position(self, note):
        """Return index of note"""
        note_position = self.notes.index(note)
        return note_position
    
    def move_n_half_steps(self, start_note, n_half_steps):
        """Return note n half steps from start_note"""
        start_index = self._return_note_position(start_note)

        stop_index = start_index + n_half_steps

        quotient, remainder = divmod(stop_index, self.num_notes)

        if stop_index >= self.num_notes:
            #return self._format_and_return_note(self.notes[remainder])
            return self.notes[remainder]

        #return self._format_and_return_note(self.notes[stop_index])
        return self.notes[stop_index]

    def return_ionian_scale(self, root):
        """Create Ionian scale"""
        scale = [root]

        for step in self.ionian_recipe:
            next_note = self.move_n_half_steps(scale[-1], step)

            scale.append(next_note)

        return scale



if __name__ == "__main__":
    sac = ScalesAndChords()
    
    root = "B"
    print(f"ROOT: {root}")

    hs = sac.move_n_half_steps(root, 1)
    ws = sac.move_n_half_steps(root, 2)

    print(f"Half step: {hs}")
    print(f"Whole step: {ws}")

    print("B Ionian")
    b_ionian = sac.return_ionian_scale(root)
    print(b_ionian)

