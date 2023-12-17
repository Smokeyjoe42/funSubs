
#holds all the information to create ONE flashcard
class flashCard:
    def __init__(self, cStartTime, cEndTime, cContent, cSource, csetName):
        #timestamps for the clips
        self.start = cStartTime
        self.end = cEndTime

        #the line thats being said in the clip
        self.content = cContent

        #the location of the source
        self.source = cSource 

        #the name of the set of cards
        self.setName = csetName 
    
    def toString(self):
        print(self.start, ":", self.end)
        print("Set Name: ", self.setName)
        print("Source: ", self.source)
        print("Content: ", self.content)
        print("") 
        
        