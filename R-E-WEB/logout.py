#!/usr/local/bin/python3

from cgitb import enable
enable()

from os import environ
from shelve import open
from http.cookies import SimpleCookie

print('Content-Type: text/html')
print()

result = '<p>You are already logged out</p>'
try:
    cookie = SimpleCookie()
    http_cookie_header = environ.get('HTTP_COOKIE')
    if http_cookie_header:
        cookie.load(http_cookie_header)
        if 'sid' in cookie:
            sid = cookie['sid'].value
            session_store = open('sess_' + sid, writeback=True)
            session_store['authenticated'] = False
            session_store.close()
            result = """
                <h1>You are now logged out. Thanks for using our website!</h1>
                <p><a href="index.html">Home</a></p>
                <p><a href="login.py">Login again</a></p>"""
except IOError:
    result = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'

print("""
    <!DOCTYPE html>
    <html lang="en" id="logoutpage">
        <head>
            <meta charset="utf-8" />
            <title>Log Out</title>
            <link rel="stylesheet" href="styles.css" />
        </head>
        <body>
            %s
        </body>
    </html>""" % (result))
