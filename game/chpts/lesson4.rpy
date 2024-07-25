#第四课
label lesson4_1:

    #日语课
    #{显示背景  p jiaoxue19}
    scene p jiaoxue19 with dissolve
    #第四课 文化常识
    #{播放BGM b0403}
    play music "audio/bgm/b0403.mp3"
    #{显示立绘TJ 1wx}
    show TJ 1wx at tjleft with dissolve
    TeacherTian "各位同学，今天我们将继续进行第四课的学习。"
    TeacherTian "上课之前，我先问问大家，你们知道和服的由来吗？"
    #{显示背景  p jiaoxue20}
    scene p jiaoxue20 with dissolve
    #{显示立绘WH 12rz}
    show WH 12rz at t_right with dissolve
    me "日本的和服应该是起源于中国的汉服吧。"
    #{显示背景  p jiaoxue21}
    scene p jiaoxue21 with dissolve
    #{显示立绘TJ 1gx}
    show TJ 1gx at tjleft with dissolve
    TeacherTian "没错。我们这里所说的汉服一般是指以华夏礼仪文化为中心，经过漫长的历史演变而形成的具有独特汉民族风貌的传统服饰体系。"
    #{显示立绘QQ 12wx}
    show QQ 12wx at t_right with dissolve
    YuanQiaoqiao "那汉服具体是什么时候诞生的呢？"
    #{显示背景  p jiaoxue22}
    scene p jiaoxue22 with dissolve
    #{显示立绘TJ 1wx}
    show TJ 1wx at tjleft with dissolve
    TeacherTian "汉服的源流可以追溯到上古时期。《周易•系辞》中有明确记录：黄帝、尧、舜垂衣裳而天下治。"
    #{显示背景  p jiaoxue23}
    scene p jiaoxue23 with dissolve
    #{显示立绘TJ 1gx}
    show TJ 1gx at tjleft with dissolve
    TeacherTian "西周时，服饰制度逐渐完善，《周礼》中记录了完整的衣冠礼制，并成为之后历代衣冠礼制的蓝本。"
    #{显示立绘LY 12jy}
    show LY 12jy at t_right with dissolve
    LiuYang "哇，没想到汉服的历史竟然如此悠久。"
    #{显示立绘TJ 1wx}
    show TJ 1wx
    TeacherTian "不仅仅是服装本身，汉服体系还包括发式、面饰、鞋履、配饰等。"
    TeacherTian "因此，汉服可谓‘衣冠上国，礼仪之邦’这一美誉的生动体现。"
    #{显示立绘QQ 12jy}
    hide LY
    show QQ 12jy at t_right
    with dissolve
    YuanQiaoqiao "原来如此。那汉服又是什么时候传到日本的呢？"
    #{显示背景  p jiaoxue24}
    scene p jiaoxue24 with dissolve
    #{显示立绘TJ 1wx}
    show TJ 1wx at tjleft with dissolve
    TeacherTian "日本在弥生时代与中国三国时期的吴国贸易往来密切，吴国的纺织缝纫技术和服饰由此传至日本。"
    #{显示背景  p jiaoxue25}
    scene p jiaoxue25 with dissolve
    TeacherTian "奈良时代日本正式从中国引入了服饰制度，当时朝廷颁布的“衣服令”仿效了唐代的冠服制度。"
    #{显示立绘XY 11zm}
    show XY 11zm at t_right with dissolve
    ZhouXiaoyu "现在的日本人还经常穿和服吗？"
    #{显示立绘TJ 1gx}
    show TJ 1gx at tjleft with dissolve
    #{显示背景  p jiaoxue26}
    TeacherTian "没错，每到日本传统的‘七五三’节，很多家长都会和孩子一起穿上和服，前去神社参拜，祈愿孩子健康成长。"
    #{显示立绘QQ 12gx}
    hide XY
    show QQ 12gx at t_right
    with dissolve
    YuanQiaoqiao "中国现在也有很多年轻人喜欢在庙会的时候穿汉服。"
    #{显示立绘TJ 1wx}
    show TJ 1wx
    TeacherTian "是啊。"
    TeacherTian "它们承载着两国的历史，延续着两国的文化生命，纵然时光流逝、岁月更替，依然散发着不可磨灭的光彩。"
    #{显示立绘TJ 1gx}
    show TJ 1gx
    TeacherTian "我们来做一个小测试，看看大家是否掌握了刚才所讲的知识。"
    jump lesson4_1_q1

