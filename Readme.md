### Overview
Application web pour offrir une page à un utilisateur de se connecter, afficher
son profile et modifier ses informations.

L'application est developpée en utilisant Django 2.1.3 et Python 3.7

### Option de deploiement

Cette application peut etre deployée en utilisant un Docker container ou bien
la méthode classique de Django

#### Avec Docker
```buildoutcfg
$ docker-compose up
```

#### Sans Docker
```
$ sudo pip3 install -r requirements.txt
$ python3 manage.py runserver
```
L'application sera disponible sur [localhost:8000](http://localhost:8000)
