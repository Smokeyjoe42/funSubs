from moviepy.editor import *
import flashCard


#TODO include a path to the media collections
def makeClips(videoFile, flashCards, mediaPath):
    video = VideoFileClip(videoFile)

    clips = []

    i = 1
    numFlashCards = len(flashCards)
    
    for card in flashCards:
        clip = video.subclip(card.start, card.end)
        source = mediaPath + card.setName + str(i) + ".mp4"
        clip.write_videofile(source) 
        card.source = "[sound:" + card.setName + str(i) + ".mp4]"
        #card.source = "<video  height=\"240\" controls>\n\t<source src=\"" + card.setName + str(i) + ".mp4" + "\" type=\"video/mp4\">\n\t</video>" 

        print("\n", "Clip", i, "of", numFlashCards, "done!", "\n")

        """<video width="320" height="240" controls>
        <source src="{{Video}}.mp4" type="video/mp4">
        </video>"""

        i += 1
     
    
    
    
    