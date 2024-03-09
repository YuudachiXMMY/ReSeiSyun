#第三课13rz
label lesson3_1:

    #{播放BGM b0202}
    play music "audio/bgm/b0202.mp3"  fadein 2.0 volume 0.1
    # TODO:{显示背景  p05 jiaoshijiu }
    scene p jiaoxue13 with dissolve
    #第三课 文化常识
    #{显示立绘TJ 1gx}
    show TJ 1gx at tjleft with dissolve
    TeacherTian "各位同学，今天我们将继续进行第三课的学习。"
    TeacherTian "我们都知道汉字是由中国传入日本的，那么你们还知道其他关于中日交流的故事吗？"
    scene blackboard with dissolve
    #{显示立绘WH 12kx}
    show WH 12kx at middle with dissolve
    "当年好像田老师讲过……"
    #{显示立绘LY 11hz}
    hide WH
    show LY 11hz at right
    with dissolve
    LiuYang "田老师，徐福东渡的故事应该体现了中日交流吧？"
    #{显示立绘TJ 1wx}
    show TJ 1wx at tjleft with dissolve
    TeacherTian "没错，徐福的确是一位非常著名的人物。秦始皇曾派他东渡寻找仙药。"
    #{显示立绘XY 11zm}
    hide LY
    show XY 11jy at t_right
    with dissolve
    ZhouXiaoyu "老师，徐福的故事是真的吗？还是只是传说呀？"
    #{显示立绘TJ 1gx}
    show TJ 1gx
    TeacherTian "这个问题问得好。虽然目前还无法断定徐福去的是否就是现在的日本，但是“徐福东渡”的故事确实在史料中有所记载。"
    TeacherTian "《史记·秦始皇本纪》中有这样的记载：‘齐人徐巿（fú）等上书，言海中有三神山，名曰蓬莱、方丈、瀛洲，仙人居之。请得斋戒，与童男女求之。于是遣徐巿发童男女数千人，入海求仙人。’"
    #{显示立绘QQ 13jy}
    hide WH
    hide XY
    show QQ 13jy at t_right
    with dissolve
    YuanQiaoqiao "徐福渡海居然是为了找神仙，真是神奇的传说啊！"
    #{显示立绘TJ 1gx}
    show TJ 1gx
    TeacherTian "传说虽然不能等同于史实，但从日本考古界出土的文物来看，在徐福东渡的公元前三世纪，确实有大批中国移民渡海到达日本，并带去了许多大陆的先进文明。"
    #{显示立绘ZH 11wx}
    hide QQ
    show ZH 11wx at t_right
    with dissolve
    ZhengHui "哦！原来如此。"
    #{显示立绘TJ 1gx}
    show TJ 1gx
    TeacherTian "日本佐贺市的金立神社，每隔50年都会举办一项规模盛大的祭祀活动。这项历史悠久的传统活动祭拜的人便是这位两千多年前来到日本的友好使者。"
    #{显示立绘WH 11wx}
    hide ZH
    show WH 11wx at t_right
    with dissolve
    me "那当时的中国文明一定对日本产生了很大的影响吧？"
    #{显示立绘TJ 1gx}
    show TJ 1gx
    TeacherTian "没错。在两汉时期，中国的铁器、铜器、丝帛等也传入了日本，促进了古代日本的生产技术和文化的发展。"
    TeacherTian "之后，隋唐时期，日本派遣使节前来学习中国文化。宋元时期，民间贸易活跃，僧侣往来频繁……"
    #{显示立绘LY 11jy}
    hide WH
    show LY 11jy at right
    with dissolve
    LiuYang "中日两国之间的文化交流可真是历史悠久呀。"
    #{显示立绘TJ 1wx}
    show TJ 1wx
    TeacherTian "是啊，学好日语可以帮助大家更好地了解中日两国的文化交流史。"
    hide LY with dissolve
    TeacherTian "我们来做一个小测试，看看大家是否掌握了刚才所讲的知识。"

    jump lesson3_1_q1

label lesson3_1_q1:
    #{显示立绘TJ 1gx}
    show TJ 1gx at tjleft
    menu l3_1_q1:
        '徐福东渡的故事最早在哪本书中有记录？'
        "1.后汉书":
            $chpt3_answer_bunka[0] = 0
            jump l3_1_q1AB
        "2.战国策":
            $chpt3_answer_bunka[0] = 0
            jump l3_1_q1AB
        "3.史记":
            $chpt3_answer_bunka[0] = 10
            jump l3_1_q1C

