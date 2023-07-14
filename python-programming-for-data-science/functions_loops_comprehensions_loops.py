#################################################
# Fonksiyonlar, Koşullar, Döngüler, Comrehensions
#################################################
# - Fonksiyonlar (Functions)
# - Koşullar (Conditions)
# - Döngüler (Loops)
# - Comrehensions (Comprehensions)


##########################
# Fonksiyonlar (Functions)
##########################
# - Fonksiyonlar bir programda bir işi yürütmek için kullanılan bir yapıdır.
# - Belirli görevleri yerine getirmek için kullanılan kod parçalarıdır.

#########################
# Fonksiyon Okuryazarlığı
#########################

print("ilker")

print("ilker", "yılmaz", sep="___")


############################
# Fonksiyonların Tanımlanması
#############################

def calculate_age(year):
    return 2022 - year


print(calculate_age(2000))


# iki argüman alan fonksiyonların tanımlanması
def calculate_age_2(name, year):
    return f"{name} is {2022 - year} years old"


print(calculate_age_2("ilker", 2000))


############################
# Docstring (Documentation String)
#############################

# fonksiyonlarımıza herkesin anlayabileceği
# ortak bir dil ile bilgi notu ekleme yoludur.

def summer(arg1, arg2):
    """
    Sum of two numbers

    Args:
        arg1: int, float
        arg2: int, float

    Returns:
        int, float
    """
    return arg1 + arg2


print(help(summer))


######################################
# Fonksiyonların Statement/Body Bölümü
######################################

# def fonksiyon_adi(arg1, arg2):
#     statements (function body)


def say_hello(string):
    print("Hello")
    print("Hi")
    print(string)


say_hello("ilker")


def multiplication(arg1, arg2):
    c = arg1 * arg2
    print(c)


multiplication(2, 3)

# girilen değerleri bir liste içinde saklayacak fonksiyon

liste = []


def list_creator(arg1, arg2):
    for i in range(arg1, arg2):
        print(i)
        liste.append(i)
        print(liste)
    return liste


list_creator(1, 10)


###################################################################
# Ön Tanımlı Argümanlar/Parametreler (Default Arguments/Parameters)
###################################################################

def divide(arg1, arg2):
    return arg1 / arg2


print(divide(10, 2))


def divide1(arg1, arg2=1):
    return arg1 / arg2


print(divide1(10))
print(divide1(10, 3))


############################################
# Ne zaman fonksiyon Yazma ihtiyacımız olur?
############################################

# Don't Repeat Yourself (DRY)
# Kendini tekrar etme..

def calculate_age(varm, moisture, charge):
    print((varm + moisture) / charge)


calculate_age(10, 20, 30)


######################################################
# Return: Fonksiyon Çıktılarını Girdi Olarak Kullanmak
######################################################

def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)


# calculate(76,100,67) * 10


def calculate(varm, moisture, charge):
    return (varm + moisture) / charge


a = calculate(76, 100, 67) * 10
print(a)


def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture) / charge

    return varm, moisture, charge, output


type(calculate(76, 100, 67))
varm, moisture, charge, output = calculate(76, 100, 67)

print(varm, moisture, charge, output)


#########################################
# Fonksiyon İçerisinden Fonksiyon Çağırma
#########################################

def calculate(varm, moisture, charge):
    return int((varm + moisture) / charge)


calculate(76, 100, 67) * 10


def standardization(a, p):
    return a * 10 / 100 * p * p


standardization(10, 100)


def all_calculation(varm, moisture, charge, p):
    a = calculate(varm, moisture, charge)
    b = standardization(a, p)
    print(b * 10)


all_calculation(76, 100, 67, 100)

#######################################################
# Lokal & Global Değişkenler (Local & Global Variables)
#######################################################

list_store = [1, 2]


def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)


add_element(10, 20)

#######################
# Koşullar (Conditions)
#######################

# True-False'u Hatırlayalım.
1 == 1
2 == 2

# if
if 1 == 1:
    print("1 == 1")

# elif
if 1 == 2:
    print("1 == 2")
elif 1 == 1:
    print("1 == 1")

# else
if 1 == 2:
    print("1 == 2")
else:
    print("1 != 2")

# if-else-if-else
if 1 == 1:
    print("1 == 1")
elif 1 == 2:
    print("1 == 2")
elif 1 == 3:
    print("1 == 3")
else:
    print("1 != 1, 2 veya 3")


