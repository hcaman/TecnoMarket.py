# About The Project
I started this project because I want to practice some basic MVC and CRUD using Django and Python, 
so I take a basic template HTML, for simulate a e-commerce site, 
and I adapt and add all the functionality using Django and sqlite for save the list of products and users.

# Prerequisites
Install Python 3.9.1 -> https://www.python.org/downloads/

# Requiriments
You must install the requirements of *requirements.txt*:

## For windows:
1. `pip install -r requirements.txt`

2. `python manage.py makemigrations`

3. `python manage.py migrate`

### Enter into admin panel */admin/* 
You must create a super user, using the command:
`python manage.py createsuperuser`

`python manage.py runserver`

## For MacOS / Fedora / Debian:
1. `pip3 install -r requirements.txt`

2. `python3 manage.py makemigrations`

3. `python3 manage.py migrate`

### Enter into admin panel */admin/* 
You must create a super user, using the command:
`python3 manage.py createsuperuser`

`python3 manage.py runserver`