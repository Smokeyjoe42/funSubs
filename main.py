#!/usr/bin/env python
import os
from subParser import createCards

videoFile = "testVid.mkv"
subFile = "subs.srt"

#Need to wrap this for use on other systems
#os.system(f"ffmpeg -i {videoFile} {subFile}")

flashCards = createCards(subFile)

for card in flashCards:
    print(card)
    
    