label l3_1_q1C:
    #选择3.史记
    #好感度参数 +10
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。《史记·秦始皇本纪》中有相关的记载。"
    jump lesson3_1_q2

label l3_1_q1AB:
    # 选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放 se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"
    TeacherTian "上课要认真听讲哦。《史记·秦始皇本纪》中有相关的记载。"
    jump lesson3_1_q2

label lesson3_1_q2:
    if chpt3_C_answer_bunka_index < 1:
        $ chpt3_C_answer_bunka_index = 1
    #{显示立绘TJ 1gx}
    show TJ 1gx at tjleft
    menu l3_1_q2:
        '日本佐贺市金立神社举办的大型祭祀活动祭拜的人是谁？'
        "1.徐福":
            $chpt3_answer_bunka[1] = 10
            jump l3_1_q2A
        "2.鉴真":
            $chpt3_answer_bunka[1] = 0
            jump l3_1_q2BC
        "3.空海":
            $chpt3_answer_bunka[1] = 0
            jump l3_1_q2BC

label l3_1_q2A:
    #选择1.徐福
    #好感度参数 +10
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。日本佐贺市的金立神社，每隔50年都会举办一项规模盛大的祭拜徐福活动。"
    jump lesson3_1_q3

label l3_1_q2BC:
    # 选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放 se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"
    TeacherTian "上课要认真听讲哦。日本佐贺市的金立神社，每隔50年都会举办一项规模盛大的祭祀徐福活动。"
    jump lesson3_1_q3

label lesson3_1_q3:
    if chpt3_C_answer_bunka_index < 2:
        $ chpt3_C_answer_bunka_index = 2
    #{显示立绘TJ 1gx}
    show TJ 1gx at tjleft
    menu l3_1_q3:
        '中国的铁器、铜器、丝帛在哪个朝代传入了日本？'
        "1.周朝":
            $chpt3_answer_bunka[2] = 0
            jump l3_1_q3AC
        "2.汉代":
            $chpt3_answer_bunka[2] = 10
            jump l3_1_q3B
        "3.隋唐时期":
            $chpt3_answer_bunka[2] = 0
            jump l3_1_q3AC

label l3_1_q3B:
    #选择2.汉代
    #好感度参数 +10
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。在两汉时期，中国的铁器、铜器、丝帛等也传入了日本，促进了古代日本的生产技术和文化的发展。"
    jump lesson3_2

label l3_1_q3AC:
    # 选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放 se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"
    TeacherTian "上课要认真听讲哦。在两汉时期，中国的铁器、铜器、丝帛等也传入了日本，促进了古代日本的生产技术和文化的发展。"
    jump lesson3_2

label lesson3_2:
    if chpt3_C_answer_bunka_index < 3:
        $ chpt3_C_answer_bunka_index = 3

    #第三课 假名部分
    #{停止播放BGM }
    stop music
    scene blackboard with dissolve
    #{显示立绘TJ 1gx}
    show TJ 1gx at tjleft with dissolve
    TeacherTian "接下来我们来学习本课的第二项内容，「な行～は行」的十个假名。"
    TeacherTian "请智子同学为我们读一下吧。"
    TeacherTian "智子ちゃん、ちょっと読んでもらえますか。（智子，能请你读一下吗？）"
    #{显示立绘ZZ 12xf}
    hide TJ
    show ZZ 12xf at left:
        xoffset -150
    with dissolve
    Tomoko "はい。（好的。）"
    #{播放 SE naha10}
    play sound "audio/se/sushiyin/naha10.mp3"
    show screen HiraKataKANA("na_no", "ha_ho", learning=False)
    if chpt3_C_answer_kana_index < 10:
        $ chpt3_C_answer_kana_index = 10
    # TODO: Hard Pause
    Tomoko "な、に、ぬ、ね、の、は、ひ、ふ、へ、ほ。"
    hide ZZ
    show TJ 1gx at left :
        xoffset -150
    with dissolve
    TeacherTian "もう一度お願いします。（请再读一遍。）"
    #{播放 SE naha10}
    play sound "audio/se/sushiyin/naha10.mp3"
    hide TJ
    show ZZ 12xf at left:
        xoffset -150
    with dissolve
    # TODO: Hard Pause
    Tomoko "な、に、ぬ、ね、の、は、ひ、ふ、へ、ほ。"
    hide screen HiraKataKANA
    #{显示立绘TJ 1gx}
    hide ZZ
    show TJ 1gx at left:
        xoffset -150
    with dissolve
    TeacherTian "大家可以跟读练习一下哦。"

    # TODO:{显示图片 十个假名 点击可以发音}
    # 点击图片可以确认发音，完成学习后点击“结束学习”按钮。
    hide TJ with dissolve
    call screen HiraKataKANA("na_no", "ha_ho")

    show TJ 1wx at left with dissolve:
        xoffset -150
    TeacherTian "既然大家都学会了，那么我们来做一个小测试吧。请大家根据听到的读音选择正确的假名。"
    #循环到此处

    jump lesson3_2_q1