def number_check(number):
    if number == 1:
        print("1")
    elif number == 2:
        print("2")
    elif number == 3:
        print("3")
    else:
        print("1, 2 veya 3 değil")


print(number_check(1))

##################
# Döngüler (LOOPS)
##################

# for loop
students = ["ilker", "fırat", "mehmet", "ahmet", "resul", "furkan", "gaffar"]
for student in students:
    print(student)

for student in students:
    print(student.upper())

salaries = [1000, 2000, 3000, 4000, 5000]
for salary in salaries:
    print(salary)

for salary in salaries:
    print((salary * 20) / 100 + salary)


def new_salary(salary, rate):
    return int((salary * rate) / 100 + salary)


print(new_salary(1000, 20))

for salary in salaries:
    print(new_salary(salary, 20))

for salary in salaries:
    if salary >= 3000:
        print(new_salary(salary, 10))
    else:
        print(new_salary(salary, 20))


###########################
# Uygulama - Mülakat Sorusu
###########################

# Amaç: Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz

# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

# aslında anlatılmak istenen şey:
# tek indekstekileri küçük harflerle değiştir
# çift indekstekileri büyük harflerle değiştir

def alternating(string):
    new_string = ""
    # girilen string'in index'lerinde gez.
    for i in range(len(string)):  # string'in uzunluğu kadar döngü oluştur
        if i % 2 == 0:  # eğer indeksteki sayı çift ise
            new_string += string[i].upper()  # çift indeksteki sayıyı büyük harfe çevir
        else:
            new_string += string[i].lower()  # tek indeksteki sayıyı küçük harfe çevir
    return new_string


mulakatcevabi = alternating("hi my name is john and i am learning python")

print(mulakatcevabi)

##########################
# break & continue & while
##########################

salaries = [1000, 2000, 3000, 4000, 5000]

# break: döngüden çık
# continue: döngüden sonraki adımı atla

for salary in salaries:
    if salary >= 3000:
        break
    print(salary)

for salary in salaries:
    if salary == 3000:
        continue
    print(salary)

# while: döngü
number = 1
while number <= 10:
    print(number)
    number += 1

##################################################
# Enumerate: Otomatik Counter/Indexer ile for loop
##################################################

students = ["ilker", "fırat", "mehmet", "ahmet", "resul", "furkan", "gaffar"]

for student in students:
    print(student)

for index, student in enumerate(students):
    print(index, ":", student)

# çift indexteki öğrencileri bir listeye, tek indexteki öğrencileri başka bir listeye alalım

A = []
B = []

for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)

print(A)
print(B)

###########################
# Uygulama - Mülakat Sorusu
###########################
# divide_students fonksiyonu yazınız
# çift indexte yer alan öğrencileri bir listeye alınız
# tek indexte yer alan öğrencileri başka bir listeye alınız
# fakat bu iki liste tek bir liste olarak return olsun

tek_liste = []
cift_liste = []


def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    return groups


print(divide_students(students))


###################################################
# alternating fonksiyonunun enumerate ile yazılması
###################################################

def alternating_with_enumerate(string):
    new_string = ""
    for index, letter in enumerate(string):
        if index % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    return new_string


print(alternating_with_enumerate("hi my name is john and i am learning python"))

#####
# Zip
#####

students = ["ilker", "fırat", "mehmet", "ahmet", "resul", "furkan", "gaffar"]
departments = ["computer science", "math", "physics", "chemistry", "biology", "history", "geography"]
ages = [20, 21, 22, 23, 24, 25, 26]

a = list(zip(students, departments, ages))
print(a)


#############################
# lambda, map, filter, reduce
#############################

def summery(a, b):
    return a + b


summer(1, 2) * 9

new_sum = lambda a, b: a + b

print(new_sum(1, 2))

# map
salaries = [1000, 2000, 3000, 4000, 5000]


def new_salary(salary):
    return int((salary * 20) / 100 + salary)


print(new_salary(1000))

for salary in salaries:
    print(new_salary(salary))

print(list(map(new_salary, salaries)))

print(list(map(lambda x: x * 30 / 100 + x, salaries)))

print(list(map(lambda x: x ** 2, salaries)))

# filter

list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(filter(lambda x: x % 2 == 0, list_store)))

# reduce
from functools import reduce

list_store = [1, 2, 3, 4]
reduce(lambda a, b: a + b, list_store)

###############
# Comprehension
###############

