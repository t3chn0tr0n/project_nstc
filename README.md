# nit_project

a django project for creating and maintaining the student database of my college

## Requirements

1. Django_2.1.1
2. Python 3 (3.6 used)
3. PostgreSQL and pgAdmin
4. psycopg2 (2.7.5 used)

## Installation/setup process for testing the project

1. Create a database in your database server (eg. `nitdb`)

2. open the file `nit_project/server_configs/settings.py` and change the server credentials (ref. line no: 63-70)

3. Run command - ``python .\manage.py migrate`` from the root folder

4. Now finally it is ready for `runserver`

## Flow of Control

Every user is needed to be logged in to access any data!
There are 3 types of users: Students, Teachers, Hods.

### Login Process

Every user must login first. If he/she is not registered they can sign up. However every random person can not signup. The list of students and teachers that is upload by the departmental HOD  [Yet to implement the upload portal] can sign up only! To sign up, users need: email(given to HOD) and id card number. After checking with database they will be sent an email with the verification link. Follwing the link they will registered and now can login.

Max fail login attempts = 3. Afer that a/c will be locked, user will be emailed and can only be unlocked by HOD. [Yet to implement!]

If they forget password, password reset process is more or less same as the registration process!

## Usage

A few dummy data has been provided in the "dummy_data" folder. The files are in csv format and can be uploaded through pgAdmin (will be working on upload files in the native website later!).

NOTE: Emails in students and teachers csv files must be changed because they will be used for logins/signups.
