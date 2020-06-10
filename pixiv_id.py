import requests
import os
import datetime

# str1 = datetime.datetime.now().strftime("%Y-%m-%d")

listt = []
listId = []


def app_id(_id,num):
    print("_id")
    url = f"https://api.imjad.cn/pixiv/v1/?type=member_illust&id={_id}&per_page={num}&page=1"
    # print(url)
    r = requests.get(url).json()['response']
    for x in r:
        listId.append(x['id'])

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
    path = str(_id) + "/" + "%s" % str(name)
    if not os.path.exists(str(_id)):
        os.mkdir(str(_id))
    # print(path)
    with open(path, 'wb') as f:
        print("---正在下载---{}".format(name))
        f.write(r.content)

if(len(os.sys.argv)==1):
    print("请输入画师id!!!!")
    print("请输入画师id!!!!")
    print("请输入画师id!!!!")
else:
    _id = os.sys.argv[1]   
    num = input("你要下载多少个作品[最小1,最大...]:")
    print("一共有三步骤")
    app_id(_id ,num)
    print("一共" + str(len(listId)) + "个作品")
    print("第一步骤完成")
    duoxiancheng(get_url, listId, 0)

    print("正在解析中")
    print("一共" + str(len(listt)) + "张图片")
    print("第二步骤完成")
    # print(listt)
    if not os.path.exists(_id):
        os.mkdir(_id)
    for x in listt:
        with open(str(_id)+"/"+str(_id) + "画师-下载直链.txt", 'a+')as f:
            f.write(x + '\n')

    duoxiancheng(down, listt, 0) #开启就是下载

    print("完成")
    print("完成")
    print("完成")
