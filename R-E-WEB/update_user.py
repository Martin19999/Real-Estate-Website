#!/usr/local/bin/python3
from os import environ
from http.cookies import SimpleCookie

from cgitb import enable

enable()

from cgi import FieldStorage
import pymysql as db
from html import escape


form_data = FieldStorage()


try:
    candidate = escape(form_data.getfirst('candidate_name'))

    connection = db.connect('cs1.ucc.ie', 'jf14', 'ieyah', 'cs6503_cs1106_jf14')
    cursor = connection.cursor(db.cursors.DictCursor)
    cursor.execute("""SELECT
                      FROM """)
except:




print('Content-Type: text/html')
print()

print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <title>update_user</title>
        </head>
        <body>
            %s
        </body>
    </html>""" % (result))
