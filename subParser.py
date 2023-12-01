import re
from flashCard import flashCard

"""Creates flashCard obj's from a subtitle file
Output: a deck of flashCards"""

#TODO add a try catch
#TODO add start and end tuples
def createCards(subFile, targetLength):
    file = open(subFile, 'r')
    
    cards = []
    
    timestamp_pattern = r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}'
    
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
            
            cards.append(flashCard(timestamp[0], timestamp[1], content, ""))
                

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
    
getTimeStamps("00:22:49,716 --> 00:22:52,588")