label lesson4_1_q1:
    #{显示背景 blackboard }
    scene blackboard with dissolve
    show TJ 1gx at tjleft with dissolve
    menu l4_1_q1:
        '以下哪项是日本和服的起源？'
        "1.韩国的韩服":
            $chpt4_answer_bunka[0] = 0
            jump l4_1_q1AC
        "2.中国的汉服":
            $chpt4_answer_bunka[0] = 10
            jump l4_1_q1B
        "3.印度的纱丽":
            $chpt4_answer_bunka[0] = 0
            jump l4_1_q1AC

label l4_1_q1B:
    #选择2.中国的汉服
    #好感度参数 +10
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。日本的和服是在中国的汉服的基础上演变而来。"
    jump lesson4_1_q2

label l4_1_q1AC:
    # 选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放 SE cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"
    TeacherTian "上课要认真听讲哦。日本的和服是在中国的汉服的基础上演变而来。"
    jump lesson4_1_q2

label lesson4_1_q2:
    if chpt4_C_answer_bunka_index < 1:
        $ chpt4_C_answer_bunka_index = 1
    #{显示立绘TJ 1gx}
    show TJ 1gx at tjleft
    menu l4_1_q2:
        '汉服什么时候传入了日本？'
        "1.三国时期":
            $chpt4_answer_bunka[1] = 10
            jump l4_1_q2A
        "2.汉代":
            $chpt4_answer_bunka[1] = 0
            jump l4_1_q2BC
        "3.唐代":
            $chpt4_answer_bunka[1] = 0
            jump l4_1_q2BC

label l4_1_q2A:
    #选择1.三国时期
    #好感度参数 +10
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。日本在弥生时代与中国三国时期的吴国贸易往来密切，吴国的纺织缝纫技术和服饰由此传至日本。"
    jump lesson4_1_q3

label l4_1_q2BC:
    # 选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放 SE cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"
    TeacherTian "上课要认真听讲哦。日本在弥生时代与中国三国时期的吴国贸易往来密切，吴国的纺织缝纫技术和服饰由此传至日本。"
    jump lesson4_1_q3

label lesson4_1_q3:

    if chpt4_C_answer_bunka_index < 2:
        $ chpt4_C_answer_bunka_index = 2
    #{显示立绘TJ 1gx}
    show TJ 1gx at tjleft
    menu l4_1_q3:
        '日本什么时候从中国引入了服饰制度？'
        "1.飞鸟时代":
            $chpt4_answer_bunka[2] = 0
            jump l4_1_q3AC
        "2.奈良时代":
            $chpt4_answer_bunka[2] = 10
            jump l4_1_q3B
        "3.平安时代":
            $chpt4_answer_bunka[2] = 0
            jump l4_1_q3AC

label l4_1_q3B:
    #选择2.奈良时代
    #好感度参数 +10
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。奈良时代日本正式从中国引入了服饰制度，当时朝廷颁布的“衣服令”仿效了唐代的冠服制度。"
    jump lesson4_2

label l4_1_q3AC:
    # 选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放 SE cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"
    TeacherTian "上课要认真听讲哦。奈良时代日本正式从中国引入了服饰制度，当时朝廷颁布的“衣服令”仿效了唐代的冠服制度。"
    jump lesson4_2


