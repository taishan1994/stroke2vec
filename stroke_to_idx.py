import json


stroke2id = {}
id2stroke = {}
res = []
with open('./data/stroke.txt','r') as fp:
    strokes = fp.read().strip().split('\n')
    for i,stroke in enumerate(strokes):
        stroke = stroke.split(' ')
        stroke2id[stroke[0]] = i
        id2stroke[i] = stroke[0]
    res.append(stroke2id)
    res.append(id2stroke)

with open('./data/stroke2id.json','w',encoding='utf-8') as fp:
    fp.write(json.dumps(res, ensure_ascii=False))