#!/usr/local/bin/python3

from cgitb import enable
enable()
from cgi import FieldStorage
from os import environ
from hashlib import sha256
from shelve import open
from http.cookies import SimpleCookie
import pymysql as db

result = """<table>
               <tr>
                   <th scope="col">Houses</th><th scope="col">Price</th>
                </tr>"""
username = ''
test=''
try:
    my_dict = {}
    key1=False
    key2=False
    key3=False
    key4=False
    key5=False
    key6=False



    cookie = SimpleCookie()
    http_cookie_header = environ.get('HTTP_COOKIE')
    if http_cookie_header:
        cookie.load(http_cookie_header)
        if 'sid' in cookie:
            sid = cookie['sid'].value
            session_store = open('sess_' + sid, writeback=False)
            if session_store.get('authenticated'):
                username = session_store.get('username')
            session_store.close()

    connection = db.connect('cs1.ucc.ie', 'jf14', 'ieyah', 'cs6503_cs1106_jf14')
    cursor = connection.cursor(db.cursors.DictCursor)

    cursor.execute("""SELECT house_id,qty
                      FROM houses
                      WHERE username=%s""", (username))
    for row in cursor.fetchall():
        my_dict[int(row['house_id'])] = int(row['qty'])

    for key in my_dict.keys():
        if key == 1:
            key1 = True
        if key == 2:
            key2 = True
        if key == 3:
            key3 = True
        if key == 4:
            key4 = True
        if key == 5:
            key5 = True
        if key == 6:
            key6 = True

    if key1:
        if my_dict[1] %2 == 1:
            result += "<tr><td><img src='Dream0.jpg' class='favpage'/></td><td>Price: &#8364 235,000</td></tr>"
    if key2:
        if my_dict[2] %2 == 1:
            result += "<tr><td><img src='king0.jpg' class='favpage'/></td><td>Price: &#8364 400,336,000</td></tr>"
    if key3:
        if my_dict[3] %2 == 1:
            result += "<tr><td><img src='Gin0.jpg' class='favpage'/></td><td>Price: &#8364 705,000</td></tr>"
    if key4:
        if my_dict[4] %2 == 1:
            result += "<tr><td><img src='c0.jpg' class='favpage'/></td><td>Price: &#8364 905,000</td></tr>"
    if key5:
        if my_dict[5] %2 ==1:
            result += "<tr><td><img src='b0.jpg' class='favpage'/></td><td>Price: &#8364 191,000</td></tr>"
    if key6:
        if my_dict[6] %2 != 0:
            result += "<tr><td><img src='h0.jpg' class='favpage'/></td><td>Price: &#8364 5,205,000</td></tr>"

    result += "</table>"

    cursor.close()
    connection.close()
except (db.Error, IOError):
    result = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'

print('Content-Type: text/html')
print()

print("""
    <!DOCTYPE html>
    <html lang="en" id="showfavpage">
        <head>
            <meta charset="utf-8" />
            <title>Your Fav List</title>
            <link rel="stylesheet" href="styles.css" />
        </head>
        <body>
            <header>
                <h1>I WANT TO BUY...</h1>
            </header>
            <main>
                <section>
                    <a href="index.html">Home</a><span>&#8226</span><a href="chooseyourplace.py">Map</a><span>&#8226</span><a href="browse.py">Houses</a>
                </section>
                <section>
                    %s
                </section>
            </main>
            <footer>
                <p><small>&copy Jianhao Feng. All rights reserved</small></p>
            </footer>
        </body>
    </html>"""%(result))