label lesson4_2:
    if chpt4_C_answer_bunka_index < 3:
        $ chpt4_C_answer_bunka_index = 3

    #第四课 假名部分
    #{停止播放BGM }
    stop music
    scene blackboard with dissolve
    #{显示立绘TJ 1gx}
    show TJ 1gx at tjleft with dissolve
    TeacherTian "接下来我们来学习本课的第二项内容，「ま行～や行」的八个假名。"
    TeacherTian "请智子同学为我们读一下吧。"
    TeacherTian "智子ちゃん、ちょっと読んでもらえますか。（智子，能请你读一下吗？）"
    #{显示立绘ZZ 12xf}
    hide TJ
    show ZZ 12xf at left:
        xoffset -150
    with dissolve
    Tomoko "はい。（好的。）"
    #{播放 SE }
    # play sound "audio/se/sushiyin/naha10.mp3"
    show screen HiraKataKANA("ma_mo", "ya_yo", learning=False)
    if chpt4_C_answer_kana_index < 10:
        $ chpt4_C_answer_kana_index = 10
    #{显示立绘ZZ 12wx}
    show ZZ 12wx
    #{播放 SE maya10}
    play sound "audio/se/sushiyin/maya10.mp3"
    Tomoko "ま、み、む、め、も、や、ゆ、よ。"
    #{显示立绘TJ 1gx}
    hide ZZ
    show TJ 1gx at left:
        xoffset -150
    with dissolve
    TeacherTian "もう一度お願いします。（请再读一遍。）"
    #{显示立绘ZZ 12wx}
    hide TJ
    show ZZ 12wx at left:
        xoffset -150
    with dissolve
    #{播放 SE maya10}
    play sound "audio/se/sushiyin/maya10.mp3"
    Tomoko "ま、み、む、め、も、や、ゆ、よ。"
    hide screen HiraKataKANA
    #{显示立绘TJ 1gx}
    hide ZZ
    show TJ 1gx at left:
        xoffset -150
    with dissolve
    TeacherTian "大家可以跟读练习一下哦。"

    # {显示图片 十个假名 点击可以发音}
    # 点击图片可以确认发音，完成学习后点击“结束学习”按钮。
    hide TJ with dissolve
    call screen HiraKataKANA("ma_mo", "ya_yo")

    show TJ 1wx at left with dissolve:
        xoffset -150
    TeacherTian "既然大家都学会了，那么我们来做一个小测试吧。请大家根据听到的读音选择正确的假名。"

    jump lesson4_2_q1

label lesson4_2_q1:
    stop music
    #循环到此处
    #{播放 SE diyiti}
    hide ZZ
    show TJ 1wx
    with dissolve
    TeacherTian "第一题。"
    play sound "audio/se/sushiyin/ma.mp3"
    pause 1.5
    #{播放 SE ma}
    menu l4_2_q1:
        "1.ま":
            $chpt4_answer_kana[0] = 5
            jump l4_2_q1A
        "2.み":
            $chpt4_answer_kana[0] = 0
            jump l4_2_q1BC
        "3.む":
            $chpt4_answer_kana[0] = 0
            jump l4_2_q1BC

label l4_2_q1A:
    #选择"1.ま"
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"
    jump lesson4_2_q2

label l4_2_q1BC:
    #选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"
    TeacherTian "好像不太对哦，再听一遍。"
    #循环到第本题开始的位置
    jump lesson4_2_q1


label lesson4_2_q2:
    #循环到此处
    #{播放 SE dierti}
    TeacherTian "第二题。"
    play sound "audio/se/sushiyin/yu.mp3"
    pause 1.5
    #{播放 SE yu}
    menu l4_2_q2:
        "1.や":
            $chpt4_answer_kana[1] = 0
            jump l4_2_q2AC
        "2.ゆ":
            $chpt4_answer_kana[1] = 5
            jump l4_2_q2B
        "3.よ":
            $chpt4_answer_kana[1] = 0
            jump l4_2_q2AC

label l4_2_q2B:
    #选择"2.ゆ"
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"
    jump lesson4_2_q3

label l4_2_q2AC:
    #选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"
    TeacherTian "好像不太对哦，再听一遍。"
    #循环到第本题开始的位置
    jump lesson4_2_q2

label lesson4_2_q3:
    #循环到此处
    #{播放 SE disanti}
    TeacherTian "第三题。"
    play sound "audio/se/sushiyin/mo.mp3"
    pause 1.5
    #{播放 se mo}
    menu l4_2_q3:
        "1.め":
            $chpt4_answer_kana[2] = 0
            jump l4_2_q3AC
        "2.も":
            $chpt4_answer_kana[2] = 5
            jump l4_2_q3B
        "3.せ":
            $chpt4_answer_kana[2] = 0
            jump l4_2_q3AC

