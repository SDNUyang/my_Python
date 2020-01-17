#亚马逊网对相关信息保护做的比较好，主要介绍怎么通过修改头信息去欺骗服务器，这不是一个爬虫！
import requests
url="https://www.amazon.cn/dp/B00PH5W2I6/ref=sr_1_8?dchild=1&keywords=Nike+%E8%80%90%E5%85%8B&p_n_global_store_origin_marketplace=1827360071%7C1844252071%7C1879515071%7C1901313071&qid=1579264439&sr=8-8"
r=requests.get(url)
print(r.status_code)                         #********输出现在的状态信息，显示的是503错误代码********
r.encoding=r.apparent_encoding               #********修改下浏览器的编码方式，主要作用是把乱码转换成我们能够看的懂的
print(r.request.headers)                     #***********输出访问的头看一下user-agent
kv={'User-Agent':'Mizalla/5.0'}
q=requests.get(url,headers=kv)               #******修改头
print(q.status_code)
print(q.encoding)
q.encoding=q.apparent_encoding
print(q.request.headers)
print(q.text)
