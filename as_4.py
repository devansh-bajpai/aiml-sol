# Solution 1
num1 = int(input())
num2 = int(input())

if (num1 < num2):
    num1, num2 = num2, num1

# The above line will ensure num1 > num2

i = 1
while True:
    if (num1*i)%num2 == 0:
        print(num1*i)
        break
    else:
        i += 1

# Solution 2
n = int(input())
for x in range(1, 11):
    print(n, "x", x, "=", n*x)


# Solution 3
myStr = input()
if myStr == myStr[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# Solution 4
import string

myStr = input()
for x in myStr:
    if x in string.punctuation:
        myStr = myStr.replace(x, "")
    
print(myStr)