label l4_2_q3B:
    #选择"2.も"
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"
    jump lesson4_2_q4

label l4_2_q3AC:
    #选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"
    TeacherTian "好像不太对哦，再听一遍。"
    #循环到第本题开始的位置
    jump lesson4_2_q3

label lesson4_2_q4:
    #循环到此处
    #{播放 SE disiti}
    TeacherTian "第四题。"
    play sound "audio/se/sushiyin/yo.mp3"
    #{播放 se yo}
    menu l4_2_q4:
        "1.ま":
            $chpt4_answer_kana[3] = 0
            jump l4_2_q4AB
        "2.や":
            $chpt4_answer_kana[3] = 0
            jump l4_2_q4AB
        "3.よ":
            $chpt4_answer_kana[3] = 5
            jump l4_2_q4C

label l4_2_q4C:
    #选择"3.よ"
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"
    jump lesson4_2_q5

label l4_2_q4AB:
    #选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"
    TeacherTian "好像不太对哦，再听一遍。"
    #循环到第本题开始的位置
    jump lesson4_2_q4

label lesson4_2_q5:
    #循环到此处
    #{播放 SE diwuti}
    TeacherTian "第五题。"
    play sound "audio/se/sushiyin/mi.mp3"
    #{播放 se mi}
    menu l4_2_q5:
        "1.も":
            $chpt4_answer_kana[4] = 0
            jump l4_2_q5AC
        "2.み":
            $chpt4_answer_kana[4] = 5
            jump l4_2_q5B
        "3.ゆ":
            $chpt4_answer_kana[4] = 0
            jump l4_2_q5AC

label l4_2_q5B:
    #选择"2.み"
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"
    jump lesson4_3

label l4_2_q5AC:
    #选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"
    TeacherTian "好像不太对哦，再听一遍。"
    #循环到第本题开始的位置
    jump lesson4_2_q5

label lesson4_3:
    show TJ 1gx
    TeacherTian "这八个假名大家都已经掌握了，接下来我们来看一下它们可以组成哪些单词。"
    TeacherTian "智子ちゃん、こちらの単語を読んでもらえますか。（智子，能请你读一下这些单词吗？）"
    #{显示立绘ZZ 12wx}
    show ZZ 12wx at right with dissolve
    Tomoko "はい。読みます。（好的，我读了。）"

    hide TJ with dissolve
    if chpt4_C_answer_tango_index < 1:
        $ chpt4_C_answer_tango_index = 1

    #{播放 se 041machi2 }
    if chpt4_C_answer_tango_index < 1:
        $ chpt4_C_answer_tango_index = 1
    show 041machi2 at middle with dissolve
    # play sound "audio/se/sushiyin/041machi2.mp3"
    Tomoko "町（まち）。"
    hide 041machi2 with dissolve


    #{播放 se 042ame2 }
    if chpt4_C_answer_tango_index < 2:
        $ chpt4_C_answer_tango_index = 2
    show 042ame2 at middle with dissolve
    # play sound "audio/se/sushiyin/042ame2.mp3"
    Tomoko "雨（あめ）。"
    hide 042ame2 with dissolve

    #{播放 se 043heya2 }
    if chpt4_C_answer_tango_index < 3:
        $ chpt4_C_answer_tango_index = 3
    show 043heya2 at middle with dissolve
    # play sound "audio/se/sushiyin/043heya2.mp3"
    Tomoko "部屋（へや）。"
    hide 043heya2 with dissolve

    #{播放 se 044yume2 }
    if chpt4_C_answer_tango_index < 4:
        $ chpt4_C_answer_tango_index = 4
    show 044yume2 at middle with dissolve
    # play sound "audio/se/sushiyin/044yume2.mp3"
    Tomoko "夢（ゆめ）。"
    hide 044yume2 with dissolve

    #{显示立绘TJ 1gx}
    show TJ 1gx at tjleft with dissolve
    TeacherTian "大家可以跟读练习一下哦。"
    hide TJ
    hide ZZ
    with dissolve

    #{显示图片1-4  点击可以发音}
    call screen Dango(Dango_L4)
    # 点击图片可以确认发音，完成学习后点击“结束学习”按钮。

    show TJ 1wx at tjleft with dissolve
    TeacherTian "既然大家都学会了，那么我们来做一个小测试吧。请大家根据听到的读音选择正确的单词。"


    jump lesson4_3_q1


