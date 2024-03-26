import re
import os

def autoLiHui(fData):

    for counts, filename in enumerate(os.listdir('images/cha/')):
        res = filename.replace('.png','')
        tar = res[0:2]+res[3:]+"}"
        res += "}\nshow " + res[0:2] + " " +res[3:]
        fData = fData.replace(tar, res)

    return fData


def autoCharacterName(fData):

    for key, val in CharacterName.items():
        fData = fData.replace(key+"：\"", val+ " \"")
        fData = fData.replace(key+"： \"", val+ " \"")
        fData = fData.replace(key+" ：\"", val+ " \"")
        fData = fData.replace(key+" ： \"", val+ " \"")
        fData = fData.replace(key+"：“", val+ " \"")
        fData = fData.replace(key+"： “", val+ " \"")
        fData = fData.replace(key+" ：“", val+ " \"")
        fData = fData.replace(key+" ： “", val+ " \"")

    return fData


def autoBGM(fData):

    for counts, filename in enumerate(os.listdir('audio/bgm/')):
        res = filename.replace('.mp3','')
        tar = "BGM "+ res +"}"
        res = tar + "\n" + "play music \"audio/bgm/" + res + ".mp3\""
        fData = fData.replace(tar, res)

    fData = fData.replace("停止播放BGM }", "停止播放BGM }\nstop music")
    fData = fData.replace("播放se cuowu}", "播放se cuowu}\nplay sound \"audio/se/sushiyin/cuowu.mp3\"")
    fData = fData.replace("播放se zhengque}", "播放se zhengque}\nplay sound \"audio/se/sushiyin/zhengque.mp3\"")

    return fData

CharacterName = {
    "周小雨" : "ZhouXiaoyu",
    "田老师" : "TeacherTian",
    "郑辉" : "ZhengHui",
    "刘洋" : "LiuYang",
    "王浩" : "Wanghao",
    "袁巧巧" : "YuanQiaoqiao",
    "高桥智子" : "Tomoko",
    "智子" : "Zhizi",
    "我" : "me"
}

fin = open("test.txt", "rt", encoding='UTF-8')
filedata = fin.read()
fin.close()

filedata = autoLiHui(filedata)
filedata = autoCharacterName(filedata)
filedata = autoBGM(filedata)

f = open("out.txt",'w', encoding='UTF-8')
f.write(filedata)
f.close()