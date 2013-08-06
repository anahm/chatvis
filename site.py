from flask import Flask
from flask import jsonify, render_template, request
app = Flask(__name__)

from flask.ext.wtf import Form, TextField, Required

from hscrape import *

@app.route('/')
def hello_world():
    return 'sup!'


def chatvisForm():
    otherName = TextField('otherName', validators = [Required()])
    searchText = TextField('searchText', validators = [Required()])

@app.route('/chatvisForm')
def chatvisFormProcess():
    otherName = request.values.get('otherName')
    searchText = request.values.get('searchText')

    # now to do the work...
    convo = getAliFile(otherName)
    if (convo == None):
        return jsonify(convoLen = 0, strCounter = 0)
    numStr = phraseCount(convo, searchText)

    return jsonify(convoLen = len(convo), strCounter = numStr)

@app.route('/chatvis')
def chatvis():
    form = chatvisForm()
    if (form):
        render_template('chatvis.html', form = form)

if __name__ == '__main__':
    app.debug = True
    app.run()
