A =input("enter your number: ")
B=input("enter your number: ")

listA=[] #stores for numA
listB=[] #stores for numB

for n in range(1,(int(A) +1)):
    if int(A) % n == 0:
        listA.append(n)
for n in range(1,(int(B) +1)):
    if int(B) % n == 0:
        listB.append(n)

print(listA) #shows list of factors of numA
print(listB) #shows list of factors of numB

listC=[]
for i in listA:
    if i in listB:
        listC.append(i)
print(max(listC)) #Shows final Greatest Common Divisor
