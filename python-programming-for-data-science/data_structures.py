#########################################
# Data Structures
#########################################
# - Veri Yapılarına Giriş ve Hızlı Özet
# - Sayılar (Numbers): int, float, complex
# - Karakter Dizileri (Strings): str
# - List, Dictionary, Tuple, Set, Boolean (TRUE-FALSE): bool
# - list: liste
# - dictionary: sözlük
# - tuple: demet
# - set: küme

#########################################
# Veri Yapılarına Giriş ve Hızlı Özet
#########################################

# sayılar (Numbers): int, float, complex
y = 46
print(type(y))

#sayılar: float
x=10.3
type(x)

#sayılar: complex
x=2j+1
type(x)

#string
a="Hello ai era"
type(a)

#boolean
True
False
type(True)
5==4
3==2
1==1
type(3==2)

#Liste (list)

x=["btc", "eth", "xrp"]
type(x)

#sözlük (dictionary)
x={"name":"Peter", "Age":36}
type(x)

# Tuple (demet)
x=("python", "ml", "ds")
type(x)

# Set (küme)
x={"python", "ml", "ds"}
type(x)

#Not: Liste, tuple, set ve dictionary veri yapıları aynı zamanda Python Collections (Arrays) olarak geçmektedir.


#########################################
# Sayılar (Numbers): int, float, complex
#########################################

a=5
b=10.5

a*3
a/7


#########################################
# Tipleri değiştirmek
#########################################

int(b)
float(a)


#########################################
# karakter dizileri (Strings)
#########################################

print("Hello ai era")

name="Peter"
print(name)

long_str="""    Hello ai era    """
print(long_str)

name[0]

#########################################
# karakter dizilerinde slice işlemi
#########################################

name[0:3]
long_str[0:3]

#########################################
# string içerisinde karakter sorgulama
#########################################


"veri" in long_str
"Veri" in long_str


#########################################
# String (karakter dizisi) metodları
#########################################

dir(long_str)

#########################################
# len() metodu
#########################################

name = "ilker"
print(type(name))
print(type(len))
print(len(name))

#########################################
# upper() & lower(): küçük-büyük dönüşümleri
#########################################

print("ilker".upper())
print("ilker".lower())


#########################################
# replace: karakter değiştirir
#########################################

merhaba = "merhaba ilker"
print(merhaba.replace("a", "b"))

#########################################
# split: karakter dizisini bölüyor
#########################################

print("Hello ai era".split())

#########################################
# strip: karakter dizisini kırpar
#########################################

print("ofofofo".strip("o"))


#########################################
# capitalize: ilk karakteri büyük yapar
#########################################
print("deniz".capitalize())


#########################################
# Liste (list)
#########################################

# Değiştirilebilir (mutable)
# Sıralıdır, Index işlemleri yapılabilir.
# Kapsayıcıdır.

notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
print(notes)
print(type(notes))

surnames = ["Kılıç", "derin", "yılmaz", "kaya"]
print(surnames)

not_nam = [1,2,3,"a","b",True,[1,2,3]]

not_nam[0] = "C"
print(not_nam[0])
print(not_nam[-1])
print(not_nam[-2])
print(not_nam[6][1])

print("listede 0'dan 3'e kadar olan elemanlar: ", not_nam[0:3])

#########################################
# Liste Metodları (list methods)
#########################################

print(dir(notes))

#########################################
# append: listeye eleman ekler
#########################################

notes.append("D#")
print(notes)

#########################################
# pop : index'e göre liste elemanını siler
#########################################

notes.pop(0)
print(notes)

#########################################
# insert: belirli bir index'e göre listeye eleman ekler
#########################################

notes.insert(3, 10)
print(notes)


#########################################
# Sözlük ( dictionary )
#########################################

# sözlükler key value şeklindedir.
# key'leri unique olmalıdır.
# value'leri değiştirilebilir.
# değiştirilebilirdir
# sırasızdır.
# kapsayıcıdır.

#key-value
dictionary = {"name":"ilker",
              "age":21,
              "city":"İstanbul",
              "country":"Türkiye"}

print(dictionary)

print(dictionary["name"])

#########################################
# key sorgulama
#########################################

print("name" in dictionary)

#########################################
# Key'e Göre Value'ya Erişmek
#########################################

print(dictionary.get("name"), dictionary.get("age"))

#########################################
# Value Değiştirme
#########################################

dictionary["age"] = 22
print(dictionary["age"])

#########################################
# tüm key'lere erişmek
#########################################

print(dictionary.keys())

#########################################
# tüm value'lara erişmek
#########################################

print(dictionary.values())

#########################################
# tüm çiftleri tuple halinde listeye çevirme
#########################################

print(dictionary.items())

#########################################
# key-value değerini güncelleme
#########################################

dictionary.update({"age":23})
print(dictionary)

dictionary.update({"age":24, "city":"Ankara"})
print(dictionary)

dictionary.update({"yeniKey":"yeniValue"})
print(dictionary)

#########################################
# Demet (Tuple)
#########################################

# Tuple, listelerin değişime kapalı kardeşidir, biraz daha aksidir :)
# Değiştirilemez,
# sıralıdır (yani bu veri yapısının elemanlarına erişilebiliyor anlamına gelir),
# kapsayıcıdır (farklı veri yapılarını saklayabilir anlamına gelmektedir.)

my_tuple = ("ilker", 1, "yılmaz", 5.5)
print(my_tuple)

print(my_tuple[0])
print(my_tuple[0:3])    # 0'dan 3'e kadar olan elemanlar
#my_tuple[0] = 100       # tuple'ın elemanlarını değiştiremezsiniz...

#tuple güncelleme yöntemi

my_tuple_list = list(my_tuple) # tuple'ı listeye çevirme
my_tuple_list[0] = 100 # liste elemanını değiştirme
my_tuple = tuple(my_tuple_list) # listeyi tuple'a çevirme

print(my_tuple)

#########################################
# Set
#########################################

# - Değiştirilebilir.
# - Sırasız + Eşsizdir.
# - Kapsayıcıdır.


#########################################
# difference() : farklılıkları bulma
#########################################

set1=set([1,2,3,4,5,6,7,8,9,10])
set2=set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

#set1'de olup set2'de olmayanları bulma
print(set1.difference(set2))

#set2'de olup set1'de olmayanları bulma
print(set2.difference(set1))

#########################################
# symetric_difference() : iki kümede de birbirlerine göre olmayanlar
#########################################

print(set1.symmetric_difference(set2))
print(set2.symmetric_difference(set1))

#########################################
# intersection() : (iki kümenin kesişimi)
#########################################

print(set1.intersection(set2))
print(set2.intersection(set1))

#########################################
# union() : (iki kümenin birleşimi)
#########################################

print(set1.union(set2))
print(set2.union(set1))

#########################################
# isdisjoint() : (iki kümenin kesişimi boş mu?)
#########################################

print(set1.isdisjoint(set2))
print(set2.isdisjoint(set1))

#########################################
# issubset() : (bir küme diğer kümenin alt kümesi mi?)
#########################################

print(set1.issubset(set2))
print(set2.issubset(set1))

#########################################
# issuperset() : (bir küme diğer kümeyi kapsıyor mu?)
#########################################

print(set1.issuperset(set2))
print(set2.issuperset(set1))
