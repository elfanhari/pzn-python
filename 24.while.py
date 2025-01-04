print('------ LOGIN ------')

username = 'admin'
password = '123'
usr = ''
pas = ''

def inputLogin():
  global usr, pas
  usr = input('Username: ')
  pas = input('Password: ')

inputLogin()

while username != usr or password != pas:
  print('Login Gagal! coba lagi')
  inputLogin()

print('Login Berhasil!')
