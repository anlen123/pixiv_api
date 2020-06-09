import requests
import os
import datetime

# str1 = datetime.datetime.now().strftime("%Y-%m-%d")

listt = []
listId = []


def app_url(num, leixing, datatimee):
    url = f"https://api.imjad.cn/pixiv/v1/?type=rank&content=illust&mode={leixing}&per_page={num}&page=1&date={datatimee}"

    #print(url)
    r = requests.get(url).json()['response'][0]['works']
    for x in r:
        listId.append(x['work']['id'])


def get_url(id):
    a = requests.get("https://www.pixiv.net/touch/ajax/illust/details?illust_id=" + str(id)).json()['body'][
        'illust_details']
    b = a['illust_images']
    if len(b) == 1:
        listt.append(a['url_big'])
    else:
        for x in a['manga_a']:
            listt.append(x['url_big'])


def duoxiancheng(Hanshu, List, Time):
    import time
    from concurrent.futures import ThreadPoolExecutor
    pool = ThreadPoolExecutor(max_workers=16)
    for i in List:
        pool.submit(Hanshu, i)
        time.sleep(Time)
    pool.shutdown()


def down(url):
    headers = {
        'referer': 'https://www.pixiv.net',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    }
    r = requests.get(url=url, headers=headers)
    name = url[-15:]
    path = str1 + "/" + str(leixing) + "/" + "%s" % str(name)
    if not os.path.exists(str1 + "/" + str(leixing)):
        os.mkdir(str1 + "/" + str(leixing))
    # print(path)
    with open(path, 'wb') as f:
        print("---正在下载---{}".format(name))
        f.write(r.content)


try:
    task = os.sys.argv[1]
    str1 = task
except:
    task = ""
    str1=str(datetime.datetime.now().strftime("%Y-%m-%d"))
num = input("你要下载多少个作品[最小1,最大500]:")
# num = 1
# op = input("你要下载哪个类型的榜单:" + "1:日榜,2:周榜,3:月榜:")
op = "1"
leixing = ""
if op == '1':
    leixing = "daily"
elif op == '2':
    leixing = "weekly"
elif op == '3':
    leixing = "monthly"

print("这是" + str(leixing) + "类型的解析")
print("一共有三步骤")
print(task)
app_url(num, leixing, task)
print("一共" + str(len(listId)) + "个作品")
print("第一步骤完成")
duoxiancheng(get_url, listId, 0)

print("正在解析中")
print("一共" + str(len(listt)) + "张图片")
print("第二步骤完成")
# print(listt)
if not os.path.exists(str1):
    os.mkdir(str1)
for x in listt:
    with open(str1 + "/" + str(leixing) + "-下载直链.txt", 'a+')as f:
        f.write(x + '\n')

# duoxiancheng(down, listt, 1) #开启就是下载

print("完成")
print("完成")
print("完成")
