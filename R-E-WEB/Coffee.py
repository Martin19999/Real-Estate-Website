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
                result = """<a href='addtofav.py?house_id=4' class='icon'>&nbsp &#10084 &nbsp</a>
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
            <title>Coffee Road</title>
            <link rel="stylesheet" href="styles.css" />
            <script src="Slideshow.js" type="module"></script>
        </head>
        <body>
            <main class="detailmain">
                <section id="slide">
                    <ul class="slideshow">
                        <li><img src="c0.jpg" alt="Frontview"/></li>
                        <li><img src="c1.jpg" alt="Dining Area"/></li>
                        <li><img src="c2.jpg" alt="Living Room" /></li>
                        <li><img src="c3.jpg" alt="Bedroom" /></li>
                    </ul>
                </section>
                <section id="text">
                    <div class="plb">
                        <a href="index.html">Home</a><span><</span><a href="chooseyourplace.py">Map</a><span><</span><a href="browse.py">Houses</a>
                        %s
                    </div>
                    <h1>Cannon, County Canvas, H12 VW71</h1>
                    <p><img src="iconbed.jpg" class="icon"></img>2 <img src="iconbath.jpg" class="icon"></img>3<img src="iconarea.jpg" class="icon"></img> 201&#13217 &nbsp &nbsp Apartment</p>
                    <p>Price: &#8364 905,000</p>
                    <p class="intro">Located in a metropolitan area, these apartments are actully not that expensive compared to other big cities in the world.\
                                     Featuring 2 en-suites and an independent bathroom, luxury is redefined.\
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
