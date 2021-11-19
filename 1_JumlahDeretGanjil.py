position = int(input("masukkan n= "))
i = 0
b = 1
total = 0
for i in range(position):
    total = total + 2*b-1
    b = b+1
    print (total)





print("jumlah deret ganjil ke-n adalah" + str(total))
