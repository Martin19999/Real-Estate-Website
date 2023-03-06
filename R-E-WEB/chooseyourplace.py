#!/usr/bin/python3

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
      <html lang="en" id="chooseyourplace">
          <head>
              <meta charset="utf-8" />
              <title>Choose Your Place</title>
              <link rel="stylesheet" href="styles.css" />
          </head>
          <body>
              <header>
                  <h1>Choose Your Place</h1>
              </header>
              <main>
                  <nav>
                      <div class="path">
                          &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<a href="index.html">Home</a>
                      </div>
                      <div class="log">
                          %s
                      </div>
                  </nav>
                  <div class="f">
                      <br><br><br><br><br><br><br><br>
                      <p>Welcome to this beautiful island! In case you didn't know, we build identical houses within a certain place. So you don't have to worry about your dream house alreday taken by others----you probably can have the same one too!</p>
                      <br><br>
                      <p>You can select the house by location using the map!</p>
                      <br><br><br><br>
                      <a href="browse.py">I prefer sorting by houses</a>
                  </div>
                  <div class="s">
                      <img src="map.jpg"></img>
                      <ul id="chooseplace">
                          <li class="A"><a href="Dream.py">Dream River</a></li>
                          <li class="B"><a href="High.py">High Island</a></li>
                          <li class="C"><a href="Coffee.py">Coffee Road</a></li>
                          <li class="D"><a href="Gin.py">Gin</a></li>
                          <li class="E"><a href="Brown.py">Brown Curtain Mountain</a></li>
                          <li class="F"><a href="King.py">King's Palace</a></li>
                      </ul>
                  </div>
              </main>
              <footer>
                  <p><small>&copy Jianhao Feng. All rights reserved</small></p>
              </footer>
          </body>
      </html>"""%(result))

