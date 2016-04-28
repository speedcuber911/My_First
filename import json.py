import json
import os
data = []
with open('ipca_class.json' , 'r') as f:
    for line in f:
        data.append(json.loads(line)