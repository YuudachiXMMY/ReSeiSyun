import re
import os

def m1():
    # Read in the file
    with open('test.txt', 'r', encoding='UTF-8') as file :
        filedata = file.read()

    for count, filename in enumerate(os.listdir('images/cha/')):
        # Replace the target string
        tar = filename[0:2]+filename[3:].replace('.png','')
        res = filename.replace('.png','')
        filedata = re.replace(tar, res, filedata)

    # Write the file out again
    with open('file.txt', 'w') as file:
        file.write(filedata)

def m2():
    fin = open("test.txt", "rt", encoding='UTF-8')
    filedata = fin.read()
    fin.close()
    for counts, filename in enumerate(os.listdir('images/cha/')):
        res = filename.replace('.png','')
        tar = res[0:2]+res[3:]+"}"
        res += "}\nshow " + res[0:2] + " " +res[3:]
        filedata = filedata.replace(tar, res)

    f = open("out.txt",'w', encoding='UTF-8')
    f.write(filedata)
    f.close()

m2()