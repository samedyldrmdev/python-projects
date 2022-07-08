'''1- Bir listeyi düzleştiren (flatten) fonksiyon yazın.
Elemanları birden çok katmanlı listelerden ([[3],2] gibi)
oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:
input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output: [1,'a','cat',2,3,'dog',4,5]
2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın.
Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.
Örnek olarak:
input: [[1, 2], [3, 4], [5, 6, 7]]
output: [[[7, 6, 5], [4, 3], [2, 1]]'''

liste = [[1, 2], [3, 4], [5, 6, 7]]
ters = [list(reversed(i)) for i in liste]
print([*reversed(ters)])

# biraz daha karmaşık halini yapmak istersek
# liste = [[1, 2, 3], [7, 8, 9, [6, 5, 3]], [11, 12, 13]]
# ters = [[*reversed(i)] for i in liste]
# print([*reversed(ters)])

