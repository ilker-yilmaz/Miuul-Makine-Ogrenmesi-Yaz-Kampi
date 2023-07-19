###########################################################################
# Virtual Environment (Sanal Ortam) ve (Package Management) Paket Yönetimi
###########################################################################

# Sanal Ortamların Listelenmesi
# conda env list

# Sanal Ortam Oluşturma
# conda create -n <isim>

# Sanal Ortamı Aktif Etme
# conda activate <isim>

# Yüklü Paketlerin Listelenmesi
# conda list

# Paket Yükleme
# conda install <paket>

# Aynı Anda Birden Fazla Paket Yükleme
# conda install <paket1> <paket2> <paket3>

# Paket Silme
# conda remove <package_name>

# Belirli Bir Versiyona Göre Paket Yükleme
# conda install <package_name>=<version>

# Paket Yükseltme
# conda upgrade <package_name>

# Tüm Paketlerin Yükseltmesi
# conda upgrade -all

# pip: pypi (python package index) paket yönetim aracı

# Paket Yükleme
# pip install <paket>

# Paket Yükleme Versiyona Göre
# pip install <paket>==<versiyon>

# Environment'in Export Edilmesi
# conda env export > environment.yaml

# Environment'in Export Edilmesi
# pip freeze > requirements.txt

# Elimizde Var Olan Bir Sanal Ortam Bilgisini Bilgisayarımıza Kurma İşlemi
# conda env create -f <isim-(environment.yaml)>
# pip install -r <requirements.txt>

# Sanal Ortam Silme
# conda env remove -n <isim>

# Sanal Ortamı Deaktif Etme
# conda deactivate

# Sanal Ortamı Güncelleme
# conda update -n <isim> --all
