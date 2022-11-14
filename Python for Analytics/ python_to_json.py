celebrity = {}
celebrity ['Styles'] = {
    'name': 'Harry Styles',
    'singer': True,
    'genres': 'pop',
    'single': True,
    'instruments' :'vocal',
    'album': 'Harrys Home',
    'tour':'Love on Tour',
    'member of': 'One Direction'
}

import json
with open("celebrity.json","w") as f:
    json.dump(celebrity, f)
with open("celebrity.json") as f:
    c = json.load(f)
print(json.dumps(c, sort_keys=True, indent=4))