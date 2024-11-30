# Solution 1
# fileName = input("Enter file name: ")
wordsList = []

fobj = open('sampleText.txt', 'r')

words = []
lines = fobj.readlines()
for line in lines:
    words = line.strip('\n').split(' ')

    for word in words:
        if word not in wordsList:
            wordsList.append(word)
        else:
            pass

wordsList.sort()
print(wordsList)

fobj.close()