# # Solution 1
# # fileName = input("Enter file name: ")
# wordsList = []

# fobj = open('sampleText.txt', 'r')

# words = []
# lines = fobj.readlines()
# for line in lines:
#     words = line.strip('\n').split(' ')

#     for word in words:
#         if word not in wordsList:
#             wordsList.append(word)
#         else:
#             pass

# wordsList.sort()
# print(wordsList)

# fobj.close()


# Solution 2
choice = input("w/r? : ")
if choice == "r":
    with open("sampleText.txt", "r") as fobj:
        print(fobj.read())
elif choice == "w":
    with open("sampleText.txt", "w") as fobj:
        myInput = input("Enter Input: ")
        fobj.write(myInput)