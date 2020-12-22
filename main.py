from flask import Flask, render_template, request, redirect, flash, url_for


app = Flask(__name__)
PORT = 5000
DEBUG = True

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

@app.route('/', methods=['GET'])
def index():
    return render_template('grapher/load_file.html')


if __name__ == '__main__':
    app.run(port=PORT, debug=DEBUG)
