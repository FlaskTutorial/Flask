# Flask Tutorial

### What is Flask, and why use it?

Flask is a microframework for Python based on [Werkzeug](http://werkzeug.pocoo.org/) and [Jinja2](http://jinja.pocoo.org/docs/dev/). Its main use is to get your Python app started very quickly.

### Before you begin...

Creating an app with Flask assumes that you have working knowledge of:
* Python
* Jinja2
* Werkzeug
* RESTful routes
* Unit testing
* Debugging

### Dependencies
Flask depends on two external libraries, Werkzeug and Jinja2. Werkzeug is a toolkit for WSGI, the standard Python interface between web applications and a variety of servers for both development and deployment. Jinja2 renders templates. 

### How to Install

Using [virtualenv](https://pypi.python.org/pypi/virtualenv) is an easy way to install a virtual Python environment for your new app. It enables multiple side-by-side installations of Python, one for each project. It doesn’t actually install separate copies of Python, but it does provide a clever way to keep different project environments isolated.

1. Install virtualenv
```
$ sudo pip install virtualenv
```
2. Create a folder for your app
```
$ virtualenv flaskapp
```
3. Activate your new app
```
$ cd flaskapp
$ . bin/activate
```
4. Install Flask!
```
$ pip install Flask
```

### Project Structure

TBD from De

