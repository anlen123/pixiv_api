# pixiv_api

下载日榜前1-500的作品,,一个作品可能包含几张图片哦

# 使用方法

```bash
python pixiv_api.py "2020-05-20"  //后面输入日期即可下载当天的日榜 
不输入参数的话,默认下载的是当天的日榜

python pixiv_api.py "2020-05-20" 3
后面可加第三个参数,第三个参数是榜单
1-7分别是
日榜,周榜,月榜,男性榜,女性榜,新人榜,和原创榜
PS：　如果你输入的日期是今天,如果在13点以前会出错,因为日榜13点更新,
如果你要下载今天的话,就不加参数就行了
你要下载今天的其他榜单的话,,你还是改代码吧,哈哈哈,我不想写了,,


新增一个一个py 文件,两个py各司其职
python pixiv_id.py "画师id" 然后输入要下载的作品个数
```





注意看这一行

```python

    # duoxiancheng(down, listt, 1) #开启就是下载 开启就是下载 开启就是下载 开启就是下载  1是多线程的下载间隔时间,单位 秒 

    print("完成")
    print("完成")
    print("完成")
    解除注释就可以下载了,,但是不推荐,,推荐获取直链后,用其他下载器下载
```

这里修改下载的是榜单

```python
if op == '1':
    leixing = "daily"
elif op == '2':
    leixing = "weekly"
elif op == '3':
    leixing = "monthly"
elif op == '4':
    leixing = "day_male"
elif op == '5':
    leixing = "day_female"
elif op == '6':
    leixing = "week_rookie"
elif op == '7':
    leixing = "week_original"
    
op ==1的时候是日榜,2的时候是周.........
```

