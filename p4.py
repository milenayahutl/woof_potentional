from random import *

def login(x):
    """

    Функция для создания логина пользователя
    x-все данные о пользователе
    return-логин вида Фамилия_ИО
    """
    f,i,o=x[1].split()
    ln=f'{f}_{i[0]}{o[0]}'
    return ln

def password():
    """
    Функция для создания пароля ползователя
    A,a,c - списки значений, которые могут использоваться в пароле
    return - пароль из 8 символов

    """
    A='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    a=A.lower()
    c='0123456789'
    p=[choice(A),choice(A),choice(A),choice(a),choice(a),choice(a), choice(c), choice(c)]
    shuffle(p)
    p=''.join(p)

    return p

a=open('students(1).csv', encoding='utf8').readlines()
shp=a.pop(0)
for i in range(len(a)):
    a[i]=a[i].strip().split(',')

    a[i]+=[login(a[i]),password()]

f=open('students(1)_password.scv', 'w', encoding='utf8')
f.write(shp. strip()+',login,password\n')
for x in a:
    f.write(','.join(x)+'\n')
