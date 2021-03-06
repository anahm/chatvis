from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from flask import jsonify, render_template, request
from flask.ext.wtf import Form, TextField, Required, validators

from hscrape import *

@app.route('/')
def hello_world():
    return 'sup!'


class ChatvisForm(Form):
    otherName = TextField('otherName', validators = [Required()])
    searchText = TextField('searchText', validators = [Required()])

@app.route('/chatvisForm', methods = ['GET', 'POST'])
def chatvisFormProcess():
    otherName = request.values.get('otherName')
    searchText = request.values.get('searchText')

    # now to do the work...
    convo = getAliFile(otherName)
    if (convo == None):
        return jsonify(convoLen = 0, strCounter = 0)
    numStr = phraseCount(convo, searchText)

    return jsonify(convoLen = len(convo), strCounter = numStr)

@app.route('/chatvis', methods = ['GET', 'POST'])
def chatvis():
    form = ChatvisForm()
    if form.validate_on_submit():
        flash('otherName="' + form.otherName.data + '", searchText=' + form.searchText.data)
        return redirect('/')
    return render_template('chatvis.html',
        title = 'blargl',
        form = form)

if __name__ == '__main__':
    app.run(debug = True)
