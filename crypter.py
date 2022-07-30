import os
import pyAesCrypt

def crypt_and_decrypt(crypt_or_decrypt,file):
        password = input('Введи пароль для шифровки. В будущем он понадобится для раскодировки: ')
        buffer = 512*1024
        bezrashireniy= file.split('.')
        if crypt_or_not == 1:
            try:
                pyAesCrypt.encryptFile(file, bezrashireniy[0] + '.word', password, buffer)
                
            except FileNotFoundError and ValueError:
                print('Не удалось сделать шифровку файла')

        elif crypt_or_not == 0:
            typefile = input('Напиши тип файла: ')
            try:
                pyAesCrypt.decryptFile(file, bezrashireniy[0]+'.'+typefile, password, buffer)

            except FileNotFoundError and ValueError:
                print('Дешифровка не вышла')

        os.remove(file)






crypt_or_not = int(input('Напишите 1 для шифровки, а 0 для дешифровки: '))
filename = input('Напишите название файла для шифровки/дешифровки: ')

crypt_and_decrypt(crypt_or_not, filename)