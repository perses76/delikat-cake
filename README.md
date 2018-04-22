# Delikat-cake site (www.delikat-cake.com)


## Project structure
    delikat-cake/ - root folder
        db/
            delikat.sqlite - project DB
        media/ - folder for project media (on host: /home/velessoft/webapps/static/delikat/)
        .env/ - virtual environment folder
        delikat-cake/
            myproject/ - Django project
                pub/ - public application of the project
                static/ - static files (on host: /home/velessoft/webapps/static/delikat/pub)
            
## Install


### Clone project and download all requirements.

```
mkdir delikat-cake
cd delikat-cake
virtualenv .env
source .env/bin/activate
git clone git@github.com:perses76/delikat-cake.git
cd delikat-cake
pip install -r requirements.txt
```


### Setup project

1. Copy local_settings.py.def to local_settings.py
2. change path to DB. Be sure that DB exists in pointed folder.
3. Define MEDIA_ROOT and STATIC_ROOT to point your local folder.


## Run dev version

```
cd delikat-cake/myproject
python manage.py runserver
```


## Deploy project

1. connect to host server using ssh (putty).
1. Copy folder `my_project` to the host server: `/home/velessoft/webapps/delikat/myproject` without  local_settings.py
2. Restart apache2: `/home/velessoft/webapps/delikat/apache2/bin/restart`
```
