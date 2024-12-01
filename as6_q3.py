# Solution 3:
with open("sampleText.txt", "r") as fobj:
    fileData = fobj.read()

with open("newText.txt", "w") as fobj:
    fobj.write(fileData)
