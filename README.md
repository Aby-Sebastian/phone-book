# Phone-Book

A Simple django application developed to learn Postgresql and Docker in django. The application stores the data in Postgressql database. The django application is put in a Docker container.

A URL management application built with `python` `django` `bootstrap`. Shortly is simlar to Bitly a popular URL management application.

A simple, reponsive  website. Built with:

- Python 🐍
- Django 🎸
- Bootstrap 4 🌈
- Vanilla JS - ES6
- JQuery

## Features 

- create a contact <br>
- update a contact <br>
- view a contact <br>
- delete a contact <br>
- Each contact can contain first name, last name, country code, phone number, email id, contacts image <br>
- User can add contact's as Favorites too and it will be shown in Favorite section in application <br>
- User can update contacts image <br>
<!--
# Shortly
 
This is a URL management application similar to Bitly. Shortly is a URL shortening service and a link management platform. 
With our platform, you shorten urls, build QR codes, see the shortened urls analytics, redirect links and leverage many more features.
# Real Estate Django Web App

A URL management application built with `python` `django` `bootstrap`. Shortly is simlar to Bitly a popular URL management application.

A simple, reponsive  website. Built with:

- Python 🐍
- Django 🎸
- Bootstrap 4 🌈
- Vanilla JS - ES6
- JQuery

## Features

- URL shortening
- ability to customize the shortened URL
- shows analytic data in charts based on clicks on short urls
- QR code generation on shortened URL
- share shortened URL in social medias
- can add Tags to categoriza links
- search functionality
- authentication

## How to run this project (Ubuntu 18.04)

1. **Clone the project**

```sh
git clone https://github.com/Aby-Sebastian/Shortly.git
```

2.  **Make sure you are in *Shortly* folder**

   1. Install all dependencies

      ```sh
      pip install -r requirements.txt
      ```

3. **Install PostgreSQL in your Ubuntu 18.04**

   1. Enable PostgreSQL Apt Repository

      ```sh
      sudo apt-get install wget ca-certificates
      
      wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
      
      # Now add the repository to your system.
      
      sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
      ```

   2. Install PostgreSQL on Ubuntu

      ```sh
      sudo apt-get update
      sudo apt-get install postgresql postgresql-contrib
      ```

   3. Connect to PostgreSQL

      ```sh
      sudo su - postgres
      psql
      ```

      Now you are logged in to PostgreSQL database server. To check login info use following command from the database command prompt.

      ```sh
      postgres-# \conninfo
      ```

   4. Create a database

      ```sh
      CREATE DATABASE shortly;
      ```

   5. Create user 

      ```sh
      CREATE USER pks WITH PASSWORD 'abc123!';
      ```
   
4. **Run Migrations**

```sh
python manage.py makemigrations
python manage.py migrate
```

5. **Run Server**

```sh
python manage.py runserver 
```

And you are good to go. 


**To run with SQLite only**

Go inside the 'realestate' folder and open 'settings.py' file and replace

```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'shortly' ,
        'USER': 'pks',
        'PASSWORD': 'abc123!',
        'HOST':'localhost',
        
    }
}
```

To: 

```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

This is the default configuration of Django database.


**Backend**

For Database I have used Postgres Database Name: shortly

Note: Please change those gmail credentials from real_estate folder you will get settings.py inside that file you will see username and password mentioned as place your Username and Password. Also do that same thing from Contacts folder views.py you will see YourEmail mentioned on line number 33.

### Screenshots

- **HOME**

![Home](https://github.com/TheCaffeineDev/Real-Estate-Django-Web-App/blob/master/screenshots/s1.JPG)

- **Listings** 


![Listings](https://github.com/TheCaffeineDev/Real-Estate-Django-Web-App/blob/master/screenshots/s3list.JPG)

- **Registration** 

![Registration](https://github.com/TheCaffeineDev/Real-Estate-Django-Web-App/blob/master/screenshots/s4reg.JPG)

- **Admin Panel - 1**

![Admin](https://github.com/TheCaffeineDev/Real-Estate-Django-Web-App/blob/master/screenshots/s5adm.JPG)

- **Admin Panel - 2**

![Admin](https://github.com/TheCaffeineDev/Real-Estate-Django-Web-App/blob/master/screenshots/s6r.JPG)

- **About**

![About ](https://github.com/TheCaffeineDev/Real-Estate-Django-Web-App/blob/master/screenshots/s2about.JPG)


## Acknowledgments

Many thanks to [@bradtraversy](https://github.com/bradtraversy) for his awesome course.
-->
## References

1. https://www.djangoproject.com/
