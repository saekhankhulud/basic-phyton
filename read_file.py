# read file
f = open("file.txt", "r")

# print all text
print(f.read())

# print part of file
print(f.read(8))

#read line
print(f.readline())
print(f.readline())
print(f.readline())

f.close()