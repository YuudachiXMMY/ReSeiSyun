#第五课
label lesson5_1:

    scene black_bg with Dissolve(2)
    #显示第五章过渡幕间图片
    #{显示背景  pz 05 }
    scene pz 05 with Dissolve(2)
    pause 1
    #{播放bgm0501}
    play music "audio/bgm/b0501.mp3"
    #{显示背景  p05 jiaoshijiu }
    scene p05 jiaoshijiu with Dissolve(2.5)
    #{显示立绘WH 11kx}
    show WH 11kx at middle with dissolve
    me "昨天为了翻译小雨写的歌词久久难以入睡。"
    me "脑袋现在还是晕晕沉沉的，上午的课一个字也没听进去。"
    me "看到王老师走进了教室，才发现已经到了上午最后一节课……"
    me "恩，打起精神听课吧。"
    #{显示背景  p jiaoxue27 }
    scene p jiaoxue27 with dissolve
    #{显示立绘TJ 1wx}
    show TJ 1wx at tjleft with dissolve
    TeacherTian "各位同学，今天我们将继续进行第五课的学习。"
    TeacherTian "我们今天聊一个比较轻松的话题——料理。大家知道“料理”这个词的由来吗？"
    #{显示背景  blackboard}
    scene blackboard with dissolve
    #{显示立绘LY 12hz}
    show LY 12hz at right with dissolve
    LiuYang "汉语和日语中都有“料理”一词。"
    #{显示立绘WH 11jy}
    show WH 11jy at left with dissolve
    me "我记得老师好像说过“料理”一词起源于中国，原意指的是“处理事务”。"
    #{显示背景  p jiaoxue29 }
    scene p jiaoxue29 with dissolve
    #{显示立绘TJ 1wx}
    show TJ 1wx at tjleft with dissolve
    TeacherTian "没错，王浩你很厉害哦。日本从平安时代开始使用“料理”一词，原本指处理食材，后来慢慢用于指称菜肴。"
    #{显示立绘QQ 11jy}
    show QQ 11jy at t_right with dissolve
    YuanQiaoqiao "原来是这样啊。"
    #{显示立绘TJ 1gx}
    show TJ 1gx
    TeacherTian "那么，你们知道有哪些“日本料理”起源于中国吗？"
    #{显示立绘ZZ 13ys}
    hide QQ
    show ZZ 13ys at t_right
    with dissolve
    Tomoko "ラーメンは中国から伝わったんですね。（拉面是从中国传到日本的吧？）"
    #{显示背景  p jiaoxue30}
    scene p jiaoxue30 with dissolve
    #{显示立绘TJ 1wx}
    show TJ 1wx at tjleft with dissolve
    TeacherTian "智子同学说得没错。除此之外其实还有很多。日本料理中最具有代表性的“刺身”也起源于中国。"
    #{显示背景  p jiaoxue31}
    scene p jiaoxue31 with dissolve
    #{显示立绘XY 11zm}
    show XY 11zm at t_right with dissolve
    ZhouXiaoyu "这样说来，我想起历史老师曾说过中国早在周朝就有吃生鱼片的记载。"
    #{显示立绘TJ 1gx}
    show TJ 1gx at tjleft with dissolve
    TeacherTian "是的。此外在餐桌礼仪上，日本的饮食文化中也能看到中国文化的影子。"
    #{显示背景  p jiaoxue32}
    scene p jiaoxue32 with dissolve
    TeacherTian "不过有一些日本的菜品虽然名字和中国菜很相近，但是做法和味道有很大的区别，例如日本的饺子和中国的饺子就不太一样。"
    #{显示立绘ZH 12zj}
    show ZH 12zj at t_right with dissolve
    ZhengHui "听说日本的饺子一般是煎饺，或者油炸的饺子，是吗？"
    #{显示立绘ZZ 14sq}
    show ZZ 14sq at left with dissolve
    Tomoko "はい、そうです。中国は水餃子ですね。（是的，中国人习惯吃水饺对吗？）"
    #{显示立绘WH 13gx}
    hide ZH
    show WH 13gx at t_right
    with dissolve
    me "そうです。それに、中国では、お正月の時に、よく餃子を食べるので、餃子は中国人にとって、特別な意味があります。（是的。而且在中国，因为大家常会在过年的时候吃饺子，所以饺子对中国人来说有特别的意义。）"
    #{显示立绘LY 13jy}
    hide WH
    show LY 13jy at right
    with dissolve
    LiuYang "智子ちゃん、日本では年越しの時に何を食べますか。（智子，日本过年的时候大家会吃什么呢？）"
    #{显示背景  p jiaoxue33}
    scene p jiaoxue33 with dissolve
    #{显示立绘ZZ 13gx}
    show ZZ 13gx at left with dissolve
    Tomoko "えっと、日本も地域によって多少違いはありますが、「年越しそば」や「お雑煮」などを食べます。（虽然日本不同地域也有差别，但常吃“过年荞麦面”和“年糕杂煮”之类的。）"
    #{显示立绘XY 13wx}
    show XY 13wx at t_right with dissolve
    ZhouXiaoyu "原来如此，真有趣。"

    #{显示立绘TJ 1gx}
    scene blackboard with dissolve
    show TJ 1gx at middle with dissolve
    TeacherTian "大家聊得很开心嘛。那我们来做一个小测试，看看大家是否掌握了刚才所讲的内容。"
    jump lesson5_1_q1