label lesson4_3_q1:
    #{播放 SE diyiti}
    hide ZZ
    show TJ 1wx
    with dissolve
    TeacherTian "第一题。"
    #{播放 se 043heya }
    pause 1.5
    play sound "audio/se/sushiyin/043heya2.mp3"
    pause 1.0
    menu l4_3_q1:
        "1.町（まち）":
            $chpt4_answer_tango[0] = 0
            jump l4_3_q1AB
        "2.雨（あめ）":
            $chpt4_answer_tango[0] = 0
            jump l4_3_q1AB
        "3.部屋（へや）":
            $chpt4_answer_tango[0] = 5
            jump l4_3_q1C

label l4_3_q1C:
    #选择"3.部屋（へや）"
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"
    jump lesson4_3_q2

label l4_3_q1AB:
    #选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"
    TeacherTian "好像不太对哦，再听一遍。"
    #循环到本题上方
    jump lesson4_3_q1

label lesson4_3_q2:
    #{播放 SE dierti}
    hide ZZ
    show TJ 1wx
    with dissolve
    TeacherTian "第二题。"
    #{播放 se 044yume }
    pause 1.5
    play sound "audio/se/sushiyin/044yume2.mp3"
    pause 1.0
    menu l4_3_q2:
        "1.部屋（へや）":
            $chpt4_answer_tango[1] = 0
            jump l4_3_q2AC
        "2.夢（ゆめ）":
            $chpt4_answer_tango[1] = 5
            jump l4_3_q2B
        "3.町（まち）":
            $chpt4_answer_tango[1] = 0
            jump l4_3_q2AC

label l4_3_q2B:
    #选择"2.夢（ゆめ）"
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"
    jump lesson4_3_q3

label l4_3_q2AC:
    #选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"
    TeacherTian "好像不太对哦，再听一遍。"
    #循环到本题上方
    jump lesson4_3_q2

label lesson4_3_q3:
    #{播放 SE disanti}
    TeacherTian "第三题。"
    #{播放 se 041machi }
    pause 1.5
    play sound "audio/se/sushiyin/041machi2.mp3"
    pause 1.0
    menu l4_3_q3:
        "1.夢（ゆめ）":
            $chpt4_answer_tango[2] = 0
            jump l4_3_q3AB
        "2.雨（あめ）":
            $chpt4_answer_tango[2] = 0
            jump l4_3_q3AB
        "3.町（まち）":
            $chpt4_answer_tango[2] = 5
            jump l4_3_q3C

label l4_3_q3C:
    #选择"3.町（まち）"
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"
    jump lesson4_4

label l4_3_q3AB:
    #选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"
    TeacherTian "好像不太对哦，再听一遍。"
    #循环到本题上方
    jump lesson4_3_q3

