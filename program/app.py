# Program CRUD Mahasiswa
import function
import time

run = True # pengecek apakah terus atau tidak
while run:

  function.menu() # Show menu yang tersedia

  menu = input('Pilih menu [0-5] : ') # menu yang dipilih

  if menu == '0': # jika quit
    break
  elif menu == '1': # jika pilih show
    function.show()
  elif menu == '2': # jika pilih create
    function.create()
  elif menu == '3': # jika pilih edit
    function.edit()
  elif menu == '4': # jika pilih delete
    function.delete()
  elif menu == '5': # jika pilih cari
    function.search()
  else: # jika pilih bukan [0-5]
    print("Menu tidak tersedia! pilih yang tepat!")
    time.sleep(1.2)

print('Program selesai, see you!')
