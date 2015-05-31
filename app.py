import os

from flask import Flask, request, Response, redirect
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
    gif     = translate(keyword)

    try:
        return Response(g.random_gif(keyword).media_url,
                        mimetype='image/gif')
    except GiphyApiException:
        try:
            return Response(g.translate(keyword).media_url,
                            mimetype='image/gif')
        except GiphyApiException:
            try:
                return Response(g.search_list(keyword, limit=1)[0].media_url,
                                mimetype='image/gif')
            except (GiphyApiException, IndexError):
                    pass


    return random.choice(responses)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
