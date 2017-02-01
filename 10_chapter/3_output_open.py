f1, f2 = open('poem.txt', 'r'), open('output.txt', 'w')

line = f1.readline()
while line != '':
    f2.writelines(line)
    line = f1.readline()

f1.close()
f2.close()
