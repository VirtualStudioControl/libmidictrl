#region Control Bytes
STATUS_NOTE_OFF = 0x80
""" NOTE OFF Status Byte"""
STATUS_NOTE_ON = 0x90
""" NOTE ON Status Byte"""
STATUS_POLYPHONIC_AFTERTOUCH = 0xA0
""" POLYPHONIC AFTERTOUCH Status Byte"""
STATUS_CONTROL_CHANGE = 0xB0
""" CONTROL CHANGE Status Byte"""
STATUS_PROGRAM_CHANGE = 0xC0
""" PROGRAM CHANGE Status Byte"""
STATUS_MONOPHONIC = 0xD0
""" MONOPHONIC Status Byte"""
STATUS_PITCH_BENDING = 0xE0
""" PITCH BENDING Status Byte"""
STATUS_SYSTEM = 0xF0
""" SYSTEM Status Byte"""

LOOKUP_STATUS_REVERSE = {
    STATUS_NOTE_OFF: "STATUS_NOTE_OFF",
    STATUS_NOTE_ON: "STATUS_NOTE_ON",
    STATUS_POLYPHONIC_AFTERTOUCH : "STATUS_POLYPHONIC_AFTERTOUCH",
    STATUS_CONTROL_CHANGE: "STATUS_CONTROL_CHANGE",
    STATUS_PROGRAM_CHANGE: "STATUS_PROGRAM_CHANGE",
    STATUS_MONOPHONIC: "STATUS_MONOPHONIC",
    STATUS_PITCH_BENDING: "STATUS_PITCH_BENDING",
    STATUS_SYSTEM: "STATUS_SYSTEM"
}
"""
Reverse Lookup Dictionary for Status Bytes
"""
#endregion

#region Notes

# Octave -2
NOTE_M2_C = 0
"""Note code: C-2 / C,,,"""
NOTE_M2_Db = 1
"""Note code: Db-2 / Cis,,,"""
NOTE_M2_D = 2
"""Note code: D-2 / D,,,"""
NOTE_M2_Eb = 3
"""Note code: Eb-2 / Dis,,,"""
NOTE_M2_E = 4
"""Note code: E-2 / E,,,"""
NOTE_M2_F = 5
"""Note code: F-2 / F,,,"""
NOTE_M2_Gb = 6
"""Note code: Gb-2 / Fis,,,"""
NOTE_M2_G = 7
"""Note code: G-2 / G,,,"""
NOTE_M2_Ab = 8
"""Note code: Ab-2 / Gis,,,"""
NOTE_M2_A = 9
"""Note code: A-2 / A,,,"""
NOTE_M2_Bb = 10
"""Note code: Bb-2 / Ais,,,"""
NOTE_M2_B = 11
"""Note code: B-2 / H,,,"""

# Octave -1
NOTE_M1_C = 12
"""Note code: C-1 / C,,"""
NOTE_M1_Db = 13
"""Note code: Db-1 / Cis,,"""
NOTE_M1_D = 14
"""Note code: D-1 / D,,"""
NOTE_M1_Eb = 15
"""Note code: Eb-1 / Dis,,"""
NOTE_M1_E = 16
"""Note code: E-1 / E,,"""
NOTE_M1_F = 17
"""Note code: F-1 / F,,"""
NOTE_M1_Gb = 18
"""Note code: Gb-1 / Fis,,"""
NOTE_M1_G = 19
"""Note code: G-1 / G,,"""
NOTE_M1_Ab = 20
"""Note code: Ab-1 / Gis,,"""
NOTE_M1_A = 21
"""Note code: A-1 / A,,"""
NOTE_M1_Bb = 22
"""Note code: Bb-1 / Ais,,"""
NOTE_M1_B = 23
"""Note code: B-1 / H,,"""

