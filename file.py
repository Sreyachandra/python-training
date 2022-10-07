#reading in to fiels
f = open("tr.txt", "r")
print(f.read())                                             #read file contents
o=open("tr.txt","r")
str1=fo.read(4)
str2=fo.read(4)
str3=fo.read()
print("str1:",str1)
print("str2:",str2)
print("str3:",str3)                                          #str1: pyth
                                                              str2: on i
                                                              str3: s a highlevel language.its great.
F = open(“file.txt”,”r”)
print(f.readline())                                 
#writing in to files
fo = open(“file.txt”,”w”)
fo.write(“python is great\n”)
fo.write(“yeah its great\n”)
fo.close()
#coping contents of file from one to another in line by line
fs=open(“file.txt”,”r+”
fd=open(“newfile.txt”,”w+”)
for line in fs:
 fd.write(line)
fs.close()
fd.close()

