import requests
from bs4 import BeautifulSoup
from collections import defaultdict
from tqdm import tqdm

def get_single_stroke_api2(char):
    url = 'http://bihua.qihaoming.com.cn/searchbh/?KeyWord={}'.format(char)
    response = requests.get(url)
    content = response.content
    # print(content)
    soup = BeautifulSoup(content,'lxml')
    bushou = ''
    bihuashu = ''
    bihua = []
    for idx,tr in enumerate(soup.find_all('tr')):
        if idx != 0:
            tds = tr.find_all('td')
            for i,td in enumerate(tds):
                content = td.string
                if content == '部首':
                    bushou = tds[i+1].string
                elif content == '笔画数':
                    bihuashu = tds[i+1].string
                elif content == '名称':
                    bihua = tds[i+1].string
                    bihua = bihua.strip().split('、')
                    bihua = [i.strip() for i in bihua if i != '']
    # print(bushou, bihuashu, bihua)
    return bushou, bihuashu, bihua

def get_all_stroke2():
    # 19968 40869
    char_with_num_and_strokeid = defaultdict(list)
    char_with_num_and_stroke = defaultdict(list)
    with open('./data/stroke2id.json','r') as fp:
        line = eval(fp.read())
        stroke2id = line[0]
    stroke_file = open('./data/stroke_test2.txt','a',encoding='utf-8')
    j = 14676
    for i in tqdm(range(34643, 40869+1)):
        char = chr(i)
        # unicode = bytes.decode(char.encode('unicode_escape')[-4:])
        bushou, bihuashu, bihua = get_single_stroke_api2(char)
        # strokeid_list = [stroke2id[i] for i in stroke_list]
        # char_with_num_and_stroke[char] = {
        #     'num':num,
        #     'stroke_list':stroke_list,
        # }
        # char_with_num_and_strokeid[char] = {
        #     'num':num,
        #     'strokeid_list': strokeid_list,
        # }
        stroke_file.write(str(j) + '\t' + char + '\t' + bushou + '\t' + str(bihuashu) + '\t' + ",".join(bihua) + '\n')
        j += 1
    stroke_file.close()
    # with open('./data/char_with_num_and_strokeid.json','w',encoding='utf-8') as fp:
    #     fp.write(json.dumps(char_with_num_and_strokeid, ensure_ascii=False))
    # with open('./data/char_with_num_and_stroke.json','w',encoding='utf-8') as fp:
    #     fp.write(json.dumps(char_with_num_and_stroke, ensure_ascii=False))

if __name__ == '__main__':
    get_all_stroke2()
    # bushou, bihuashu, bihua = get_single_stroke_api2('一')
    # print(bushou, bihuashu, bihua)
    # print(ord('龥'))

