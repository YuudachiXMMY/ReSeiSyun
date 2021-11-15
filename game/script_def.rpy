#################################################################
## Character Definations
define me = Character("我", color='#ffff')
define question = Character("???", color='#ffff')
define ZhouXiaoyu = Character("周小雨", color='#ffff')

define TeacherTian = Character("田老师", color='#ffff')
define ZhengHui = Character("郑辉", color='#ffff')
define LiuYang= Character("刘洋", color='#ffff')
define YuanQiaoqiao = Character("袁巧巧", color='#ffff')
define Tomoko = Character("高桥智子", color='#ffff')


#################################################################
## Lesson 1 Greetings
image l1 picture1 = "images/greetings/l1/Picture1.jpg"
image l1 picture2 = "images/greetings/l1/Picture2.jpg"
image l1 picture3 = "images/greetings/l1/Picture3.jpg"
image l1 picture4 = "images/greetings/l1/Picture4.jpg"

#################################################################
## Variables
define persistent.lesson1_attempt = []


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
transform middle:
    zoom 0.6
    ypos 25 xalign 0.5

transform left:
    zoom 0.6
    ypos 25 xalign 0.02

transform right:
    zoom 0.6
    ypos 25 xalign 0.9

transform MidToLeft:
    zoom 0.6
    ypos 25 xalign 0.5
    linear 1 xpos 0.2

transform LeftToMid:
    zoom 0.6
    ypos 25 xalign 0.2
    linear 1 xpos 0.4
