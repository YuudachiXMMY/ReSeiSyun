
label lesson1_1:
    #第一课 文化常识
    #{显示黑板背景 p jiaoxue01 }
    scene p jiaoxue01 with dissolve
    #{显示立绘 TJ1gx}
    show TJ 1gx at tjleft with dissolve
    #{播放BGM b0109 }
    play music "audio/bgm/b0109 shangke.mp3" fadein 2.0 volume 0.1
    #{播放vioce 2030}
    TeacherTian "各位同学，欢迎大家进入日语学习的第一课。"
    #{播放vioce 2031}
    TeacherTian "今天我们有三个学习任务……"
    #{显示立绘 WH12zm}
    show WH 12zm at right with dissolve
    Wanghao "我记得第一堂日语课是学习假名的由来……"
    #{显示立绘 TJ1wx}
    show TJ 1wx
    #{显示黑板背景 p jiaoxue02 }
    scene p jiaoxue02 with dissolve
    #{播放vioce 2032}
    TeacherTian "一是了解日语中“万叶假名”的由来，二是学习「あ行～か行」的假名，三是学习「あ行～か行」假名的相关单词。"
    #{显示黑板背景 p jiaoxue03}
    scene p jiaoxue03 with dissolve
    #{播放vioce 2033}
    TeacherTian "《隋书》中有一句对日本的记载：“无文字，唯刻木结绳。敬佛法，于百济求得佛经，始有文字。”"
    #{播放vioce 2034}
    TeacherTian "也就是说，日本起初有自己的语言，却没有用于记录的文字，主要通过口耳相传。"
    #{显示立绘 XY11jy}
    show XY 11jy at right with dissolve
    #{播放vioce 2035}
    ZhouXiaoyu "原来是这样啊。那日本什么时候开始有了文字呢？"
    #{显示立绘 TJ1wx}
    show TJ 1wx at tjleft with dissolve
    #{播放vioce 2036}
    TeacherTian "大约在公元三世纪至五世纪，汉字逐渐从中国传入日本。"
    #{显示立绘 LY12jy}
    #{播放vioce 2037}
    hide XY with dissolve
    show ly 12jy at right with dissolve
    LiuYang "当时没有字典，也没有翻译软件，日本人是如何学习汉字的呢？"
    #{显示黑板背景 p jiaoxue04}
    scene p jiaoxue04 with dissolve
    #{显示立绘 TJ1wx}
    show TJ 1wx at tjleft with dissolve
    #{播放vioce 2038}
    TeacherTian "这个问题问得很好。其实汉字传入日本后出现了两种用法。一种是“汉字的正用”，也就是严格遵循汉字的本义使用。"
    #{播放vioce 2039}
    TeacherTian "例如日本人使用“山”这个汉字来表示山峰。但是这个字有两种读音。一种是原本日语中的发音“yama”，另一种是中文的发音“shan”。"
    #{显示立绘 ZH12wn}
    show ZH 12wn at right with dissolve
    #{播放vioce 2040}
    ZhengHui "那不是很麻烦吗？"
    #{显示立绘 TJ1gx}
    show TJ 1gx
    #{播放vioce 2041}
    TeacherTian "哈哈，确实。尤其是“shan”这个读音日本人并不熟悉，因此汉字起初更多的是被当作“表音文字”来使用，日本人由此创造出了“万叶假名”。"
    #{显示黑板背景 p jiaoxue05}
    scene p jiaoxue05 with dissolve
    #{播放vioce 2042}
    TeacherTian "这里的“假”就是“假借(汉字)”的意思。“万叶假名”借用一部分汉字的读音来记录日语中原本的发音。"
    # TODO: {显示图片 山的万叶假名}
    #{播放vioce 2043}
    TeacherTian "例如日语中的“山”读作“yama”，就可以用“也麻、野麻”等汉字来记录。这种使用方法就被称为“万叶假名”。"
    #{显示立绘 QQ12jy}
    show QQ 12jy at right with dissolve
    #{播放vioce 2044}
    YuanQiaoqiao "原来如此。那既然有“假名”，是不是还有“真名”呢？"
    #{显示立绘 TJ1wx}
    show TJ 1wx at tjleft with dissolve
    #{播放vioce 2045}
    TeacherTian "当然有。“真名”指的就是汉字原来的用法。"
    #{显示黑板背景 p jiaoxue06}
    scene p jiaoxue06 with dissolve
    #{播放vioce 2046}
    TeacherTian "此后，在万叶假名的基础上，演化出了平假名「ひらがな」和片假名「カタカナ」。"
    #{播放vioce 2047}
    TeacherTian "今天我们就要来学习十个假名的读法与写法。"
    #{播放vioce 2048}
    TeacherTian "在这之前我们先来做一个小测试吧。看看大家是否掌握了刚才所讲的知识。"

    jump lesson1_1_q1

