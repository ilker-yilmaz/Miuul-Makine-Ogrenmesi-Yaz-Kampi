###########################################
# Sayılar (Numbers) vec Karakter Dizileri (String)
###########################################
# Atamalar ve Değişkenler
###########################################

#Virtual environment (sanal ortam) nedir?
#izole çalışma ortamları oluşturmak için kullanılan araçlardır.
#farklı çalışmalar için oluşabilecek farklı kütüphane ve versiyon ihtiyaçlarını çalışmalar birbirini etkilemeyecek şekilde oluşturma imkanı sağlar.

#sanal ortamların listelenmesi:
#pip list
#conda env list

#sanal ortam oluşturma:
#conda create -n <isim>

#sanal ortamı aktif etme:
#conda activate <isim>

#yüklü paketlerin listelenmesi:
#conda list

#paket yükleme:
#conda install <paket>

#aynı anda birden fazla paket yükleme:
#conda install <paket1> <paket2> <paket3>

#paket silme:
#conda remove <package_name>

#belirli bir versiyona göre paket yükleme:
#conda install <package_name>=<version>

#paket yükseltme:
#conda upgrade <package_name>

#tüm paketlerin yükseltmesi:
#conda upgrade -all

#pip: pypi (python package index) paket yönetim aracı

#paket yükleme:
#pip install <paket>

#paket yükleme versiyona göre:
#pip install <paket>==<versiyon>

#environment'in export edilmesi:
#conda env export > environment.yaml

#environment'in export edilmesi:
#pip freeze > requirements.txt

#elimizde var olan bir sanal ortam bilgisini bilgisayarımıza kurma işlemi
#conda env create -f <isim-(environment.yaml)>
#pip install -r <requirements.txt>


