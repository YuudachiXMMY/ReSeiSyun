#################################################################
## Character Definations
define me = Character("我", color='#ffff')
define question = Character("???", color='#ffff')
define MenWei = Character("门卫", color='#ffff')

define ZhouXiaoyu = Character("周小雨", color='#ffff')
define TeacherTian = Character("田老师", color='#ffff')
define ZhengHui = Character("郑辉", color='#ffff')
define LiuYang= Character("刘洋", color='#ffff')
define Wanghao = Character("王浩", color='#ffff')
define YuanQiaoqiao = Character("袁巧巧", color='#ffff')
define Tomoko = Character("高桥智子", color='#ffff')
define Zhizi = Character("智子", color='#ffff')


#################################################################
## Lesson 1 Greetings
image l1 picture1 = "images/greetings/l1/Picture1.jpg"
image l1 picture2 = "images/greetings/l1/Picture2.jpg"
image l1 picture3 = "images/greetings/l1/Picture3.jpg"
image l1 picture4 = "images/greetings/l1/Picture4.jpg"


#################################################################
## Variables
default HaoGan = 0
# define persistent.lesson1_attempt = []
# Prologue
default prologue_select = [0, 0, 0, 0]
default prologue_answer = [0, 0, 0, 0, 0, 0]
default Baohe = 0

# Chpt 1
default chpt1_select = [0, 0, 0, 0, 0]
default chpt1_answer_bunka = [0, 0, 0]
default chpt1_answer_kana = [0, 0, 0, 0, 0]
default chpt1_answer_tango = [0, 0, 0]
default chpt1_answer_kaiwa = [0, 0, 0]


#################################################################
## Auto Declar Pictures
init python hide:
    for file in renpy.list_files():
        if file.startswith('images/cha'):
            if file.endswith('.png'):
                name = file.replace('images/cha/','').replace('.png','')
                renpy.image(name, Image(file, ))
                continue
            continue
        if file.startswith('images/wupin'):
            if file.endswith('.png'):
                name = file.replace('images/wupin/','').replace('.png','')
                renpy.image(name, Image(file, ))
                continue
            continue


#################################################################
## Default Sound Channels
define config.default_music_volume = 0.5
define config.default_sfx_volume = 0.5
define config.default_voice_volume = 1.0
define config.auto_voice = "audio/voice/{id}.mp3"


#################################################################
## Hirakana & Katakana
define HiraKataKANA = {
    "a_o" : ["a","i","u","e","o"],
    "ka_ko" : ["ka","ki","ku","ke","ko"]
}


#################################################################
## Transforms
# 物品
transform wleft:
    zoom 1.0
    ypos 25 xalign 0.02

transform middle:
    zoom 1.0
    ypos 25 xalign 0.5

transform tjleft:
    zoom 1.0
    ypos 25 xalign 0.0
    xoffset -50

# 2人
transform left:
    zoom 1.0
    ypos 25 xalign 0.1

transform right:
    zoom 1.0
    ypos 25 xalign 1.1

transform MidToLeft:
    zoom 1.0
    ypos 25 xalign 0.5
    linear 1 xpos 0.25

transform LeftToMid:
    zoom 1.0
    ypos 25 xalign 0.25
    linear 1 xalign 0.5

transform MidToRight:
    zoom 1.0
    ypos 25 xalign 0.5
    linear 1 xpos 0.7

transform RightToMid:
    zoom 1.0
    ypos 25 xalign 0.7
    linear 1 xpos 0.5

# 3人
transform t_left:
    zoom 1.0
    ypos 25 xalign 0.05

transform t_right:
    zoom 1.0
    ypos 25 xalign 0.85

transform t_MidToLeft:
    zoom 1.0
    ypos 25 xalign 0.5
    linear 1 xpos 0.2

transform t_LeftToMid:
    zoom 1.0
    ypos 25 xalign 0.2
    linear 1 xalign 0.5

transform t_MidToRight:
    zoom 1.0
    ypos 25 xalign 0.5
    linear 1 xpos 0.75

transform t_RightToMid:
    zoom 1.0
    ypos 25 xalign 0.75
    linear 1 xpos 0.5

# 4人
transform f_left:
    zoom 1.0
    ypos 25 xalign 0.275

transform f_lleft:
    zoom 1.0
    ypos 25 xalign -0.1

transform f_right:
    zoom 1.0
    ypos 25 xalign 0.7

transform f_rright:
    zoom 1.0
    ypos 25 xalign 1.0

# 5人
transform fi_left:
    zoom 1.0
    ypos 25 xalign 0.19

transform fi_lleft:
    zoom 1.0
    ypos 25 xalign -0.1

transform fi_right:
    zoom 1.0
    ypos 25 xalign 0.85

transform fi_rright:
    zoom 1.0
    ypos 25 xalign 1.1