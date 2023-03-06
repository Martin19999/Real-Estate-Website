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
                result = """<a href='addtofav.py?house_id=6' class='icon'>&nbsp &#10084 &nbsp</a>
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
            <title>High Island</title>
            <link rel="stylesheet" href="styles.css" />
            <script src="Slideshow.js" type="module"></script>
        </head>
        <body>
            <main class="detailmain">
                <section id="slide">
                    <ul class="slideshow">
                        <li><img src="h0.jpg" alt="Frontview"/></li>
                        <li><img src="h1.jpg" alt="Dining Area"/></li>
                        <li><img src="h2.jpg" alt="Living Room" /></li>
                        <li><img src="h3.jpg" alt="Bedroom" /></li>
                        <li><img src="h4.jpg" alt="Bathroom"/></li>
                        <li><img src="h5.jpg" alt="Kitchen" /></li>
                        <li><img src="h6.jpg" alt="Living Room" /></li>
                        <li><img src="h7.jpg" alt="Bedroom" /></li>
                        <li><img src="h8.jpg" alt="Bathroom"/></li>
                        <li><img src="h9.jpg" alt="Kitchen" /></li>
                    </ul>
                </section>
                <section id="text">
                    <div class="plb">
                        <a href="index.html">Home</a><span><</span><a href="chooseyourplace.py">Map</a><span><</span><a href="browse.py">Houses</a>
                        %s
                    </div>
                    <h1>Tullow, County Maine, R93 R858</h1>
                    <p><img src="iconbed.jpg" class="icon"></img>7 <img src="iconbath.jpg" class="icon"></img>9<img src="iconarea.jpg" class="icon"></img> 821&#13217 &nbsp &nbsp House</p>
                    <p>Price: &#8364 5,205,000</p>
                    <p class="intro">Ever dreamt of living in a big mansion? You should probably consider this one. Featuring 7 capacious bedrooms,\
                                     9 luxury modern bathrooms, 15 carport spaces, a professional kictchen, a home-cinema, a basement where you can store wines, a gym,\
                                     a big backyard with a swimming pool... Anything else do I have to say? Come and check it out in person by contacting\
                                     Tom right now!</p>
                    <div class="idencard">
                      <img src="t.jpg" alt="Avatar" >
                      <div class="line">
                        <h4><b>Tom Cinnamon</b></h4>
                        <p>Tel: +353 0852639110</p>
                        <p>E-mail: 256q4@gmail.com</p>
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
