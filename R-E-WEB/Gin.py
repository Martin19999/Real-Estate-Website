#!/usr/local/bin/python3

from cgitb import enable
enable()

from comments import get_comments

from os import environ
from shelve import open
from http.cookies import SimpleCookie


print('Content-Type: text/html')
print()

result = """<a href="login.py">Log in</a>
            <a href="register.py">Sign up</a>"""
commentbutton = False

try:
    cookie = SimpleCookie()
    http_cookie_header = environ.get('HTTP_COOKIE')
    if http_cookie_header:
        cookie.load(http_cookie_header)
        if 'sid' in cookie:
            sid = cookie['sid'].value
            session_store = open('sess_' + sid, writeback=False)
            if session_store.get('authenticated'):
                result = """<a href='addtofav.py?house_id=3' class='icon'>&nbsp &#10084 &nbsp</a>
                            <a href="showfav.py">My &#10084</a>
                            <a href="logout.py">Log Out</a>"""
                commentbutton = True
            session_store.close()
except IOError:
    result = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'


print("""
    <!DOCTYPE html>
    <html lang="en" class="detailpage">
        <head>
            <meta charset="utf-8" />
            <title>Gin</title>
            <link rel="stylesheet" href="styles.css" />
            <script src="Slideshow.js" type="module"></script>
        </head>
        <body>
            <main class="detailmain">
                <section id="slide">
                    <ul class="slideshow">
                        <li><img src="Gin0.jpg" alt="Frontview"/></li>
                        <li><img src="Gin1.jpg" alt="Dining Area"/></li>
                        <li><img src="Gin2.jpg" alt="Living Room" /></li>
                        <li><img src="Gin3.jpg" alt="Bedroom" /></li>
                        <li><img src="Gin4.jpg" alt="Bathroom"/></li>
                        <li><img src="Gin5.jpg" alt="Kitchen" /></li>
                    </ul>
                </section>
                <section id="text">
                    <div class="plb">
                        <a href="index.html">Home</a><span><</span><a href="chooseyourplace.py">Map</a><span><</span><a href="browse.py">Houses</a>
                        %s
                    </div>
                    <h1>5348 Buckhannon Pike, Coalton, Gin 26257</h1>
                    <p><img src="iconbed.jpg"></img>3 <img src="iconbath.jpg"></img>3<img src="iconarea.jpg"></img> 277&#13217 &nbsp &nbsp Apartment</p>
                    <p>Price: &#8364 705,000</p>
                    <p class="intro">Located in the beautiful Gin area, and by the bank of River Tonn, these apartments are the ideal choices for those who wants to settle here.\
                                     Those apartments are right in the heart of the city. So you can access to schools, markets, etc. literally everywhere effortlessly.\
                    In these well-furnished apartments featuring 3 bedrooms and 3 bathrooms, you'll enjoy a better standard of life.\
                    For more information, please contact John Smith.</p>
                    <div class="idencard">
                      <img src="simpsons.jpg" alt="Avatar" >
                      <div class="line">
                        <h4><b>John Smith</b></h4>
                        <p>Tel: +353 0873525156</p>
                        <p>E-mail: 2222@gmail.com</p>
                      </div>
                    </div>
                </section>
                %s

            </main>
            <footer>
                <p><small>&copy Jianhao Feng. All rights reserved</small></p>
            </footer>

        </body>
    </html>""" % (result,get_comments(commentbutton)))
