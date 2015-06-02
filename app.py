import os
import requests
import json
from flask import Flask, request, Response, redirect, send_file, json
import giphypop
from giphypop import translate
from slacker import Slacker


token = 'SLACK_TOKEN'
slack = Slacker(token)
app = Flask(__name__)
key = 'dc6zaTOxFJmzC' #Giphy public key
g = giphypop.Giphy(api_key=key, strict=True)

@app.route('/')
def hello():
    return redirect('https://github.com/gtkesh/hedwig')


@app.route('/hedwig', methods=['post'])
def hedwig():
    keyword = request.values.get('text')
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

    slack.chat.post_message('#bullshit', filename, username='Hedwig')
    return ''

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
