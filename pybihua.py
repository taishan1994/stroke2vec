import json


class BiHua:
    def __init__(self):
        self.load_everything()

    def load_everything(self):
        with open('./data/char_with_num_and_stroke.json', 'r') as fp:
            self.char_with_num_and_stroke = json.loads(fp.read())
        with open('./data/char_with_num_and_strokeid.json', 'r') as fp:
            self.char_with_num_and_strokeid = json.loads(fp.read())

    def get_char_with_radical_and_num_and_stroke(self, char):
        return self.char_with_num_and_stroke[char]

    def get_char_with_radical_and_num_and_strokeid(self, char):
        return self.char_with_num_and_strokeid[char]

if __name__ == '__main__':
    bihua = BiHua()
    char = '博'
    res = bihua.get_char_with_radical_and_num_and_stroke(char)
    print('字符：', char)
    print('部首：', res['radical'])
    print('笔画数：', res['num'])
    print('笔画：', res['stroke_list'])
    print(bihua.get_char_with_radical_and_num_and_strokeid('博'))