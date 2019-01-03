a = [int(input("Enter id:"))]
b = [input("Enter name:")]
c = [input("Enter location:")]
d = []
for i in enumerate(a):
    for j in enumerate(b):
        for k in enumerate(c):
           if i[0]==j[0]==k[0]:
               d.append((i[1],j[1],k[1]))
print(d)




