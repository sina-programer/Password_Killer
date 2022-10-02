import subprocess
import psutil
import time

import os
os.system('cls')

users = [user.name for user in psutil.users()]
loading_chars = list('/-\|')

time.sleep(.5)
print('\n Welcome to Password Killer (written by Sina.f)\n')
time.sleep(1)


for idx, user in enumerate(users, 1):
    print(f' {idx}_ {user}')
    time.sleep(.5)


selected_user = input('\n\n Select a user to kill(remove) its login password: ')

while True:
    time.sleep(.5)

    try:
        selected_user = int(selected_user)
        assert selected_user <= len(users) and selected_user > 0
        selected_user -= 1
        break

    except AssertionError:
        print(f'\n "{selected_user}" is not a valid user number!')
        time.sleep(.5)
        selected_user = input('\n Please enter a valid user number: ')

    except Exception:  # <selected_user> is string
        if selected_user in users:
            selected_user = users.index(selected_user)
            break

        else:
            print(f'\n "{selected_user}" is not a valid user!')
            time.sleep(.5)
            selected_user = input('\n Please enter a valid user: ')


time.sleep(.7)
user = users[selected_user]

if input(f'\n\n Are you sure to remove the password for "{user}" (y/n)? ').lower() == 'y':
    cmd = subprocess.Popen(['net', 'user', user, '*'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    cmd.stdin.write('\n'.encode())
    cmd.stdin.write('\n'.encode())
    cmd.stdin.close()

    print()
    output, error = cmd.communicate()
    time.sleep(1)

    if error:
        print(' Please run app as adminstrator!')

    else:
        for i in range(10):
            for char in loading_chars:
                print(f'\r Processing... {char}', end='')
                time.sleep(0.15)

        time.sleep(1)
        print(f'\n\n Password for "{user}" successfully killed(removed)!')
        time.sleep(.5)


figlet = '''\n
   _____ _                __ 
  / ____(_)              / _|
 | (___  _ _ __   __ _  | |_ 
  \___ \| | '_ \ / _` | |  _|
  ____) | | | | | (_| |_| |  
 |_____/|_|_| |_|\__,_(_)_| 
\n\n'''

for line in figlet.splitlines():
    print(line)
    time.sleep(.2)


time.sleep(.5)
input('\n\n Press <enter> to exit...')