####################
# List Comprehension
####################

salaries = [1000, 2000, 3000, 4000, 5000]


def new_salary(salary):
    return int((salary * 20) / 100 + salary)


for salary in salaries:
    print(new_salary(salary))

null_list = []
for salary in salaries:
    null_list.append(new_salary(salary))

print(null_list)

for salary in salaries:
    if salary >= 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary * 2))

# list comprehension ile:
[new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries]

# örnek: salaries listesindeki her bir maaşı 2 ile çarmap istediğimizi düşünelim

[salary * 2 for salary in salaries]

[salary * 2 for salary in salaries if salary < 3000]

[salary * 2 if salary < 3000 else salary * 0 for salary in salaries]

[new_salary(salary * 2) if salary < 3000 else new_salary(salary * 0) for salary in salaries]

students = ["ahmet", "resul", "furkan", "gaffar"]

students_no = ["ilker", "fırat", "resul", ]

yeni_liste = [student.lower() if student in students_no else student.upper() for student in students]

print(yeni_liste)

[student.upper() if student not in students_no else student.lower() for student in students]

####################
# Dict Comprehension
####################

dictionary = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4, }

dictionary.keys()
dictionary.values()
dictionary.items()

{k: v ** 2 for (k, v) in dictionary.items()}

{k.upper(): v for (k, v) in dictionary.items()}

{k.upper(): v ** 2 for (k, v) in dictionary.items()}

###########################
# Uygulama - Mülakat Sorusu
###########################

# Amaç: çift sayıların karesi alınarak bir sözlüğe eklenmek istenmektedir
# Key'ler orijinal değerler, value'ler ise karesi olmalı.

numbers = range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2

print(new_dict)

# diğer çözümü:
{n: n ** 2 for n in numbers if n % 2 == 0}

#########################################
# List & Dict Comprehension - Uygulamalar
#########################################

####################################################
# Bir Veri Setindeki Değişken İsimlerini Değiştirmek
####################################################

# before:
# ['total', 'speeding', 'alcohol', 'not__previous', 'ins_premium', 'ins_losses', 'abbrev']

# after:
# ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT__PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']


import seaborn as sns

df = sns.load_dataset("car_crashes")
print(df.columns)

df.columns = [col.upper() for col in df.columns]
print(df.columns)


####################################################
# İsminde "INS" olan değişkenlerin başına FLAG diğerlerine NO_FLAG eklemek istiyoruz.
####################################################

# before:
# ['total',
# 'speeding',
# 'alcohol',
# 'not_distracted',
# 'no_previous',
# 'ins_premium',
# 'ins_losses',
# 'abbrev'],

# after:
# ['NO_FLAG_TOTAL',
# 'NO_FLAG_SPEEDING',
# 'NO_FLAG_ALCOHOL',
# 'NO_FLAG_NOT_DISTRACTED',
# 'NO_FLAG_NO_PREVIOUS',
# 'FLAG_INS_PREMIUM',
# 'FLAG_INS_LOSSES',
# 'NO_FLAG_ABBREV'],

INS_iceren_liste = [col for col in df.columns if "INS" in col]

flag_liste= ["FLAG_" + col for col in df.columns if "INS" in col]

flag_ve_no_flag_liste = ["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

print(INS_iceren_liste)
print(flag_liste)
print(flag_ve_no_flag_liste)


####################################################
# Amaç key'i string, value'su aşağıdaki gibi bir liste olan sözlük oluşturmak
# sadece sayısal değişkenler için yapmak istiyoruz
####################################################

# Output:
#  {'total': ['mean','min','max','var'],
#     'speeding': ['mean','min','max','var'],
#     'alcohol': ['mean','min','max','var'],
#   'not_distracted': ['mean','min','max','var'],
#     'not_previous': ['mean','min','max','var'],
#     'ins_premium': ['mean','min','max','var'],
#     'ins_losses': ['mean','min','max','var'],
#   }


import seaborn as sns

df = sns.load_dataset("car_crashes")
print(df.columns)

num_cols = [col for col in df.columns if df[col].dtype != "O"]

print(num_cols)

soz = {}

agg_list = ['mean', 'min', 'max', 'sum']

for col in num_cols:
    soz[col] = agg_list

print(soz)

# kısa yol:
soz2 = {col: ['mean', 'min', 'max', 'sum'] for col in num_cols}
print(soz2)

df[num_cols].head()

df[num_cols].agg(soz2)

