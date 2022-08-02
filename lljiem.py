# -*- coding: utf-8 -*-
import time


class Eternal:
    def __init__(self):
        self.ax0 = 'a'  # 0
        self.ax1 = 'b'  # 1
        self.ax2 = 'c'  # 2
        self.ax3 = 'd'  # 3
        self.ax4 = 'e'  # 4
        self.ax5 = 'j'  # 5
        self.ax6 = 'k'  # 6
        self.ax7 = 'l'  # 7
        self.ax8 = 'm'  # 8
        self.ax9 = 'n'  # 9
        self.love = 520
        self.like = 1314

    # cpu_xor解密
    def cpu_xor_jiem(self, sz, cpuzy):
        jg = []
        for i in sz:
            num = int(i)
            jg.append(int(cpuzy) ^ num)
        return jg

    # 时间戳异或-解密
    def xor_time_jiemi(self, sz, sjc):
        jg = []
        for i in sz:
            num = int(i)
            try:
                jg.append(int(sjc) ^ num)
            except:
                exit('错误！！！')
        return jg

    def jiem_api(self, sc, sjc, xzys, cpuzy):
        sjc = int(sjc)
        st1 = []
        st2 = ''
        a = ''
        m = ''
        n = []
        qq = ''
        lb = sc.split('o')
        lb = [i for i in lb if i]
        for str1 in lb:
            for st in str1:
                if st == self.ax0:
                    st2 = st2 + '0'
                elif st == self.ax1:
                    st2 = st2 + '1'
                elif st == self.ax2:
                    st2 = st2 + '2'
                elif st == self.ax3:
                    st2 = st2 + '3'
                elif st == self.ax4:
                    st2 = st2 + '4'
                elif st == self.ax5:
                    st2 = st2 + '5'
                elif st == self.ax6:
                    st2 = st2 + '6'
                elif st == self.ax7:
                    st2 = st2 + '7'
                elif st == self.ax8:
                    st2 = st2 + '8'
                elif st == self.ax9:
                    st2 = st2 + '9'
            st1.append(st2)
            st2 = ''
            # 输入的字符串转ascii再转八进制 再在23489167233中获取索引 > sx > xor_time > cpu_xor > 替换
        xxx = self.cpu_xor_jiem(st1, cpuzy)
        xxx = self.xor_time_jiemi(xxx, sjc)
        # xxx = self.jdxs_jiem(xxx, sjc)
        a_list = xzys
        for i in a_list:
            a = a + str(ord(i))
        listl = list(a)
        lists = list(set(listl))
        lists.sort(key=listl.index)
        sy = "".join(lists)
        sl = len(sy)
        listl = list(sy)
        if sl <= 9:
            tib = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            sy = listl + tib
            sy = [i for i in sy if int(i) < 9]
            formatlist = list({}.fromkeys(sy).keys())
            sy = formatlist
        else:
            sy = sy
        sy = "".join(sy)
        c = sy
        list1 = list(c)
        for os in xxx:
            os = str(os)
            for s in os:
                m = m + list1[int(s) - 1]
            n.append(m)
            m = ''
        for zyq in n:
            cwk = int(zyq, 8)
            qq = qq + chr(cwk)
        return qq

    def api_jie(self, sc, sjc, xzys, cpuzy):
        m = Eternal()
        # self,sc,sjc,xzys,cpuzy
        c = m.jiem_api(sc=sc, sjc=sjc, xzys=xzys, cpuzy=cpuzy)
        return c

