#!/usr/bin/env python
#-*- coding:utf-8 -*-

f=open('blackuser','a+')
u=open('userlist','w')
u.write('hsggj 123456'+'\n' 'jack 111')
u.close()
a=[]

for i in range(0,3):
    name = input('name: ')
    if name in open('blackuser').read():
        print('is a locked,please try')
        continue
    if name not in open('userlist').read():
        print('The user is not exists')
        continue
    password = input('pass: ')
    # if password.isdigit():
    #     password = int(password)
    for j in open('userlist').readlines():
        username,security=j.strip().split()

        if name == username and security == password:
            print('Welcome login')
            break
    else:
        print('The username or password is wrong,please try agine')
        a.append(name)
    if a.count(name) >= 3:
        print('The name is three wrong,now is locked')
        f.write(name+'\n')
