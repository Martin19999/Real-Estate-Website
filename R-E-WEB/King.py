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
                result = """<a href='addtofav.py?house_id=2' class='icon'>&nbsp &#10084 &nbsp</a>
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
            <title>King's Palace</title>
            <link rel="stylesheet" href="styles.css" />
            <script src="Slideshow.js" type="module"></script>
            <script src="iconchanging.js" type="moudule"></script>
        </head>
        <body>
            <main class="detailmain">
                <section id="slide">
                    <ul class="slideshow">
                        <li><img src="king0.jpg" alt="Frontview"/></li>
                        <li><img src="king1.jpg" alt="Dining Area"/></li>
                        <li><img src="king2.jpg" alt="Living Room" /></li>
                        <li><img src="king4.jpg" alt="Bathroom"/></li>
                        <li><img src="king5.jpg" alt="Bedroom" /></li>
                        <li><img src="king6.jpg" alt="Bathroom"/></li>
                    </ul>
                </section>
                <section id="text">
                    <div class="plb">
                        <a href="index.html">Home</a><span><</span><a href="chooseyourplace.py">Map</a><span><</span><a href="browse.py">Houses</a>
                        %s
                    </div>
                    <h1>Charlemont Street, South City, King</h1>
                    <p><img src="iconbed.jpg" class="icon"></img>12 <img src="iconbath.jpg" class="icon"></img>18<img src="iconarea.jpg" class="icon"></img> 1,094&#13217 &nbsp &nbsp House</p>
                    <p>Price: &#8364 400,336,000</p>
                    <p class="intro" id="kingtext">Located in suburb area, but it only takes you 10 minutes to get to the city by driving. Like the name\
                                     "King's Palace", these series of 5-story-mansions give you the feelings of living in a royal palace. Retro is the\
                                     theme and aristocracy is the anthem. Exquisiteness and elegance can be found everywhere: invaulable\
                                     paintings hanging on the wall, carefully designed crystal chandeliers, the daintly golden toilet&nbsp(Our advice is do not use it)...\
                                     even every detail is a form of art: elaborate candlesticks, the arm of a chair, etc. Featuring 12 bedrooms,\
                                     18 bathrooms, a huge parking lot with a capacity of 20 cars in maximum, a heliport, a big open yard where you can even play\
                                     golf, not to mention something like swimming pool, which is very basic for a mansion, your dream will come true.\
                                     For more information, please contact John.</p>
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
