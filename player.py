from songs import songs
import random
import time

playing=True

while playing:
    song= songs[random.randint(0,len(songs)-1)]
    print(f"Playing: {song["name"]} ({song["length"]} seconds)")
    time.sleep(song["length"])