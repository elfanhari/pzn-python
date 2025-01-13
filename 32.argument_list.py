def jumlahkan(x, y, **listAngka): # *tandanya mengkonvert argumen menjadi list
  total = 0
  for angka in listAngka:
    total += angka
  print(f"x: {x}")
  print(f"y: {y}")
  print(f"total {listAngka} = {total}")
jumlahkan(10, 12, 32, 35, 31)
