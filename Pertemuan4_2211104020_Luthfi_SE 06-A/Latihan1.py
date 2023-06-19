#Latihan1
print("=============LOGIN=============")

count = 3

while True :
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    
    if count == 0:
        print('akun anda terblokir')
        break

    elif username == 'luthfi' and password == '123123':
        print('Login Berhasil.')
        break

    else:
        print('Password salah, silahkan coba lagi.')
        count -= 1
        
# else:
#     print("Akun anda terblokir")

print("===============================")