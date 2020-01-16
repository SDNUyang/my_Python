import requests
import time
def getHTML(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
    except:
        return "error"
time0=time.time()
if __name__=='__main__':
    url = 'https://www.baidu.com'
    for i in range(100):
        getHTML(url)
        if (i%10==0):
            print("正在爬取第%d次"%i)
    print(time.time()-time0)