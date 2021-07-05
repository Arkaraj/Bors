# Bors

A Simple rest api (CRUD) for dogs, made with django framework (MVT) python.

## Setting up Django

From the command line, cd into a directory where you’d like to store your code, then run the following command

```bash

django-admin startproject projectName

## Migration
python manage.py migrate

## Creating SuperUser
python manage.py createsuperuser

## Creating Tables
python manage.py makemigrations
python manage.py migrate --run-syncdb

```

## Django Docs

https://docs.djangoproject.com/en/3.2/

https://docs.djangoproject.com/en/3.2/intro/tutorial01/

## Tech Stack

- Django python web framework
- SQL database (Sqlite)

## Routes

- [x] GET api/v1/dogs - Get all Dogs
- [x] GET api/v1/dogs/:id - Get specific Dog
- [x] POST api/v1/dogs/add - add new Dogs
- [x] PUT api/v1/dogs/add/:id - add Dog owner
- [x] DELETE api/v1/dogs/:id - delete specific Dog

- [x] GET api/v1/users - Get all Users
- [x] GET api/v1/users/:id - Get specific User
- [x] POST api/v1/users - add new User
