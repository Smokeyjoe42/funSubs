from moviepy.editor import *
import flashCard

def makeClips(videoFile, flashCards):
    video = VideoFileClip(videoFile)

    setName = "eXSetName"

    clips = []

    i = 1

    for card in flashCards:
        clip = video.subclip(card.start, card.end)
        source = "clips/" + setName + str(i) + ".mp4"
        clip.write_videofile(source) 
        card.source = source
        i += 1
     
    
    
    
    