label lesson5_1_q1:
    show TJ 1gx at tjleft with dissolve
    menu l5_1_q1:
        '“料理”一词在中国古代的意思是什么？'
        "1.处理事务":
            $chpt5_answer_bunka[0] = 10
            jump l5_1_q1A
        "2.处理食材":
            $chpt5_answer_bunka[0] = 0
            jump l5_1_q1BC
        "3.菜肴":
            $chpt5_answer_bunka[0] = 0
            jump l5_1_q1BC

label l5_1_q1A:
    #选择1.处理事务
    #好感度参数 +10
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。“料理”一词起源于中国，原意指的是“处理事务”。"
    jump lesson5_1_q2

label l5_1_q1BC:
    # 选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放 SE cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"  fadein 2.0
    TeacherTian "上课要认真听讲哦。“料理”一词起源于中国，原意指的是“处理事务”。"
    jump lesson5_1_q2

label lesson5_1_q2:
    if chpt5_C_answer_bunka_index < 1:
        $ chpt5_C_answer_bunka_index = 1
    #{显示立绘TJ 1gx}
    show TJ 1gx at tjleft
    menu l5_1_q2:
        '以下哪种日本料理不是起源于中国的？'
        "1.寿司":
            $chpt5_answer_bunka[1] = 0
            jump l5_1_q2AB
        "2.生鱼片":
            $chpt5_answer_bunka[1] = 0
            jump l5_1_q2AB
        "3.咖喱":
            $chpt5_answer_bunka[1] = 10
            jump l5_1_q2C

label l5_1_q2C:
    #选择3.咖喱
    #好感度参数 +10
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。寿司和生鱼片都是起源于中国。"
    jump lesson5_1_q3

label l5_1_q2AB:
    # 选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放 SE cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"  fadein 2.0
    TeacherTian "上课要认真听讲哦。寿司和生鱼片都是起源于中国。"
    jump lesson5_1_q3

label lesson5_1_q3:

    if chpt5_C_answer_bunka_index < 2:
        $ chpt5_C_answer_bunka_index = 2
    #{显示立绘TJ 1gx}
    show TJ 1gx at tjleft
    menu l5_1_q3:
        '以下哪一项不是日本人过年时吃的食物？'
        "1.荞麦面":
            $chpt5_answer_bunka[2] = 0
            jump l5_1_q3AC
        "2.水饺":
            $chpt5_answer_bunka[2] = 10
            jump l5_1_q3B
        "3.年糕杂煮":
            $chpt5_answer_bunka[2] = 0
            jump l5_1_q3AC

label l5_1_q3B:
    #选择2.水饺
    #好感度参数 +10
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。日本人过年常吃“过年荞麦面”和“年糕杂煮”等食物。"
    jump lesson5_2

