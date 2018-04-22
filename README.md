# 


## Install


### Clone project and download all requirements.

```
mkdir delikat-cake
cd delikat-cake
git clone git@github.com:perses76/delikat-cake.git
cd delikat-cake
virtualenv .env
source .env/bin/activate
pip install -r requirements.txt
```


### Setup project

1. Copy local_settings.py.def to local_settings.py and change path to DB. Be sure that DB exists in pointed folder.


## Run dev version

```
python manage.py runserver
```
