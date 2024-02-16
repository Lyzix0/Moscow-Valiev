from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def image(prof):
    return render_template('second.html', prof=prof)


@app.route('/list_prof/<string:list>')
def list_prof(list):
    return render_template('third.html', list=list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
