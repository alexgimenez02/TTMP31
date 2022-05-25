from electricguitar import electricGuitar
from music import *

if "__main__" in __name__:
   

   instr = electricGuitar("Guitar test", 120)
   
   
   pitches =  [SILENT, G5, G5, E5, D5, D5, DS5, DF5, C5, SILENT, D5, D5, SILENT]
   duration = [QN, DHN, WN, QN, DHN, SN, SN, DQN, DHN, HN, HN, DHN, QN]
   instr.addToPhase(pitches, duration)
   
   pitches = [G5, G5, E5, A5, E5, G5, SILENT, DS5, DF5, C5, SILENT, C5, B4, A4, SILENT]
   duration =  [DHN, QN, SN, SN, SN, DHN, EN, QN, QN, HN, EN, QN, QN, HN, QN]
   instr.addToPhase(pitches, duration)
   
   pitches = [D4, DS4, E4, SILENT, A4, E4, G4, G4, SILENT, G4, A4, SILENT, D5, C5, SILENT]
   duration = [QN, QN, DHN, QN, QN, QN, HN, DQN, EN, QN, HN, QN, HN, HN, QN]
   instr.addToPhase(pitches, duration)
   
   pitches =  [D4, DS4, E4, SILENT, C5, D5, E5, G5, G5, SILENT, C6, C6, C6, SILENT, A5, E6, SILENT]
   duration = [QN, QN, DHN, QN, SN, SN, QN, EN, DHN, QN, DHN, QN, DQN, EN, QN, DHN, HN]
   instr.addToPhase(pitches, duration)
   
   pitches = [DS6, D6, F6, C6, DS6, AS5, GS5, F5, A5, G5, SILENT]
   duration = [HN, QN, EN, EN, EN, EN, EN, EN, EN, EN, QN]
   instr.addToPhase(pitches, duration)
   
   pitches = [AS5, GS5, A5, G5, A5, SILENT, GS5, F5, SILENT, [D6, AS5], [C6, GS5], [D6,A5], [C6, G5], SILENT]
   duration = [QN, EN, QN, EN, QN, EN, EN, DHN, EN, EN, EN, EN, EN, EN]
   instr.addToPhase(pitches, duration)

   pitches = [SILENT, C6, GS6, G6, SILENT, G6, F6, G6, D6, F6, SILENT, DS6, D6, C6, DS6, AS5, AS5, GS5, AS5, C6, SILENT, SILENT]
   duration = [EN, QN, HN, DQN, EN, QN, EN, EN, EN, DQN, QN, QN, QN, EN, HN, HN, HN, HN, HN, HN, EN, DHN]
   instr.addToPhase(pitches, duration)
   
   pitches = [[G4, D4, F3], [G4, D4, F3], [G4, D4, F3], [A4, E4, A3], [A4, E4, A3], [A4, E4, A3], [A4, E4, A3], [B4, FS4, B3], [B4, FS4, B3], [B4, F4, B3], [B4, FS4, B3], [C5, G4, C4], [D5, A4, D4], SILENT]
   duration = [HN, HN, QN, QN, HN, HN, QN, QN, HN, HN, QN, WN, WN, QN]
   instr.addToPhase(pitches, duration)
   
   pitches = [[G4, D4, F3], [G4, D4, F3], [G4, D4, F3], [A4, E4, A3], [A4, E4, A3], [A4, E4, A3], [A4, E4, A3], [B4, FS4, B3], [B4, F4, B3], [B4, FS4, B3], [B4, F4, B3], [C5, G4, C4], [C5, G4, C4], [D5, A4, D4], [D5, A4, D4], SILENT]
   duration = [HN, HN, QN, QN, HN, HN, QN, QN, HN, HN, QN, QN, DHN, QN, DHN, QN]
   instr.addToPhase(pitches, duration)
   
   pitches = [A5, A5, A5, G5, A5, A5, A5, A5, SILENT, A5, C6, D6, SILENT, D6, C6, E6, SILENT]
   duration = [DHN, QN, QN, QN, QN, QN, QN, HN, QN, QN, QN, HN, QN, QN, QN, DHN, QN]
   instr.addToPhase(pitches, duration)
   
   pitches = [A5, A5, A5, G5, A5, A5, G5, A5, G5, E5, D5, E5, DS5, A4, SILENT]
   duration = [QN, HN, HN, QN, QN, HN, HN, QN, QN, HN, HN, HN, HN, HN, HN]
   instr.addToPhase(pitches, duration)
   
   instr.playTheme()