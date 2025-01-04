# program sederhana dari For-Loop, List, dan Range.
# ceritanya kita mau add Daftar Tiket

def rp(angka): # fungsi format rupiah
  angka_str = f"{angka:,}"
  angka_str = angka_str.replace(',','.')
  return f'Rp{angka_str}'

print('--- DATA TIKET PERSIB VS REAL MADRID ---')

jumlahJenisTiket = int(input('Berapa jenis tiketnya? '))

nama = []
harga = []

for i in range(0, jumlahJenisTiket):
   namaTiket = input(f'Nama Tiket ke {i+1}: ')
   hargaTiket = int(input(f'Harga tiket {namaTiket}: '))

   nama.append(namaTiket)
   harga.append(hargaTiket)

print('\n----- DAFTAR TIKET -----')
for a in range(0, len(nama)):
    print(f'{a+1}: {nama[a]} {rp(harga[a])}')
print('------------------------')

print('\n----- BELI TIKET -------')
tiketDipilih = int(input(f'Pilih tiket nomor berapa? ' ))
jumlahBeli = int(input('Beli berapa tiket? ' ))

print('\n----- STRUK ------')
print(f'Tiket Dipilih: {nama[tiketDipilih-1]}')
print(f'Harga Tiket: {rp(harga[tiketDipilih-1])}')
print(f'Jumlah Beli: {jumlahBeli}')
print('-------------------')
totalHarga = harga[tiketDipilih-1] * jumlahBeli
print(f'Total: {rp(totalHarga)}')
print('-------------------')
