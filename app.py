import os


from flask import Flask, request, Response, redirect
app = Flask(__name__)


@app.route("/")
def hello():
    return redirect('https://github.com/gtkesh/hedwig')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)
