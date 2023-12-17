#!/usr/bin/env python
import os
from subParser import createCards
from flashCard import flashCard
from clips import *
from anki import createAnkiFile

videoFile = "testVid.mkv"
subFile = "subs.srt"
mediaCollDir = "/mnt/c/Users/joewm/appdata/Roaming/Anki2/User 1/collection.media/"
setName = "whatWeDoInTheShadows"
flashCardPath = "/mnt/c/Users/joewm/Documents/ankiDecks/"

#Need to wrap this for use on other systems
#os.system(f"ffmpeg -i {videoFile} {subFile}")

numOfCards = 30
targetLength = 5 

#?Creates a list of FlashCard objects
flashCards = createCards(subFile, targetLength, setName, numOfCards)

#?Cuts the flashcards into clips
makeClips(videoFile, flashCards, mediaCollDir)

for card in flashCards:
    print(card.toString())

#?creates the source file for the flashcards in anki
createAnkiFile(flashCards, flashCardPath, setName)
