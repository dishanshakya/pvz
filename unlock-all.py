#!/usr/bin/env python3
"""Generate an unlocked PvZ-Portable profile (users.dat + user1.dat)."""
import os
import struct
import sys

PROFILE_NAME = sys.argv[1] if len(sys.argv) > 1 else "Player"
USERDATA_DIR = os.path.expanduser("~/.local/share/io.github.wszqkzqk/PvZPortable/userdata")
os.makedirs(USERDATA_DIR, exist_ok=True)

users_dat = os.path.join(USERDATA_DIR, "users.dat")
if not os.path.exists(users_dat):
    name_bytes = PROFILE_NAME.encode("utf-8")
    # ProfileMgr version=14, count=1, [len(uint16), name, mUseSeq=1, mId=1]
    u = bytearray()
    u += struct.pack("<IH", 14, 1)
    u += struct.pack("<H", len(name_bytes)) + name_bytes
    u += struct.pack("<II", 1, 1)
    with open(users_dat, "wb") as f:
        f.write(u)
    print(f"Created {users_dat} (profile: {PROFILE_NAME})")

out = bytearray()
out += struct.pack("<I", 12)               # Version = 12
out += struct.pack("<III", 1, 99999, 1)    # mLevel=1, mCoins=99999 ($999,990), mFinishedAdventure=1

records = [0] * 100
for i in range(0, 10):    # Survival Normal & Hard -> unlocks Survival Endless
    records[i] = 5
for i in range(15, 35):   # 20 Mini-Games
    records[i] = 1
for i in range(50, 59):   # Vasebreaker 1-9 -> unlocks Vasebreaker Endless
    records[i] = 1
for i in range(60, 69):   # I, Zombie 1-9 -> unlocks I, Zombie Endless
    records[i] = 1
out += struct.pack("<100I", *records)

purchases = [0] * 80
for i in range(0, 9):     # Gatling Pea .. Imitater
    purchases[i] = 1
purchases[13] = 1         # Gold Watering Can
purchases[14] = 1020      # Fertilizer (20)
purchases[15] = 1020      # Bug Spray (20)
purchases[16] = 1         # Phonograph
purchases[17] = 1         # Gardening Glove
purchases[18] = 1         # Mushroom Garden
purchases[19] = 1         # Wheel Barrow
purchases[20] = 1         # Stinky the Snail
purchases[21] = 4         # 10 Seed Slots (6 + 4)
purchases[22] = 1         # Pool Cleaner
purchases[23] = 1         # Roof Cleaner
purchases[24] = 3         # Rake (3 uses)
purchases[25] = 1         # Aquarium Garden
purchases[26] = 1010      # Chocolate (10)
purchases[27] = 1         # Tree of Wisdom
purchases[28] = 1010      # Tree Food (10)
purchases[29] = 1         # Wall-nut First Aid
out += struct.pack("<80I", *purchases)

fields = [
    0, 0, 0, 0, 0, 0, 0, 0,  # playtime/misc/stinky
    1, 1,                     # mHasUnlockedMinigames, mHasUnlockedPuzzleMode
    0, 0, 0, 0,               # new flags
    1,                        # mHasUnlockedSurvivalMode
    0, 0, 0, 0, 0,            # message/taco/stinky/upsell/stats
    0,                        # mNumPottedPlants
]
out += struct.pack("<21I", *fields)
out += struct.pack("<20H", *([0] * 20))    # achievements
out += struct.pack("<BI", 0, 0)            # Zombatar accepted/count
out += bytes([1] * 20)                     # aMiniGameFlags[20]
out += struct.pack("<B", 0)                # Zombatar created before

user1_dat = os.path.join(USERDATA_DIR, "user1.dat")
with open(user1_dat, "wb") as f:
    f.write(out)
print(f"Wrote unlocked save to {user1_dat} ({len(out)} bytes)")