label lesson3_2_q1:
    stop music
    #{播放 SE diyiti}
    hide ZZ
    show TJ 1wx
    with dissolve
    TeacherTian "第一题。"
    play sound "audio/se/sushiyin/ni.mp3"
    pause 1.5
    #{播放 SE ni}
    menu l3_2_q1:
        "1.な":
            $chpt3_answer_kana[0] = 0
            jump l3_2_q1AC
        "2.に":
            $chpt3_answer_kana[0] = 5
            jump l3_2_q1B
        "3.ぬ":
            $chpt3_answer_kana[0] = 0
            jump l3_2_q1AC

label l3_2_q1B:
    #选择2.に
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"
    jump lesson3_2_q2

label l3_2_q1AC:
    #选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"  fadein 2.0
    TeacherTian "好像不太对哦，再听一遍。"
    #循环到第本题开始的位置
    jump lesson3_2_q1

label lesson3_2_q2:
    #{播放 SE dierti}
    TeacherTian "第二题。"
    play sound "audio/se/sushiyin/ha.mp3"
    pause 1.5
    #{播放 SE ha}
    menu l3_2_q2:
        "1.は":
            $chpt3_answer_kana[1] = 5
            jump l3_2_q2A
        "2.ひ":
            $chpt3_answer_kana[1] = 0
            jump l3_2_q2BC
        "3.ふ":
            $chpt3_answer_kana[1] = 0
            jump l3_2_q2BC

label l3_2_q2A:
    #选择1.は
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"
    jump lesson3_2_q3

label l3_2_q2BC:
    #选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"  fadein 2.0
    TeacherTian "好像不太对哦，再听一遍。"
    #循环到第本题开始的位置
    jump lesson3_2_q2

label lesson3_2_q3:
    #{播放 SE disanti}
    TeacherTian "第三题。"
    play sound "audio/se/sushiyin/ne.mp3"
    pause 1.5
    #{播放 SE ne}
    menu l3_2_q3:
        "1.ね":
            $chpt3_answer_kana[2] = 5
            jump l3_2_q3A
        "2.へ":
            $chpt3_answer_kana[2] = 0
            jump l3_2_q3BC
        "3.て":
            $chpt3_answer_kana[2] = 0
            jump l3_2_q3BC

label l3_2_q3A:
    #选择1.ね
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"
    jump lesson3_2_q4

label l3_2_q3BC:
    #选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"  fadein 2.0
    TeacherTian "好像不太对哦，再听一遍。"
    #循环到第本题开始的位置
    jump lesson3_2_q3

label lesson3_2_q4:
    #{播放 SE disiti}
    TeacherTian "第四题。"
    play sound "audio/se/sushiyin/ho.mp3"
    pause 1.5
    #{播放 SE ho}
    menu l3_2_q4:
        "1.の":
            $chpt3_answer_kana[3] = 0
            jump l3_2_q4AC
        "2.ほ":
            $chpt3_answer_kana[3] = 5
            jump l3_2_q4B
        "3.と":
            $chpt3_answer_kana[3] = 0
            jump l3_2_q4AC

label l3_2_q4B:
    #选择2.ほ
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"
    jump lesson3_2_q5

label l3_2_q4AC:
    #选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"  fadein 2.0
    TeacherTian "好像不太对哦，再听一遍。"
    #循环到第本题开始的位置
    jump lesson3_2_q4

