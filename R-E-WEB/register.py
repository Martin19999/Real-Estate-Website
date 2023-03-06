#!/usr/local/bin/python3

from cgitb import enable
enable()

import sys
sys.path.append("/Users/realmartt/miniforge3/lib/python3.9/site-packages")

from cgi import FieldStorage
from html import escape
from hashlib import sha256
from time import time
from shelve import open
from http.cookies import SimpleCookie
import mysql.connector as db

form_data = FieldStorage()
username = ''
result = ''
if len(form_data) != 0:
    username = escape(form_data.getfirst('username', '').strip())
    password1 = escape(form_data.getfirst('password1', '').strip())
    password2 = escape(form_data.getfirst('password2', '').strip())
    if not username or not password1 or not password2:
        result = '<p>Error: user name and passwords are required</p>'
    elif password1 != password2:
        result = '<p>Error: passwords must be equal</p>'
    else:
        try:
            connection = db.connect(host='localhost',user='jf14',password='11229870',database='jf14')
            cursor = connection.cursor(db.cursors.DictCursor)
            cursor.execute("""SELECT * FROM users
                              WHERE username = %s""", (username))
            if cursor.rowcount > 0:
                result = '<p>Error: user name already taken</p>'
            else:
                sha256_password = sha256(password1.encode()).hexdigest()
                cursor.execute("""INSERT INTO users (username, password)
                                  VALUES (%s, %s)""", (username, sha256_password))
                connection.commit()
                cursor.close()
                connection.close()
                cookie = SimpleCookie()
                sid = sha256(repr(time()).encode()).hexdigest()
                cookie['sid'] = sid
                session_store = open('sess_' + sid, writeback=True)
                session_store['authenticated'] = True
                session_store['username'] = username
                session_store.close()
                result = """
                           <p>Succesfully inserted!</p>
                           <a href="logout.py">Logout</a>
                         """
                print(cookie)
        except (db.Error, IOError):
            result = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'

print('Content-Type: text/html')
print()
print("""
    <!DOCTYPE html>
    <html lang="en" id="signpage">
        <head>
            <meta charset="utf-8" />
            <title>Web Dev 2</title>
            <link rel="stylesheet" href="styles.css">
        </head>
        <body>
            <h1>We are happy you are here...</h1>
            <p>Register to mark up your dream houses!</p>
            <form action="register.py" method="post">
                <label for="username">User name: </label>
                <input type="text" name="username" id="username" value="%s" />
                <label for="password1">Password: </label>
                <input type="password" name="password1" id="password1" />
                <label for="passwords2">Re-enter password: </label>
                <input type="password" name="password2" id="password2" />
                <input type="submit" value="Register" />
            </form>
            %s
            <a href="index.html">Home</a><span>&#8226</span><a href="chooseyourplace.py">Map</a><span>&#8226</span><a href="browse.py">Houses</a>
        </body>
    </html>""" % (username, result))
