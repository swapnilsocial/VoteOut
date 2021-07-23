from flask import Flask, render_template, Response, request, redirect, url_for
import voteout_functions as vfs
import os

app = Flask(__name__)

USER_FOLDER = os.path.dirname(os.path.abspath(__file__))

# Landing Page
@app.route('/voteout', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


# Call demo voting page -pets
@app.route('/voteout/pets')
def vote_pets():
    return render_template('pets.html')


# Post status of demo voting page
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


# call form from index
@app.route('/create_polling', methods=['POST', 'GET'])
def create_polling():
    uname = request.form.get('Name').lower()
    title = request.form.get('title')
    theme = request.form.get('theme')
    contestants = int(request.form.get('contestants'))
    poll_key = theme + "_" + str(contestants)
    user_status = vfs.get_user_details(uname)
    template_name = vfs.create_poll_template(contestants, poll_key, uname)
    page = '/users/' + uname + '/' + template_name
    # time.sleep(2)
    return render_template(page, user_status=user_status, poll_key=poll_key, title=title, theme=theme, uname=uname)


# create a dynamic route and page for any voting scenario
@app.route('/<uname>/<poll_key>/<title>/votenow', methods=['GET', 'POST'])
def vote_now(uname, poll_key, title):
    uname = uname
    poll_key = poll_key.strip()
    PAGE_HOME = os.path.join(USER_FOLDER + "/static/users/" + uname, poll_key + ".json")
    num_contestants = int(poll_key.split('_')[1])
    theme = poll_key.split('_')[0]
    title = title
    contestant_dict = {}
    list_con = []
    if os.path.isfile(PAGE_HOME):
        vfs.fetch_page_stats_from_json(PAGE_HOME)
        pass
    else:
        if request.method == 'POST':
            for i in range(1, num_contestants + 1):
                value = request.form.get('text_title{}'.format(i))
                contestant_dict.update({value: 0})
                list_con.append(value)
            user_dictionary = {"uname": uname, "title": title, "contestants": num_contestants}
            user_dictionary.update(contestant_dict)
        # load data in json
        vfs.update_votes_dynamic(uname, poll_key, user_dictionary)
        vfs.dynamic_vote_template(poll_key, uname, list_con)
        url = 'http://192.168.62.35:8025/' + uname + '/' + poll_key + '/' + title + '/votenow'
        template_name = vfs.dynamic_vote_template(poll_key, uname, list_con)
        page = '/users/' + uname + '/' + template_name
    return render_template(page, poll_key=poll_key, title=title, theme=theme, uname=uname)


# DYNAMIC VOTING PAGE
@app.route('/<uname>/<poll_key>/<title>/vote', methods=['GET', 'POST'])
def dynamic_vote(uname, poll_key, title):
    return "Vote stats to be printed here"


# check server is up or not?
@app.route('/')
def server_status():
    return "Server is up and running!"


# run flask and expose ip and port
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8025)
