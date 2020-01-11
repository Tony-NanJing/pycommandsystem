#!python3
#-*-coding: UTF-8-*-
#pycs.py
#PYthonCommandSystem
ver = '0.0.4'
ver_str = 'Eagle'

import pygame

print('Booting...')
print('Initing sound system...')

pygame.init()
pygame.mixer.init()
print('Playing booting music...')
pygame.mixer.music.load('./res/boot.mid')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(1)
import os,time,pyautogui
print('Will clear the display 2 seconds later')
time.sleep(2)
os.system('cls')

print('''PythonCommandSystem %s (%s) By Tony Nan
Warning: Unstable version, might exit suddenly.''' % (ver,ver_str))
command = ''
path = '/'
strDisp = ''
lenp = 0
odir = 0
while True:
    if path=='/':
        strDisp = ''

    else:
        strDisp = path[:-1]

    command = input(strDisp + '> ')
    try:
        if command == 'halt':
            print('Will now halt.')
            break

        elif command[0:3] == 'mkd':
            os.system('md ' + command[4:])

        elif command[0:2] == 'lf':
            ls = os.listdir('.')
            print(str(len(ls)) + ' files/directorys')
            for i in ls:
                print(i + '\t' + '   ',end='')

            print('')

        elif command[0:2] == 'dl':
            os.system('del ' + command[3:])
            os.system('rd ' + command[3:])
        
        elif command[0:2] == 'cd':
            ls = os.listdir('./')
            bpath = path
            if command[3:] in ls:
                try:
                    path += command[3:] + '/'
                    lenp = len(command[3:])
                    os.chdir('./' + command[3:])
                except OSError:
                    path = bpath
                    print('Isn\'t a directory')

                odir += 1

            else:
                print('No directory')

        elif command[0:2] == 'ex':
            os.system(command[3:])

        elif command[0:4] == 'edit':
            if command[5:] in os.listdir('./'):
                s = open(command[5:],'r').read()
                f = open(command[5:],'w')
                print('Input \'saveit!@#$%^&*();;;\' to save file(press Enter before this).')
                fs = ''
                a = 0
                i = ''
                while True:
                    if a == 0:
                        pyautogui.typewrite(s)

                    i = input()
                    if i == 'saveit!@#$%^&*();;;':break
                    fs += i
                    fs += '\n'
                    a += 1
                
                f.write(fs)
                f.close()


            else:
                f = open(command[5:],'w')
                print('Input \'saveit!@#$%^&*();;;\' to save file(press Enter before this).')
                fs = ''
                i = ''
                while True:
                    i = input()
                    if i == 'saveit!@#$%^&*();;;':break
                    fs += i
                    fs += '\n'
                
                f.write(fs)
                f.close()

        elif command[0:3] == 'cat':
            try:
                print(open(command[4:],'r').read())

            except FileNotFoundError:
                print('No such file.')

        elif command[0:2] == 'bk':
            if lenp == 0:
                pass

            else:
                path = path[:-lenp-1]
                os.chdir(open(odir * '../' + 'pth.res','r').readline() + path)
                odir -= 1

        elif command[0:3] == 'run':
            try:
                s = open(command[4:], 'r').read()
                pyautogui.typewrite(s)

            except FileNotFoundError:
                print('No such file.')
        elif command[0:2] == 'sw':
            if command[3:] in os.listdir(odir * '../' + 'softwares'):
                os.system(odir * '..\\' + 'softwares\\' + command[3:])

            else:
                print('No such software.')

        elif command[0:4] == 'echo':
            print(command[5:])

        elif command[0:2] == 'cp' and command[0:3] != 'cpd':
            l = command[3:].split(' ')
            if len(l) == 2:
                os.system('copy ' + l[0].replace('/','\\') + ' ' + l[1].replace('/','\\'))

            else:
                print('IndexError')

        elif command[0:3] == 'cut' and command[0:4] != 'cutd':
            l = command[4:].split(' ')
            if len(l) == 2:
                os.system('copy ' + l[0].replace('/','\\') + ' ' + l[1].replace('/','\\'))
                os.system('del ' + l[0].replace('/','\\'))

            else:
                print('IndexError')

        elif command[0:3] == 'cpd':
            l = command[4:].split(' ')
            if len(l) == 2:
                try:
                    os.system('md ' + l[1].replace('/','\\'))
                    os.system('copy ' + l[0].replace('/','\\') + '\\*' + ' ' + l[1].replace('/','\\'))

                except OSError:
                    print('Invalid path.')

            else:
                print('IndexError')

        elif command[0:4] == 'help':
            print(open(odir * '../' + 'res/help.res', 'r').read())

        elif command[0:4] == 'cutd':
            l = command[5:].split(' ')
            if len(l) == 2:
                try:
                    os.system('md ' + l[1].replace('/','\\'))
                    os.system('copy ' + l[0].replace('/','\\') + '\\*' + ' ' + l[1].replace('/','\\'))
                    os.system('del ' + l[0].replace('/','\\') + '\\*')
                    os.system('rd ' + l[0].replace('/','\\'))

                except OSError:
                    print('Invalid path.')

            else:
                print('IndexError')

        elif command[0:5] == 'cldsp':
            os.system('cls')
        
        else:
            print('Unknown command.')

    except IndexError:
     #   print('SyntaxError')
         pass

os.system('cls')
print('Playing halting music...')
pygame.mixer.music.load(odir * '../' + './res/halt.mid')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(1)
time.sleep(35)
print('Quitting pygame')
pygame.quit()
