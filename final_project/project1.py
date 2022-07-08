'''1- Bir listeyi düzleştiren (flatten) fonksiyon yazın.
Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi,
non-scalar verilerden de oluşabilir.'''

liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

new_list = []
for i in liste:
    if type(i)==list:
        for a in i:
            if type(a)==list:
                for b in a:
                    if type(b)==list:
                        for c in b:
                            new_list.append(c)
                    else:
                        new_list.append(b)
            else:
                new_list.append(a)
    else:
        new_list.append(i)
print(new_list)
