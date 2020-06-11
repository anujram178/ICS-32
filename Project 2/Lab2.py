def validWord(word):
    hawaiWordSet = {'a','e','i','o','u','p','k','h','l','m','n','w',' ',"\'"}
    wordSet = set(word.lower())
    if wordSet < hawaiWordSet:
        return True
    else:
        return False

def pronunciate(phrase):
    phrase = phrase.lower()
    if "iw" or "ew" in phrase:
        phrase = phrase.replace("iw","iv")
        phrase = phrase.replace("ew","ev")
    hawaiWordsList = phrase.split()
    hawaiDict = dict()
    pronounce = ''
    hawaiDict.update([('iw','v'),('ew','v'),('a','ah-'),('e','eh-'),('i','ee-'),('o','oh-'),('u','oo-')])
    hawaiDict.update([('ai','eye-'),('ae','eye-'),('ao','ow-'),('au','ow-'),('ei','ay-'),('eu','eh-oo'),('iu','ew-'),('oi','oy-'),('ou','ow-'),('ui','ooey-')])
    sentence = ''
    for word in hawaiWordsList:
        pronounce = ''
        i = 0
        while i < len(word):
            twoLetters = word[i:i+2]
            if twoLetters in hawaiDict:
                pronounce += hawaiDict[twoLetters]
                i = i+2
            elif twoLetters[0] in hawaiDict:
                pronounce += hawaiDict[twoLetters[0]]
                i += 1
            else:
                pronounce += word[i]
                i += 1
        while word[-1] == "-" or word[-1] == " ":
            word = word[0:-1]
        pronounce = pronounce[0:-1]
        sentence += pronounce.capitalize() + ' '
    if "-\'" in sentence:
        sentence = sentence.replace("-\'","\'")
    if "-," in sentence:
        sentence = sentence.replace("-,",",")
    while sentence[-1] == "-" or sentence[-1] == " ":
        sentence = sentence[0:-1]
    return sentence 


def createGuide(inputFile, outputFile):
    try:
        inFile = open(inputFile,'r')
    except FileNotFoundError:
        print("Input file was not found")
        return
    outFile = open(outputFile,"w")
    phrase = inFile.readlines()
    hawaiWordSet = {'a','e','i','o','u','p','k','h','l','m','n','w',' ',"\'",",","."}
    for line in phrase:
        line = line.strip("\n")
        words = line.split()
        outLine = ''
        for word in words:
            wordSet = set(word.lower())
            if wordSet < hawaiWordSet:
                outLine = outLine+ pronunciate(word) + ' '        
            else:
                outLine = "\"" + word + "\""
        outLine = outLine.strip()
        outFile.write(outLine +"\n")






               
    
    
    
    
