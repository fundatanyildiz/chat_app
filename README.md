#  Chat Application

Chat application is a web-app project coded in Python using Flask. It provides an interface to registered users for sending and receiving messages from each others.

## Requirements

 You need to install Python3 and below libraries in order to use this application. 

- Flask
- Flask-SQLAlchemy
- Marshmallow

Or the following command will install the packages according to the configuration file.

```
$ pip3 install -r requirements.txt
```
 Install Postgresql as database management systems to store application data. You can check this tutorial to install on
 Mac [https://adamtheautomator.com/install-postgresql-on-mac/](https://adamtheautomator.com/install-postgresql-on-mac/).

 After installing the packages and db, first run the 'models.py' file to create database tables. You need to do this just once.

```
 $ python3 models.py
```
 To run the app:

```
$ python3 main.py
```
 Visit [http://127.0.0.1:5000](http://127.0.0.1:5000/) in your browser to see the results.

## Usage

Include here a few examples of commands you can run and what they do. Finally link out to a resource to learn more (next paragraph).

For more details, check the [getting started guide]().

## Useful Resources

Include here any other links that are relevant for the project, such as more docs, tutorials, and demos.