label lesson1_1_q1:
    #{显示背景 heiban }
    scene blackboard with dissolve
    #{显示立绘 TJ1wx}
    show TJ 1wx at tjleft with dissolve
    TeacherTian "第一题。"
    # TODO: {播放se diyiti}
    #play sound "audio/se/sushiyin/diyiti.mp3"
    pause 1.5
    menu l1_1_q1:
        '日本是先有语言还是先有文字？'
        "A.先有语言":
            $chpt1_answer_bunka[0] = 10
            jump l1_1_q1A
        "B.先有文字":
            $chpt1_answer_bunka[0] = 0
            jump l1_1_q1BC
        "C.同时出现":
            $chpt1_answer_bunka[0] = 0
            jump l1_1_q1BC

label l1_1_q1A:
    #选择A.语言
    #好感度参数 +10
    #{显示立绘 TJ1gx}
    show TJ 1gx
    #{播放vioce 2049}
    TeacherTian "回答正确。日本起初有自己的语言，却没有用于记录的文字，主要通过口耳相传。"

    jump lesson1_1_q2

label l1_1_q1BC:
    # 选择 其他选项
    #{显示立绘 TJ1ng}
    show TJ 1ng
    #{播放vioce 2050}
    TeacherTian "上课要认真听讲哦。日本起初有自己的语言，却没有用于记录的文字，主要通过口耳相传。"

    jump lesson1_1_q2

label lesson1_1_q2:
    if chpt1_C_answer_bunka_index < 7:
        $ chpt1_C_answer_bunka_index = 7
    #{显示立绘 TJ1wx}
    show TJ 1wx
    TeacherTian "第二题。"
    # TODO: {播放se dierti}
    #play sound "audio/se/sushiyin/dierti.mp3"
    pause 1.5
    menu l1_1_q2:
        '日语中“汉字的正用”是指什么意思？'
        "A.正确地书写汉字":
            $chpt1_answer_bunka[1] = 0
            jump l1_1_q2AB
        "B.把汉字正过来写":
            $chpt1_answer_bunka[1] = 0
            jump l1_1_q2AB
        "C.按照汉字原本的意思来使用":
            $chpt1_answer_bunka[1] = 10
            jump l1_1_q2C

label l1_1_q2C:
    #选择C.按照汉字原本的意思来使用
    #好感度参数 +10
    #{显示立绘 TJ1gx}
    show TJ 1gx
    #{播放vioce 2510}
    TeacherTian "回答正确。“汉字的正用”，也就是严格遵循汉字的本义使用。例如日语中的“山”，读作“yama”，写作“山”。"

label l1_1_q2AB:
    # 选择 其他选项
    #{显示立绘 TJ1ng}
    show TJ 1ng
    #{播放vioce 2052}
    TeacherTian "上课要认真听讲哦。“汉字的正用”，也就是严格遵循汉字的本义使用。例如日语中的“山”，读作“yama”，写作“山”。"

label lesson1_1_q3:
    if chpt1_C_answer_bunka_index < 8:
        $ chpt1_C_answer_bunka_index = 8
    #{显示立绘 TJ1wx}
    show TJ 1wx
    TeacherTian "第三题。"
    #{播放se disanti}
    #play sound "audio/se/sushiyin/disanti.mp3"
    pause 1.5
    menu l1_1_q3:
        '“万叶假名”中的“假”指什么意思？'
        "A.假冒":
            $chpt1_answer_bunka[2] = 0
            jump l1_1_q3AC
        "B.假借":
            $chpt1_answer_bunka[2] = 10
            jump l1_1_q3B
        "C.假如":
            $chpt1_answer_bunka[2] = 0
            jump l1_1_q3AC

label l1_1_q3B:
    #选择B.假借
    #好感度参数 +10
    #{显示立绘 TJ1gx}
    show TJ 1gx
    #{播放vioce 2053}
    TeacherTian "回答正确。“日本人把汉字称为“真名”，“假名”中的“假”就是“假借(汉字)”的意思。“万叶假名”是一种表音文字，借用汉字的读音记录日语中原本的发音。"
    jump lesson1_2

