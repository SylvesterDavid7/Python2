import json

with open('file.json') as f:
  data = json.load(f)
  
  h = list(filter(lambda i: i['type'] == "URL", filter(lambda x: x['type'], [e for elements in list(map(lambda y: y['indicators'], data['data'])) for e in elements])))
  
  print(h)
