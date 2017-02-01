with open("poem.txt", 'r') as poem, open("output.txt", 'w') as output:
    line = poem.readline()
    while line != '':
        output.writelines(line)
        line = poem.readline()
