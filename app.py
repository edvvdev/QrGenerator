#generar  y mostrar codigo qr con flask

from flask import Flask, render_template, request, redirect, url_for
from flask_qrcode import QRcode
import qrcode
import os

app = Flask(__name__)
QRcode(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generar', methods=['POST'])
def generar():
    if request.method == 'POST':
        codigo = request.form['codigo']
        img = qrcode.make(codigo)
        img.save('static/img/qr.png')
        return redirect(url_for('index'))

#borrar imagen en carpeta static/img/qr al inciar el servidor
@app.before_first_request
def borrar():
    try:
        os.remove('static/img/qr.png')
    except:
        pass


if __name__ == '__main__':
    app.run(debug=True)


    