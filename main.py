#!/usr/bin/env python
import os
from subParser import createCards
from flashCard import flashCard
from clips import *

videoFile = "testVid.mkv"
subFile = "subs.srt"

#Need to wrap this for use on other systems
#os.system(f"ffmpeg -i {videoFile} {subFile}")

targetLength = 10

flashCards = createCards(subFile, targetLength)
makeClips(videoFile, flashCards)
