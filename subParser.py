import re
from flashCard import flashCard

"""Creates flashCard obj's from a subtitle file
Output: a deck of flashCards"""

#TODO add a try catch
#TODO add start and end tuples
def createCards(subFile, targetLength, setName, numOfCards):
    try:
        file = open(subFile, 'r')
    except:
        print("An error occured opening ", subFile)
    
    allCards = []
    
    #timestamp_pattern = r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}'
    timestamp_pattern = r'\d{2}:\d{2}:\d{2},\d{3}'
    
    while line := file.readline():
        line = line.replace("\n","")
        
        #checks for EOF
     
        if(re.match("^[0-9]+$", line)):
            #cards.append(line)
            s_timestamp = file.readline()
            s_timestamp = s_timestamp.replace("\n","")
            
            
            
            content = file.readline()
            content = content.replace("\n","")
            while True:
                cLine = file.readline()
                cLine = cLine.replace("\n", "")
                
                if not cLine:
                    break
                
                content += " " + cLine
            
            timestamp = getTimeStamps(s_timestamp)
            #print(timestamp[0], ":", timestamp[1], '\n')
            
            allCards.append(flashCard(timestamp[0], timestamp[1], content, "", setName))
                

    #return allCards
    
    """break the flashcards into londer segements based on the length of the flashCard"""
    cards = [] 
    start = 0
    needsNewStart = False
    i = 0

    for card in allCards:

        if(i >= numOfCards):        
            break
        
        if (needsNewStart):
            start = card.start
            needsNewStart = False
            content = ""

        content += card.content
        
        if (card.end - start > targetLength):
           cards.append(flashCard(start, card.end, content, "", setName)) 
           #print("card created ->", start, ":", allCards[i].end)
           needsNewStart = True
           i += 1

    #for card in cards: 
        #print("card created ->", card.start, ":", card.end)

    return cards


def getTimeStamps(s_timeStamp):
    timestamp_pattern = r'\d{2}:\d{2}:\d{2},\d{3}'
    getDigit = r'\d{2}'

    startAndEnd = re.findall(timestamp_pattern, s_timeStamp)
    
    s_start = re.findall('\d{2}', startAndEnd[0])
    
    start = 0
    
    start += int(s_start[0]) * 3600
    start += int(s_start[1]) * 60
    start += int(s_start[2])
    
    s_end = re.findall('\d{2}', startAndEnd[1])
    
    end = 0
    end += int(s_end[0]) * 3600
    end += int(s_end[1]) * 60
    end += int(s_end[2]) + 1
    
    return(start, end)
    
#getTimeStamps("00:22:49,716 --> 00:22:52,588")
