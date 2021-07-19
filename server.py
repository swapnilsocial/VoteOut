from flask import Flask, render_template, Response, request, redirect, url_for
import json

app = Flask(__name__)


def current_votes():
    with open('votes.json') as v:
        v1 = json.load(v)
        cat_votes = v1.get('cats')
        dog_votes = v1.get('dogs')
        total_votes = sum(v1.values())
        return cat_votes, dog_votes, total_votes


@app.route('/voteout', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/voteout/pets')
def vote_pets():
    return render_template('pets.html')


@app.route('/voteout/cat/status', methods=['POST', 'GET'])
def cat_status():
    cat, dog, total = current_votes()
    cat = cat + 1
    total = total + 1
    voted = "You have voted for CAT. Vote registered"
    vote_stat = "CAT has {} out of {} votes".format(cat, total)
    return render_template('pets_voted.html', voted=voted, vote_stat=vote_stat)

@app.route('/voteout/dog/status', methods=['POST', 'GET'])
def dog_status():
    cat, dog, total = current_votes()
    dog = dog + 1
    total = total + 1
    voted = "You have voted for DOG. Vote registered"
    vote_stat = "DOG has {} out of {} votes".format(dog, total)
    return render_template('pets_voted.html', voted=voted, vote_stat=vote_stat)

@app.route('/create_polling', methods=['POST', 'GET'])
def create_polling():
    uname=request.form.get('Name')
    poll=request.form.get('poll')
    contestants=request.form.get('contestants')
    email=request.form.get('email')
    return "hi {}! Work in progress...!!!".format(uname)

@app.route('/')
def server_status():
    return "Server is running at http://127.0.0.1:5000/voteout!"


app.run(debug=True, host='0.0.0.0', port=8025)
