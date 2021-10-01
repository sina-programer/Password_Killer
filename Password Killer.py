from itertools import cycle
from sys import stdout
from time import sleep
import subprocess
import psutil
import os

users = [user.name for user in psutil.users()]
loading_chars = iter(cycle('/-\|'))
os.system('cls')

sleep(.5)
print('''\n Welcome to Password Killer(written by Sina.f)\n''')
sleep(1)

for i in range(32):
    sleep(0.15)
    stdout.write(f'\r Extracting users... {next(loading_chars)}')

print('\n')
sleep(1)

for idx, user in enumerate(users):
    print(f' {idx+1}_ {user}')
    sleep(1)
    
    
selected_user = input('\n Select a user to kill(remove) the login password: ')

while True:
    sleep(.5)
    try:
        selected_user = int(selected_user)
        assert selected_user <= len(users) and selected_user > 0
        selected_user -= 1
        break
    
    except AssertionError:
        print(f'\n "{selected_user}" is not a valid user number!')
        sleep(.5)
        selected_user = input('\n Please enter a valid user: ')        
        
    except:
        if selected_user in users:
            selected_user = users.index(selected_user)
            break
            
        else:
            print(f'\n "{selected_user}" is not a valid user!')
            sleep(.5)
            selected_user = input('\n Please enter a valid user: ')
                
user = users[selected_user]
sleep(.7)
submit = input(f'\n Are you sure to remove the password for "{user}" (y/n)? ').lower()

if submit == 'y':
    # cmd --> command prompt
    cmd = subprocess.Popen(['net', 'user', user, '*'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    cmd.stdin.write('\n'.encode())
    cmd.stdin.write('\n'.encode())
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
        print(f'\n\n Password for "{user}" successfully killed(removed)!')
        sleep(.5)
    
figlet =  '''\n
   _____ _                __ 
  / ____(_)              / _|
 | (___  _ _ __   __ _  | |_ 
  \___ \| | '_ \ / _` | |  _|
  ____) | | | | | (_| |_| |  
 |_____/|_|_| |_|\__,_(_)_| 
\n\n'''

for line in figlet.splitlines():
    print(line)
    sleep(.2)
    
sleep(1)
input(' Press enter to exit...')
