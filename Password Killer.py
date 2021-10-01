from itertools import cycle
from sys import stdout
from time import sleep
import subprocess
import os

loading_chars = iter(cycle('/-\|'))
current_user = os.getlogin()
os.system('cls')

print('''\n Welcome to Password Killer(written by Sina.f)\n''')
sleep(1)
submit = input(' Are you sure to remove the password for current user?(y/n) ').lower()

if submit == 'y':
    # cmd --> command prompt
    cmd = subprocess.Popen(['net', 'user', current_user, '*'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    cmd.stdin.write(''.encode())
    cmd.stdin.write(''.encode())
    cmd.stdin.close()
    
    print()
    output, error = cmd.communicate()
    sleep(1)

    if error:
        print(' Please run app as adminstrator')
    
    else:
        for i in range(52):
            sleep(0.15)
            stdout.write(f'\r Processing... {next(loading_chars)}')
            
        sleep(1)
        print('\n\n Your password successfully removed!')
        sleep(.5)

figlet =  f'''\n
   _____ _                __ 
  / ____(_)              / _|
 | (___  _ _ __   __ _  | |_ 
  \___ \| | '_ \ / _` | |  _|
  ____) | | | | | (_| |_| |  
 |_____/|_|_| |_|\__,_(_)_| 
'''

for line in figlet.splitlines():
    print(line)
    sleep(.2)
    
sleep(1)
input('\n\n Press enter to exit...')
