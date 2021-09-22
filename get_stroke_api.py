import requests
import re
import json
from collections import defaultdict
from tqdm import tqdm

def get_single_stroke_api(char):
    url = 'http://bishun.shufaji.com/0x{}.html'.format(char)
    response = requests.get(url)
    content = response.content.decode('utf-8')
    pattern = '<div id="hzcanvas">(.*?)</div>'
    result = re.search(pattern, content, re.S)
    data = result.groups()[0]
    num_pattern = '共([0-9]+)画'
    num_res = re.search(num_pattern, data)
    if num_res:
        num = num_res.groups()[0]
        stroke_pattern = r'笔顺：([\u4E00-\u9FA5,\/]+)'
        stroke_res = re.search(stroke_pattern, data)
        stroke = stroke_res.groups()[0]
        stroke_list = stroke.split(',')
    else:
        num = 0
        stroke_list = []
    return num, stroke_list

def get_all_stroke():
    # 19968 40869
    char_with_num_and_strokeid = defaultdict(list)
    char_with_num_and_stroke = defaultdict(list)
    with open('./data/stroke2id.json','r') as fp:
        line = eval(fp.read())
        stroke2id = line[0]
    stroke_file = open('./data/stroke_test.txt','a',encoding='utf-8')
    j = 2020
    for i in tqdm(range(21987, 40869+1)):
        char = chr(i)
        unicode = bytes.decode(char.encode('unicode_escape')[-4:])
        num, stroke_list = get_single_stroke_api(unicode)
        # strokeid_list = [stroke2id[i] for i in stroke_list]
        # char_with_num_and_stroke[char] = {
        #     'num':num,
        #     'stroke_list':stroke_list,
        # }
        # char_with_num_and_strokeid[char] = {
        #     'num':num,
        #     'strokeid_list': strokeid_list,
        # }
        stroke_file.write(str(j) + '\t' + char + '\t' + str(num) + '\t' + ",".join(stroke_list) + '\n')
        j += 1
    stroke_file.close()
    # with open('./data/char_with_num_and_strokeid.json','w',encoding='utf-8') as fp:
    #     fp.write(json.dumps(char_with_num_and_strokeid, ensure_ascii=False))
    # with open('./data/char_with_num_and_stroke.json','w',encoding='utf-8') as fp:
    #     fp.write(json.dumps(char_with_num_and_stroke, ensure_ascii=False))

if __name__ == '__main__':
    get_all_stroke()
    # num, stroke_list = get_single_stroke_api(bytes.decode('冬'.encode('unicode_escape')[-4:]))
    # print(stroke_list)
    # print(ord('龥'))