label l1_1_q3AC:
    # 选择 其他选项
    #{显示立绘 TJ1ng}
    show TJ 1ng
    #{播放vioce 2054}
    TeacherTian "上课要认真听讲哦。日本人把汉字称为“真名”，“假名”中的“假”就是“假借(汉字)”的意思。“万叶假名”是一种表音文字，借用汉字的读音记录日语中原本的发音。"
    jump lesson1_2

label lesson1_2:
    if chpt1_C_answer_bunka_index < 9:
        $ chpt1_C_answer_bunka_index = 9
    #第一课 假名部分

    #{显示立绘 TJ1wx}
    show TJ 1wx at left with dissolve
    #{播放vioce 2055}
    TeacherTian "接下来我们来学习本课的第二项内容，「あ行～か行」的十个假名。"
    #{显示图片 十个假名}
    # hide TJ with dissolve
    show screen HiraKataKANA("a_o", "ka_ko", learning=False)
    # show TJ 1wx at left with dissolve
    #{播放vioce 2056}
    TeacherTian "请智子同学为我们读一下吧。"
    #{播放vioce 2057}
    TeacherTian "智子ちゃん、ちょっと読んでもらえますか。（智子，能请你读一下吗？）"
    #{显示立绘 ZZ11gx}
    hide TJ with dissolve
    show ZZ 11gx at left with dissolve:
        xoffset -150
    #{播放vioce 2058}
    Tomoko "はい。（好的。）"
    #{播放SE 01aka }
    stop music
    play sound "audio/se/sushiyin/01aka.mp3"
    show screen HiraKataKANA("a_o", "ka_ko", learning=False)
    if chpt1_C_answer_kana_index < 10:
        $ chpt1_C_answer_kana_index = 10
    Tomoko "あ、い、う、え、お。か、き、く、け、こ。"
    #{显示立绘 TJ1wx}
    hide ZZ with dissolve
    show TJ 1wx at left with dissolve:
        xoffset -150
    #{播放vioce 2059}
    TeacherTian "もう一度お願いします。（请再读一遍。）"
    #{显示立绘 ZZ11gx}
    hide TJ with dissolve
    show ZZ 11gx at left with dissolve:
        xoffset -150
    #{播放SE 01aka }
    play sound "audio/se/sushiyin/01aka.mp3"
    show screen HiraKataKANA("a_o", "ka_ko", learning=False)
    if chpt1_C_answer_kana_index < 10:
        $ chpt1_C_answer_kana_index = 10
    Tomoko "あ、い、う、え、お。か、き、く、け、こ。"
    hide screen HiraKataKANA
    #{显示立绘 TJ1wx}
    hide ZZ with dissolve
    play music "audio/bgm/b0109 shangke.mp3" fadein 2.0
    show TJ 1wx at left with dissolve:
        xoffset -150
    #{播放vioce 2060}
    TeacherTian "大家可以跟读练习一下哦。"
    #{显示图片 十个假名 点击可以发音}
    # 点击图片可以确认发音，完成学习后点击“结束学习”按钮。
    hide TJ with dissolve
    call screen HiraKataKANA("a_o", "ka_ko")
    #{播放vioce 2061}
    show TJ 1wx at left with dissolve:
        xoffset -150
    TeacherTian "既然大家都学会了，那么我们来做一个小测试吧。请大家根据听到的读音选择正确的假名。"
    hide ZZ with dissolve
    stop music

    jump lesson1_2_q1

label lesson1_2_q1:
    #{显示立绘 TJ1wx}
    stop music
    show TJ 1wx
    TeacherTian "第一题。"
    #{播放se diyiti}
    #play sound "audio/se/sushiyin/diyiti.mp3"
    pause 1.5
    #{播放SE u}
    play sound "audio/se/sushiyin/u.mp3"
    pause 1.0
    menu l1_2_q1:
        "A.あ":
            $chpt1_answer_kana[0] = 0
            jump l1_2_q1AB
        "B.お":
            $chpt1_answer_kana[0] = 0
            jump l1_2_q1AB
        "C.う":
            $chpt1_answer_kana[0] = 5
            jump l1_2_q1C

label l1_2_q1C:
    #选择C.う
    #好感度参数 +5
    #{显示立绘 TJ1gx}
    show TJ 1gx
    #{播放zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"

    jump lesson1_2_q2

