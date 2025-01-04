tinggi = int(input('Jumlah baris:'))

for i in range (1, tinggi + 1):
  space = " " * (tinggi - i)
  star = "*" * (2 * i - 1)
  print(space + star)
