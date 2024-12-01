# Solution 5
vowels = "aeiou"
myStr = input()
ans = 0

for x in myStr:
    if x in vowels:
        ans+=1

print(ans)