label l1_2_q1AB:
    #选择 其他选项
    #{显示立绘 TJ1ng}
    show TJ 1ng
    #{播放se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"
    TeacherTian "好像不太对哦，再听一遍。"
    #{播放SE u}
    play sound "audio/se/sushiyin/u.mp3"
    pause 1.0
    #{显示立绘 LY13wx}
    show LY 13wx at right with dissolve
    #{播放vioce 20612}
    LiuYang "我觉得这道题是C.う。"
    #{显示立绘 TJ1gx}
    show TJ 1gx
    #{播放zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"
    hide LY with dissolve

    jump lesson1_2_q2

label lesson1_2_q2:
    #{显示立绘 TJ1wx}
    show TJ 1wx
    TeacherTian "第二题。"
    #{播放se dierti}
    #play sound "audio/se/sushiyin/dierti.mp3"
    pause 1.5
    #{播放SE ki}
    play sound "audio/se/sushiyin/ki.mp3"
    pause 1.0
    menu l1_2_q2:
        "A.か":
            $chpt1_answer_kana[1] = 0
            jump l1_2_q2AC
        "B.き":
            $chpt1_answer_kana[1] = 5
            jump l1_2_q2B
        "C.け":
            $chpt1_answer_kana[1] = 0
            jump l1_2_q2AC

label l1_2_q2B:
    #选择B.き
    #好感度参数 +5
    #{显示立绘 TJ1gx}
    show TJ 1gx
    #{播放zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"

    jump lesson1_2_q3

label l1_2_q2AC:
    #选择 其他选项
    #{显示立绘 TJ1ng}
    show TJ 1ng
    #{播放se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"
    TeacherTian "好像不太对哦，再听一遍。"
    #{播放SE ki}
    play sound "audio/se/sushiyin/ki.mp3"
    pause 1.0
    #{显示立绘 XY11}
    show XY 12cx at right with dissolve
    #{播放vioce 20613}
    ZhouXiaoyu "应该选B.き。"
    #{显示立绘 TJ1gx}
    show TJ 1gx
    #{播放zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"
    hide XY with dissolve

    jump lesson1_2_q3


label lesson1_2_q3:
    #{显示立绘 TJ1wx}
    show TJ 1wx
    TeacherTian "第三题。"
    #{播放se disanti}
    #play sound "audio/se/sushiyin/disanti.mp3"
    pause 1.5
    #{播放SE ko}
    play sound "audio/se/sushiyin/ko.mp3"
    pause 1.0
    menu l1_2_q3:
        "A.お":
            $chpt1_answer_kana[2] = 0
            jump l1_2_q3AB
        "B.か":
            $chpt1_answer_kana[2] = 0
            jump l1_2_q3AB
        "C.こ":
            $chpt1_answer_kana[2] = 5
            jump l1_2_q3C

label l1_2_q3C:
    #选择C.こ
    #好感度参数 +5
    #{显示立绘 TJ1gx}
    show TJ 1gx
    #{播放zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"

    jump lesson1_2_q4

label l1_2_q3AB:
    #选择 其他选项
    #{显示立绘 TJ1ng}
    show TJ 1ng
    #{播放se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"
    TeacherTian "好像不太对哦，再听一遍。"
    #{播放SE ko}
    play sound "audio/se/sushiyin/ko.mp3"
    pause 1.0
    #{显示立绘 QQ13dy}
    show QQ 13dy at right with dissolve
    #{播放vioce 20614}
    YuanQiaoqiao "这题我知道，应该是C.こ。"
    #{显示立绘 TJ1gx}
    show TJ 1gx
    #{播放zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"
    hide QQ with dissolve

    jump lesson1_2_q4

label lesson1_2_q4:
    #{显示立绘 TJ1wx}
    show TJ 1wx
    TeacherTian "第四题。"
    #{播放se disiti}
    #play sound "audio/se/sushiyin/disiti.mp3"
    pause 1.5
    #{播放SE e}
    play sound "audio/se/sushiyin/e.mp3"
    pause 1.0
    menu l1_2_q4:
        "A.く":
            $chpt1_answer_kana[3] = 0
            jump l1_2_q4AB
        "B.い":
            $chpt1_answer_kana[3] = 0
            jump l1_2_q4AB
        "C.え":
            $chpt1_answer_kana[3] = 5
            jump l1_2_q4C

label l1_2_q4C:
    #选择C.え
    #好感度参数 +5
    #{显示立绘 TJ1gx}
    show TJ 1gx
    #{播放zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"

    jump lesson1_2_q5

