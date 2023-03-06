#!/usr/local/bin/python3

from cgitb import enable
enable()

from os import environ
from shelve import open
from http.cookies import SimpleCookie


print('Content-Type: text/html')
print()

result = """<a href="login.py">Log in</a>
            <a href="register.py">Sign up</a>"""

try:
    cookie = SimpleCookie()
    http_cookie_header = environ.get('HTTP_COOKIE')
    if http_cookie_header:
        cookie.load(http_cookie_header)
        if 'sid' in cookie:
            sid = cookie['sid'].value
            session_store = open('sess_' + sid, writeback=False)
            if session_store.get('authenticated'):
                result = """<a href="showfav.py">My &#9829</a>
                            <a href="logout.py">Log Out</a>"""
            session_store.close()
except IOError:
    result = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'

print("""
      <!DOCTYPE html>
            <html lang="en" id="browse">
                <head>
                    <meta charset="utf-8" />
                    <title>Find Your House</title>
                    <link rel="stylesheet" href="styles.css" />
                </head>
                <body>
                    <header>
                        <h1>Find Your House</h1>
                    </header>
                    <nav>
                        <div class="path">
                            <a href="index.html">Home</a><span><</span><a href="chooseyourplace.py">Map</a>
                        </div>
                        <div class="log">

                            %s
                        </div>
                    </nav>
                    <main>
                        <section class="Dream River">
                            <h1>Dream River</h1>
                            <figure>
                                <a href="Dream.py">
                                    <img src="Dream0.jpg" width="300em" />
                                </a>
                                <figcaption>
                                    <p>Castletown Road, County Louth, A91 C9F7</p>
                                    <p><img src="iconbed.jpg" class="icon"></img>3 <img src="iconbath.jpg" class="icon"></img>2<img src="iconarea.jpg" class="icon"></img> 211&#13217 &nbsp &nbsp House</p>
                                    Price: &#8364 235,000
                                </figcaption>
                            </figure>
                        </section>

                        <section class="King's Palace">
                            <h1>King's Palace</h1>
                            <figure>
                                <a href="King.py">
                                    <img src="king0.jpg" width="300em" />
                                </a>
                                <figcaption>
                                    Charlemont Street, South City, King
                                    <p><img src="iconbed.jpg" class="icon"></img>12 <img src="iconbath.jpg" class="icon"></img>18<img src="iconarea.jpg" class="icon"></img> 1,094&#13217 &nbsp &nbsp House</p>
                                    Price: &#8364 400,336,000
                                </figcaption>
                            </figure>
                        </section>

                        <section class="Gin">
                            <h1>Gin</h1>
                            <figure>
                                <a href="Gin.py">
                                    <img src="Gin0.jpg" width="300em" />
                                </a>
                                <figcaption>
                                    5348 Buckhannon Pike, Coalton, Gin 26257
                                    <p><img src="iconbed.jpg" class="icon"></img>3 <img src="iconbath.jpg" class="icon"></img>3<img src="iconarea.jpg" class="icon"></img> 277&#13217 &nbsp &nbsp Apartment</p>
                                    Price: &#8364 705,000
                                </figcaption>
                            </figure>
                        </section>

                        <section class="Coffee Road">
                            <h1>Coffee Road</h1>
                            <figure>
                                <a href="Coffee.py">
                                    <img src="c0.jpg" width="300em" />
                                </a>
                                <figcaption>
                                    Cannon, County Canvas, H12 VW71
                                    <p><img src="iconbed.jpg" class="icon"></img>2 <img src="iconbath.jpg" class="icon"></img>3<img src="iconarea.jpg" class="icon"></img> 201&#13217 &nbsp &nbsp Apartment</p>
                                    Price: &#8364 905,000
                                </figcaption>
                            </figure>
                        </section>

                        <section class="Brown Curtain Mountain">
                            <h1>Brown Curtain Mountain</h1>
                            <figure>
                                <a href="Brown.py">
                                    <img src="b0.jpg" width="300em" />
                                </a>
                                <figcaption>
                                    Moynalty, Kells, County Meath
                                    <p><img src="iconbed.jpg" class="icon"></img>3 <img src="iconbath.jpg" class="icon"></img>2<img src="iconarea.jpg" class="icon"></img> 298&#13217 &nbsp &nbsp House</p>
                                    Price: &#8364 191,000
                                </figcaption>
                            </figure>
                        </section>

                        <section class="High Island">
                            <h1>High Island</h1>
                            <figure>
                                <a href="High.py">
                                    <img src="h0.jpg" width="300em" />
                                </a>
                                <figcaption>
                                    Tullow, County Maine, R93 R858
                                    <p><img src="iconbed.jpg" class="icon"></img>7 <img src="iconbath.jpg" class="icon"></img>9<img src="iconarea.jpg" class="icon"></img> 821&#13217 &nbsp &nbsp House</p>
                                    Price: &#8364 5,205,000
                                </figcaption>
                            </figure>
                        </section>


                    </main>
                    <footer>
                        <p><small>&copy Jianhao Feng. All rights reserved</small></p>
                    </footer>
                </body>
            </html>



      """%(result))
