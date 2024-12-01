# Solution 2
choice = input("w/r? : ")
if choice == "r":
    with open("sampleText.txt", "r") as fobj:
        print(fobj.read())
elif choice == "w":
    with open("sampleText.txt", "w") as fobj:
        myInput = input("Enter Input: ")
        fobj.write(myInput)
