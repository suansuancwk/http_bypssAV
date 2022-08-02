

import requests
from lxml import etree
import random
class aqsy():
    def baidu(self):
        a=''
        headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47'
        }
        lis=['aries','taurus','gemini','cancer','leo','virgo','libra','scorpio','sagittarius','capricorn','aquarius','pisces']
        xz=random.choice(lis)
        html=requests.get(url='https://www.xzw.com/fortune/'+xz,headers=headers,timeout=10).text
        html = etree.HTML(html)
        a_list = html.xpath('//*[@id="view"]/div[2]/div[3]/div[2]/p[2]/span/text()')[0]
        for i in a_list:
            a=a+str(ord(i))
        listl = list(a)
        lists = list(set(listl))
        lists.sort(key=listl.index)
        sy = "".join(lists)
        sl=len(sy)
        listl = list(sy)
        if sl <= 9:
            tib = ['0', '1', '2', '3', '4', '5', '6', '7', '8','9']
            sy = listl + tib
            sy = [i for i in sy if int(i) < 9]
            formatlist = list({}.fromkeys(sy).keys())
            sy = formatlist
        else:
            sy=sy
        sy = "".join(sy)
        return sy,a_list,xz

    def zdy(self,zfc):
        a=''
        for i in zfc:
            a=a+str(ord(i))
        listl = list(a)
        lists = list(set(listl))
        lists.sort(key=listl.index)
        sy = "".join(lists)
        sl=len(sy)
        listl = list(sy)
        if sl <= 9:
            tib = ['0', '1', '2', '3', '4', '5', '6', '7', '8','9']
            sy = listl + tib
            sy = [i for i in sy if int(i) < 9]
            formatlist = list({}.fromkeys(sy).keys())
            sy = formatlist
        else:
            sy=sy
        sy = "".join(sy)
        # print(sy)
        return sy,zfc,None