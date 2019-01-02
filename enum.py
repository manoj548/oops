l1 = [5,6]
l2 = ['manu','nani']
l3 = ['blr','hyd']
l4 = []
for i in enumerate(l1):
    print(i)
    for j in enumerate(l2):
        for k in enumerate(l3):
           if i[0]==j[0]==k[0]:
               l4.append((i[1],j[1],k[1]))
print(l4)




