import requests
from bs4 import BeautifulSoup
import os


# 为了获取网页数据我们要使用requests的get()方法：
url = "https://www.ivsky.com/bizhi/fuchouzhelianmeng_t13547/index_{}.html"
page = requests.get(url)
# 输出200相应成功，说明连接成功
# pint(page.status_code)"


soup = BeautifulSoup(page.content, 'html.parser')
all_img = soup.find('ul', class_='pli',).find_all('img')
for img in all_img:
    src = 'http:' +img['src']
    img_url = src
    print(img_url)
    root = 'E:/pic/'
    path = root + img_url.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            for i in range(1,11):
                url=url.format(i)
                r = requests.get(img_url)
                with open(path, 'wb') as f:
                    f.write(r.content)
                    f.close()
                    print("文件保存成功")
        else:
            print("文件已存在")
    except:
        print("爬取失败")