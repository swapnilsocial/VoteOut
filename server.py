from flask import Flask, render_template

app = Flask(__name__)

@app.route('/voteout')
def voteout():
    return render_template('index.html')

@app.route('/pets')
def vote_pets():
    return render_template('pets.html')

@app.route('/')
def serverstatus():
    return "Server is running at http://127.0.0.1:5000/voteout!"
app.run(debug=True)