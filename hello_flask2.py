
from flask import Flask

from vsearch import search4letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/search')
def do_search() -> str:
    """Calls search4letters() and returns string of found letters."""
    return str(search4letters('bwabeldoupe is the word!',))

app.run()


