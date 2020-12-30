import os
from flask import Flask, render_template, request, redirect, flash, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './files'
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
PORT = 5000
DEBUG = True
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

@app.route('/', methods=['GET'])
def index():
    return render_template('grapher/load_file.html')

@app.route('/us', methods=['GET'])
def us():
    return render_template('about/us.html')

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        # recibir el archivo 
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        # revisar que sea del tipo csv
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #De serlo, ir a la nueva pagina una vez subido
            return redirect(url_for('uploaded', filename=filename))
        #Sino, seguir en la misma pagina, agregar el mensaje de errors
    return redirect(url_for('index'))

@app.route('/uploaded', methods=['GET'])
def uploaded():
    return render_template('grapher/uploaded_file.html')


if __name__ == '__main__':
    app.run(port=PORT, debug=DEBUG)
