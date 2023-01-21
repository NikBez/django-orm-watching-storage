# Storage application
This application is used by bank security to control access to the vault

## How to install
````
pip install -r requirements.txt
````

Create `.env ` using this template:

````
DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASSWORD=
DEBUG=FALSE
SECRET_KEY=[REPLACE_ME]
INSTALLED_APPS=datacenter
ALLOWED_HOSTS=*
````
DESCTIPTION:  
DB_HOST - Database hostname   
DB_PORT - Database port   
DB_NAME - Database name   
DB_USER - Database user name   
DB_PASSWORD - Database user password   
DEBUG - Debug mode  
SECRET_KEY -  Key for password encryption  
INSTALLED_APPS - list of registrated django apps  
ALLOWED_HOSTS - list of allowed hosts  


Run local server:
````
python3 manage.py runserver
````

Then app will be available in `127.0.0.1:8000/`

## How to use
The application is under development. You don't have access to our DB. That's why you can look only how queries and HTML pages are builded. 

At the moment, it is possible to monitor the activity of visits to the storage and analyze suspiciousness by the duration of the visit

## Versions
Python 3.11.1

## Authors
**Nik Bez ** - *Initial works* - [NkiBez](https://github.com/NikBez)