# Octave 0
NOTE_0_C = 24
"""Note code: C0 / C,"""
NOTE_0_Db = 25
"""Note code: Db0 / Cis,"""
NOTE_0_D = 26
"""Note code: D0 / D,"""
NOTE_0_Eb = 27
"""Note code: Eb0 / Dis,"""
NOTE_0_E = 28
"""Note code: E0 / E,"""
NOTE_0_F = 29
"""Note code: F0 / F,"""
NOTE_0_Gb = 30
"""Note code: Gb0 / Fis,"""
NOTE_0_G = 31
"""Note code: G0 / G,"""
NOTE_0_Ab = 32
"""Note code: Ab0 / Gis,"""
NOTE_0_A = 33
"""Note code: A0 / A,"""
NOTE_0_Bb = 34
"""Note code: Bb0 / Ais,"""
NOTE_0_B = 35
"""Note code: B0 / H,"""

# Octave 1
NOTE_1_C = 36
"""Note code: C1 / C"""
NOTE_1_Db = 37
"""Note code: Db1 / Cis"""
NOTE_1_D = 38
"""Note code: D1 / D"""
NOTE_1_Eb = 39
"""Note code: Eb1 / Dis"""
NOTE_1_E = 40
"""Note code: E1 / E"""
NOTE_1_F = 41
"""Note code: F1 / F"""
NOTE_1_Gb = 42
"""Note code: Gb1 / Fis"""
NOTE_1_G = 43
"""Note code: G1 / G"""
NOTE_1_Ab = 44
"""Note code: Ab1 / Gis"""
NOTE_1_A = 45
"""Note code: A1 / A"""
NOTE_1_Bb = 46
"""Note code: Bb1 / Ais"""
NOTE_1_B = 47
"""Note code: B1 / H"""

# Octave 2
NOTE_2_C = 48
"""Note code: C2 / c"""
NOTE_2_Db = 49
"""Note code: Db2 / cis"""
NOTE_2_D = 50
"""Note code: D2 / d"""
NOTE_2_Eb = 51
"""Note code: Eb2 / dis"""
NOTE_2_E = 52
"""Note code: E2 / e"""
NOTE_2_F = 53
"""Note code: F2 / f"""
NOTE_2_Gb = 54
"""Note code: Gb2 / fis"""
NOTE_2_G = 55
"""Note code: G2 / g"""
NOTE_2_Ab = 56
"""Note code: Ab2 / gis"""
NOTE_2_A = 57
"""Note code: A2 / a"""
NOTE_2_Bb = 58
"""Note code: Bb2 / ais"""
NOTE_2_B = 59
"""Note code: B2 / h"""

# Octave 3
NOTE_3_C = 60
"""Note code: C3 / c'"""
NOTE_3_Db = 61
"""Note code: Db3 / cis'"""
NOTE_3_D = 62
"""Note code: D3 / d'"""
NOTE_3_Eb = 63
"""Note code: Eb3 / dis'"""
NOTE_3_E = 64
"""Note code: E3 / e'"""
NOTE_3_F = 65
"""Note code: F3 / f'"""
NOTE_3_Gb = 66
"""Note code: Gb3 / fis'"""
NOTE_3_G = 67
"""Note code: G3 / g'"""
NOTE_3_Ab = 68
"""Note code: Ab3 / gis'"""
NOTE_3_A = 69
"""Note code: A3 / a'"""
NOTE_3_Bb = 70
"""Note code: Bb3 / ais'"""
NOTE_3_B = 71
"""Note code: B3 / h'"""

# Octave 4
NOTE_4_C = 72
"""Note code: C4 / c''"""
NOTE_4_Db = 73
"""Note code: Db4 / cis''"""
NOTE_4_D = 74
"""Note code: D4 / d''"""
NOTE_4_Eb = 75
"""Note code: Eb4 / dis''"""
NOTE_4_E = 76
"""Note code: E4 / e''"""
NOTE_4_F = 77
"""Note code: F4 / f''"""
NOTE_4_Gb = 78
"""Note code: Gb4 / fis''"""
NOTE_4_G = 79
"""Note code: G4 / g''"""
NOTE_4_Ab = 80
"""Note code: Ab4 / gis''"""
NOTE_4_A = 81
"""Note code: A4 / a''"""
NOTE_4_Bb = 82
"""Note code: Bb4 / ais''"""
NOTE_4_B = 83
"""Note code: B4 / h''"""

