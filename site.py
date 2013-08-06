from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from flask import jsonify, render_template, request

from flask.ext.wtf import Form, TextField, Required, validators

from hscrape import *

@app.route('/')
def hello_world():
    return 'sup!'


class chatvisForm(Form):
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

@app.route('/chatvis', methods=['GET', 'POST'])
def chatvis():
    form = chatvisForm(request.form)
    render_template('chatvis.html',
            title="blargl",
            form=form)

if __name__ == '__main__':
    app.run(debug = True)
