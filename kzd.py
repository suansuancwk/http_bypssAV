import os
import sys
import time
import lljiam
import lljiem


def getdata():
    with open('index1.html', 'r', encoding='utf8') as f:
        data = f.read()
        f.close()
    # print(data)
    return data


def fsml(data):
    ml = input('执行命令>>>')
    app = lljiam.Eternal()
    test = app.api_jia('2', ml, zfc='suansuan')  # 密文 cpu 时间戳
    # print(test)
    html = data.format(time=test[2], cpu=test[1], ml=test[0])
    with open('index.html', 'w') as f:
        f.write(html)
        f.close()
    if ml == 'exit()':
        sys.exit(0)


# fsml(getdata())

def readhx():
    with open('log.txt', 'r') as f:
        jg = f.read()
        f.close()
    jg = jg.split(',')
    data = jg[0]
    cpu = jg[1]
    time1 = jg[2]
    app = lljiem.Eternal()
    ml = app.api_jie(sc=data, sjc=time1, xzys='suansuanadmin', cpuzy=cpu)
    print(ml)
    os.remove("log.txt")


# readhx()
def ks():
    while True:
        data = getdata()
        fsml(data)
        pd()
        time.sleep(2)


def pd():
    while 1:
        if not os.path.exists('log.txt'):
            time.sleep(1)
        else:
            readhx()
            break


ks()
