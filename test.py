with open('sampleText.txt', 'r+') as fobj:
    lines = fobj.readlines()
    i = 0

    for line in lines:
        line = line.replace('java', 'python')
        lines[i] = line
        i += 1

    

with open('sampleText.txt', 'w') as fobj:
    fobj.writelines(lines)
    