import os
import requests
import json
import logging
from flask import Flask, request, Response, redirect, send_file, json
import giphypop
from giphypop import translate
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
    payload = {'text': 'muteli'}
    requests.post('https://hooks.slack.com/services/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',
                  payload)
    return 'hey'

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
