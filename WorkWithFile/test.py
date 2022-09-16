import zipfile
import os
import time
from tkinter import *
from tkinter.filedialog import askopenfilename

def createFile():
    z = zipfile.ZipFile('spam.zip', 'w')        # Создание нового архива
    print('Содержимое архива:')
    z.printdir()
    return z

def openFile():
    Tk().withdraw() 
    filename = askopenfilename()
    print('Имя файла:')
    print(filename)
    return filename

def writeFile(filename,z):
    z.write(filename, os.path.basename(filename))
    z.close()
    print('Данные об архиве:')
    print(os.stat('spam.zip'))
    print('Содержимое архива:')
    z.printdir()

def readFile(filename,z):
    z = zipfile.ZipFile('spam.zip', 'r') 
    z.extract(os.path.basename(filename))
    z.close()
    print('Данные о файле:')
    print(os.stat(os.path.basename(filename)))

def deleteFileAndZip(filename,z):
    os.remove(os.path.basename(filename))
    os.remove('spam.zip') 

z=createFile()
filename=openFile()
writeFile(filename,z)
readFile(filename,z)
time.sleep(10)
deleteFileAndZip(filename,z)