# Octave 5
NOTE_5_C = 84
"""Note code: C5 / c'''"""
NOTE_5_Db = 85
"""Note code: Db5 / cis'''"""
NOTE_5_D = 86
"""Note code: D5 / d'''"""
NOTE_5_Eb = 87
"""Note code: Eb5 / dis'''"""
NOTE_5_E = 88
"""Note code: E5 / e'''"""
NOTE_5_F = 89
"""Note code: F5 / f'''"""
NOTE_5_Gb = 90
"""Note code: Gb5 / fis'''"""
NOTE_5_G = 91
"""Note code: G5 / g'''"""
NOTE_5_Ab = 92
"""Note code: Ab5 / gis'''"""
NOTE_5_A = 93
"""Note code: A5 / a'''"""
NOTE_5_Bb = 94
"""Note code: Bb5 / ais'''"""
NOTE_5_B = 95
"""Note code: B5 / h'''"""

# Octave 6
NOTE_6_C = 96
"""Note code: C6 / c''''"""
NOTE_6_Db = 97
"""Note code: Db6 / cis''''"""
NOTE_6_D = 98
"""Note code: D6 / d''''"""
NOTE_6_Eb = 99
"""Note code: Eb6 / dis''''"""
NOTE_6_E = 100
"""Note code: E6 / e''''"""
NOTE_6_F = 101
"""Note code: F6 / f''''"""
NOTE_6_Gb = 102
"""Note code: Gb6 / fis''''"""
NOTE_6_G = 103
"""Note code: G6 / g''''"""
NOTE_6_Ab = 104
"""Note code: Ab6 / gis''''"""
NOTE_6_A = 105
"""Note code: A6 / a''''"""
NOTE_6_Bb = 106
"""Note code: Bb6 / ais''''"""
NOTE_6_B = 107
"""Note code: B6 / h''''"""

# Octave 7
NOTE_7_C = 108
"""Note code: C7 / c'''''"""
NOTE_7_Db = 109
"""Note code: Db7 / cis'''''"""
NOTE_7_D = 110
"""Note code: D7 / d'''''"""
NOTE_7_Eb = 111
"""Note code: Eb7 / dis'''''"""
NOTE_7_E = 112
"""Note code: E7 / e'''''"""
NOTE_7_F = 113
"""Note code: F7 / f'''''"""
NOTE_7_Gb = 114
"""Note code: Gb7 / fis'''''"""
NOTE_7_G = 115
"""Note code: G7 / g'''''"""
NOTE_7_Ab = 116
"""Note code: Ab7 / gis'''''"""
NOTE_7_A = 117
"""Note code: A7 / a'''''"""
NOTE_7_Bb = 118
"""Note code: Bb7 / ais'''''"""
NOTE_7_B = 119
"""Note code: B7 / h'''''"""

# Octave 8
NOTE_8_C = 120
"""Note code: C8 / c''''''"""
NOTE_8_Db = 121
"""Note code: Db8 / cis''''''"""
NOTE_8_D = 122
"""Note code: D8 / d''''''"""
NOTE_8_Eb = 123
"""Note code: Eb8 / dis''''''"""
NOTE_8_E = 124
"""Note code: E8 / e''''''"""
NOTE_8_F = 125
"""Note code: F8 / f''''''"""
NOTE_8_Gb = 126
"""Note code: Gb8 / fis''''''"""
NOTE_8_G = 127
"""Note code: G8 / g''''''"""
#endregion