label lesson4_4:
    #{播放BGM b0403}
    play music "audio/bgm/b0403.mp3"
    #{显示背景  blackboard}
    scene blackboard with dissolve
    #{显示立绘TJ 1gx}
    show TJ 1gx at tjleft with dissolve
    TeacherTian "今天的内容就是这些，同学们都掌握了吗？"
    TeacherTian "对了，明天是智子同学在我们学校的最后一天哦。为了让她能够更好地了解中国文化，明天下午全班一起去七宝老街进行文化体验活动。"
    #{显示立绘QQ 13gx}
    hide TJ
    show QQ 13gx at middle
    with dissolve
    YuanQiaoqiao "太好了，又可以出去玩啦。"
    #{显示立绘ZZ 13wx}
    show QQ at MidToRight
    show ZZ 13wx at left with dissolve
    Zhizi "七宝老街ってどんなところ？(七宝老街是怎么样的地方啊？) "
    #{显示立绘LY 13wx}
    hide QQ
    show LY 13wx at right
    with dissolve
    # TODO: Missing Voice Audio
    LiuYang "中国の古い町って感じかな。（就是中国的古镇。）"
    #{显示立绘ZZ 11gx}
    show ZZ 11gx
    Zhizi "へえ、面白そう！ (听上去很有意思！) "
    #{显示立绘XY 13dx}
    hide LY
    show XY 13dx at t_right
    with dissolve
    ZhouXiaoyu "明天我们组一起带智子好好逛逛吧！"


    #晚上宿舍
    #{显示背景  qinshi}
    scene p06 qinshi with dissolve
    #{播放BGM b0404}
    play music "audio/bgm/b0404.mp3"
    "晚自修结束后，我坐在书桌边，回忆起今天中午发生的事情……"
    #{显示立绘WH 12zm}
    show WH 12zm at middle with dissolve
    "郑辉虽然平时挺内向的，为了巧巧能够毫不犹豫地挺身而出，这可能就是爱的力量吧。"
    #{显示立绘WH 13wx}
    show WH 13wx
    "明天就是智子在学校的最后一天了，和智子在一起的时光感觉又真实又奇妙。"
    "明明现在的智子是小自己十岁的小女孩，但是我却在她身上感受到了超越年龄的成熟和坚定。"
    #{显示立绘WH 11wx}
    show WH 11wx
    "或许这就是我当年感受到的魅力吧……"
    "聊天软件的提示音打断了我的思绪。"
    #{显示立绘ZZ 13wx}
    show WH at MidToRight
    show ZZ 13wx at left with dissolve
    Zhizi "こんばんは。(*′σ∀`)p（晚上好啊。）"

    #{显示选项  文本框居中，选项竖排1 2}
    menu l4_4_q1:
        "1.おはよう。":
            $chpt4_answer_kaiwa[0] = 0
            jump l4_4_q1A
        "2.こんばんは。":
            $chpt4_answer_kaiwa[0] = 10
            jump l4_4_q1B

label l4_4_q1B:
    if chpt4_C_answer_kaiwa_index < 1:
        $ chpt4_C_answer_kaiwa_index = 1
    #选择2.
    #好感度参数 +10
    #{显示立绘WH 13gx}
    show WH 13gx
    me "こんばんは。今日はありがとう。本当に助かったよ。（晚上好，今天谢谢你啊，真是帮大忙了。）"
    jump lesson4_5

label l4_4_q1A:
    if chpt4_C_answer_kaiwa_index < 1:
        $ chpt4_C_answer_kaiwa_index = 1
    #选择1.
    me "不对，不对。现在是晚上了，应该说……"
    #{显示立绘WH 13gx}
    show WH 13gx
    me "こんばんは。今日はありがとう。本当に助かったよ。（晚上好，今天谢谢你啊，真是帮大忙了。）"
    jump lesson4_5

