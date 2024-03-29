A='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧЪЬЭЮЯ'
a=A.lower()
A='*'+A+a+' '

def hash(s):

    s=s[1]
    p=67
    m=10**9+9
    h=0
    for i in range(len(s)):
        h+=A.find(s[i])*p**i
    h=h%m
    return str(h)


a=open('students(1).csv', encoding='utf8').readlines()
scp=a.pop(0)
for i in range(len(a)):
    a[i]=a[i].strip().split(',')


f=open('students_with_hash.csv', 'w', encoding='utf8')
f.write(scp)
for x in a:
    x[0]=hash(x)
    f.write(','.join(x)+'\n')

