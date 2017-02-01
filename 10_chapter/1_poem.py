poemFile = open('poem.txt', 'r')
line = poemFile.readline()

while line != '':
    print(line.strip('\n'))
    line = poemFile.readline()

poemFile.close()
