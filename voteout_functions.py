import json
import os


USER_FOLDER = os.path.dirname(os.path.abspath(__file__))
vote_file = os.path.join(USER_FOLDER, 'votes.json')
users_file = os.path.join(USER_FOLDER+"/all_users", 'users.json')
template_user_home = os.path.join(USER_FOLDER+"/templates/users", "")
static_user_home = os.path.join(USER_FOLDER+"/static/users", "")

def update_votes(cat_votes, dog_votes):
    D = {'cats': cat_votes, 'dogs': dog_votes}
    with open(vote_file, 'w')as f:
        json.dump(D, f)

def new_user_readiness(uname='default'):
    template_folder_name=template_user_home + uname
    os.mkdir(template_folder_name)
    static_folder_home=static_user_home+ uname
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
            return"Welcome back!"
    uf1.append(user_details)
    with open(users_file, 'w')as f:
        json.dump(uf1, f)
    new_user_readiness(user_details)
    return "User details registered."