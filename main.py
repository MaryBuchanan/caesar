#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from caesar import encrypt

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Ceasar</title>
    <style type = "text">
    </style>
</head>
<body>
    <h1>
        <a href = "/">Caesar</a>
    </h1>
"""
page_footer = """
</body>
</html>
"""



class MainHandler(webapp2.RequestHandler):
    """Handles requests"""
    def get(self):
        #edit_header = "<h1>Caesar Cipher</h1>"
        #add the form
        cipher = self.request.get("cipher")

        add_form = """
        <form action = "/cipher" method = "post">
            <label>
                <br>
                Rotate by:
                <input type = "text" name = "rotate"/>
            </label>
            <br>
            <br>
            <br>
            <label>
                Text:
                <input type = "text" name = "text" style = "height:150px; width:300px" value="{}"/>
            </label>
            <br>
            <br>
            <br>
            <input type = "submit" value = "Submit"/>
        </form>
        """.format(cipher)
        self.response.write(page_header + add_form + page_footer)

class CaesarCipher(webapp2.RequestHandler):
    """Takes care of cipher"""
    def post(self):
        #looks to see what the user typed
        text = self.request.get("text")
        rotate = self.request.get("rotate")
        cipher = encrypt(text, rotate)
        self.redirect("/?cipher={}".format(cipher))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/cipher', CaesarCipher)
], debug=True)