label l1_2_q4AB:
    #选择 其他选项
    #{显示立绘 TJ1ng}
    show TJ 1ng
    #{播放se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"
    TeacherTian "好像不太对哦，再听一遍。"
    #{播放SE e}
    play sound "audio/se/sushiyin/e.mp3"
    pause 1.0
    #{显示立绘 ZH12gx}
    show ZH 12gx at right with dissolve
    #{播放vioce 20615}
    ZhengHui "是C.え吧。"
    #{显示立绘 TJ1gx}
    show TJ 1gx
    #{播放zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"
    hide ZH with dissolve

    jump lesson1_2_q5

label lesson1_2_q5:
    #{显示立绘 TJ1wx}
    show TJ 1wx
    TeacherTian "第五题。"
    #{播放se diwuti}
    #play sound "audio/se/sushiyin/diwuti.mp3"
    pause 1.5
    #{播放SE ku}
    play sound "audio/se/sushiyin/ku.mp3"
    pause 1.0
    menu l1_2_q5:
        "A.く":
            $chpt1_answer_kana[4] = 5
            jump l1_2_q5A
        "B.け":
            $chpt1_answer_kana[4] = 0
            jump l1_2_q5BC
        "C.お":
            $chpt1_answer_kana[4] = 0
            jump l1_2_q5BC

label l1_2_q5A:
    #选择A.く
    #好感度参数 +5
    #{显示立绘 TJ1gx}
    show TJ 1gx
    #{播放zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"

    jump lesson1_3

label l1_2_q5BC:
    #选择 其他选项
    #{显示立绘 TJ1ng}
    show TJ 1ng
    #{播放se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"
    TeacherTian "好像不太对哦，再听一遍。"
    #{播放SE ku}
    play sound "audio/se/sushiyin/ku.mp3"
    pause 1.0
    #{显示立绘 XY12wx}
    show XY 12wx at right with dissolve
    #{播放vioce 20616}
    ZhouXiaoyu "这道题应该是A.く。"
    #{显示立绘 TJ1gx}
    show TJ 1gx
    #{播放zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"
    hide XY with dissolve

    jump lesson1_3

label lesson1_3:
    #{显示立绘 TJ1wx}
    show TJ 1wx
    #{播放vioce 20617}
    TeacherTian "这十个假名大家都已经掌握了，接下来我们来看一下它们可以组成哪些单词。"
    #{播放vioce 2062}
    TeacherTian "智子ちゃん、こちらの単語を読んでもらえますか。（智子，能请你读一下这些单词吗？）"
    #{显示立绘 ZZ11gx}
    show ZZ 11gx at right with dissolve
    #{播放vioce 2063}
    Tomoko "はい。読みます。（好的，我读了。）"
    #点击屏幕后逐个在黑板上显示，并同步播放音频，过程中停止其他操作。（音频还没有录好）
    hide TJ with dissolve
    # {显示图片 011ai2}
    if chpt1_C_answer_tango_index < 1:
        $ chpt1_C_answer_tango_index = 1
    show 011ai2 at middle with dissolve
    #{播放se 011ai2}
    play sound "audio/se/sushiyin/011ai2.mp3"
    pause 1.0
    Tomoko "愛（あい）。"
    hide 011ai2 with dissolve
    # {显示图片 012au2}
    show 012au2 at middle with dissolve
    #{播放se 012au2}
    if chpt1_C_answer_tango_index < 2:
        $ chpt1_C_answer_tango_index = 2
    play sound "audio/se/sushiyin/012au2.mp3"
    pause 1.0
    Tomoko "会う（あう）。"
    hide 012au2 with dissolve
    # {显示图片 013aki2}
    show 013aki2 at middle with dissolve
    #{播放se 013aki2}
    if chpt1_C_answer_tango_index < 3:
        $ chpt1_C_answer_tango_index = 3
    play sound "audio/se/sushiyin/013aki2.mp3"
    pause 1.0
    Tomoko "秋（あき）。"
    hide 013aki2 with dissolve
    # {显示图片 014koi2}
    show 014koi2 at middle with dissolve
    #{播放se 014koi2}
    if chpt1_C_answer_tango_index < 4:
        $ chpt1_C_answer_tango_index = 4
    play sound "audio/se/sushiyin/014koi2.mp3"
    pause 1.0
    Tomoko "恋（こい）。"
    hide 014koi2 with dissolve
    #{显示立绘 TJ1wx}
    show TJ 1wx at tjleft with dissolve
    #{播放vioce 2064}
    TeacherTian "大家可以跟读练习一下哦。"
    hide TJ with dissolve
    hide ZZ with dissolve
    #{显示图片1-4  点击可以发音}
    call screen Dango(Dango_L1)
    # 点击图片可以确认发音，完成学习后点击“结束学习”按钮。

    show TJ 1wx at tjleft with dissolve
    #{播放vioce 2065}
    TeacherTian "既然大家都学会了，那么我们来做一个小测试吧。请大家根据听到的读音选择正确的单词。"

    hide ZZ with dissolve

    jump lesson1_3_q1

