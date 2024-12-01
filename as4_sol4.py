# Solution 4
import string

myStr = input()
for x in myStr:
    if x in string.punctuation:
        myStr = myStr.replace(x, "")
    
print(myStr)

