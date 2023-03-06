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
                result = """<a href='addtofav.py?house_id=1' class='icon'>&nbsp &#10084 &nbsp</a>
                            <a href='showfav.py'>My &#10084</a>
                            <a href='logout.py'>Log Out</a>"""
                commentbutton = True
            session_store.close()
except IOError:
    result = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'


print("""
    <!DOCTYPE html>
    <html lang="en" class="detailpage">
        <head>
            <meta charset="utf-8" />
            <title>Dream River</title>
            <link rel="stylesheet" href="styles.css" />
            <script src="Slideshow.js" type="module"></script>
            <script src="iconchanging.js" type="moudule"></script>
        </head>
        <body>
            <main class="detailmain">
                <section id="slide">
                    <ul class="slideshow">
                        <li><img src="Dream0.jpg" alt="Frontview"/></li>
                        <li><img src="Dream1.jpg" alt="Dining Area"/></li>
                        <li><img src="Dream3.jpg" alt="Bedroom" /></li>
                        <li><img src="Dream4.jpg" alt="Bathroom"/></li>
                        <li><img src="Dream5.jpg" alt="Kitchen" /></li>
                    </ul>
                </section>
                <section id="text">
                    <div class="plb">
                        <a href="index.html">Home</a><span><</span><a href="chooseyourplace.py">Map</a><span><</span><a href="browse.py">Houses</a>
                        %s
                    </div>
                    <h1>Castletown Road, County Louth, A91 C9F7</h1>
                    <p><img src="iconbed.jpg" class="icon"></img>3 <img src="iconbath.jpg" class="icon"></img>2<img src="iconarea.jpg" class="icon"></img> 211&#13217 &nbsp &nbsp House</p>
                    <p>Price: &#8364 235,000</p>
                    <p class="intro">Quality, privacy and stress-free living, in a quiet location. This lovely home sits among good company in a\
                                     small unit block surrounded by lovely neighbours. Close to sumpermarkets and pubs, and a river! For the house itself, it gives\
                                     you a 90s vibe, but that doesn't mean the facilities are in bad conditions - on the contrary, they are in pretty \
                                     decent conditions. Featuring 3 bedrooms, 2 bathrooms, 2 carport spaces and a big front yard, it's definately an ideal place to live in.\
                                     For more information, please contact Alex O'Mahony. Inspections welcomed.</p>
                    <div class="idencard">
                      <img src="spon.jpg" alt="Avatar" >
                      <div class="line">
                        <h4><b>Alex O'Mahony</b></h4>
                        <p>Tel: +353 0873695176</p>
                        <p>E-mail: 236@gmail.com</p>
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
