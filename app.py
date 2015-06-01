import os
import requests
import json
import pyslack
import logging
from flask import Flask, request, Response, redirect, send_file, json
import giphypop
from giphypop import translate
from pyslack import SlackClient

client = SlackClient('xoxp-5029789749-5008179958-5152873814-1e2b32')
app = Flask(__name__)

key = 'dc6zaTOxFJmzC'
g = giphypop.Giphy(api_key=key, strict=True)

responses = [
    "That sucks...",
    "Can't find shit, sorry man..."
]

@app.route('/')
def hello():
    return redirect('https://github.com/gtkesh/hedwig')


@app.route('/hedwig', methods=['post'])
def hedwig():
    keyword = request.values.get('text')
    logging.info('passed keyword', keyword)
    gif     = translate(keyword)
    filename = 'https://media1.giphy.com/media/fAT2Db0j0Mblu/200_s.gif'
    try:
        filename = g.random_gif(keyword).media_url
    except GiphyApiException:
        try:
            filename = g.translate(keyword).media_url
        except GiphyApiException:
            try:
                filename = g.search_list(keyword, limit=1[0]).media_url
            except (GiphyApiException, IndexError):
                    pass
    return client.chat_post_message('#general', "test,testtttt", username='Hedwig')
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
