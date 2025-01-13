def jumlahkan(*listAngka):
  total = 0
  for angka in listAngka:
    total += angka
  return (listAngka, total) # return tuple

listAngka, total = jumlahkan(10, 12, 32, 35,)
print(f"Total {listAngka} = {total}")
