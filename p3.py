a=open('C:\\Users\\student\\Downloads\\students.csv', encoding='utf8').readlines()
a.pop(0)
for i in range(len(a)):
    a[i]=a[i].strip().split(',')
    a[i][2]=int(a[i][2])

while 1:
    id=input()
    if id=='СТОП':
        break
    id =int(id)
    f=0
    for x in a:
        if x[2]==id:
            f, i, o = x[1].split()
            name = f'{i[0]}. {f}'
            print(f'Проект № {x[2]} делал: {name} он(а) получил(а) оценку - {x[4]}')
            f=1
            break
    if f==0:
        print('Ничего не найдено.')
