teks = "Kumpulan warna : "
teks_list = ["Biru", " Hijau", " Merah"]

f = open("tulisText.txt", "w")

f.write(teks)
f.writelines(teks_list)

f.close()