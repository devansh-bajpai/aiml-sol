# Solution 1
fileName = input("Enter file name: ")
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


# Solution 2
choice = input("w/r? : ")
if choice == "r":
    with open("sampleText.txt", "r") as fobj:
        print(fobj.read())
elif choice == "w":
    with open("sampleText.txt", "w") as fobj:
        myInput = input("Enter Input: ")
        fobj.write(myInput)

# Solution 3:
with open("sampleText.txt", "r") as fobj:
    fileData = fobj.read()

with open("newText.txt", "w") as fobj:
    fobj.write(fileData)


# Solution 4:

# Reading CSV:
import csv
with open('names.csv', 'r') as fobj:
    csv_reader = csv.reader(fobj)

    for line in csv_reader:
        print(line)

# Writing CSV:
import csv
with open('myCSV.csv', 'w', newline='') as fobj:
    csv_writer = csv.writer(fobj, delimiter=',')
    csv_writer.writerow(['devansh', 'bajpai', 'devansh@mnnit'])


# Reading JPG File
import cv2

myImg = cv2.imread('rose.jpg')
cv2.imshow("original image", myImg)
cv2.waitKey(0)
