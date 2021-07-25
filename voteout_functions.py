import json
import os
import shutil
import re
from pathlib import Path

## define all path variables here.
USER_FOLDER = os.path.dirname(os.path.abspath(__file__))
vote_file = os.path.join(USER_FOLDER, 'votes.json')
users_file = os.path.join(USER_FOLDER + "/all_users", 'users.json')
template_user_home = os.path.join(USER_FOLDER + "/templates/users", "")
static_user_home = os.path.join(USER_FOLDER + "/static/users", "")
base_create_poll_template = os.path.join(USER_FOLDER + "/templates", "create_polling.html")
base_create_vote_template = os.path.join(USER_FOLDER + "/templates", "polling_vote.html")
base_create_status_template = os.path.join(USER_FOLDER + "/templates", "polling_status.html")


# fetch sample votes
def update_votes(cat_votes, dog_votes):
    D = {'cats': cat_votes, 'dogs': dog_votes}
    with open(vote_file, 'w')as f:
        json.dump(D, f)


# fetch votes for demo and reflect back
def current_votes():
    with open(vote_file) as v:
        v1 = json.load(v)
        cat_votes = v1.get('cats')
        dog_votes = v1.get('dogs')
        total_votes = sum(v1.values())
        return cat_votes, dog_votes, total_votes


# set paths and folders for NEW user
def new_user_readiness(uname='default'):
    template_folder_name = template_user_home + uname
    os.mkdir(template_folder_name)
    static_folder_home = static_user_home + uname
    os.mkdir(static_folder_home)


# check user status and call other functions for new users
def get_user_details(uname):
    user_details = uname.lower()
    with open(users_file) as uf:
        uf1 = json.load(uf)
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


# this function will create the templates for designing user voting scenario
def create_poll_template(n, pk, uname):
    n = n + 1
    uname = uname
    template = '''<span class="textfield" >Contestant {}</span> <input type="text" placeholder="type here" required name="text_title{}"></br> '''
    magic_list = []
    for i in range(1, n):
        magic_list.append(template.format(i, i, i))
    poll_template = ''''''
    for i in range(len(magic_list)):
        poll_template = poll_template + magic_list[i]
    pk = pk + '.html'
    poll_user_home = os.path.join(USER_FOLDER + "/templates/users/" + uname, pk)
    shutil.copy(base_create_poll_template, poll_user_home)
    replace(poll_user_home, 'magic_template_replace_here', poll_template)
    return pk


# create user data dictionary and updated for each run
def update_votes_dynamic(uname, poll_key, user_dictionary):
    user_dictionary = user_dictionary
    dynamic_vote_file = os.path.join(USER_FOLDER + "/static/users/" + uname, poll_key + '.json')
    with open(dynamic_vote_file, 'w')as f:
        json.dump(user_dictionary, f)


def dynamic_vote_template(pk, uname, list_con):
    list_con = list_con
    n = len(list_con)
    uname = uname
    template = '''<button value="{}" type="submit" name="elector" class="a" >{}</button></br>
    '''
    magic_list = []
    for i in range(0, n):
        v = list_con[i]
        magic_list.append(template.format(v, v))
    voter_template = ''''''
    for i in range(len(magic_list)):
        voter_template = voter_template + magic_list[i]
    pk = pk + '_vote.html'
    poll_user_home = os.path.join(USER_FOLDER + "/templates/users/" + uname, pk)
    shutil.copy(base_create_vote_template, poll_user_home)
    replace(poll_user_home, 'polling_template_replace_here', voter_template)
    return pk


def dynamic_status_template(pk, uname, list_con):
    list_con = list_con
    n = len(list_con)
    uname = uname
    template = '''<button value="{}" type="submit" name="elector" class="a" >{}</button></br>
    '''
    magic_list = []
    for i in range(0, n):
        v = list_con[i]
        magic_list.append(template.format(v, v))
    voter_template = ''''''
    for i in range(len(magic_list)):
        voter_template = voter_template + magic_list[i]
    pk = pk + '_vote.html'
    poll_user_home = os.path.join(USER_FOLDER + "/templates/users/" + uname, pk)
    shutil.copy(base_create_vote_template, poll_user_home)
    replace(poll_user_home, 'polling_template_replace_here', voter_template)
    return pk


def ip_check_add(uname, poll_key, ip):
    ip_path = os.path.join(static_user_home + '/' + uname, poll_key + '_ip.json')
    if os.path.exists(ip_path):
        pass
    else:
        Path(ip_path).touch()
        with open(ip_path, 'w') as f:
            json.dump([], f)
    with open(ip_path) as ip_adr:
        ip_adr1 = json.load(ip_adr)
    if ip in ip_adr1:
        # true means ip was found
        return "no"
    ip_adr1.append(ip)
    print(ip_adr1)
    with open(ip_path, 'w')as f:
        json.dump(ip_adr1, f)
        # False means ip was not found. User can vote
    return "yes"


def fetch_page_stats_from_json(PAGE_HOME):
    vote_json = PAGE_HOME
    with open(vote_json) as v:
        v1 = json.load(v)
        data_set = {}
        for k, v in v1.items():
            if k not in ("uname", "title", "contestants"):
                data_set.update({k: v})
    return data_set


def dynamic_vote_register(uname, poll_key, result):
    user_dictionary = result
    dynamic_vote_file = os.path.join(USER_FOLDER + "/static/users/" + uname, poll_key + '.json')
    with open(dynamic_vote_file) as v:
        v1 = json.load(v)
    v1.update(user_dictionary)
    with open(dynamic_vote_file, 'w')as f:
        json.dump(v1, f)
    return "Your vote is registered"