label lesson3_2_q5:
    #{播放 SE diwuti}
    TeacherTian "第五题。"
    play sound "audio/se/sushiyin/hu.mp3"
    pause 1.5
    #{播放 SE hu}
    menu l3_2_q5:
        "1.ぬ":
            $chpt3_answer_kana[4] = 0
            jump l3_2_q5AB
        "2.の":
            $chpt3_answer_kana[4] = 0
            jump l3_2_q5AB
        "3.ふ":
            $chpt3_answer_kana[4] = 5
            jump l3_2_q5C

label l3_2_q5C:
    #选择3.ふ
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"
    jump lesson3_3

label l3_2_q5AB:
    #选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"  fadein 2.0
    TeacherTian "好像不太对哦，再听一遍。"
    #循环到第本题开始的位置
    jump lesson3_2_q5

label lesson3_3:
    #{显示立绘TJ 1gx}
    show TJ 1gx
    TeacherTian "这十个假名大家都已经掌握了，接下来我们来看一下它们可以组成哪些单词。"
    TeacherTian "智子ちゃん、こちらの単語を読んでもらえますか。（智子，能请你读一下这些单词吗？）"
    #{显示立绘ZZ 12xf}
    show ZZ 12xf at right with dissolve
    Tomoko "はい。読みます。（好的，我读了。）"

    hide TJ with dissolve
    if chpt3_C_answer_tango_index < 1:
        $ chpt3_C_answer_tango_index = 1


    #{播放 SE 031inu}
    if chpt3_C_answer_tango_index < 1:
        $ chpt3_C_answer_tango_index = 1
    show 031inu2 at middle with dissolve
    play sound "audio/se/sushiyin/031inu2.mp3"
    Tomoko "犬（いぬ）。"
    hide 031inu2 with dissolve


    #{播放 SE 032neko}
    if chpt3_C_answer_tango_index < 2:
        $ chpt3_C_answer_tango_index = 2
    show 032neko2 at middle with dissolve
    play sound "audio/se/sushiyin/032neko2.mp3"
    Tomoko "猫（ねこ）。"
    hide 032neko2 with dissolve


    #{播放 SE 033hana}
    if chpt3_C_answer_tango_index < 3:
        $ chpt3_C_answer_tango_index = 3
    show 033hana2 at middle with dissolve
    play sound "audio/se/sushiyin/033hana2.mp3"
    Tomoko "花（はな）。"
    hide 033hana2 with dissolve


    #{播放 SE 034hoshi}
    if chpt3_C_answer_tango_index < 4:
        $ chpt3_C_answer_tango_index = 4
    show 034hoshi2 at middle with dissolve
    play sound "audio/se/sushiyin/034hoshi2.mp3"
    Tomoko "星（ほし）。"
    hide 034hoshi2 with dissolve


    #{显示立绘TJ 1wx}
    show TJ 1wx at tjleft with dissolve
    TeacherTian "大家可以跟读练习一下哦。"
    hide TJ
    hide ZZ
    with dissolve

    #{TODO: 显示图片1-4  点击可以发音}
    call screen Dango(Dango_L3)
    # 点击图片可以确认发音，完成学习后点击“结束学习”按钮。

    show TJ 1wx at tjleft with dissolve
    TeacherTian "既然大家都学会了，那么我们来做一个小测试吧。请大家根据听到的读音选择正确的单词。"


    jump lesson3_3_q1

label lesson3_3_q1:
    #{播放 SE diyiti}
    hide ZZ
    show TJ 1wx
    with dissolve
    TeacherTian "第一题。"
    #{播放 SE 033hana}
    pause 1.5
    play sound "audio/se/sushiyin/033hana2.mp3"
    pause 1.0
    menu l3_3_q1:
        "1.犬（いぬ）":
            $chpt3_answer_tango[0] = 0
            jump l3_3_q1AB
        "2.猫（ねこ）":
            $chpt3_answer_tango[0] = 0
            jump l3_3_q1AB
        "3.花（はな）":
            $chpt3_answer_tango[0] = 5
            jump l3_3_q1C

label l3_3_q1C:
    #选择3.花（はな）
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"
    jump lesson3_3_q2

label l3_3_q1AB:
    #选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"  fadein 2.0
    TeacherTian "好像不太对哦，再听一遍。"
    #循环到本题上方
    jump lesson3_3_q1

