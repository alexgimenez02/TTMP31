from music import *


class Piano:
    name = ""
    bpm = 0
    score = None
    l_hand_part = None
    r_hand_part = None

    def __init__(self, name='Piano', bpm=60, part_num=[0, 1]):
        self.name = name
        self.score = Score(name, bpm)
        self.l_hand_part = Part(PIANO, part_num[0])
        self.r_hand_part = Part(PIANO, part_num[1])


    def addPhrase(self, pitches, duration, n_repetitions=0, hand="r"):
        phrase = Phrase()
        phrase.addNoteList(pitches, duration)
        if n_repetitions > 0:
            Mod.repeat(phrase, n_repetitions)  # repeat first phrase n times
        if hand == "l":
            self.l_hand_part.addPhrase(phrase)
        elif hand == "r":
            self.r_hand_part.addPhrase(phrase)

    def addPhraseTwoHands(self, l_pitches, l_duration, r_pitches, r_duration, n_repetitions=0):
        self.addPhrase(l_pitches, l_duration, n_repetitions, "l")
        self.addPhrase(r_pitches, r_duration, n_repetitions, "r")

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