label l5_1_q3AC:
    # 选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放 SE cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"  fadein 2.0
    TeacherTian "上课要认真听讲哦。日本人过年常吃“过年荞麦面”和“年糕杂煮”等食物。"
    jump lesson5_2


label lesson5_2:
    if chpt5_C_answer_bunka_index < 3:
        $ chpt5_C_answer_bunka_index = 3

    #第五课 假名部分
    #{停止播放BGM }
    stop music
    scene blackboard with dissolve
    #{显示立绘TJ 1gx}
    show TJ 1gx at tjleft with dissolve
    TeacherTian "接下来我们来学习本课的第二项内容，「ら行〜わ行」的假名以及拨音的读音与书写。"
    TeacherTian "请智子同学为我们读一下吧。"
    TeacherTian "智子ちゃん、ちょっと読んでもらえますか。（智子，能请你读一下吗？）"
    #{显示立绘ZZ 12gx}
    hide TJ
    show ZZ 12gx at left:
        xoffset -150
    with dissolve
    Tomoko "はい。（好的。）"
    # play sound "audio/se/sushiyin/rawa10.mp3"
    show screen HiraKataKANA("ra_ro", "wa_n", learning=False)
    if chpt5_C_answer_kana_index < 10:
        $ chpt5_C_answer_kana_index = 10
    #{播放 SE rawa10}
    Tomoko "ら、り、る、れ、ろ、わ、を、ん。"
    #{显示立绘TJ 1wx}
    hide ZZ
    show TJ 1wx at left:
        xoffset -150
    with dissolve
    TeacherTian "もう一度お願いします。（请再读一遍。）"
    #{显示立绘ZZ 12gx}
    hide TJ
    show ZZ 12gx at left:
        xoffset -150
    with dissolve
    #{播放 SE rawa10}
    Tomoko "ら、り、る、れ、ろ、わ、を、ん。"
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
    call screen HiraKataKANA("ra_ro", "wa_n")

    show TJ 1wx at left with dissolve:
        xoffset -150
    TeacherTian "既然大家都学会了，那么我们来做一个小测试吧。请大家根据听到的读音选择正确的假名。"

    jump lesson5_2_q1

label lesson5_2_q1:
    stop music
    #循环到此处
    #{播放 SE diyiti}
    hide ZZ
    show TJ 1wx
    with dissolve
    TeacherTian "第一题。"
    play sound "audio/se/sushiyin/ra.mp3"
    pause 1.5
    #{播放 SE ra}
    menu l5_2_q1:
        "1.ら":
            $chpt5_answer_kana[0] = 10
            jump l5_2_q1A
        "2.み":
            $chpt5_answer_kana[0] = 0
            jump l5_2_q1BC
        "3.ろ":
            $chpt5_answer_kana[0] = 0
            jump l5_2_q1BC

label l5_2_q1A:
    #选择"1.ら"
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"
    jump lesson5_2_q2

label l5_2_q1BC:
    #选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"  fadein 2.0
    TeacherTian "好像不太对哦，再听一遍。"
    #循环到第本题开始的位置
    jump lesson5_2_q1


label lesson5_2_q2:
    #循环到此处
    #{播放 SE dierti}
    TeacherTian "第二题。"
    play sound "audio/se/sushiyin/ru.mp3"
    pause 1.5
    #{播放 SE ru}
    menu l5_2_q2:
        "1.り":
            $chpt5_answer_kana[1] = 0
            jump l5_2_q2AC
        "2.る":
            $chpt5_answer_kana[1] = 10
            jump l5_2_q2B
        "3.を":
            $chpt5_answer_kana[1] = 0
            jump l5_2_q2AC

label l5_2_q2B:
    #选择"2.る"
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"
    jump lesson5_2_q3

label l5_2_q2AC:
    #选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"  fadein 2.0
    TeacherTian "好像不太对哦，再听一遍。"
    #循环到第本题开始的位置
    jump lesson5_2_q2

