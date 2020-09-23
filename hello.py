import requests
import json

post_data = {
    "topic": "计算机",
    "publishid":"17120162"
}
urlad = "http://192.168.149.184:5000"
res = requests.get(url=urlad+"/select/chat_main", json=post_data)
getdict = json.loads(res.text)
print(getdict)
