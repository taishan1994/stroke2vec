from collections import defaultdict
import json


stroke_list = []
strokeid_list = []

with open('stroke_test2.txt','r',encoding='utf-8') as fp:
    data = fp.read().strip()
    data = data.split('\n')
    nid = ''
    char = ''
    bushou = ''
    bihuashu = ''
    bihua = ''
    char_with_num_and_strokeid = defaultdict(list)
    char_with_num_and_stroke = defaultdict(list)
    with open('./data/stroke2id.json', 'r') as fp:
        line = eval(fp.read())
        stroke2id = line[0]
    for d in data:
        d = d.split('\t')
        nid = d[0]
        char = d[1]
        bushou = d[2]
        bihuashu = d[3]
        bihua = d[4]
        stroke_list = bihua.split(',')
        stroke_list = [i.split('/')[0] for i in stroke_list]
        stroke_list = [i for i in stroke_list if i != '']
        strokeid_list = [stroke2id[i] for i in stroke_list]
        char_with_num_and_stroke[char] = {
            'radical':bushou,
            'num':bihuashu,
            'stroke_list':stroke_list,
        }
        char_with_num_and_strokeid[char] = {
            'radical': bushou,
            'num':bihuashu,
            'strokeid_list': strokeid_list,
        }
        # print(char_with_num_and_stroke)
        # print(char_with_num_and_strokeid)
        # break
with open('./data/char_with_num_and_strokeid.json','w',encoding='utf-8') as fp:
        fp.write(json.dumps(char_with_num_and_strokeid, ensure_ascii=False))
with open('./data/char_with_num_and_stroke.json','w',encoding='utf-8') as fp:
    fp.write(json.dumps(char_with_num_and_stroke, ensure_ascii=False))