label lesson1_3_q1:
    #{显示立绘 TJ1wx}
    show TJ 1wx
    TeacherTian "第一题。"
    #{播放se diyiti}
    #play sound "audio/se/sushiyin/diyiti.mp3"
    pause 1.5
    # {播放SE  koi}
    play sound "audio/se/sushiyin/014koi2.mp3"
    pause 1.0
    menu l1_3_q1:
        "A.秋（あき）":
            $chpt1_answer_tango[0] = 0
            jump l1_3_q1AC
        "B.恋（こい）":
            $chpt1_answer_tango[0] = 5
            jump l1_3_q1B
        "C.会う（あう）":
            $chpt1_answer_tango[0] = 0
            jump l1_3_q1AC

label l1_3_q1B:
    #选择 B.恋（こい）
    #好感度参数 +5
    #{显示立绘 TJ1gx}
    show TJ 1gx
    #{播放zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"

    jump lesson1_3_q2

label l1_3_q1AC:
    #选择 其他选项
    #{显示立绘 TJ1ng}
    show TJ 1ng
    #{播放se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"
    TeacherTian "好像不太对哦，再听一遍。"
    # {播放SE  koi}
    play sound "audio/se/sushiyin/014koi2.mp3"
    pause 1.0
    #{显示立绘 QQ12dy}
    show QQ 12dy at right with dissolve
    #{播放vioce 2066}
    YuanQiaoqiao "选B.恋（こい），是恋爱的意思。对不对？"
    #{显示立绘 TJ1gx}
    show TJ 1gx
    #{播放zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"
    hide QQ with dissolve

    jump lesson1_3_q2

label lesson1_3_q2:
    #{显示立绘 TJ1wx}
    show TJ 1wx
    TeacherTian "第二题。"
    #play sound "audio/se/sushiyin/dierti.mp3"
    pause 1.5
    # {播放SE  ai}
    play sound "audio/se/sushiyin/011ai2.mp3"
    pause 1.0
    menu l1_3_q2:
        "A.愛（あい）":
            $chpt1_answer_tango[1] = 5
            jump l1_3_q2A
        "B.会う（あう）":
            $chpt1_answer_tango[1] = 0
            jump l1_3_q2BC
        "C.秋（あき）":
            $chpt1_answer_tango[1] = 0
            jump l1_3_q2BC

label l1_3_q2A:
    #选择 A.愛（あい）
    #好感度参数 +5
    #{显示立绘 TJ1gx}
    show TJ 1gx
    #{播放zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"

    jump lesson1_3_q3

label l1_3_q2BC:
    #选择 其他选项
    #{显示立绘 TJ1ng}
    show TJ 1ng
    #{播放se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"
    TeacherTian "好像不太对哦，再听一遍。"
    # {播放SE  ai}
    play sound "audio/se/sushiyin/011ai2.mp3"
    pause 1.0
    #{显示立绘 LY13wx}
    show LY 13wx at right with dissolve
    #{播放vioce 2067}
    LiuYang "这题很简单，选A.愛（あい）。"
    #{显示立绘 TJ1gx}
    show TJ 1gx
    #{播放zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"
    hide LY with dissolve

    jump lesson1_3_q3

label lesson1_3_q3:
    #{显示立绘 TJ1wx}
    show TJ 1wx
    TeacherTian "第三题。"
    #play sound "audio/se/sushiyin/disanti.mp3"
    pause 1.5
    # {播放SE  aki}
    play sound "audio/se/sushiyin/013aki2.mp3"
    pause 1.0
    menu l1_3_q3:
        "A.恋（こい）":
            $chpt1_answer_tango[2] = 0
            jump l1_3_q3AC
        "B.秋（あき）":
            $chpt1_answer_tango[2] = 5
            jump l1_3_q3B
        "C.会う（あう）":
            $chpt1_answer_tango[2] = 0
            jump l1_3_q3AC

