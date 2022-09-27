"""Module for Flask/webbrowser use of meme generator."""

import random
import os
import requests
from flask import Flask, render_template, request

from QuoteEngine import Ingestor
from MemeEngine import MemeEngine


app = Flask(__name__)

meme = MemeEngine('./tmp')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"

    imgs = []
    for root, dirs, files in os.walk(images_path):
        for name in files:
            img = os.path.join(root, name)
            imgs.append(img)

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    allowed_extensions = ['jpg', 'png']

    img_url = request.form['image_url']

    ext = img_url.split('.')[-1].lower()

    if ext not in allowed_extensions:
        raise ValueError(f'file type with extension {ext} not valid')

    if img_url != '':
        result = requests.get(img_url, stream=True)

        tmp_file = os.path.join(
            './tmp', f'meme_{random.randint(1, 10000)}.{ext}'
        )

        with open(tmp_file, 'wb') as output:
            output.write(result.content)

    else:
        tmp_file = random.choice(imgs)

    body = request.form.get('body')
    author = request.form.get('author')

    if not body:
        qoute = random.choice(quotes)
        body = qoute.body
        author = qoute.author

    path = meme.make_meme(tmp_file, body, author)

    if img_url:
        os.remove(tmp_file)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
