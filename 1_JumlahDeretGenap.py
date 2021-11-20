#Memakai for
position = int(input("masukkan n= "))
i = 0
b = 1
total = 0
for i in range(position):
    total = total + 2*b
    b = b+1
    print (total, end=" ")

print("\njumlah deret genap ke-"+ str(position) + " adalah " + str(total))

a = input('').split(" ")[0]
print(a)

#Memakai while
n = int(input("masukkan n = "))
i=0
jml=0
while i<=n:
    jml = jml + 2*i
    i = i+1
    print (jml, end=" ")
print("\njumlah deret Genap ke-"+ str(n)+ " adalah " + str(jml))

