import sys
import pickle
import time
import os
import requests
import json
from bs4 import BeautifulSoup

print("赫尔墨斯为您提供帮助，您现在使用的版本是1.0")
print("赫尔墨斯请您选择需要的帮助并输入所需服务的序号：1、疫情查询  2、百度热搜  3、赫尔墨斯账本  4、退出程序 请输入数字并键入回车")
m=int(input())
if m==1:
    print("赫尔墨斯为您提供帮助，向您播报最近的全国疫情信息:") 
    def Down_data():
        url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
        headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36'
        }
        r = requests.get(url, headers)
        res = json.loads(r.text)
        data_res = json.loads(res['data'])
        return data_res
 
    def Parse_data1():
        data = Down_data()
        list = ['截至时间：' + str(data['lastUpdateTime']) + '\n'
                '全国确诊人数：' + str(data['chinaTotal']['confirm']) + '\n'
                '今日新增确诊：' + str(data['chinaAdd']['confirm']) + '\n'
                '全国疑似：' + str(data['chinaTotal']['suspect']) + '\n'
                '今日新增疑似：' + str(data['chinaAdd']['suspect']) + '\n'
                '全国治愈：' + str(data['chinaTotal']['heal']) + '\n'
                '今日新增治愈：' + str(data['chinaAdd']['heal']) + '\n'
                '全国死亡：' + str(data['chinaTotal']['dead']) + '\n'
                '今日新增死亡：' + str(data['chinaAdd']['dead']) + '\n']
        result = ''.join(list)
        print(result)
 
    Down_data()
    Parse_data1()
    input()

elif m==2:
    print("赫尔墨斯为您提供帮助，向您播报此时的百度热搜") 
    url = 'http://top.baidu.com/buzz?b=1&fr=topindex'
    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
 
    }
    r = requests.get(url, headers=headers, timeout=30)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text,'html.parser')
    title_list=soup.find_all(attrs={'class':'c-single-text-ellipsis'})
    hot_list=soup.find_all(attrs={'class':'hot-index_1Bl1a'})
    for j in range(len(title_list)):
        print(str((j+1)) + '.' + str(title_list[j].get_text())+'('+'热度指数'+':'+str(hot_list[j].get_text())+')')
    input()

