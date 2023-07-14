########
# Pandas
########

# Pandas Series
# Veri Okuma (Reading Data)
# Veriye Hızlı Bakış (Quick Look at Data)
# Pandas'ta Seçim İşlemleri (Selection in Pandas)
# Toplulaştırma ve Gruplama (Aggregation and Grouping)
# Apply ve Lambda
# Birleştirme (Join) İşlemleri

###############
# Pandas Series
###############

# pandas serileri tek boyutlu ve index bilgisi barındıran bir veri tipidir.
# pandas dataframe ise çok boyutlu ve index bilgisi barındıran bir veri tipidir.

import pandas as pd # pandas kütüphanesini pd olarak import ettik.

# pandas serisi oluşturmak için pd.Series() fonksiyonunu kullanırız.
pd_series = pd.Series([1, 2, 3, 4, 5]) # bu liste üzerinden bir pandas serisi oluşturulacak.
print("pd_series:\n",pd_series)
print("type of pd_series: ",type(pd_series))
print("pd_series.index: ",pd_series.index) # pandas serisinin index bilgisi.
print("pd_series.values: ",pd_series.values) # pandas serisinin değer bilgisi. bu bir numpy array'idir.
print("pd_series.dtype: ",pd_series.dtype) # pandas serisinin veri tipi.
print("pd_series.ndim: ",pd_series.ndim) # pandas serisinin boyut sayısı. bu seri tek boyutludur ve index bilgisi vardır.
print("pd_series.head: ",pd_series.head(3)) # pandas serisinin ilk 3 elemanını gösterir.
print("pd_series.tail: ",pd_series.tail(3)) # pandas serisinin son 3 elemanını gösterir.


# pandas serisi oluştururken index bilgisi de verilebilir.
pd_index_series = pd.Series([1, 2, 3, 4, 5], index=["a", "b", "c", "d", "e"])
#print("pd_index_series:\n",pd_index_series)
#print("type of pd_index_series: ",type(pd_index_series))


###########################
# Veri Okuma (Reading Data)
###########################

import pandas as pd

# csv dosyası okuma
df = pd.read_csv("../datasets/Advertising.csv")
print("df:\n",df)
print("df.head():\n",df.head()) # ilk 5 satırı gösterir.

#########################################
# Veriye Hızlı Bakış (Quick Look at Data)
#########################################

import pandas as pd
import seaborn as sns

titanic = sns.load_dataset("titanic") # seaborn kütüphanesindeki titanic veri setini yükler.
print("titanic.head():\n",titanic.head()) # ilk 5 satırı gösterir.
print("titanic.tail():\n",titanic.tail()) # son 5 satırı gösterir.
print("titanic.shape: ",titanic.shape) # veri setinin boyut bilgisi.
print("titanic.info:\n",titanic.info()) # veri setinin bilgileri.
print("titanic.columns: ",titanic.columns) # veri setinin sütun bilgileri.
print("titanic.index: ",titanic.index) # veri setinin index bilgileri.
print("titanic.describe():\n",titanic.describe().T) # veri setinin istatistiksel bilgileri. sonuna da .T ekleyerek transpoze edebiliriz. bu sayede daha kolay okunabilir hale gelir.
print("titanic.isnull().values.any(): ",titanic.isnull().values.any()) # veri setinde null değer var mı?
print("titanic.isnull().sum():\n",titanic.isnull().sum()) # veri setinde değişkenlerdeki eksiklik durumu incelemesi
print("titanic['embark_town'].value_counts()",titanic["embark_town"].value_counts()) # veri setindeki embark_town değişkenindeki kategorik değerlerin sayıları.


#################################################
# Pandas'ta Seçim İşlemleri (Selection in Pandas)
#################################################
import pandas as pd
import seaborn as sns
df = sns.load_dataset("titanic")
print("df.head():\n",df.head())

print(df.index)  # index bilgisi
print(df[0:13])  # 0'dan 13'e kadar olan satırları gösterir.
df.drop(0,axis=0).head()  # 0. satırı siler. axis=0 satırı gösterir. axis=1 ise sütunu gösterir.
print(df)

