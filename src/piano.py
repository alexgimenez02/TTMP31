from music import *


class Piano:
    name = ""
    bpm = 0
    score = None
    l_hand_part = Part(PIANO, 0)
    r_hand_part = Part(PIANO, 1)

    def __init__(self, name='Piano', bpm=60):
        self.name = name
        self.score = Score(name, bpm)

    def addPhrase(self, pitches, duration, hand="r"):
        phrase = Phrase()
        phrase.addNoteList(pitches, duration)
        if hand == "l":
            self.l_hand_part.addPhrase(phrase)
        elif hand == "r":
            self.r_hand_part.addPhrase(phrase)

    def addPhraseTwoHands(self, l_pitches, l_duration, r_pitches, r_duration):
        self.addPhrase(l_pitches, l_duration, "l")
        self.addPhrase(r_pitches, r_duration, "r")

    def changeTempo(self, tempo):
        pass

    def create_score(self):
        if self.l_hand_part.getSize() > 0:
            self.score.addPart(self.l_hand_part)
        if self.r_hand_part.getSize() > 0:
            self.score.addPart(self.r_hand_part)

    def write_mdi(self, path):
        Write.midi(self.score, path)

    def play_theme(self):
        self.create_score()
        Play.midi(self.score)
