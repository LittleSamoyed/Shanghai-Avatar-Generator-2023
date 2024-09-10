import tkinter
import tkinter.font
import tkinter.messagebox
import random
import turtle as t
import os
import webbrowser
import time
# 出现报错？shell/cmd安装   'pip install requests'
import requests
# something wrong? Shell or cmd download it      'pip install requests'
import re

#def part#
def guanggao_open1():
    global words
    webbrowser.open(words[1])
def guanggao_open2():
    global words2
    webbrowser.open(words2[1])
def guanggao():
    global words
    # 下载一个网页
    url = 'https://www.kakazheng.cf/2022/04/18/guanggao/'
    # 模拟浏览器发送http请求
    response = requests.get(url)
    # 编码方式
    response.encoding='utf-8'
    # 目标小说主页的网页源码
    html = response.text
    html2=html.split('<p>')
    html3=html2[1].split('</p>')
    words=html3[0].split(' &#8211; &#8211; LINK &#8211; &#8211; ')

def guanggao2():
    global words2
    # 下载一个网页
    url = 'https://www.kakazheng.cf/2022/04/18/guanggao2/'
    # 模拟浏览器发送http请求
    response = requests.get(url)
    # 编码方式
    response.encoding='utf-8'
    # 目标小说主页的网页源码
    html = response.text
    html2=html.split('<p>')
    html3=html2[1].split('</p>')
    words2=html3[0].split(' &#8211; &#8211; LINK &#8211; &#8211; ')



# 团长
def tuanzhang():
    webbrowser.open('https://www.kakazheng.cf/2022/04/15/%e5%9b%a2%e9%95%bf%ef%bc%8c%e4%bd%a0%e5%a5%bd-%e9%ad%94%e9%83%bd%e5%9b%a2%e9%95%bf%e3%80%81%e5%b9%b3%e6%b0%91%e5%a4%b4%e5%83%8f-v-001/2/')


# 平民
# turtle画图
def make():
    global entry1_get
    global entry2
    global entry3
    # windows_3.destroy()
    t.clear()
    loudong=entry2.get()
    zhuhu=entry3.get()
    t.setup(250+20*2,250+20*2)
    lst1=['dodgerblue','lime','magenta']
    lst2=['deepskyblue','palegreen','lightpink']
    lst3=['azure','mediumseagreen','purple']
    a=random.randint(0,len(lst2)-1)
    t.tracer(False)
    t.penup()
    t.goto(-128,128)
    t.pendown()
    t.pencolor('black')
    t.begin_fill()
    t.fillcolor(lst2[a])
    t.goto(-128,-128)
    t.goto(128,-128)
    t.goto(128,128)
    t.goto(-128,128)
    t.end_fill()
    t.begin_fill()
    t.fillcolor(lst1[a])
    t.goto(-128,0)
    t.goto(100,0)
    t.goto(100,128)
    t.goto(-128,128)
    t.end_fill()
    t.fillcolor(lst2[a])
    t.goto(-128,10)
    t.goto(70,10)
    t.penup()
    t.goto(70,-10)
    t.pendown()
    t.goto(-128,-10)
    t.penup()
    t.goto(-90,15)
    t.pendown()
    t.color(lst3[a])
    t.write(loudong,font=(entry1_get,65))
    # 多少字符（3、4）
    if len(zhuhu)==4:
        t.penup()
        t.goto(-120,-100)
        t.pendown()
    elif len(zhuhu)==3:
        t.penup()
        t.goto(-100,-100)
        t.pendown()
    t.write('平民  '+zhuhu,font=(entry1_get,40))
    t.hideturtle()
    t.update()


