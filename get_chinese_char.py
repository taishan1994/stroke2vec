# coding=utf-8
# 4E00-9FA5


chinese_char_list = []

start_char = str('\u4E00').encode('utf-8').decode('utf-8')
start_char_ascii = ord(start_char)
end_char = str('\u9FA5').encode('utf-8').decode('utf-8')
end_char_ascii = ord(end_char)
print(start_char_ascii, end_char_ascii)
chinese_char_list.append(start_char)


for i in range(int(start_char_ascii)+1, int(end_char_ascii)):
    chinese_char_list.append(chr(i))
chinese_char_str = "\n".join(chinese_char_list)

with open('./data/chinese_char.txt','w', encoding='utf-8') as fp:
    fp.write(chinese_char_str)
chinese_char_list.append(end_char)