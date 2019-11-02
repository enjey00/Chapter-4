all = ['Alymbekov@gmail.com', 'Alymbekov@mail.ru', 'Alymbekov@.kg']
g = []
m = []
k = []
for i in all:
    a = i.split('@')[1]

    if a == 'gmail.com':
        g.append(i)
    elif a == 'mail.ru':
        m.append(i)
    else:
        k.append(i)

print(g)
print(m)
print(k)