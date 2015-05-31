from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return redirect('https://github.com/gtkesh/hedwig')

if __name__ == "__main__":
    app.run()
