import json
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
vote_file = os.path.join(THIS_FOLDER, 'votes.json')

def update_votes(cat_votes, dog_votes):
    D = {'cats': cat_votes, 'dogs': dog_votes}
    with open(vote_file, 'w')as f:
        json.dump(D, f)


def current_votes():
    with open(vote_file) as v:
        v1 = json.load(v)
        cat_votes = v1.get('cats')
        dog_votes = v1.get('dogs')
        total_votes = sum(v1.values())
        return cat_votes, dog_votes, total_votes
