from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        print(request.form['letter'])
    return render_template('game.html')


@app.route('/scoreboard')
def score_board():
    return render_template('scoreboard.html')


app.run(debug=True, port=8080)