label l1_3_q3B:
    #选择 B.秋（あき）
    #好感度参数 +5
    #{显示立绘 TJ1gx}
    show TJ 1gx
    #{播放zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"

    jump lesson1_4

label l1_3_q3AC:
    #选择 其他选项
    #{显示立绘 TJ1ng}
    show TJ 1ng
    #{播放se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"
    TeacherTian "好像不太对哦，再听一遍。"
    # {播放SE  aki}
    play sound "audio/se/sushiyin/013aki2.mp3"
    pause 1.0
    #{显示立绘 XY12wx}
    show XY 12wx at right with dissolve
    #{播放vioce 2068}
    ZhouXiaoyu "是B.秋（あき），意思是秋天。"
    #{显示立绘 TJ1gx}
    show TJ 1gx
    #{播放zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"
    hide XY with dissolve

    jump lesson1_4

label lesson1_4:
    # {播放SE  下课铃}
    #{显示立绘 TJ1wx}
    show TJ 1wx
    #{播放vioce 2069}
    TeacherTian "今天的内容就是这些，同学们都掌握了吗？"
    #{播放vioce 2070}
    TeacherTian "希望大家在睡前用5分钟的时间回顾一下今天所学的内容，不要忘记了哦。"
    #{播放vioce 2071}
    TeacherTian "本节课到此结束，明天见。"

    jump lesson1_5

label lesson1_5:
    #第一课 对话部分
    #{播放BGM b0110 sushe}
    play music "audio/bgm/b0110 sushe.mp3" fadein 2.0
    #{显示寝室图片 p06 qinshi }
    scene p06 qinshi with dissolve
    #{显示立绘 WH13wx}
    show WH 13wx at middle with dissolve
    me "不知不觉一天就过去了……"
    me "晚自修结束后回到自己的宿舍，再次体验到了久违的住校生活。"
    me "今天的课都像在听天书。原本以为自己是个学渣，现在再看高中的数学题，感觉当年的自己简直是天才。"
    #{显示立绘 WH13wx}
    show WH 13wx
    me "看着老师们倾尽全力在讲台上讲课，心里有一种莫名的感动。"
    me "毕业了以后，很少能碰到像“老师”这样愿意为他人付出、不求回报的大人。"
    # TODO: {显示 手机来电 图片w10  2012年的华为手机}
    show w10 at wleft with dissolve
    #{播放se s0116 shoujiling }
    play sound "audio/se/s0116 shoujiling.mp3"
    #{显示立绘 WH12jy}
    show WH 12jy
    me "……一个陌生的号码。"
    #{显示立绘 ZZ14wx}
    hide w10 with dissolve
    show WH at MidToRight
    show ZZ 14wx at left with dissolve
    #{播放vioce 2072}
    Zhizi "こんばんは。高橋智子です。夜遅くにて、すみません。王浩さんの電話でしょうか。（晚上好，我是高桥智子。不好意思这么晚打扰你。请问这是王浩的手机号码吗？）"
    #{显示立绘 WH11rz}
    show WH 11pj
    me "智子打来的电话？！我应该如何回答……"

    jump lesson1_5_q1

label lesson1_5_q1:
    #{显示选项  文本框居中，选项竖排1 2}
    menu l1_5_q1:
        "A.こんばんは。":
            $chpt1_answer_kaiwa[0] = 10
            jump l1_5_q1A
        "B.すみません。":
            $chpt1_answer_kaiwa[0] = 0
            jump l1_5_q1B

label l1_5_q1A:
    #选择A.
    #好感度参数 +10
    #{显示立绘 WH13wx}
    show WH 13wx
    me "こんばんは。王浩です。（晚上好，我是王浩。）"

    jump lesson1_5_q2

label l1_5_q1B:
    #选择B.
    #{显示立绘 WH11kx}
    show WH 11kx
    me "「すみません」表示道歉，这里不太合适……"
    #{显示立绘 WH13wx}
    show WH 13wx
    me "こんばんは。王浩です。（晚上好，我是王浩。）"

    jump lesson1_5_q2

label lesson1_5_q2:
    #{显示立绘 ZZ11wx}
    show ZZ 11wx
    #{播放vioce 2073}
    Zhizi "今日はありがとう。王さんはとても日本語がお上手ですね。（今天谢谢你的帮助。你的日语说得真好啊。）"
    #{显示立绘 WH13wx}
    show WH 13wx
    me "(智子还是这么温柔礼貌，突然被夸赞了，有点不知所措。)我应该说……"
    #{显示选项  文本框居中，选项竖排1 2}
    menu l1_5_q2:
        "A.はい、上手です。":
            $chpt1_answer_kaiwa[1] = 0
            jump l1_5_q2A
        "B.いえいえ。":
            $chpt1_answer_kaiwa[1] = 10
            jump l1_5_q2B

