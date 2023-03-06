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
                result = """<a href='addtofav.py?house_id=5' class='icon'>&nbsp &#10084 &nbsp</a>
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
            <title>Brown Curtain Mountain</title>
            <link rel="stylesheet" href="styles.css" />
            <script src="Slideshow.js" type="module"></script>
        </head>
        <body>
            <main class="detailmain">
                <section id="slide">
                    <ul class="slideshow">
                        <li><img src="b0.jpg" alt="Frontview"/></li>
                        <li><img src="b1.jpg" alt="Dining Area"/></li>
                        <li><img src="b2.jpg" alt="Living Room" /></li>
                        <li><img src="b3.jpg" alt="Bedroom" /></li>
                        <li><img src="b4.jpg" alt="Bathroom"/></li>
                        <li><img src="b5.jpg" alt="Kitchen" /></li>
                    </ul>
                </section>
                <section id="text">
                    <div class="plb">
                        <a href="index.html">Home</a><span><</span><a href="chooseyourplace.py">Map</a><span><</span><a href="browse.py">Houses</a>
                        %s
                    </div>
                    <h1>Moynalty, Kells, County Meath</h1>
                    <p><img src="iconbed.jpg" class="icon"></img>3 <img src="iconbath.jpg" class="icon"></img>2<img src="iconarea.jpg" class="icon"></img> 298&#13217 &nbsp &nbsp House</p>
                    <p>Price: &#8364 191,000</p>
                    <p class="intro">Located in the beautiful countryside, this house really comfortable to live in. It only takes you 7 minutes to\
                                     drive to the supermarkets. And the price is affordable for most people. For a tour to the house or more \
                                     information, please contact Jerry.</p>
                    <div class="idencard">
                      <img src="je.jpg" alt="Avatar" >
                      <div class="line">
                        <h4><b>Jerry Grennan</b></h4>
                        <p>Tel: +353 0875246603</p>
                        <p>E-mail: 125712@gmail.com</p>
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
