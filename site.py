from flask import Flask
app = Flask(__name__)

from flask.ext.wtf import Form, TextField, Required

from hscrape import *

@app.route('/')
def hello_world():
    return 'sup!'


def chatvisForm():
    otherName = TextField('otherName', validators = [Required()])
    searchText = TextField('searchText', validators = [Required()])

@app.route('/chatvis')
def chatvis():
    form = chatvisForm()
    render_template('chatvis.html',
            form = form)

if __name__ == '__main__':
    app.debug = True
    app.run()
