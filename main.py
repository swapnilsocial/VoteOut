import json
import os

USER_FOLDER = os.path.dirname(os.path.abspath(__file__))
user_home = os.path.join(USER_FOLDER+"/templates/users", "")

def new_user_readiness(uname='default'):
    folder_name=user_home + uname
    os.mkdir(folder_name)

new_user_readiness("Swapnil")