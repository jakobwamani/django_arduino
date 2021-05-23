## March 19 2021 
My name is Wamani Jacob a Developer . I have been with computers most of my life time 

I want to track the pool table balls


## How?
Track motion of pool balls


## Logic
The pool table game ends when a 14 balls have sunk in the pool table pockets so my project will count balls that have sunk in the pcokets

With that information , i can know how many games where played and how long the game took

## Setup Django 
https://django.readthedocs.io/en/stable/

## Setup Users in Django User Management

Start by the disabling the users inside settings.py>AUTH_PASSWORD_VALIDATORS


## Create a dashboard view

## Create an index page

## Work With Django User Management
Django has a lot of user management–related resources that’ll take care of almost everything, including login, logout, password change, and password reset. Templates aren’t part of those resources, though. You have to create them on your own.

inside the apps>urls.py>urlpatterns add the element below
url(r"^accounts/", include("django.contrib.auth.urls")),


accounts/login/ is used to log a user into your application. Refer to it by the name "login".

accounts/logout/ is used to log a user out of your application. Refer to it by the name "logout".

accounts/password_change/ is used to change a password. Refer to it by the name "password_change".

accounts/password_change/done/ is used to show a confirmation that a password was changed. Refer to it by the name "password_change_done".

accounts/password_reset/ is used to request an email with a password reset link. Refer to it by the name "password_reset".

accounts/password_reset/done/ is used to show a confirmation that a password reset email was sent. Refer to it by the name "password_reset_done".

accounts/reset/<uidb64>/<token>/ is used to set a new password using a password reset link. Refer to it by the name "password_reset_confirm".

accounts/reset/done/ is used to show a confirmation that a password was reset. Refer to it by the name "password_reset_complete

## Create a login page
For the login page, Django will try to use a template called registration/login.html.

## Create a logout page 
registration/logged_out.html.

## Change Passwords
1.registration/password_change_form.html to display the password change form

2.registration/password_change_done.html to show a confirmation that the password was successfully changed

## How am i going to connect the user table to the other tables
Am going to extend the User table and make it as a foreign key in the pool table because i want each user to store there own data and see , their own data.

## What tables database tables am i going to have?
Pool table
To hold the location , table name

Action table
To hold 
'id', 'status', 'date', 'time'


## Requirements
Django
Arduino IDE
SQL
HTML
Python

## References
How to Play Pool Table
https://www.gametablesonline.com/blog/how-to-play-pool-beginners-guide/

User management using Django
https://realpython.com/django-user-management/