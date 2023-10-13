import json

data = [{"name":"熊大","age":3},{"name":"熊二","age":2},{"name":"光头强","age":30}]
# 将数据转为json
json_str = json.dumps(data,ensure_ascii=False) #ensure_ascii=False输入中文
print(json_str)

#将json转为python对象
s = '[{"name": "熊大", "age": 3}, {"name": "熊二", "age": 2}, {"name": "光头强", "age": 30}]'
l = json.loads(s)
print(l)