delete_indexes = [1,3,5,7]
df.drop(delete_indexes,axis=0).head(10) # 1,3,5,7. satırları siler.

# pandas'ta seçim işlemleri için 2 yöntem vardır.
# 1. loc
# 2. iloc

# loc
print("df.loc[0]:\n",df.loc[0]) # 0. index'in tüm değişkenlerini gösterir.
print("df.loc[0, 'survived']:\n",df.loc[0, "survived"]) # 0. index'in survived değişkenini gösterir.
print("df.loc[0:3, 'survived']:\n",df.loc[0:3, "survived"]) # 0-3. index'in survived değişkenini gösterir.
print("df.loc[0:3, 'survived':'age']:\n",df.loc[0:3, "survived":"age"]) # 0-3. index'in survived ve age değişkenlerini gösterir.
print("df.loc[:, 'survived']:\n",df.loc[:, "survived"]) # tüm indexlerin survived değişkenini gösterir.
print("df.loc[:, 'survived':'age']:\n",df.loc[:, "survived":"age"]) # tüm indexlerin survived ve age değişkenlerini gösterir.
print("df.loc[0:3, ['survived', 'age']]:\n",df.loc[0:3, ["survived", "age"]]) # 0-3. index'in survived ve age değişkenlerini gösterir.
print("df.loc[0:3, 'survived':]:\n",df.loc[0:3, "survived":]) # 0-3. index'in survived ve sonrasındaki tüm değişkenleri gösterir.
print("df.loc[0:3, :'age']:\n",df.loc[0:3, :"age"]) # 0-3. index'in age değişkenine kadar olan tüm değişkenleri gösterir.
print("df.loc[0:3, 'survived'::2]:\n",df.loc[0:3, "survived"::2]) # 0-3. index'in survived değişkeninden başlayarak 2'şer 2'şer atlayarak tüm değişkenleri gösterir.
print("df.loc[0:3, 'survived'::-1]:\n",df.loc[0:3, "survived"::-1]) # 0-3. index'in survived değişkeninden başlayarak sondan başlayarak tüm değişkenleri gösterir.
print("df.loc[0:3, 'survived'::-2]:\n",df.loc[0:3, "survived"::-2]) # 0-3. index'in survived değişkeninden başlayarak sondan başlayarak 2'şer 2'şer atlayarak tüm değişkenleri gösterir.

# iloc
print("df.iloc[0]:\n",df.iloc[0]) # 0. index'in tüm değişkenlerini gösterir.
print("df.iloc[0, 1]:\n",df.iloc[0, 1]) # 0. index'in 1. değişkenini gösterir.
print("df.iloc[0:3, 1]:\n",df.iloc[0:3, 1]) # 0-3. index'in 1. değişkenini gösterir.
print("df.iloc[0:3, 1:4]:\n",df.iloc[0:3, 1:4]) # 0-3. index'in 1-4. değişkenlerini gösterir.
print("df.iloc[:, 1]:\n",df.iloc[:, 1]) # tüm indexlerin 1. değişkenini gösterir.
print("df.iloc[:, 1:4]:\n",df.iloc[:, 1:4]) # tüm indexlerin 1-4. değişkenlerini gösterir.
print("df.iloc[0:3, [1, 4]]:\n",df.iloc[0:3, [1, 4]]) # 0-3. index'in 1 ve 4. değişkenlerini gösterir.
print("df.iloc[0:3, 1:]:\n",df.iloc[0:3, 1:]) # 0-3. index'in 1. değişkeninden başlayarak tüm değişkenleri gösterir.
print("df.iloc[0:3, :4]:\n",df.iloc[0:3, :4]) # 0-3. index'in 4. değişkenine kadar olan tüm değişkenleri gösterir.
print("df.iloc[0:3, 1::2]:\n",df.iloc[0:3, 1::2]) # 0-3. index'in 1. değişkeninden başlayarak 2'şer 2'şer atlayarak tüm değişkenleri gösterir.
