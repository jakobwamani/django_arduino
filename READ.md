# June 5th 2021

## Google Docs
[This document contains the Hardware and Software Specifications](https://docs.google.com/document/d/1VmVc4CmjYzYFPzCeiBg8k-KrPtAwDRACMsuuZYY_06A/edit)

# SOFTWARE AND HARDWARE REQUIREMENTS FOR GAME BIT SYSTEMS

### Chapter one 

### Background
Owners of game station can only monitor their stations when present or else entrust someone

### Chapter two

### Problem statement
Inconsistent tracking of the game station earnings which could be solved by computerised tracking 

### Objectives of the project

### General objective of the project
To provide a new way of game station earnings tracking

### Specific objectives 

+ To study the current system being used at game stations.
+ To identify the requirements for developing an a bit game system to counter the current system
+ To develop the bit game system
+ To test and validate the bit game system to establish whether it addresses the general objective.

### Chapter three

### Requirements specification

Specific requirements are split into two that is user and system requirements.

+ **User Requirements**
The Bit Game System will be accessible to the bit game users.

+ **System Requirements**
These are requirements for the system to be able to perform its functionality efficiently and effectively.

#### Functional requirements
+ Time the game station has been active on a specific day
+ Detect presence of a client on a particular console
+ Store presence data on a particular console
+ Display presence data on a particular console

#### Non-Functional requirements
+ The bit game system should be upload its data 5 times a day.


### Chapter four 

### System designs


# Installing Ubuntu Server on Raspberry pi 3
+ First, insert the microSD card into your computer.

If you are on Ubuntu, you can run:

sudo snap install rpi-imager

Open the imager and follow the prompts

This takes up some time so what i did was to download the ubuntu server 20.04.2 meant for raspberry pi 3 

Right click on the "Disk image Writer" 

Restore the intended disk

With the SD card still inserted in your laptop, open a file manager and locate the “system-boot” partition on the card. It contains initial configuration files that load during the first boot process.

Edit the network-config file to add your Wi-Fi credentials. 

### **Note: wifi name must be enclosed in quotation marks**


### Raspberry pi ubuntu server 21.04 command-line login
ubuntu login :ubuntu
password : ubuntu

After that you will be prompted to create a new password and then retype the new password


### using nmap to find the ip address of the raspberry pi

i used nmap tool

$ nmap -sn 192.168.43.0/24

### using open shh to remotely connect to the raspberry pi
Logging in from other computers

Although SSH has many uses, its main job is to provide access to a command-line over a network. Even if you are installing SSH for completely different reasons, it's best to get command-line access before you try anything more complicated. 

To login remotely using ssh i used my terminal

$ ssh ubuntu@192.168.43.35

### install ubuntu desktop

$ sudo apt update
$ sudo apt upgrade

$ sudo apt install xubuntu-desktop

$ sudo reboot

### Enable auto login in console

Enter the command **sudo raspi-config**. Scroll down to **Boot Options** and select **Console Autologin**. Then exit the configuration menu and reboot.

#### Next Step

I made this file: /etc/systemd/system/getty@tty1.service.d/autologin.conf
And put this in it:


```
[Service]
ExecStart=
ExecStart=-/sbin/agetty --autologin pi --noclear %I 38400 linux
```

After that, i runned this:

$ sudo systemctl enable getty@tty1.service

### installing git
$ sudo apt install git

### copy files remotely via shh using SCP "secure copy" utility

$ scp requirements.txt ubuntu@192.168.43.35:/home/ubuntu/venvs/tangibleai


### Clone Github repository
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

## How am i going to connect the user table to the other tables?
Am going to extend the User table and make it as a foreign key in the pool table because i want each user to store there own data and see , their own data.

First i will import user model.

from django.contrib.auth.models import User

Then create a field in the pool_table
user = models.OneToOneField(User, on_delete=models.CASCADE)

## What do i want the user to see on the dashboard
Games played in a day
-how are we getting the games played 

By the word dashboard , it means that am going to be dealing with views , so the logic is going to be in the views.py module

Pull the user 
grab the user whose data that i want to show

Pull his or table

Pull the data

Show the data

so i will grab data for a specfic date first 

Then loop through it and code that for every input in the whole range
if input status is equal 1 then add it to pockets variable

if the pockets variable is equal to 15 its means that one game has been played 

one game is equal to 50/=


Money collected in a day

## What tables database tables am i going to have?
Pool table
To hold the location , table name

Action table
To hold 
'id', 'status', 'date', 'time'

So a user has a pool table and his pooltable played on , so when am registering , i can combine a user to have the user's details and the pool table that they are having .

## Combination of user table and the pool_table

## Requirements
+ Django
+ Arduino IDE
+ SQL
+ HTML
+ Python

## References
How to Play Pool Table
https://www.gametablesonline.com/blog/how-to-play-pool-beginners-guide/

User management using Django
https://realpython.com/django-user-management/

Open ssh
https://help.ubuntu.com/community/SSH/OpenSSH/ConnectingTo

How-to-enable-disable-automatic-login-in-ubuntu
https://vitux.com/how-to-enable-disable-automatic-login-in-ubuntu/