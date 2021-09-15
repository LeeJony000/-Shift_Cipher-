import sys
import platform

# 加密
def shift_cipher_encrypt():
    list_s = []
    list_s = []
    r_move = int(input('请输入加密移位参数(右移)：  '))
    s = input('请输入需要加密的字符： ')
    print("密文:", end='')
    for i in s:
        list_s.append(ord(i))
    for i in list_s:
        #       处理空格
        if i == 32:
            print(' ', end='')
        #       对大写字母进行处理
        elif 65 <= i <= 90:
            i += r_move
            while i > 90:
                i -= 26

        #       对小写字母进行处理
        elif 97 <= i <= 122:
            i += r_move
            while i > 122:
                i -= 26
        print(chr(i), end='')


def shift_cipher_encrypt(s, r_move):
    list_s = []
    for i in s:
        list_s.append(ord(i))
    for i in list_s:
        #       处理空格
        if i == 32:
            print(' ', end='')
        #       对大写字母进行处理
        elif 65 <= i <= 90:
            i += r_move
            while i > 90:
                i -= 26

        #       对小写字母进行处理
        elif 97 <= i <= 122:
            i += r_move
            while i > 122:
                i -= 26
            i -= 32
        print(chr(i), end='')


# 解密


def shift_cipher_decrypt():
    l_move = int(input('请输入解密移位参数(左移)： '))
    s = input('请输入需要解密的字符： ')
    list_s = []
    for i in s:
        list_s.append(ord(i))
    for i in list_s:
        if i == 32:
            print(' ', end='')
        elif 65 <= i <= 90:
            i -= l_move
            while i < 65:
                i += 26
        elif 97 <= i <= 122:
            i -= l_move
            while i < 97:
                i += 26
        print(chr(i), end='')


def shift_cipher_decrypt(s, l_move):
    list_s = []
    for i in s:
        list_s.append(ord(i))
    for i in list_s:
        if i == 32:
            print(' ', end='')
        elif 65 <= i <= 90:
            i -= l_move
            while i < 65:
                i += 26
            i += 32
        elif 97 <= i <= 122:
            i -= l_move
            while i < 97:
                i += 26
        print(chr(i), end='')


if __name__ == '__main__':
    logo = R'''
     ____  _     _  __ _         ____ _       _               
/ ___|| |__ (_)/ _| |_      / ___(_)_ __ | |__   ___ _ __ 
\___ \| '_ \| | |_| __|____| |   | | '_ \| '_ \ / _ \ '__|
 ___) | | | | |  _| ||_____| |___| | |_) | | | |  __/ |   
|____/|_| |_|_|_|  \__|     \____|_| .__/|_| |_|\___|_|   
                                   |_|                                        
    '''

    if platform.system() == 'Windows':
        import publish_logo
        publish_logo.printSkyBlue(logo)
    elif platform.system() == 'Linux':
        print(f"\033[36m{logo}\033[0m")
    print('\n')

    while 1:
        answer = input("请输入所需的操作：移位加密/E or 移位解密/D or 退出/Q: ")
        i = 1
        if answer.upper() == 'E':
            s = input('请输入需要加密的字符： ')
            r_move = int(input('请输入加密移位参数(右移)：'))
            shift_cipher_encrypt(s, r_move)
            print('\n')
        elif answer.upper() == 'D':
            s = input('请输入需要解密的字符： ')
            print("可能的明文:")
            while i <= 25:
                shift_cipher_decrypt(s, i)
                print('\r')
                i = i + 1
            print('\n')
        elif answer.upper() == 'Q':
            sys.exit()
        else:
            print('输入错误！')
