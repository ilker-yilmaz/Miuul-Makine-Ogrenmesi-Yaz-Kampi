############################
# Data Analysis with Python
############################

# - NumPy
# - Pandas
# - Veri Görselleştirme: Matplotlib & Seaborn
# - Gelişmiş Fonksiyonlar Keşifçi Veri Analizi (Advanced Functions for Exploratory Data Analysis)

###########
# NUMPY
###########

# Neden NumPy? (Why NumPy?)
# - NumPy, Python'da veri analizi yapmak için kullanılan en önemli kütüphanelerden biridir.
# NumPy Array'i Oluşturmak (Creating NumPy Arrays)
# NumPy Array Özelliklerri (Attributes of NumPy Array)
# Yeniden Şekillendirme (Reshaping)
# Index Seçimi (Index Selection)
# Slicing
# Fancy Index
# Numpy'da Koşullu İşlemler (Conditions on Numpy)
# Matematiksel İşlemler (Mathematical Operations)

import numpy as np

############################
# Neden NumPy? (Why NumPy?)
############################
# listelere göre daha hızlıdır. çünkü sabit tipte veri tutar. yani verimli veri saklar. bundan dolayı hızlıdır
# yüksek seviyeden işlemler yapmayı sağlar. yani daha az kod yazmamızı sağlar.

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
print(a * b)

##################################################
# NumPy Array'i Oluşturmak (Creating NumPy Arrays)
##################################################

import numpy as np

np.array([1, 2, 3, 4, 5])  # bu liste üzerinden bir numpy array'i oluşturulacak.
print(type(np.array([1, 2, 3, 4, 5])))

zeros_array = np.zeros(10,
                       dtype=int)  # 10 elemanlı bir array oluşturur. tüm elemanları 0'dır. dtype = int ile tüm elemanların tipini int olarak belirledik.
randint_array = np.random.randint(0, 10,
                                  size=10)  # 0 ile 10 arasında 10 elemanlı bir array oluşturur. random sayılar üretir.
normal_array = np.random.normal(10, 4, (
3, 4))  # 3x4'lük bir array oluşturur. ortalama 10, standart sapma 4 olan normal dağılımdan sayılar üretir.

print("zeros array: ", zeros_array)
print("randint array: ", randint_array)
print("normal array:\n", normal_array)

######################################################
# NumPy Array Özelliklerri (Attributes of NumPy Array)
######################################################
import numpy as np

# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

a = np.random.randint(10, size=5)
print("a array: ", a)
print("a.ndim:", a.ndim)  # tek boyutlu bir array olduğu için 1 döner.
print("a.shape:", a.shape)  # tek boyutlu olduğu için (5,) döner.
print("a.size:", a.size)  # toplam eleman sayısı olarak 5 döner.
print("a.dtype:", a.dtype)  # array veri tipi olarak int32 döner.

###################################
# Yeniden Şekillendirme (Reshaping)
###################################
import numpy as np

b = np.random.randint(1, 10, size=9)
print("b array: ", b)
ar = b.reshape((3,
                3))  # 3x3'lük bir array oluşturur. 9 elemanlı olduğu için 3x3'lük bir array oluşturulamaz. bu yüzden hata verir.
print("ar array:\n", ar)

################################
# Index Seçimi (Index Selection)
################################
import numpy as np

c = np.random.randint(10, size=10)
print("c array: ", c)
print("c[0]: ", c[0])  # 0. index
print("c[4]: ", c[4])  # 4. index
print("c[-1]: ", c[-1])  # sondan 1. index
print("c[-2]: ", c[-2])  # sondan 2. index
print("c[0:3]: ", c[0:3])  # 0'dan 3'e kadar olan indexleri seçer. 3 dahil değil.
print("c[:3]: ", c[:3])  # 0'dan 3'e kadar olan indexleri seçer. 3 dahil değil.

m = np.random.randint(10, size=(3, 5))
print("m array:\n", m)
print("m[0,0]: ", m[0, 0])  # 0. satır, 0. sütun
print("m[1,4]: ", m[1, 4])  # 1. satır, 4. sütun
print("m[1,4]: ", m[1, -1])  # 1. satır, sondan 1. sütun
print("m[:,0]: ", m[:, 0])  # tüm satırlar, 0. sütun
print("m[0,:]: ", m[0, :])  # 0. satır, tüm sütunlar
print("m[0:2,0:3]: ", m[0:2, 0:3])  # 0'dan 2'ye kadar olan satırlar, 0'dan 3'e kadar olan sütunlar
m[0, 0] = 99  # 0. satır, 0. sütun değerini 99 yapar.
print("m array [0,0]: ", m[0, 0])

# numpy sabit tip array'dir. yani bir array oluşturulduğunda tüm elemanları aynı tip olmalıdır.
# m[2,3] = 2,9
print("m array [2,3]: ",
      m[2, 3])  # hata verir. çünkü 2. satır, 3. sütun değeri 2,9 olamaz. çünkü array sabit tip bir array'dir.

