from flask import Flask, render_template, Response, request, redirect, url_for
import voteout_functions as vfs

app = Flask(__name__)



@app.route('/voteout', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/voteout/pets')
def vote_pets():
    return render_template('pets.html')


@app.route('/voteout/pet/status', methods=['POST', 'GET'])
def cat_status():
    cat, dog, total = vfs.current_votes()
    total = total + 1
    if request.method == 'POST':
        # print(request.form.get('pet'))
        if request.form['pet'] == 'kitty':
            cat = cat + 1
            vfs.update_votes(cat, dog)
            my_pet='CAT'
            vote_stat = "{} has {} out of {} votes".format(my_pet, cat, total)
        elif request.form['pet'] == 'doggy':
            dog = dog + 1
            vfs.update_votes(cat, dog)
            my_pet='DOG'
            vote_stat = "{} has {} out of {} votes".format(my_pet, dog, total)
        else:
            pass
    voted = "You have voted for {}. Vote registered".format(my_pet)
    return render_template('pets_voted.html', voted=voted, vote_stat=vote_stat)


@app.route('/create_polling', methods=['POST', 'GET'])
def create_polling():
    uname = request.form.get('Name')
    poll = request.form.get('poll')
    contestants = request.form.get('contestants')
    email = request.form.get('email')
    return "hi {}! Work in progress...!!!".format(uname)


@app.route('/')
def server_status():
    return "Server is running at http://127.0.0.1:5000/voteout!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8025)
