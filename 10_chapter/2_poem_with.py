with open("poem.txt", 'r') as poem:
    line = poem.readline()
    while line != '':
        print(line.strip('\n'))
        line = poem.readline()