label lesson3_3_q2:
    #{播放 SE dierti}
    show TJ 1wx
    TeacherTian "第二题。"
    #{播放 SE 034hoshi}
    pause 1.5
    play sound "audio/se/sushiyin/034hoshi2.mp3"
    pause 1.0
    menu l3_3_q2:
        "1.花（はな）":
            $chpt3_answer_tango[1] = 0
            jump l3_3_q2AC
        "2.星（ほし）":
            $chpt3_answer_tango[1] = 5
            jump l3_3_q2B
        "3.猫（ねこ）":
            $chpt3_answer_tango[1] = 0
            jump l3_3_q2AC

label l3_3_q2B:
    #选择2.星（ほし）
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"
    jump lesson3_3_q3

label l3_3_q2AC:
    #选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"  fadein 2.0
    TeacherTian "好像不太对哦，再听一遍。"
    #循环到本题上方
    jump lesson3_3_q2

label lesson3_3_q3:
    #{播放 SE disanti}
    show TJ 1wx
    TeacherTian "第三题。"
    #{播放 SE 031inu}
    pause 1.5
    play sound "audio/se/sushiyin/031inu2.mp3"
    pause 1.0
    menu l3_3_q3:
        "1.星（ほし）":
            $chpt3_answer_tango[2] = 0
            jump l3_3_q3AC
        "2.犬（いぬ）":
            $chpt3_answer_tango[2] = 5
            jump l3_3_q3B
        "3.花（はな）":
            $chpt3_answer_tango[2] = 0
            jump l3_3_q3AC

label l3_3_q3B:
    #选择2.犬（いぬ）
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    play sound "audio/se/sushiyin/zhengque.mp3"
    TeacherTian "回答正确。"
    jump lesson3_4

label l3_3_q3AC:
    #选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放se cuowu}
    play sound "audio/se/sushiyin/cuowu.mp3"  fadein 2.0
    TeacherTian "好像不太对哦，再听一遍。"
    #循环到本题上方
    jump lesson3_3_q3

label lesson3_4:
    #{显示立绘TJ 1gx}
    show TJ 1gx
    TeacherTian "今天的内容就是这些，同学们都掌握了吗？"
    TeacherTian "希望大家在睡前用5分钟的时间回顾一下今天所学的内容，不要忘记了哦。"
    TeacherTian "本节课到此结束，明天见。"

    jump lesson3_5

