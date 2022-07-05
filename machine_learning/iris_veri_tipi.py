# 1.İris veri setinin yüklenmesi

from sklearn.datasets import load_iris

iris_dataset = load_iris()
# print(iris_dataset)
# 2.Verinin ikiye bölünmesi

from sklearn.model_selection import train_test_split

x_ogren, x_test, y_ogren, y_test = train_test_split(iris_dataset["data"], iris_dataset[
    "target"])  # ,test_size=0,33) olarak verirsek %33 - %67 olarak ayıracak. Standart olarak %75-%25
print(x_ogren.shape)  # shape komutu boyutları döndürüyor.
print(x_test.shape)
# Bu kısımda x_ogren verisi 112, x_test verisi de 38'e eşit oluyor. Toplamda 150 çiçek var.
# Öğrenme verisini öğrenirken kullanacağız. Daha sonra test verisini de test etmek için kullanacağız.
# Bu kısımda %75-%25 yaptığımız için öğrenme verisi 150'nin %75'i olarak karşımıza çıkıyor.

# 3.Uygun modeli seçme

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1)  # en yakın nokta seçiyoruz. Bu da 1.
print(knn)

# 4.Öğrenme

knn.fit(x_ogren, y_ogren)
# 5.Tahmin

x_yeni = [[3.5, 2.1, 3.4, 1.2]]  # bilinmeyen değerleri giriyoruz.
tahmin = knn.predict(x_yeni)
print(tahmin)

# 6.Doğruluk ve Test Verisi

dogruluk = knn.predict(x_test)
print(dogruluk)

import numpy as np

print(np.mean(dogruluk == y_test) * 100)
