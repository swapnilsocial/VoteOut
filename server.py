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
    uname = request.form.get('Name').lower()
    title = request.form.get('title')
    theme = request.form.get('theme')
    contestants = int(request.form.get('contestants'))
    poll_key=uname+"_"+theme+"_"+str(contestants)
    user_status=vfs.get_user_details(uname)
    return render_template('create_polling.html', uname=uname, user_status=user_status, poll_key=poll_key, title=title)

@app.route('/<uname>/<poll_key>/votenow', methods=['GET'])
def vote_now(uname, poll_key):
    uname=uname
    poll_key=poll_key
    #write logic of a dynamic template here
    return "Vote now for {}".format(poll_key)

@app.route('/')
def server_status():
    return "Server is running!"



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8025)