label lesson3_5:
    #{显示背景  p06 qinshi }
    scene p06 qinshi with dissolve
    #{播放BGM b0304}
    play music "audio/bgm/b0110 sushe.mp3"  fadein 2.0
    "回到寝室，我看到刘洋正坐在桌前看书，想起今天在社团招新活动中一直没见到他。"
    #{显示立绘WH 12jy}
    show WH 12jy at t_right with dissolve
    me "刘洋，你今天去社团招新活动了吗？"
    #{显示立绘LY 11wx}
    show LY 11wx at left with dissolve
    LiuYang "没啊，中午和周小雨一起去办公室帮老师整理资料了。"
    #{显示立绘WH 11wx}
    show WH 11wx
    me "哦，这样啊。"
    hide WH
    hide LY
    with dissolve
    "突然，我心里泛起一丝不安。"
    "本来今天应该是刘洋和智子一起去逛社团的，然而我却暗暗和周小雨一起改变了历史，这会不会影响未来的结果呢？"
    "可是转念一想，或许上天让我现在回到这里，就是给我一次改变的机会。"
    #{显示立绘WH 11ng}
    show WH 12wx at middle with dissolve
    me "你……觉得智子怎么样？"
    "我鼓起勇气说起这个话题。"
    #{显示立绘LY 12gx}
    show WH at MidToRight
    show LY 12jy at left with dissolve
    LiuYang "挺好啊。怎么了？"
    "刘洋不假思索的回答让我有些意外。"
    #{显示立绘WH 11ng}
    show WH 11ng
    me "那小雨呢？"
    #{显示立绘LY 11jy}
    show LY 11wx
    LiuYang "小雨怎么了？"
    #{显示立绘WH 11wx}
    show WH 11wx
    me "就是作为一个女生，你觉得她怎么样？"
    #{显示立绘LY 11jy}
    show LY 11jy
    LiuYang "为什么突然问这个问题啊？难不成你……"
    #{显示立绘WH 11rz}
    show WH 12kx
    "我也不知为何会脱口问出小雨的事情。刘洋的回答中略带一丝紧张和不安。"
    me "不不不，我没那个意思。你不是说你们是青梅竹马嘛，关系也比较好。好奇而已。"
    #{显示立绘LY 11gx}
    show LY 11gx
    LiuYang "哦，吓我一跳。我还想谁会喜欢上那个傻丫头呢。"
    "刘洋略带释然的话语中反而透出了一些暧昧。"
    show WH 12wx
    "原来如此……这两个人原来是两情相悦，却彼此没有敞开心扉。怪不得10年后还未修成正果。"
    #{显示立绘LY 12wx}
    show LY 12wx
    LiuYang "对了，不知道为什么今天小雨看上去很高兴，我问她怎么了她也不说。"
    "刘洋突然扯开话题。"
    #{显示立绘WH 12kx}
    show WH 12kx
    me "她和你说什么没？"
    #{显示立绘LY 11jy}
    show LY 11jy
    LiuYang "说什么？"
    #{显示立绘WH 11zm}
    show WH 11zm
    me "没……没什么。"
    "我想起了昨天晚上小雨的话，或许她已经有了自己的答案吧。"
    #{显示立绘WH 11rz}
    show WH 11rz
    me "对了，你昨天说想去日本读大学对不？"
    #{显示立绘LY 11rz}
    show LY 11rz
    LiuYang "是啊。"
    #{显示立绘WH 12gx}
    show WH 12gx
    me "我听说国内很多大学也有交换留学的机会，说不定这样更好哦。"
    #{显示立绘LY 12gx}
    show LY 12gx
    LiuYang "哦，这样啊。确实这样也不错。"
    #{显示立绘WH 12wx}
    hide LY
    show WH 12wx at middle
    with dissolve
    "不知道刘洋对我这突如其来的建议是否会感觉有些奇怪。"
    "既然原世界线里刘洋和小雨同时考上了华师大，那我就按照这个路线推他们一把吧，也算是成人之美。"
    #{停止播放BGM }
    stop music fadeout 2.0

    "我躺在床上，迷迷糊糊快要睡着的时候，听见刘洋的声音。"
    #{显示立绘LY 12jy}
    hide WH
    show LY 12jy at left
    with dissolve
    LiuYang "这是什么？新游戏吗？"
    #{显示游戏光盘封面 w12}
    "刘洋举起我放在桌上的光盘问我。"
    #{显示立绘WH 13kx}
    show WH 11jy at t_right with dissolve
    #{播放BGM b0305}
    play music "audio/bgm/b0304.mp3"  fadein 2.0
    me "啊，是郑辉给我的，他做的日语学习游戏。"
    #{显示立绘LY 13qx}
    show LY 13qx
    LiuYang "这倒是挺新鲜的。"
    hide LY
    hide WH
    with dissolve
    "睡意一扫而空。我突然想到我还没有体验过这个游戏。我很好奇当年没有打开的游戏里藏着怎样的世界。"
    "我打开电脑，放入光盘。"
    #{显示游戏过程 w13}
    "电脑上出现了一间日语教室，同学们正在教室里上日语课。"
    #{显示游戏过程 w14}
    "主人公是个日语学渣，在课上回答不出老师的问题。"
    "再次回到教室的时候，发现老师和同学们都不见了。"
    #{显示游戏过程 w15}
    "不知为何幻想世界的入口被打开，突然出现了幻想世界的怪物，把老师和同学都抓走了。"
    #{显示游戏过程 w16}
    "通过回答日语题目来收集道具，拯救被困在幻想世界里的老师和同学。"
    #{显示游戏过程 w17}
    #{显示游戏过程 w18}
    "打怪的过程中有日语解题环节，故事情节也很有趣。"
    #{显示游戏过程 w19}
    "还有很多有意思的技能，升级以后还能替换装备。"
    #{物品图片消失}
    "竟然是RPG类型的游戏，没想到高中时代的郑辉已经能够做出完成度那么高的游戏了。打怪+学日语的模式确实新颖。"
    "有时间我试试能不能玩通关……"

    #{显示立绘WH 11kx}
    show WH 11kx at middle with dissolve
    me "对了，田老师说过睡前要复习一下今天上课的内容，看一下笔记吧。"
    #{打开复习回顾界面，添加第三课的内容。}
    stop music
    #{停止播放BGM}

    call screen bunka_review()

    #{显示立绘 WH 13rz}
    show WH 13rz at middle with dissolve
    me "复习了一下，果然思路清晰多了。"
    me "好了，时间不早了，先休息吧……"

    hide WH with dissolve

    return