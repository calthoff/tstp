# IF YOU ARE READING THIS YOU ARE READING 
# AN OUTDATED VERSION OF THE BOOK.
# I am working with Amazon to resolve this.
# The new version is much better and has correctly formatted code examples
# In the book.
# Please email me at cory@theselftaughtprogrammer.io
# For an updated version

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"

app.run(port='8000')
