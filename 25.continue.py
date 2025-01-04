ganjil = 1
genap = 2

for i in range(1, 100):
  if i % 2 == genap: # jika i modulus 2 hasilnya genap, maka lewati/skip
    continue
  print(i)

# kode tersebut akan mencetak ganjil atau genap saja sajaa