label lesson4_5:
    #{显示立绘ZZ 14gx}
    show ZZ 14gx
    Zhizi "ううん、無事に解決できて、よかった。（不必谢。能顺利解决太好了。）"
    #{显示立绘ZZ 11xf}
    show ZZ 11xf
    Zhizi "でも、鄭さんがいきなり告白して、びっくりした。（不过，看到郑辉大胆告白，着实吃了一惊呢。）"
    #{显示立绘WH 13jy}
    show WH 13jy
    me "日本人はストレートに告白しないの？（日本人不会直接表白吗？）"
    #{显示立绘ZZ 13wx}
    show ZZ 13wx
    Zhizi "「愛してる」とか、「好きだ」とかあんまり言わないかも。（不太会直接说爱喜欢之类的。）"
    #{显示立绘WH 11rz}
    show WH 11rz
    me "じゃあ、何って言えばいいの？（那怎么说呢？）"
    #{显示立绘ZZ 11wx}
    show ZZ 11wx
    Zhizi "そうね…夏目漱石のあの有名な話、知ってる？（恩，你有听过夏目漱石那个有名的故事吗？）"
    #{显示立绘WH 12gx}
    show WH 12gx
    me "夏目漱石って、『吾輩は猫である』の作者だよね。（我是猫的作者对吧。）"
    #{显示立绘ZZ 13gx}
    show ZZ 13gx
    Zhizi "そう。実はね、夏目漱石が英語教師をしていた時、生徒たちに「I love you.」を訳すよう言ったの。（是的，其实夏目漱石在做英语老师的时候，曾教学生翻译I love you.这句话。）"
    #{显示立绘ZZ 14xf}
    show ZZ 14xf
    Zhizi "教え子たちはみんな「君を愛してる」って訳したんだけど、夏目漱石は「日本人はそんなことは口にしない」と怒ったそうよ。（学生们回答我爱你这样的答案，但夏目漱石生气地却说日本人不会说这样的话。）"
    #{显示立绘WH 11rz}
    show WH 11rz
    me "そうなの？正解は？（是吗？那应该怎么说呢？）"
    #{显示立绘ZZ 11wx}
    show ZZ 11wx
    Zhizi "少し考えてみて。(〃^∇^)o（你先想想哦。）"
    "智子发了一个可爱的颜文字，留下了对明天的遐想。我也不好再去追问，便和智子互相道了晚安。"
    hide ZZ with dissolve
    "刚想躺下休息，突然想起了电话铃。"
    #{播放BGM b0405 shinianhou}
    # play music "audio/bgm/b0405 shinianhou.mp3"
    #{显示立绘XY 13zm}
    show XY 13zm at left with dissolve
    ZhouXiaoyu "喂，王浩。你在忙什么呢，怎么不回消息啊！"
    "电话那头传来了小雨有些埋怨的声音。"
    #{显示立绘WH 13jy}
    show WH 13jy
    me "没，没忙啥。有什么事吗？"
    #{显示立绘XY 11cx}
    show XY 11cx
    ZhouXiaoyu "呵呵，不会是在和智子小姐姐聊天吧。我发你消息都不回。"
    #{显示立绘WH 12jy}
    show WH 12jy
    me "我……"
    "被周小雨怼了一句顿时无言以答，刚刚根本没注意到她发来的消息。"
    #{显示立绘XY 12wx}
    show XY 12wx
    ZhouXiaoyu "好了好了，不为难你了。和你说正事啊。明天不是智子在我们学校的最后一天了嘛，我写了首歌，想明天和我们组的小伙伴一起唱给她听，你觉得如何？"
    "说起写歌的事情，当年周小雨好像确实说要写首歌。后来被飞来的足球击中了手腕，结果也就不了了之了。"
    "这次的穿越避免了周小雨受伤的事情发生，看来真的是改变了原本时间线。"
    #{显示立绘WH 12gx}
    show WH 12gx
    me "我觉得很好啊，发过来听听呗。"
    #{显示立绘XY 13cx}
    show XY 13cx
    ZhouXiaoyu "你也觉得好是吧，那太好了。嗯，不过还有一点遗憾，就是我不会写日语歌词，能不能请你帮个忙？"
    #{显示立绘WH 11kx}
    show WH 11kx
    me "可以是可以啊，你为啥不找刘洋啊？"
    #{显示立绘XY 12zm}
    show XY 12zm
    ZhouXiaoyu "不行不行，他身上的那些音乐细胞估计早就灭绝了。"
    #{显示立绘WH 13gx}
    show WH 13gx
    me "确实。这么说来就没听过刘洋唱歌……。好吧，我试试看哦。"
    #{显示立绘XY 12dx}
    show XY 12dx
    ZhouXiaoyu "ok。就这么说定了，记得看短信。"
    #{立绘消失}
    hide XY
    hide WH
    with dissolve
    #{停止播放BGM}
    stop music
    "还没来得及回答，周小雨便挂断了电话，还是一贯地那么雷厉风行……。打开手机看到了周小雨发过来的歌词，并点开了音频。"
    #{播放BGM b0406 xiaoyu }
    play music "audio/bgm/b0406 xiaoyu.mp3"
    $ renpy.pause(26, hard=True)
    #强制以上BGM播放完毕以后再操作，bgm不重复滚动
    stop music
    "非常好听的曲子，歌词也很有青春气息。看来周小雨选择做音乐老师太正确了。"
    "日语歌词如果仅仅是翻译的话，感觉又有一些单调。让我想想如何去写吧……"
    "放下手机，躺在床上却久久难以入睡，又回想到这两天和智子还有小伙伴们相处的点点滴滴。不由地感到有些温暖。"
    "高中时代同学之间纯真友谊和对梦想的憧憬让我感到了温暖和希望……"

    jump lesson5_1