# 输入楼栋住户
def pingmin2():
    global entry2
    global entry3
    global windows_3
    windows_2.destroy()
    windows_3=tkinter.Tk()
    windows_3.geometry("600x700")  # window's size
    windows_3.title("输入楼栋、住户")  # window's name
    label3 = tkinter.Label(windows_3, text="输入楼栋、住户", font=('华文新魏', 20))     #title
    label3.pack(pady=50)
    label4 = tkinter.Label(windows_3, text="输入楼栋,例如：44 # / 02 # 注意: 楼栋+空格+井号 ", font=('华文新魏', 20))     #title
    label4.pack(pady=50)
    entry2 = tkinter.Entry(windows_3, font=('华文新魏', 20))    #entry
    entry2.pack(pady=20)
    label5 = tkinter.Label(windows_3, text="输入住户,例如：404 / 1403 ", font=('华文新魏', 20))     #title
    label5.pack(pady=50)
    entry3 = tkinter.Entry(windows_3, font=('华文新魏', 20))    #entry
    entry3.pack(pady=20)
    bt4  = tkinter.Button(windows_3, text="完成", font=('华文新魏', 20), width=20,command=make)
    bt4.pack(pady=20)


# 字体确认
def check_font():
    global entry1_get
    entry1_get=entry1.get()
    if entry1_get not in Fonts:
        tkinter.messagebox.showerror('warning','你输入的字体不在您电脑的字体库中')
    else:
        tkinter.messagebox.showinfo('字体设置成功','你输入的字体在您电脑的字体库中，即将进入下一项')
        pingmin2()
# 字体选择
def pingmin(): #For button-1
    global entry1
    global windows_2
    windows_1.destroy()
    windows_2=tkinter.Tk()
    windows_2.geometry("600x700")  # window's size
    windows_2.title("选择字体 - 平民")  # window's name
    label2 = tkinter.Label(windows_2, text="选择字体", font=('华文新魏', 20))     #title
    label2.pack(pady=50)
    entry1 = tkinter.Entry(windows_2, font=('华文新魏', 20))    #entry
    entry1.pack(pady=20)
    #tkinter.messagebox.showinfo('Your fonts:',Fonts_str)
    btn3 = tkinter.Button(windows_2, text="完成", font=('华文新魏', 20), width=20,command=check_font)
    btn3.pack(pady=20)
##
#path = r'D:\Users\kakaz\Desktop\...头像'      # root of Fonts
#files = os.listdir(path)   # read files




# 读取字体
a=tkinter.Tk()
a.withdraw()
lis=tkinter.font.families()
Fonts=[]   # 字体列表



# 去除部分的@
for i in lis:
    if '@' in i:
        Fonts.append(i[1:])
    else:
        Fonts.append(i)
Fonts_t=Fonts
# for i in range(len(Fonts_t)-1,6):
#     Fonts_t[i]=Fonts_t[i]+'\n'
# Fonts_str=''
# for i in Fonts_t:
#     Fonts_str=Fonts_str+i+'     '
#print(Fonts)


# 第一个窗口
windows_1=tkinter.Tk()
windows_1.geometry("850x500")  # window's size
windows_1.title("选择")  # window's name
'''
img_gif = tkinter.PhotoImage(file = 'Snipaste_2022-04-18_19-31-46.png')
label_img = tkinter.Label(windows_1, image = img_gif)
label_img.pack(0,0)
'''
#
label1 = tkinter.Label(windows_1, text="选择类型", font=('华文新魏', 20))
label1.pack(pady=50)
#button-1
btn1 = tkinter.Button(windows_1, text="我是平民", font=('华文新魏', 20), width=50,command=pingmin)   #,command=log
btn1.pack(pady=20)
#button-2
btn2 = tkinter.Button(windows_1, text="我是团长", font=('华文新魏', 20), width=50,command=tuanzhang)   #,command=log
btn2.pack(pady=20)




guanggao()
guanggao2()
#button-3       广告
btn3 = tkinter.Button(windows_1, text=words[0], font=('华文新魏', 20), width=50,command=guanggao_open1)   #,command=log
btn3.pack(pady=20)
btn4 = tkinter.Button(windows_1, text=words2[0], font=('华文新魏', 20), width=50,command=guanggao_open2)   #,command=log
btn4.pack(pady=20)
#Keep Opening
tkinter.mainloop()
t.done()
