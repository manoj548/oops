import re
f1 = open("C:/Users/M/Desktop/test5.txt","r")
print(re.findall(r'[a-zA-Z0-9.]+@[a-z.]+',f1.read()))



