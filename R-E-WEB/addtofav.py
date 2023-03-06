#!/usr/local/bin/python3

from cgitb import enable
enable()

from cgi import FieldStorage
from os import environ
from hashlib import sha256
from shelve import open
from http.cookies import SimpleCookie
import pymysql as db

print('Content-Type: text/plain')
print()

result = 'I &#10084'       #when you never click the I heart/broken heart icon
username = ''
flag=0
try:
    cookie = SimpleCookie()
    http_cookie_header = environ.get('HTTP_COOKIE')
    if http_cookie_header:
        cookie.load(http_cookie_header)
        if 'sid' in cookie:
            sid = cookie['sid'].value
            session_store = open('sess_' + sid, writeback=False)
            if session_store.get('authenticated'):
                username = session_store.get('username')         #store username to the variable "username"
            session_store.close()

    form_data = FieldStorage()
    house_id = int(form_data.getfirst('house_id'))                      #get the house_id from the url


    connection = db.connect('cs1.ucc.ie', 'jf14', 'ieyah', 'cs6503_cs1106_jf14')
    cursor = connection.cursor(db.cursors.DictCursor)

    cursor.execute("""SELECT username,house_id
                      FROM houses""")
    for row in cursor.fetchall():
        if row['username'] == username and int(row['house_id']) == int(house_id):
            flag = flag + 1

    if flag==0:
        cursor.execute("""INSERT INTO houses (username,house_id,qty)
                          VALUES (%s,%s,0)""", (username,house_id))          # insert username,house_id into the DB and set the qty as 0
        connection.commit()

    cursor.execute("""UPDATE houses
                      SET qty = qty + 1
                      WHERE house_id=%s AND username=%s""",(house_id,username))  # increase the qty by 1
    connection.commit()


    cursor.execute("""SELECT house_id, qty
                      FROM houses
                      WHERE username=%s""", (username))                    #read the data that already been stored

    for row in cursor.fetchall():
        if int(row['house_id'])==1:
            if row['qty'] is None:
                house1 = True
            elif int(row['qty']) %2 == 0:            # Now I've only made the house_id = 1 available , so when house_id =1, qty is 1, and the rest qtys are None
                house1 = True                        # house1 is a boolean that tells the computer whether to display "I heart"or "broken heart"
            elif int(row['qty']) %2 == 1:            #qty can be None(so not this page u don't have to worry about it)
                house1 = False                       #    can be odd, that means u have clicked "I heart" so display a broken heart
        if int(row['house_id'])==2:                  #    can be even, so u have clicked"broken heart" , u unfav this house, so display "I heart"
            if row['qty'] is None:
                pass
            elif int(row['qty']) %2 == 0:
                house2 = True
            elif int(row['qty']) %2 == 1:
                house2 = False
        if int(row['house_id'])==3:
            if row['qty'] is None:
                pass
            elif int(row['qty']) %2 == 0:
                house3 = True
            elif int(row['qty']) %2 == 1:
                house3 = False
        if int(row['house_id'])==4:
            if row['qty'] is None:
                pass
            elif int(row['qty']) %2 == 0:
                house4 = True
            elif int(row['qty']) %2 == 1:
                house4 = False
        if int(row['house_id'])==5:
            if row['qty'] is None:
                pass
            elif int(row['qty']) %2 == 0:
                house5 = True
            elif int(row['qty']) %2 == 1:
                house5 = False
        if int(row['house_id'])==6:
            if row['qty'] is None:
                pass
            elif int(row['qty']) %2 == 0:
                house6 = True
            elif int(row['qty']) %2 == 1:
                house6 = False


    if house_id==1:
        if house1:
            result="You successfully removed this house from your favorite list!"
        else:
            result="You successfully added this house to your favorite list!"
    if house_id==2:
        if house2:
            result="You successfully removed this house from your favorite list!"
        else:
            result="You successfully added this house to your favorite list!"
    if house_id==3:
        if house3:
            result="You successfully removed this house from your favorite list!"
        else:
            result="You successfully added this house to your favorite list!"
    if house_id==4:
        if house4:
            result="You successfully removed this house from your favorite list!"
        else:
            result="You successfully added this house to your favorite list!"
    if house_id==5:
        if house5:
            result="You successfully removed this house from your favorite list!"
        else:
            result="You successfully added this house to your favorite list!"
    if house_id==6:
        if house6:
            result="You successfully removed this house from your favorite list!"
        else:
            result="You successfully added this house to your favorite list!"
    print(result)
    cursor.close()
    connection.close()

except IOError:
    print('Error')
