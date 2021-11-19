#mengikuti tutorial youtube Kristara cyber

position = int(input("masukkan angka= "))

def ganjil():
    for i in range(position):
        if i % 2 != 0:
            print(i, end=" ")

def genap():
    for i in range(position):
        if i % 2 == 0:
            print(i, end=" ")

print("Bilangan Ganjil")
ganjil()

print()

print("Bilangan Genap")
genap()