label l1_5_q2B:
    #选择B.
    #好感度参数 +10
    #{显示立绘 WH11kx}
    show WH 11kx
    me "いえいえ。（哪里哪里。）"

    jump lesson1_5_q3

label l1_5_q2A:
    #选择A.
    #{显示立绘 WH11kx}
    show WH 11kx
    me "一般受到夸赞会表示一下谦虚……"
    me "いえいえ。（哪里哪里。）"

    jump lesson1_5_q3

label lesson1_5_q3:
    if chpt1_C_answer_kaiwa_index < 1:
        $ chpt1_C_answer_kaiwa_index = 1
    #{显示立绘 ZZ11}
    show ZZ 11gx
    #{播放vioce 2074}
    Zhizi "これから、いろいろ教えてくださいね。^^（今后还请多多指教哦。）"
    #{显示立绘 WH11gx}
    show WH 11gx
    me "こちらこそ、よろしくお願いします。（也请你多多关照。）"
    #{显示立绘 ZZ13gx}
    show ZZ 11gx
    #{播放vioce 2075}
    Zhizi "明日、よかったら、一緒にお昼ご飯はどうですか。（方便的话，明天能一起吃午饭吗？）"
    #{显示立绘 WH11gx}
    show WH 11gx
    me "はい、もちろん。楽しみにしています。（好的，当然可以。我非常期待。）"
    #{显示立绘 ZZ11wx}
    show ZZ 11wx
    #{播放vioce 2076}
    Zhizi "じゃあ、お休みなさい。（那么晚安咯。）"

    #{显示选项  文本框居中，选项竖排1 2}
    menu l1_5_q3:
        "A.こんにちは。":
            $chpt1_answer_kaiwa[2] = 0
            jump l1_5_q3A
        "B.お休みなさい。":
            $chpt1_answer_kaiwa[2] = 10
            jump l1_5_q3B

label l1_5_q3B:
    #选择B.
    #好感度参数 +10
    #{显示立绘 WH11wx}
    show WH 11wx
    me "お休みなさい。（晚安。）"
    hide ZZ with dissolve

    jump lesson1_6

label l1_5_q3A:
    #选择A.
    #{显示立绘 WH11kx}
    show WH 11kx
    me "现在是晚上该休息的时间了……"
    me "お休みなさい。（晚安。）"
    hide ZZ with dissolve

    jump lesson1_6

label lesson1_6:
    if chpt1_C_answer_kaiwa_index < 2:
        $ chpt1_C_answer_kaiwa_index = 2
    #{显示立绘 WH11jy}
    show WH 11jy at RightToMid:
        xoffset 100
    me "……"
    me "没想到智子会主动给我打电话……还约我一起吃午饭。"
    me "当年因为不会说日语，只能在一旁看着刘洋和智子聊天。"
    me "看来历史真的可以改写……"
    #{显示立绘 LY11jy}
    show WH at MidToRight
    show LY 11jy at left with dissolve
    #{播放vioce 2077}
    LiuYang "刚刚在和日本留学生打电话吗？"
    "正在我神游之际，室友刘洋回到了寝室。"
    #{显示立绘 WH11jy}
    show WH 11jy
    me "我……那个……"
    #{显示立绘 LY12gx}
    show LY 12gx
    #{播放vioce 2078}
    LiuYang "嗨，紧张什么呀。日语说得很不错啊。"
    hide LY with dissolve
    show WH at middle with dissolve
    "刘洋反而安慰起我来。"
    "刘洋的坦然让我感到了一丝愧疚。原本应该是刘洋接到这个电话，现在却被我……"
    "不知道这场神奇的穿越之旅会持续到什么时候。"
    "或许睡一觉梦就会醒吧……"
    #{显示立绘 WH13rz}
    show WH 13rz
    me "对了，田老师说过睡前要复习一下今天的内容，看一下今天的笔记吧。"
    # TODO: {打开复习回顾界面，添加第一课的内容。并设定倒计时5分钟，无法退出界面。}
    call screen kana_review()
    #{显示立绘 WH13rz}
    show WH 13rz
    me "复习了一下，果然思路清晰多了。"
    me "好了，时间不早了，先休息吧……"

    hide WH with dissolve

    jump chpt2_1