import requests
#r=requests.get("https://item.jd.com/2967929.html")
#print(r.status_code)
#print(r.encoding)
#print(r.text)
url="https://www.amazon.cn/dp/B078GL9C6V/ref=sr_1_2?dchild=1&keywords=Champion&p_n_global_store_origin_marketplace=1827360071%7C1844252071%7C1879515071%7C1901313071&qid=1579263354&sr=8-2&th=1&psc=1"
q=requests.get(url)
print(q.status_code)
try:
    r=requests.get(url)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败!!!")