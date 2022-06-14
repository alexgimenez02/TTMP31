from electricguitar import electricGuitar
from music import *

if "__main__" in __name__:
   

   instr = electricGuitar("Guitar test", 120)
   
   
   pitches =  [SILENT, A5, G5, E5, D5, D5, DS5, D5, C5, SILENT, E5, D5, SILENT]
   duration = [QN, DHN, WN, QN, DHN, SN, SN, DQN, DHN, HN, HN, DHN, QN]
   instr.addToPhase(pitches, duration)
   
   pitches = [A5, G5, E5, A5, E5, G5, SILENT, DS5, D5, C5, SILENT, C5, B4, A4, SILENT]
   duration =  [DHN, QN, SN, SN, SN, DHN, EN, QN, QN, HN, EN, QN, QN, HN, QN]
   instr.addToPhase(pitches, duration)
   
   pitches = [D4, DS4, E4, SILENT, A4, E4, G4, G4, SILENT, G4, A4, SILENT, D5, C5, SILENT]
   duration = [QN, QN, DHN, QN, QN, QN, HN, DQN, EN, QN, HN, QN, HN, HN, QN]
   instr.addToPhase(pitches, duration)
   
   pitches =  [D4, DS4, E4, SILENT, C5, D5, E5, G5, G5, SILENT, D6, C6, C6, SILENT, A5, E6, SILENT]
   duration = [QN, QN, DHN, QN, SN, SN, QN, EN, DHN, QN, DHN, QN, DQN, EN, QN, DHN, HN]
   instr.addToPhase(pitches, duration)
   
   pitches = [ES6, D6, F6, C6, DS6, BS5, GS5, F5, A5, G5, SILENT]
   duration = [HN, QN, EN, EN, EN, EN, EN, EN, EN, EN, QN]
   instr.addToPhase(pitches, duration)
   
   pitches = [B5, G5, B5, G5, B5, SILENT, G5, F5, SILENT, [D6, A5], [C6, G5], [D6,A5], [C6, G5], SILENT]
   duration = [QN, EN, QN, EN, QN, EN, EN, DHN, EN, EN, EN, EN, EN, EN]
   instr.addToPhase(pitches, duration)

   pitches = [SILENT, C6, AS6, GS6, SILENT, G6, F6, G6, D6, F6, SILENT, DS6, ES6, C6, DS6, AS5, BS5, GS5, AS5, C6, SILENT, SILENT]
   duration = [EN, QN, HN, DQN, EN, QN, EN, EN, EN, DQN, QN, QN, QN, EN, HN, HN, HN, HN, HN, HN, EN, DHN]
   instr.addToPhase(pitches, duration)
   
   pitches = [[G4, D4, F3], [G4, D4, F3], [G4, D4, F3], [A4, E4, A3], [A4, E4, A3], [A4, E4, A3], [A4, E4, A3], [B4, FS4, B3], [B4, FS4, B3], [B4, FS4, B3], [B4, FS4, B3], [C5, G4, C4], [D5, A4, D4], SILENT]
   duration = [HN, HN, QN, QN, HN, HN, QN, QN, HN, HN, QN, WN, WN, QN]
   instr.addToPhase(pitches, duration)
   
   pitches = [[G4, D4, F3], [G4, D4, F3], [G4, D4, F3], [A4, E4, A3], [A4, E4, A3], [A4, E4, A3], [A4, E4, A3], [B4, FS4, B3], [B4, FS4, B3], [B4, FS4, B3], [B4, FS4, B3], [C5, G4, C4], [C5, G4, C4], [D5, A4, D4], [D5, A4, D4], SILENT]
   duration = [HN, HN, QN, QN, HN, HN, QN, QN, HN, HN, QN, QN, DHN, QN, DHN, QN]
   instr.addToPhase(pitches, duration)
   
   pitches = [B5, A5, A5, G5, A5, B5, A5, A5, SILENT, A5, C6, D6, SILENT, D6, C6, E6, SILENT]
   duration = [DHN, QN, QN, QN, QN, QN, QN, HN, QN, QN, QN, HN, QN, QN, QN, DHN, QN]
   instr.addToPhase(pitches, duration)
   
   pitches = [A5, B5, A5, G5, A5, B5, G5, A5, G5, E5, D5, E5, DS5, A4, SILENT]
   duration = [QN, HN, HN, QN, QN, HN, HN, QN, QN, HN, HN, HN, HN, HN, HN]
   instr.addToPhase(pitches, duration)
   
   instr.playTheme()