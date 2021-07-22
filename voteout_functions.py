import json
import os, shutil
import re

USER_FOLDER = os.path.dirname(os.path.abspath(__file__))
vote_file = os.path.join(USER_FOLDER, 'votes.json')
users_file = os.path.join(USER_FOLDER + "/all_users", 'users.json')
template_user_home = os.path.join(USER_FOLDER + "/templates/users", "")
static_user_home = os.path.join(USER_FOLDER + "/static/users", "")
base_create_poll_template = os.path.join(USER_FOLDER + "/templates", "create_polling.html")


def update_votes(cat_votes, dog_votes):
    D = {'cats': cat_votes, 'dogs': dog_votes}
    with open(vote_file, 'w')as f:
        json.dump(D, f)


def new_user_readiness(uname='default'):
    template_folder_name = template_user_home + uname
    os.mkdir(template_folder_name)
    static_folder_home = static_user_home + uname
    os.mkdir(static_folder_home)


def current_votes():
    with open(vote_file) as v:
        v1 = json.load(v)
        cat_votes = v1.get('cats')
        dog_votes = v1.get('dogs')
        total_votes = sum(v1.values())
        return cat_votes, dog_votes, total_votes


def get_user_details(uname):
    user_details = uname.lower()
    with open(users_file) as uf:
        uf1 = json.load(uf)
    l = len(uf1)
    if user_details in uf1:
        return "Welcome Back {}..!!".format(uname.capitalize())
    uf1.append(user_details)
    with open(users_file, 'w')as f:
        json.dump(uf1, f)
    new_user_readiness(user_details)
    return "Hi {}! Your username is registered.".format(uname.capitalize())


# defining the replace method
def replace(file_path, text, subs, flags=0):
    with open(file_path, "r+") as file:
        file_contents = file.read()
        text_pattern = re.compile(re.escape(text), flags)
        file_contents = text_pattern.sub(subs, file_contents)
        file.seek(0)
        file.truncate()
        file.write(file_contents)


def create_poll_template(n, pk):
    n = n + 1
    template = ''' <p style="color:red"><span style="background-color:#00FF00">Contestant {} : </span><input class="a" type="text" required name="text_title{}"></p> 
    '''
    magic_list = []
    for i in range(1, n):
        magic_list.append(template.format(i,i))
    poll_template = ''''''
    for i in range(len(magic_list)):
        poll_template = poll_template + magic_list[i]
    pk = pk + '.html'
    poll_user_home = os.path.join(USER_FOLDER + "/templates/users/create_polls", pk)
    shutil.copy(base_create_poll_template, poll_user_home)
    replace(poll_user_home, 'magic_template_replace_here', poll_template)
    return pk
