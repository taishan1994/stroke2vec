# stroke2vec
获取中文的笔画向量。<br>
本项目提供了中文汉字的部首、笔画数、笔画信息，具体的汉字范围是中文unicode编码范围内的20902个汉字。相关的数据可以在data下找到。

# 使用方法
```python
from pybihua import BiHua
bihua = BiHua()
char = '博'
res = bihua.get_char_with_radical_and_num_and_stroke(char)
print('字符：', char)
print('部首：', res['radical'])
print('笔画数：', res['num'])
print('笔画：', res['stroke_list'])
print(bihua.get_char_with_radical_and_num_and_strokeid('博'))
```
结果：
```python
字符： 博
部首： 十
笔画数： 12
笔画： ['横', '竖', '横', '竖', '横折', '横', '横', '竖', '点', '横', '竖钩', '点']
{'radical': '十', 'num': '12', 'strokeid_list': [1, 2, 1, 2, 6, 1, 1, 2, 0, 1, 21, 0]}
```
说明：
bihua.get_char_with_radical_and_num_and_stroke(char)返回一个字典，笔画是未经过映射的。bihua.get_char_with_radical_and_num_and_strokeid(char)返回的是一个字典，笔画是经过映射的，具体映射的文件在data下，有32个笔画。