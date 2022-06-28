# veri önisleme = Veri setini, model belirtmek için hazır hale getirmek

# 1- veri setindeki eksik değerleri tamamlama
# 2- kategorileri numaralandırma
# 3- özellikleri ölçekleme
# 4- veri setini öğrenme ve test şeklinde ikiye bölme
# 5- veriyi görselleştirme

# Aşamalar

# 1- veri setini yükle. pandas kullanarak.
# 2- kayıp değerleri doldur. (.csv dosyasındaki)
# 3- etiket olan (kategori) verileri numaralandır / sayısallaştır.
# 4- veriyi öğrenme ve test şeklinde ikiye böl.

# 1- Gerekli kütüphanelerin eklenmesi

import numpy as np  # bilimsel python kütüphanesi
import pandas
import pandas as pd  # verileri okutmak için kullanılıyor.
import matplotlib.pyplot as plt  # görselleştirmek için kullanılıyor.

# 2- Veri setinin pandas'a yüklenmesi

dataset = pd.read_csv("Data.csv")
# print(dataset)
# print(type(dataset))
# ülkeler, yaş, maaş, maaşın alınıp alınmadığı

# 3- Python ":" Operatörü ve Fonksiyonlar

# pandas.DataFrame Önemli Fonksiyonlar
#
# values = Veri setini numpy.ndarray şeklinde döndürür.
# ndim = Veri setinde kaç boyut olduğunu döndürür.
# size = Veri setinin kaç tane elemanı olduğunu döndürür.
# shape= Veri setinin boyutlarını döndürür. (satır,sütun)
# iloc = Veri setinde tam sayı kullanarak elamanlara erişiminizi sağlar.
# empty = Veri setinde eleman olup olmadığını kontrol eder.
# dtypes = Veri setindeki elemanların tipini döndürür.

# print(dataset.values)
# print(type(dataset.values))
# print(dataset.values[0])
#
# print("kaç boyut:", dataset.ndim)
# print("eleman sayısı:", dataset.size)
# print("boyutları:", dataset.shape)
# print("boyutları:", dataset.values.shape)
# print("---:", dataset.iloc)
# print("eleman var mı yok mu:", dataset.empty)
# print("elemanların tipi:", dataset.dtypes)

# object : string

# values = dataset.values
# print(values[0])
# print(values[0][2])
# print(values[0, 2])  # pythonda genelde bu kullanılır.
# print(values[0:2])
# print(values[:2])
# print(values[:])
# print(values[:,2]) #sadece maaşları yazdırmak için.
# print(values[:,2:])
# print(values[0::2]) #2şer atlayarak gidiyoruz. 0'dan başla - 2 atlayarak git.

# 4- Veriyi X ve Y olarak bölme

# print(dataset.iloc[0])
# print(dataset.iloc[0].values)
# print(type(dataset.iloc[0].values))

x = dataset.iloc[:, :-1].values  # veya [:,:3] şeklinde yazılabilir.
y = dataset.iloc[:, 3].values
# print(x)
# print(y)

# 5- Kayıp Değerleri Doldurma

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
# Kayıp değerler (missing values) = np.nan olarak gösterilmekte.
# "mean" stratejisi yani ortalamaları baz alarak doldur. Sadece sayısal veriler için kullanılır.
# np.nan default olarak geliyor, normalde eklemeye gerek yok.

# print(x[:, 1:])
imputer.fit(x[:, 1:])  # ülke isimlerini almıyoruz çünkü string ifadeler "mean" için uygun değil.
# fit: veriyi tanımlamak için kullanılır. oturtmak anlamına gelir.
x[:, 1:] = imputer.transform(x[:, 1:])
# print(x[:,1:]) #Ve görüldüğü gibi non değerleri mean ile ortalama alınarak bulundu.
print(x)
# 6- Etiket olan değerleri numaralandırma

# Veri setimize uygun matematiksel veri bulabilmek için etiket olan değerleri numaralandırıyoruz.

# LabelEncoder: 2 veya daha az sınıf sayılarında kullanılır.
# Etiketleri 0 ile sınıf_sayisi-1 aralığında numaralandırılır.
# Sonuç etiketimiz: No:0 Yes:1

# OneHotEncoder: 2'den daha fazla sınıf sayılarında kullanılır.
# Etiketleri ünik olarak ikili sayı sisteminde numaralandırılır.
# Ülke etiketimiz:
# Fransa : 0 0 1
# İspanya: 0 1 0
# Almanya: 1 0 0

# 6.1- Bağımsız değişkeni numaralandırma

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder  # bağımsız: onehotencoder bağımlı: labelencoder

ct = ColumnTransformer(transformers=[("encoder", OneHotEncoder(), [0])], remainder="passthrough")
# remainder : throughyani kalanları boş ver, geç. Bu ifadeyi yazmazsak encoding işlemi tamamlanmaz.

x = np.array(ct.fit_transform(x))
# print(x)

# 6.2- Bağımlı değişkeni numaralandırma

le = LabelEncoder()
y = le.fit_transform(y)
# print(y)

# 7- Veri Setini İkiye Bölme

from sklearn.model_selection import train_test_split  # train : öğren

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)  # random_state=1)
# print(x_train)

# 7- Özellikleri Ölçekleme

# Bütün özelliklerin aynı ölçekte işlem görmesini sağlıyor.
# Bazı özelliklerin diğer özellikleri domine etmesinden kaynaklı kullanılır.
# Bütün değerler aynı aralıkta olur.

# Standardisation / Standardizasyon
# x(std) = [x-ort(x)]/standart_sapma(x) #Her zaman çalışır ancak normal dağılımlarda önerilmez
#
# Normalisation / Normalizasyon
# x(norm) = [x-min(x)]/[max(x)-min(x)] #Normal dağılımlarda kullanılması önerilir.
#
# ÖNEMLİ NOT!
#
# Özellikleri ölçeklemeyi veri setini öğrenme ve test şeklinde ikiye böldükten sonra
# sadece ÖĞRENME VERİSİ'nde uygulamalıyız!

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

x_train[:, 3:] = scaler.fit_transform(x_train[:, 3:])
x_test[:, 3:] = scaler.transform(x_test[:, 3:])

print(x_train)
print(x_test)
