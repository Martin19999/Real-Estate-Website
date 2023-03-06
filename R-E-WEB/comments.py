#!/usr/local/bin/python3

from cgitb import enable
enable()
from html import escape

import sys
sys.path.append("/Users/realmartt/miniforge3/lib/python3.9/site-packages")

commentbutton = False

def get_comments(commentbutton):
    from cgi import FieldStorage
    import mysql.connector as db
    from os import environ

    comments = ''
    url = environ.get('SCRIPT_NAME')
    try:
        connection = db.connect(host='localhost',user='jf14',password='11229870',database='jf14')
#        cursor = connection.cursor(db.cursors.DictCursor)
#        form_data = FieldStorage()
#        if len(form_data) != 0:
#            username = escape(form_data.getfirst('username').strip())
#            new_comment = escape(form_data.getfirst('new_comment').strip())
#            cursor.execute("""INSERT INTO comments_table (username, url, comment)
#                              VALUES (%s, %s, %s)""", (username, url, new_comment))
#            connection.commit()
#        cursor.execute("""SELECT * FROM comments_table
#                          WHERE url = %s
#                          ORDER BY comment_id """, (url))
#        for row in cursor.fetchall():
#            comments += '<article><h1>%s</h1><p>%s</p></article>' % (row['username'], row['comment'])
#        cursor.close()
        connection.close()
    except db.Error:
        comments = '<p>Sorry!! We are experiencing problems at the moment. Please call back later.</p>'

    if commentbutton:
        return """
                <section id="comments">
                    <h1>Comments</h1>
                    <form action="%s" method="post">
                        <fieldset>
                            <legend>Post a new comment</legend>
                            <label for="username">Name:</label>
                            <input type="text" name="username" id="username" />
                            <label for="new_comment">Comment:</label>
                            <textarea name="new_comment" id="new_comment" rows="5" cols="50">
                            </textarea>
                            <input type="submit" />
                        </fieldset>
                    </form>
                    <div class="comments">
                        %s
                    </div>
                </section>""" % (url, comments)
    else:
        return """
                <section id="comments">
                    <h1>Comments</h1>
                    <form action="%s" method="post">
                        <fieldset>
                            <legend>Log in to post a new comment</legend>

                            <label for="username">Name:</label>
                            <input type="text" name="username" id="username" size="40" disabled/>
                            <label for="new_comment">Comment:</label>
                            <textarea name="new_comment" id="new_comment" rows="5"  disabled></textarea>
                            <input type="submit" disabled/>

                        </fieldset>
                    </form>
                    <span class="comments">
                        %s
                    </span>
                </section>""" % (url, comments)
