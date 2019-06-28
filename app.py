"""A spell check API using Flask and TextBlob & Python  - Avinash Nahar
This app wraps a very simple JSON interface around TextBlob and provides very
basic spell checking and correction support (english only for now).
"""
# third-party imports
from flask import Flask
from flask import jsonify
from flask import request
from textblob import TextBlob
from textblob import Word


# define Flask app that does all the magic
app = Flask(__name__)

@app.route('/')
def home():
	return "WEOLCOME to Simple Spell Checker"

@app.route('/correction')
def correction():
    text = request.args.get('text', '')
    text = TextBlob(text)
    return jsonify(text=unicode(text.correct()))


@app.route('/spellCorrect')
def spellcheck():
	# test your spelling after the ('text', '<here>')
	# test it via 127.0.0.1:5000/spellCorrect
    text = request.args.get('text', 'Home-work')
    words = {}
    for word in text.split():
        words[word] = Word(word).spellcheck()
    return jsonify(**words)


if __name__ == '__main__':

    # app runs in debug mode, turn this off if you're deploying
    app.run(debug=True)