from flask import Flask

from apps.sample.views import sample_bp


app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Flask!"

app.register_blueprint(sample_bp)

if __name__ == '__main__':
    app.run(debug=True)