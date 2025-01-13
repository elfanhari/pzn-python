import time

mahasiswas = [
  {
    "name" : "Reza",
    "nim" : "01",
  },
  {
    "name" : "Azhar",
    "nim" : "02",
  },
  {
    "name" : "Elfan",
    "nim" : "03"
  }
]

def menu():
  print('\n----- MENU -----')
  print('================')
  print(f'1. Show All Mahasiswa ({len(mahasiswas)})')
  print('2. Add Mahasiswa')
  print('3. Edit Mahasiswa')
  print('4. Delete Mahasiswa')
  print('5. Search Mahasiswa')
  print('0. Quit')
  print('================\n')

def printMhs(name, nim, no = 1):
  print("================")
  print(f"{no}.")
  print(f"Nama : {name}")
  print(f"NIM : {nim}")

def show():
  print('\n-- DATA MAHASISWA --')
  inM = 1 # index
  for mhs in mahasiswas:
    printMhs(mhs['name'], mhs['nim'], inM)
    inM += 1
  print("================")
  print('')
  time.sleep(1.2) # delay 2 detik


def create():
  print('\n-- TAMBAH DATA MAHASISWA --\n')
  name = input('Nama : ')
  nim = input('NIM : ')

  mahasiswa = {
    "name" : name,
    "nim" : nim,
  }
  mahasiswas.append(mahasiswa)
  print(f'Data Mahasiswa {name} berhasil ditambahkan!\n')
  time.sleep(1.2)

def edit():
  print('\n-- EDIT DATA MAHASISWA --\n')
  print('Ketik 0 untuk ke menu utama')
  while True:
    nimEdited = input("Input NIM Mahasiswa : ")
    if nimEdited == '0':
      print('Kembali ke menu utama..')
      time.sleep(0.5)
      break

    mhs = []
    for mh in mahasiswas:
      if mh['nim'] == nimEdited:
          mhs = mh
          break

    if mhs:
      print('NIM ditemukan! silakan edit')
      nameEdited = input(f"Edit Nama [{mhs['name']}] : ")
      nimEdited = input(f"Edit NIM [{mhs['nim']}] : ")
      mhs['name'] = nameEdited
      mhs['nim'] = nimEdited
      editAct = False
      print(f"Data Mahasiswa berhasil di update!")
      time.sleep(1.2)
      break
    else:
      print('NIM tidak ditemukan! Cari lagi!' )


def delete():
  print('\n-- HAPUS DATA MAHASISWA --\n')
  print('Ketik 0 untuk ke menu utama')

  delRun = True
  nimDel = 0
  while delRun == True or nimDel == '0':
    nim = input("Input NIM Mahasiswa : ")
    index = -1
    nimDel = nim

    for i in range(0, len(mahasiswas)):
        mhs = mahasiswas[i]
        mhsName = mhs['name']
        if nim == mhs['nim']:
          index = i
          break

    if index == -1:
      print('Data tidak ditemukan! cari lagi!')
    else:
      del mahasiswas[index]
      delRun = False
      print(f"\nData Mahasiswa {mhs['name']} berhasil dihapus!\n")
      time.sleep(1.2)

def search():
  print('\n-- CARI DATA MAHASISWA --\n')
  print('Ketik 0 untuk ke menu utama!')

  searchRun = True
  while searchRun == True:
    nameSearched = input("Input Nama Mahasiswa : ")
    if nameSearched == '0':
      break

    mhs = []
    for mh in mahasiswas:
      if mh['name'].lower().find(nameSearched.lower()) != -1:
        mhs = mh

    if mhs:
      print(f"\nMahasiswa ditemukan..")
      time.sleep(1.2)
      printMhs(mhs['name'], mhs['nim'])
      print("================\n")
      searchRun = False
    else:
      print('Data tidak ditemukan! cari lagi!')
