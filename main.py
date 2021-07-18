import json

def add_votes():
    with open('votes.json') as v:
        v1=json.load(v)
        cat_votes=v1.get('cats')
        dog_votes=v1.get('dogs')
        total_votes=sum(v1.values())
        print(cat_votes, dog_votes, total_votes)

print(add_votes())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
