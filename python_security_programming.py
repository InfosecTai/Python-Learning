# get os name
import os
print(os.name)

path = os.path.join('anhtai','python_scripts')
print(path)

dir = os.getcwd()

print(dir)

sys1 = os.system('ipconfig ifcount')

print(sys1)

# open and read file
file = open('/home/kali/pythonPractice/fileToBeRead.txt')

readTxt = file.read()

# open new file and write to it
newFile = open('/home/kali/pythonPractice/newfile.txt', 'w')
newFile.write('Hello world. Saturday 10/17/2020 9:34 am')
file.close()
