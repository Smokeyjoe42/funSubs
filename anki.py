

def createAnkiFile(fC, path, setName):
    try:
        f = open(path + setName + ".txt", "w")
    except:
        print("Failed to create ", setName)
    
    for card in fC: f.write(card.content + ";" + card.source +  "\n")
    f.close()

    print("Anki file saved at", path + setName, "\n")