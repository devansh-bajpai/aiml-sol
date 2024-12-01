# Solution 6
fobj = open("sampleText.txt", 'r')

myLines = fobj.readlines()
linesCount = len(myLines)
wordCount = 0
charCount = 0
for line in myLines:
    words = line.split(" ")
    wordCount += len(words)
    
    for word in words:
        myWord = word.replace('\n', "")
        charCount += len(myWord)


print(linesCount, wordCount, charCount)

fobj.close()