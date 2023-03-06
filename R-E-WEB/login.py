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
homeenable = True
if len(form_data) != 0:
    username = escape(form_data.getfirst('username', '').strip())
    password = escape(form_data.getfirst('password', '').strip())
    if not username or not password:
        result = '<p>Error: user name and password are required</p>'
    else:
        sha256_password = sha256(password.encode()).hexdigest()
        try:
            connection = db.connect(host='localhost',user='jf14',password='11229870',database='jf14')
            cursor = connection.cursor(db.cursors.DictCursor)
            cursor.execute("""SELECT * FROM users
                              WHERE username = %s
                              AND password = %s""", (username, sha256_password))
            if cursor.rowcount == 0:
                result = '<p>Error: incorrect user name or password</p>'
            else:
                cookie = SimpleCookie()
                sid = sha256(repr(time()).encode()).hexdigest()
                cookie['sid'] = sid
                session_store = open('sess_' + sid, writeback=True)
                session_store['authenticated'] = True
                session_store['username'] = username
                session_store.close()
                result = """
                           <p>Succesfully logged in!</p>
                           <a href="index.html">Home</a><span><</span><a href="chooseyourplace.py">Map</a><span><</span><a href="browse.py">Houses</a><a href="showfav.py">My &#10084</a><a href="logout.py">Log Out</a>

                         """
                homeenable = False
                print(cookie)
            cursor.close()
            connection.close()
        except (db.Error, IOError):
            result = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'



if homeenable:
    form1 = """
            <form action="login.py" method="post">
                <label for="username">User name: </label>
                <input type="text" name="username" id="username" value="%s" />
                <label for="password">Password: </label>
                <input type="password" name="password" id="password" />
                <input type="submit" value="Login" />
            </form>
            <a href="index.html">Home</a><span><</span><a href="chooseyourplace.py">Map</a><span><</span><a href="browse.py">Houses</a>
            """ %(username)
else:
    form1 = """
            <form action="login.py" method="post">
                <label for="username">User name: </label>
                <input type="text" name="username" id="username" value="%s" />
                <label for="password">Password: </label>
                <input type="password" name="password" id="password" />
                <input type="submit" value="Login" />
            </form>
            """ %(username)




print('Content-Type: text/html')
print()

print("""
    <!DOCTYPE html>
    <html lang="en" id="loginpage">
        <head>
            <meta charset="utf-8" />
            <title>Log in</title>
            <link rel="stylesheet" href="styles.css" />
        </head>
        <body>
            <header>
                <h1>Welcome to our page!</h1>
            </header>
            <main>
                %s
                %s
            </main>
            <footer>
                <p><small>&copy Jianhao Feng. All rights reserved</small></p>
            </footer>

        </body>
    </html>""" % (form1, result))
