import json
import os, shutil

#create_vote_template():

USER_FOLDER = os.path.dirname(os.path.abspath(__file__))
# user_home = os.path.join(USER_FOLDER+"/templates/users", "")
# abc='abc.html'
# poll_user_home = os.path.join(USER_FOLDER + "/templates/users/create_polls", abc)
# base_create_poll_template = os.path.join(USER_FOLDER+"/templates", "create_polling.html")
# shutil.copy(base_create_poll_template, poll_user_home)


uname='swapnilj'
poll_key='food_3'
PAGE_HOME = os.path.join(USER_FOLDER + "/static/users/"+uname, poll_key+".json")
def fetch_page_stats_from_json(PAGE_HOME):
    vote_json = PAGE_HOME
    with open(vote_json) as v:
        v1 = json.load(v)
        for k,v in v1.items():
            if k not in ("uname", "title","contestants"):
                print(k,v)

fetch_page_stats_from_json(PAGE_HOME)