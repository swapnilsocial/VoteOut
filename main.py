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

Dict={"delhi": 0, "mumbai": 0, "pune": 0}
dic_len=len(Dict)
all_keys= Dict.keys()
for i in range(0, dic_len):
        print(type(all_keys))
#             updated_result = {all_keys[i], result.get(all_keys[i])}
#             print(updated_result)
# result.update(updated_result)