label lesson5_2_q3:
    #循环到此处
    #{播放 SE disanti}
    TeacherTian "第三题。"
    play sound "audio/se/sushiyin/re.mp3"
    pause 1.5
    #{播放 se re}
    menu l5_2_q3:
        "1.れ":
            $chpt5_answer_kana[2] = 10
            jump l5_2_q3A
        "2.る":
            $chpt5_answer_kana[2] = 0
            jump l5_2_q3BC
        "3.け":
            $chpt5_answer_kana[2] = 0
            jump l5_2_q3BC

label l5_2_q3A:
    #选择"1.れ"
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"
    jump lesson5_2_q4

label l5_2_q3BC:
    #选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"  fadein 2.0
    TeacherTian "好像不太对哦，再听一遍。"
    #循环到第本题开始的位置
    jump lesson5_2_q3

label lesson5_2_q4:
    #循环到此处
    #{播放 SE disiti}
    TeacherTian "第四题。"
    play sound "audio/se/sushiyin/ri.mp3"
    #{播放 se ri}
    menu l5_2_q4:
        "1.り":
            $chpt5_answer_kana[3] = 10
            jump l5_2_q4A
        "2.し":
            $chpt5_answer_kana[3] = 0
            jump l5_2_q4BC
        "3.わ":
            $chpt5_answer_kana[3] = 0
            jump l5_2_q4BC

label l5_2_q4A:
    #选择"1.り"
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"
    jump lesson5_2_q5

label l5_2_q4BC:
    #选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"  fadein 2.0
    TeacherTian "好像不太对哦，再听一遍。"
    #循环到第本题开始的位置
    jump lesson5_2_q4

label lesson5_2_q5:
    #循环到此处
    #{播放 SE diwuti}
    TeacherTian "第五题。"
    play sound "audio/se/sushiyin/wa.mp3"
    #{播放 se wa}
    menu l5_2_q5:
        "1.ん":
            $chpt5_answer_kana[4] = 0
            jump l5_2_q5AC
        "2.わ":
            $chpt5_answer_kana[4] = 10
            jump l5_2_q5B
        "3.ゆ":
            $chpt5_answer_kana[4] = 0
            jump l5_2_q5AC

label l5_2_q5B:
    #选择"2.わ"
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"
    jump lesson5_3

label l5_2_q5AC:
    #选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"  fadein 2.0
    TeacherTian "好像不太对哦，再听一遍。"
    #循环到第本题开始的位置
    jump lesson5_2_q5

label lesson5_3:
    show TJ 1gx
    TeacherTian "这八个假名大家都已经掌握了，接下来我们来看一下它们可以组成哪些单词。"
    TeacherTian "智子ちゃん、こちらの単語を読んでもらえますか。（智子，能请你读一下这些单词吗？）"
    #{显示立绘ZZ 12gx}
    show ZZ 12gx at right with dissolve
    Tomoko "はい。読みます。（好的，我读了。）"

    hide TJ with dissolve
    if chpt5_C_answer_tango_index < 1:
        $ chpt5_C_answer_tango_index = 1

    #{播放 se 051sora2 }
    if chpt5_C_answer_tango_index < 1:
        $ chpt5_C_answer_tango_index = 1
    show 051sora2 at middle with dissolve
    play sound "audio/se/sushiyin/051sora2.mp3"
    Tomoko "空（そら）。"
    hide 051sora2 with dissolve


    #{播放 se 052iro2 }
    if chpt5_C_answer_tango_index < 2:
        $ chpt5_C_answer_tango_index = 2
    show 052iro2 at middle with dissolve
    play sound "audio/se/sushiyin/052iro2.mp3"
    Tomoko "色（いろ）。"
    hide 052iro2 with dissolve

    #{播放 se 053watashi2 }
    if chpt5_C_answer_tango_index < 3:
        $ chpt5_C_answer_tango_index = 3
    show 053watashi2 at middle with dissolve
    play sound "audio/se/sushiyin/053watashi2.mp3"
    Tomoko "私（わたし）。"
    hide 053watashi2 with dissolve

    #{播放 se 054hon2 }
    if chpt5_C_answer_tango_index < 4:
        $ chpt5_C_answer_tango_index = 4
    show 054hon2 at middle with dissolve
    play sound "audio/se/sushiyin/054hon2.mp3"
    Tomoko "本（ほん）。"
    hide 054hon2 with dissolve

    #{显示立绘TJ 1gx}
    show TJ 1gx at tjleft with dissolve
    TeacherTian "大家可以跟读练习一下哦。"
    hide TJ
    hide ZZ
    with dissolve

    #{显示图片1-4  点击可以发音}
    call screen Dango(Dango_L5)
    # 点击图片可以确认发音，完成学习后点击“结束学习”按钮。

    show TJ 1wx at tjleft with dissolve
    TeacherTian "既然大家都学会了，那么我们来做一个小测试吧。请大家根据听到的读音选择正确的单词。"


    jump lesson5_3_q1