elif m==3:
    #!/usr/bin/env Python
    #-*- coding:utf-8 -*-
    class ColorMe:
       def __init__(self, some_str):
           self.color_str = some_str
 
       def blue(self):
           str_list = ["\033[34;1m", self.color_str, "\033[0m"]
           return ''.join(str_list) # "\033[34;1m" + self.color_str + "\033[0m"
 
       def green(self):
           str_list = ["\033[32;1m", self.color_str, "\033[0m"]
           return ''.join(str_list) # "\033[34;1m" + self.color_str + "\033[0m"
 
       def yellow(self):
           str_list = ["\033[33;1m", self.color_str, "\033[0m"]
           return ''.join(str_list) # "\033[34;1m" + self.color_str + "\033[0m"
 
       def red(self):
           str_list = ["\033[31;1m", self.color_str, "\033[0m"]
           return ''.join(str_list) # "\033[34;1m" + self.color_str + "\033[0m"
 
 
    def main():
        ColorMe('somestr').blue()
 
    if __name__ == '__main__':
       main()

    #!/usr/bin/env python
    # -*- coding:utf-8 -*-
 
 
    init = ["赫尔墨斯提示：此信息为初始化信息"]
 
    class Memo(object):
        def __init__(self, name, thing, date, time):
           self.name = name
           self.thing = thing
           self.date = date
           self.time = time
           self.__id = 0
 
        @property
        def id(self):
           return self.__id
 
        def set_id(self, restart):
           self.__id = restart + self.__id
           return self.__id
 
        def welcome(self):
           print(f"赫尔墨斯账本为您提供帮助.".center(60,"-"))
 
 
    class MemoAdmin(object):
        def __init__(self):
            self.user_list = []
 
        def user_add(self):
            count = True
            while (count):
                Your_title = input("请您输入交易名称：".strip())
                Your_event = input("请您输入交易数据：".strip())
                Your_date = input("请您输入交易时间：".strip())
                time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
 
                if Your_title == "":
                    print("交易名称不能为空！！！")
 
                elif Your_event == "":
                    print("交易金额不能为空")
 
                elif Your_date == "":
                    print("交易时间不能为空")
 
                else:
                    self.create(Your_title, Your_event, Your_date, time1)
                    count = False
 
        def create(self,Your_title, Your_event, Your_date, time1):
            memo = Memo(Your_title, Your_event, Your_date, time1)
            user_result = (f"ID：{memo.set_id(self.count())}、交易名称：{Your_title}、交易数据：{Your_event}、交易时间：{Your_date}、创建时间 : {time1}")
 
            self.user_list.append(user_result)
            self.save()
 
        def user_delete(self):
            if os.path.isfile("db.pkl"):
                user_delete = int(input("赫尔墨斯请您输入您需要删除的id号：".strip()))
                with open('db.pkl', 'rb') as f:
                    data = pickle.load(f)
                    data.pop(user_delete)
                    self.user_list = []
                for a in data:
                    self.user_list.append(a)
 
                self.save()
            else:
                print("nonono")
 
        def user_search(self):
            search_result = int(input("赫尔墨斯请您输入您需要查找的ID：".strip()))
            if os.path.isfile("db.pkl"):
                with open('db.pkl', 'rb') as f:
                    data = pickle.load(f)
                    print(data[search_result])
            else:
                search_result = ColorMe("没有交易信息，请您选择添加交易信息并创建").red()
                print(search_result)
 
 
        def save(self):
            with open('db.pkl', 'wb') as f:
                pickle.dump(self.user_list, f)
                save_result = ColorMe(f"您当前一共有{len(self.user_list)}条交易信息").green()
                print(save_result)
 
        def load(self):
            if os.path.isfile("db.pkl"):
                with open('db.pkl', 'rb') as f:
                    data = pickle.load(f)
                load_welcome = ColorMe("交易记录，数据如下：".center(60, "-")).green()
                print(load_welcome)
                for line in data:
                    print(line)
            else:
                load_warning = ColorMe("没有交易信息，请你添加并创建").red()
                print(load_warning)
 
        def count(self):
            with open('db.pkl', 'rb') as f:
                data = pickle.load(f)
                result = len(data)
                return  result
 
        def exit(self):
            save_Tips = ColorMe("赫尔墨斯向您说再见".center(60,"-")).green()
            print(save_Tips)
            sys.exit()
 
        def delete(self):
            if os.path.isfile("db.pkl"):
                os.remove("db.pkl")
                delete_success = ColorMe("赫尔墨斯成功帮您清除了交易记录！").green()
                print(delete_success)
            else:
                delete_warning =  ColorMe("没有交易记录，请你添加并创建").red()
                print(delete_warning)
 
        def user_input(self):
           print(f"欢迎使用赫尔墨斯账本".center(60,"-"))
           user_menu = {
               "1" : "添加交易数据",
               "2" : "删除交易数据",
               "3" : "查找交易数据",
               "p" : "查看交易数据",
               "d" : "清空交易数据",
               "Q" : "退出交易数据"
           }
 
           user_menu2 = {
               "1" : "user_add",
               "2" : "user_delete",
               "3" : "user_search",
               "p" : "load",
               "d" : "delete",
               "Q" : "exit"
           }
 
           if os.path.isfile("db.pkl"):
              with open('db.pkl', 'rb') as f:
                  data = pickle.load(f)
                  for a in data:
                      self.user_list.append(a)
                  Os_Tips_result = ColorMe(f"赫尔墨斯提示，初始交易数据准备成功,目前一共有{len(self.user_list)}条交易数据").green()
                  print(Os_Tips_result)
 
           else:
              with open('db.pkl', 'wb') as f:
                  C = ColorMe("赫尔墨斯提示：赫尔墨斯1.0程序初始化完毕，请再次打开.....").green()
                  print(C)
                  pickle.dump(init, f)
                  sys.exit()
 
           try:
              while True:
                  for k, v in user_menu.items():
                      print(f"""
                       {k}、{v}
                       """)
                  User_choice = input("请您输入选项：".strip())
                  if User_choice.strip() == "":
                      error_warning = ColorMe("请您输入正确的数值！").red()
                      print(error_warning)
                  else:
                      if hasattr(self,user_menu2.get(User_choice)):
                          func = getattr(self,user_menu2.get(User_choice))
                          func()
                      else:
                          error_warning2 = ColorMe("赫尔墨斯检测错误，请您输入正确的选项").red()
                          print(error_warning2)
           except Exception as f:
              print(f)
 
    if __name__=="__main__":
       Admin = MemoAdmin()
       Admin.user_input()

if m==4:
    exit()
