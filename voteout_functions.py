import json


def update_votes(cat_votes, dog_votes):
    D = {'cats': cat_votes, 'dogs': dog_votes}
    with open('votes.json', 'w')as f:
        json.dump(D, f)


def current_votes():
    with open('votes.json') as v:
        v1 = json.load(v)
        cat_votes = v1.get('cats')
        dog_votes = v1.get('dogs')
        total_votes = sum(v1.values())
        return cat_votes, dog_votes, total_votes