label lesson5_3_q1:
    #{播放 SE diyiti}
    hide ZZ
    show TJ 1wx
    with dissolve
    TeacherTian "第一题。"
    #{播放 se 052iro }
    pause 1.5
    play sound "audio/se/sushiyin/052iro2.mp3"
    pause 1.0
    menu l5_3_q1:
        "1.空（そら）":
            $chpt5_answer_tango[0] = 0
            jump l5_3_q1AC
        "2.色（いろ）":
            $chpt5_answer_tango[0] = 10
            jump l5_3_q1B
        "3.私（わたし）":
            $chpt5_answer_tango[0] = 0
            jump l5_3_q1AC

label l5_3_q1B:
    #选择"2.色（いろ）"
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"
    jump lesson5_3_q2

label l5_3_q1AC:
    #选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"  fadein 2.0
    TeacherTian "好像不太对哦，再听一遍。"
    #循环到本题上方
    jump lesson5_3_q1

label lesson5_3_q2:
    #{播放 SE dierti}
    hide ZZ
    show TJ 1wx
    with dissolve
    TeacherTian "第二题。"
    #{播放 se 044yume }
    pause 1.5
    play sound "audio/se/sushiyin/053watashi2.mp3"
    pause 1.0
    menu l5_3_q2:
        "1.色（いろ）":
            $chpt5_answer_tango[1] = 0
            jump l5_3_q2AC
        "2.私（わたし）":
            $chpt5_answer_tango[1] = 10
            jump l5_3_q2B
        "3.本（ほん）":
            $chpt5_answer_tango[1] = 0
            jump l5_3_q2AC

label l5_3_q2B:
    #选择"2.私（わたし）"
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"
    jump lesson5_3_q3

label l5_3_q2AC:
    #选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"  fadein 2.0
    TeacherTian "好像不太对哦，再听一遍。"
    #循环到本题上方
    jump lesson5_3_q2

label lesson5_3_q3:
    #{播放 SE disanti}
    TeacherTian "第三题。"
    #{播放 se 054hon }
    pause 1.5
    play sound "audio/se/sushiyin/054hon2.mp3"
    pause 1.0
    menu l5_3_q3:
        "1.空（そら）":
            $chpt5_answer_tango[2] = 0
            jump l5_3_q3AB
        "2.私（わたし）":
            $chpt5_answer_tango[2] = 0
            jump l5_3_q3AB
        "3.本（ほん）":
            $chpt5_answer_tango[2] = 10
            jump l5_3_q3C

label l5_3_q3C:
    #选择"3.本（ほん）"
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"
    jump lesson5_4

label l5_3_q3AB:
    #选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"  fadein 2.0
    TeacherTian "好像不太对哦，再听一遍。"
    #循环到本题上方
    jump lesson5_3_q3

label lesson5_4:
    #{播放BGM b0403}
    play music "audio/bgm/b0403.mp3"
    #{显示背景  blackboard}
    scene blackboard with dissolve
    #{显示立绘TJ 1gx}
    show TJ 1gx at tjleft with dissolve
    TeacherTian "今天的内容就是这些，同学们都掌握了吗？"
    TeacherTian "到此为止，大家已经完成了最基础的五十音图的学习，下周开始我们将进行浊音、拗音等其他假名的学习。"
    TeacherTian "本节课到此结束，下午我们一起乘校车去七宝老街，别迟到哦。"

    jump chpt5_1