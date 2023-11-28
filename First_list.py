from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():

    return render_template('index.html', title = 'Home X-Style')


@app.route('/clothes/')
def clothes():
    context = {'title': 'Эскизы одежды'}
    return render_template('clothes.html', **context)


@app.route('/shoes/')
def shoes():
    context = {'title': 'Обувь'}
    return render_template('shoes.html', **context)

if __name__ == '__main__':
    app.run(debug=True)