############################################
# Fancy Index Seçimi (Fancy Index Selection)
############################################
import numpy as np

v = np.arange(0, 30, 3)  # 0'dan 30'a kadar 3'er 3'er artan bir array oluşturur.
print("v array: ", v)
v[1]
v[3]
v[5]
print("v[[1,3,5]]: ", v[[1, 3, 5]])  # 1,3,5 indexlerini seçer.

catch = [1, 3, 5]
print("v catch: ", v[catch])

#################################################
# Numpy'da Koşullu İşlemler (Conditions on Numpy)
#################################################
import numpy as np

z = np.array([1, 2, 3, 4, 5])
print("z array: ", z)

####################
# klasik döngü ile
####################
new_z = []
for i in z:
    if i < 3:
        new_z.append(i)

print("new_z array: ", new_z)

###########
# numpy ile
###########
print("z<3: ", z < 3)  # z array'inin her bir elemanı 3'ten küçük mü diye kontrol eder. true false döner.
print("z[z<3]: ", z[z < 3])  # z array'inin her bir elemanı 3'ten küçük mü diye kontrol eder. true olanları döner.
print("z[z>3]: ", z[z > 3])  # z array'inin her bir elemanı 3'ten büyük mü diye kontrol eder. true olanları döner.
print("z[z!=3]: ", z[z != 3])  # z array'inin her bir elemanı 3'e eşit değil mi diye kontrol eder. true olanları döner.
print("z[z<=3]: ",
      z[z <= 3])  # z array'inin her bir elemanı 3'ten küçük veya eşit mi diye kontrol eder. true olanları döner.
print("z[z>=3]: ",
      z[z >= 3])  # z array'inin her bir elemanı 3'ten büyük veya eşit mi diye kontrol eder. true olanları döner.

###################################################################
# Numpy'da Matematiksel İşlemler (Mathematical Operations on Numpy)
###################################################################
import numpy as np

d = np.array([1, 2, 3, 4, 5])
print("d array: ", d)
print("d+5: ", d + 5)  # d array'inin her bir elemanına 5 ekler.
print("d-5: ", d - 5)  # d array'inin her bir elemanından 5 çıkarır.
print("d*5: ", d * 5)  # d array'inin her bir elemanını 5 ile çarpar.
print("d/5: ", d / 5)  # d array'inin her bir elemanını 5'e bölür.
print("d//5: ", d // 5)  # d array'inin her bir elemanını 5'e bölüp sonucun tam kısmını alır.
print("d**5: ", d ** 5)  # d array'inin her bir elemanını 5. kuvvetini alır.
print("d%5: ", d % 5)  # d array'inin her bir elemanını 5'e bölüp kalanı alır.

print("np.subtract(d,5): ", np.subtract(d, 5))  # d array'inin her bir elemanından 5 çıkarır.
print("np.add(d,5): ", np.add(d, 5))  # d array'inin her bir elemanına 5 ekler.
print("np.multiply(d,5): ", np.multiply(d, 5))  # d array'inin her bir elemanını 5 ile çarpar.
print("np.divide(d,5): ", np.divide(d, 5))  # d array'inin her bir elemanını 5'e böler.
print("np.floor_divide(d,5): ", np.floor_divide(d, 5))  # d array'inin her bir elemanını 5'e bölüp sonucun tam kısmını alır.
print("np.power(d,5): ", np.power(d, 5))  # d array'inin her bir elemanını 5. kuvvetini alır.
print("np.mod(d,5): ", np.mod(d, 5))  # d array'inin her bir elemanını 5'e bölüp kalanı alır.

print("np.add(d,1)", np.add(d, 1))  # d array'inin her bir elemanına 1 ekler.
print("np.min(d)", np.min(d))  # d array'inin en küçük elemanını döner.
print("np.max(d)", np.max(d))  # d array'inin en büyük elemanını döner.
print("np.mean(d)", np.mean(d))  # d array'inin ortalamasını döner.
print("np.median(d)", np.median(d))  # d array'inin medyanını döner.
print("np.std(d)", np.std(d))  # d array'inin standart sapmasını döner.
print("np.var(d)", np.var(d))  # d array'inin varyansını döner.

###########################################
# NumPy ile İki Bilinmeyenli Denklem Çözümü
###########################################
import numpy as np

# 5*x0 + x1 = 12
# x0 + 3*x1 = 10

a = np.array([[5, 1], [1, 3]]) # a matrisi
b = np.array([12, 10]) # b matrisi

x = np.linalg.solve(a, b)
print("x: ", x)

# Neden NumPy?
# Verimli veri sakladığı için hızlıdır
# Sabit tipte veri sakladığı için hızlı çalışır

