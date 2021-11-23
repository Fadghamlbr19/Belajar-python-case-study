#membuka file
file_text = open("2_readtext.txt" ,"r")

#membaca text
print(file_text.readlines())

#tutup file
file_text.close()

a = input('').split(" ")[0]
print(a)

file_text = open("2_readtextperline.txt" ,"r")
read_text = file_text.readlines()

print(read_text[1])
print(read_text[3])


file_text.close()

a = input('').split(" ")[0]
print(a)

file_text = open("2_readtextperline.txt" ,"r")
read_text = file_text.readlines()

for i in read_text:
    print(i)

file_text.close()