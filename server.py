from flask import Flask, render_template, Response, Request, redirect, url_for

app = Flask(__name__)

def add_votes():
    with open('votes.json') as v:
        pass

@app.route('/voteout')
def index():
    return render_template('index.html')

@app.route('/voteout/pets')
def vote_pets():
    return render_template('pets.html')

@app.route('/voteout/cat/status' ,methods=['POST'])
def cat_status():
    voted = "You have voted for CAT. Vote registered"
    return render_template('pets_voted.html', voted=voted)

@app.route('/voteout/dog/status' ,methods=['POST'])
def dog_status():
    voted = "You have voted for Dog. Vote registered"
    return render_template('pets_voted.html', voted=voted)

@app.route('/')
def server_status():
    return "Server is running at http://127.0.0.1:5000/voteout!"


app.run(debug=True)
