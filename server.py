from flask import Flask, render_template, Response, request, redirect, url_for
import voteout_functions as vfs
import time

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
            my_pet = 'CAT'
            vote_stat = "{} has {} out of {} votes".format(my_pet, cat, total)
        elif request.form['pet'] == 'doggy':
            dog = dog + 1
            vfs.update_votes(cat, dog)
            my_pet = 'DOG'
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
    poll_key = uname + "_" + theme + "_" + str(contestants)
    user_status = vfs.get_user_details(uname)
    template_name = vfs.create_poll_template(contestants, poll_key)
    page='/users/create_polls/'+template_name
    # time.sleep(2)
    return render_template(page, user_status=user_status, poll_key=poll_key, title=title, theme=theme, uname=uname)


@app.route('/<uname>/<poll_key>/<title>/votenow', methods=['GET', 'POST'])
def vote_now(uname, poll_key, title):
    uname = uname
    poll_key = poll_key
    num_contestants=int(poll_key.split('_')[2]) + 1
    title=title
    contenstant_list=[]
    if request.method == 'POST':
        for i in range(1, num_contestants):
            contenstant_list.append(request.form.get('text_title{}'.format(i)))
    print(contenstant_list)
    url='http://192.168.62.35:8025/'+uname+'/'+poll_key+'/'+title+'/votenow'
    # title = request.form.get('title')
    # write logic of a dynamic template here
    return "Share this url for voting - {}".format(url)


@app.route('/')
def server_status():
    return "Server is running!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8025)
