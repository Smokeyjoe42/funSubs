import re


#TODO add a try catch
#TODO add start and end tuples
def createCards(subFile):
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
            
            cards.append(content)
                

    return cards


def getTimeStamps(s_timeStamp):
    timestamp_pattern = r'\d{2}:\d{2}:\d{2},\d{3}'
    
    startAndEnd = re.findall(timestamp_pattern, s_timeStamp)
    
    print("Start: ", startAndEnd[0])
    print("End: ", startAndEnd[1])
    
getTimeStamps("00:22:49,716 --> 00:22:52,588")