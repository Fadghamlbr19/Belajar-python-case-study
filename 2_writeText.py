#PROGRAM MENULIS FILE TEKS

#Input dari user
nama = input("Nama   : ")
umur = input("Umur   : ")
club = input("Club   : ")

teks  = "Nama: {}\nUmur: {}\nClub: {}".format(nama,umur,club)

file_bio = open("2_writeText.txt","w")

file_bio.write(teks)

file_bio.close()