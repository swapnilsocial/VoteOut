import json
import os,shutil

#create_vote_template():

USER_FOLDER = os.path.dirname(os.path.abspath(__file__))
user_home = os.path.join(USER_FOLDER+"/templates/users", "")
abc='abc.html'
poll_user_home = os.path.join(USER_FOLDER + "/templates/users/create_polls", abc)
base_create_poll_template = os.path.join(USER_FOLDER+"/templates", "create_polling.html")
shutil.copy(base_create_poll_template, poll_user_home)