#第二课
label lesson2_1:
    #{播放BGM b0206}
    play music "audio/bgm/b0206.mp3"
    #{显示背景 p jiaoxue07}
    scene p jiaoxue07 with dissolve
    #{显示立绘TJ 1wx}
    show TJ 1wx at tjleft with dissolve
    TeacherTian "各位同学，今天我们将继续进行第二课的学习。"
    TeacherTian "大家还记得上节课介绍的万叶假名吗？"
    #{显示立绘XY 12wx}
    scene blackboard with dissolve
    show XY 12wx at left with dissolve
    ZhouXiaoyu "万叶假名就是借用一部分汉字的读音来记录日语中原有的发音。"
    #{显示立绘ZH 12wx}
    show ZH 12wx at right with dissolve:
        xoffset -200
    ZhengHui "后来又演化成了平假名和片假名。"
    #{显示背景 p jiaoxue08}
    #{显示立绘TJ 1gx}
    scene p jiaoxue08 with dissolve
    show TJ 1gx at tjleft with dissolve
    TeacherTian "没错，大家上课听得很认真。今天我们也有三个学习任务。"
    TeacherTian "一是了解平假名和片假名的由来，二是学习「さ行～た行」的假名，三是学习「さ行～た行」的相关单词。"
    TeacherTian "上节课说到汉字传到日本之后开始为日本人所用。但实际上，汉字在当时被视为权威和尊严的代表，一般只有男性才可以使用。"
    #{显示立绘QQ 11sq}
    hide TJ
    show QQ 11sq at tjleft with dissolve
    YuanQiaoqiao "那女性怎么办呢？难道就无法使用文字了吗？"
    #{显示背景 p jiaoxue09}
    scene p jiaoxue09 with dissolve
    #{显示立绘TJ 1wx}
    show TJ 1wx at tjleft with dissolve
    TeacherTian "这便是平假名「ひらがな」的由来。平假名大约诞生于公元九世纪，最初被宫廷中的女性所使用。"
    TeacherTian "由于汉字笔画较多，因此宫中的女官们将汉字的草书简化成便于书写的形式，慢慢地演变成了平假名。"
    #{显示立绘LY 12gx}
    hide TJ
    show LY 12gx at tjleft with dissolve
    LiuYang "原来如此。难怪之前听说过平假名也被称为女手。"
    #{显示背景 p jiaoxue10}
    scene p jiaoxue10 with dissolve
    #{显示立绘TJ 1wx}
    show TJ 1wx at tjleft with dissolve
    TeacherTian "没错。紫式部所写的《源氏物语》，以及清少纳言所写的《枕草子》中都使用了平假名。"
    TeacherTian "不过，实际上平假名不仅限于女性使用，《古今和歌集》等男性书写的作品中也使用了平假名。"
    #{显示立绘XY 12zm}
    hide TJ
    show XY 12zm at tjleft with dissolve
    ZhouXiaoyu "那现在日语中的平假名有什么作用呢？"
    #{显示立绘TJ 1gx}
    hide XY
    show TJ 1gx at tjleft with dissolve
    TeacherTian "现在日语中的平假名除了用于书写和语单词、标注汉字读音以外，还常常用于单词的词尾部分，如「分かる、美味しい」等。"
    #{显示立绘ZH 12wn}
    hide TJ with dissolve
    show ZH 12wn at tjleft with dissolve
    ZhengHui "原来是这样呀。那片假名有什么用呢？"
    #{显示背景 p jiaoxue11}
    scene p jiaoxue11 with dissolve
    #{显示立绘TJ 1wx}
    show TJ 1wx at tjleft with dissolve
    TeacherTian "这个问题问得很好，其实片假名和平假名原本有完全不同的用途。片假名比平假名出现的时间还要早，大约诞生于公元八世纪。当时日本的僧人在念佛经的时候，为了标注汉字的读音，便用汉字的偏旁部首做一些标记。这些标记慢慢变成了一种假名文字。"
    #{显示立绘QQ 13xf}
    hide TJ
    show QQ 13xf at tjleft with dissolve
    YuanQiaoqiao "原来不论平假名还是片假名，都和汉字密切相关啊！"
    #{显示背景 p jiaoxue12}
    scene p jiaoxue12 with dissolve
    #{显示立绘TJ 1gx}
    show TJ 1gx at tjleft with dissolve
    TeacherTian "是的，不过现在的片假名主要用于表示外来语。例如外国的人名、地名、专有词汇，或是其他需要强调的词。"
    #{显示立绘XY 11zm}
    hide TJ
    show XY 11zm at tjleft with dissolve
    ZhouXiaoyu "那么平假名、片假名、汉字到底应该怎么用呢？"
    #{显示立绘TJ 1wx}
    hide XY
    show TJ 1wx at tjleft with dissolve
    TeacherTian "问得好。其实这三种文字都是日语中的正式文字，常见的文章中也会混用。日文也被称为「漢字仮名交じり文」，译为汉字假名混合文。"

    #{显示立绘TJ 1gx}
    scene blackboard with dissolve
    show TJ 1gx at tjleft with dissolve
    TeacherTian "接下来我们将继续学习「さ行～た行」十个假名的读法与写法。"
    TeacherTian "在这之前我们先来做一个小测试，看看大家是否掌握了刚才所讲的知识。"

    jump lesson2_1_q1

label lesson2_1_q1:
    #{显示立绘TJ 1gx}
    show TJ 1gx at tjleft
    menu l2_1_q1:
        '平假名为什么又被称为女手？'
        "1.早期平假名多为女性所用":
            $chpt2_answer_bunka[0] = 10
            jump l2_1_q1A
        "2.平假名只能由女性使用":
            $chpt2_answer_bunka[0] = 0
            jump l2_1_q1BC
        "3.女性更擅长书写平假名":
            $chpt2_answer_bunka[0] = 0
            jump l2_1_q1BC

label l2_1_q1A:
    if chpt2_C_answer_bunka_index < 1:
        $ chpt2_C_answer_bunka_index = 1
    #选择1.
    #好感度参数 +10
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    TeacherTian "回答正确。实际上平假名不仅限于女性使用，《古今和歌集》等男性书写的作品中也使用了平假名。"

    jump lesson2_1_q2

label l2_1_q1BC:
    if chpt2_C_answer_bunka_index < 1:
        $ chpt2_C_answer_bunka_index = 1
    # 选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放 SE cuowu}
    TeacherTian "上课要认真听讲哦。实际上平假名不仅限于女性使用，《古今和歌集》等男性书写的作品中也使用了平假名。"

    jump lesson2_1_q2

label lesson2_1_q2:
    show TJ 1gx
    menu l2_1_q2:
        '平假名的起源是？'
        "1.汉字的偏旁部首":
            $chpt2_answer_bunka[1] = 0
            jump l2_1_q2AC
        "2.汉字的草书":
            $chpt2_answer_bunka[1] = 10
            jump l2_1_q2B
        "3.汉字的楷书":
            $chpt2_answer_bunka[1] = 0
            jump l2_1_q2AC

label l2_1_q2B:
    if chpt2_C_answer_bunka_index < 2:
        $ chpt2_C_answer_bunka_index = 2
    #选择2.
    #好感度参数 +10
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    TeacherTian "回答正确。宫中的女官们将汉字的草书简化成便于书写的形式，慢慢地演变成了平假名。"

    jump lesson2_1_q3

label l2_1_q2AC:
    if chpt2_C_answer_bunka_index < 2:
        $ chpt2_C_answer_bunka_index = 2
    # 选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放 SE cuowu}
    TeacherTian "上课要认真听讲哦。宫中的女官们将汉字的草书简化成便于书写的形式，慢慢地演变成了平假名。"

    jump lesson2_1_q3

label lesson2_1_q3:
    #{显示立绘TJ 1gx}
    show TJ 1gx at tjleft
    menu l2_1_q3:
        '以下哪个不是片假名的功能？'
        "1.标注外国的人名和地名":
            $chpt2_answer_bunka[2] = 0
            jump l2_1_q3AB
        "2.突出需要强调的词":
            $chpt2_answer_bunka[2] = 0
            jump l2_1_q3AB
        "3.作为助词使用":
            $chpt2_answer_bunka[2] = 10
            jump l2_1_q3C

label l2_1_q3C:
    if chpt2_C_answer_bunka_index < 3:
        $ chpt2_C_answer_bunka_index = 3
    #选择3
    #好感度参数 +10
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    TeacherTian "回答正确。现在的片假名主要用于表示外来语。例如外国的人名、地名、专有词汇，或是其他需要强调的词。"

    jump lesson2_2

label l2_1_q3AB:
    if chpt2_C_answer_bunka_index < 3:
        $ chpt2_C_answer_bunka_index = 3
    # 选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放 SE cuowu}
    TeacherTian "上课要认真听讲哦。现在的片假名主要用于表示外来语。例如外国的人名、地名、专有词汇，或是其他需要强调的词。"

    jump lesson2_2

label lesson2_2:
    #{停止播放BGM}
    stop music
    #第二课 假名部分
    scene blackboard with dissolve
    #{显示立绘TJ 1gx}
    show TJ 1gx at tjleft with dissolve
    TeacherTian "接下来我们来学习本课的第二项内容，「さ行～た行」的十个假名。"
    TeacherTian "请智子同学为我们读一下吧。"
    TeacherTian "智子ちゃん、ちょっと読んでもらえますか。（智子，能请你读一下吗？）"
    #{显示立绘ZZ 11gx}
    hide TJ with dissolve
    show ZZ 11gx at left with dissolve:
        xoffset -150
    Zhizi "はい。（好的。）"
    #{播放SE sata10 }
    play sound "audio/se/sushiyin/sata10.mp3"
    show screen HiraKataKANA("sa_so", "ta_to", learning=False)
    if chpt2_C_answer_kana_index < 10:
        $ chpt2_C_answer_kana_index = 10
    # TODO: Hard Pause
    Zhizi "さ、し、す、せ、そ、た、ち、つ、て、と。"
    #{显示立绘TJ 1wx}
    hide ZZ with dissolve
    show TJ 1wx at left with dissolve:
        xoffset -150
    TeacherTian "もう一度お願いします。（请再读一遍。）"
    #{播放SE sata10 }
    play sound "audio/se/sushiyin/sata10.mp3"
    hide TJ with dissolve
    show ZZ 11gx at left with dissolve:
        xoffset -150
    # TODO: Hard Pause
    Zhizi "さ、し、す、せ、そ、た、ち、つ、て、と。"
    hide screen HiraKataKANA
    #{显示立绘TJ 1gx}
    hide ZZ with dissolve
    show TJ 1gx at left with dissolve:
        xoffset -150
    TeacherTian "大家可以跟读练习一下哦。"

    # TODO:{显示图片 十个假名 点击可以发音}
    # 点击图片可以确认发音，完成学习后点击“结束学习”按钮。
    hide TJ with dissolve
    call screen HiraKataKANA("sa_so", "ta_to")

    show TJ 1wx at left with dissolve:
        xoffset -150
    TeacherTian "既然大家都学会了，那么我们来做一个小测试吧。请大家根据听到的读音选择正确的假名。"
    #循环到此处
    hide ZZ with dissolve

    jump lesson2_2_q1

label lesson2_2_q1:
    stop music
    #{播放se diyiti}
    show TJ 1wx
    TeacherTian "第一题。"
    play sound "audio/se/sushiyin/su.mp3"
    pause 1.5
    #{播放SE su}
    menu l2_2_q1:
        "1.さ":
            $chpt2_answer_kana[0] = 0
            jump l2_2_q1AB
        "2.し":
            $chpt2_answer_kana[0] = 0
            jump l2_2_q1AB
        "3.す":
            $chpt2_answer_kana[0] = 5
            jump l2_2_q1C

label l2_2_q1C:
    #选择3.す
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    TeacherTian "回答正确。"
    jump lesson2_2_q2

label l2_2_q1AB:
    #选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放se cuowu}
    TeacherTian "好像不太对哦，再听一遍。"
    #循环到第一题的位置
    jump lesson2_2_q1

label lesson2_2_q2:
    #循环到此处
    #{播放se dierti}
    show TJ 1wx
    TeacherTian "第二题。"
    play sound "audio/se/sushiyin/chi.mp3"
    pause 1.5
    #{播放SE chi}
    menu l2_2_q2:
        "1.た":
            $chpt2_answer_kana[1] = 0
            jump l2_2_q2AC
        "2.ち":
            $chpt2_answer_kana[1] = 5
            jump l2_2_q2B
        "3.つ":
            $chpt2_answer_kana[1] = 0
            jump l2_2_q2AC

label l2_2_q2B:
    #选择2.ち
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    TeacherTian "回答正确。"
    jump lesson2_2_q3

label l2_2_q2AC:
    #选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放se cuowu}
    TeacherTian "好像不太对哦，再听一遍。"
    #循环到第二题的位置
    jump lesson2_2_q2

label lesson2_2_q3:
    #循环到此处
    #{播放se disanti}
    TeacherTian "第三题。"
    play sound "audio/se/sushiyin/te.mp3"
    pause 1.5
    #{播放SE te}
    menu l2_2_q3:
        "1.そ":
            $chpt2_answer_kana[2] = 0
            jump l2_2_q3AB
        "2.せ":
            $chpt2_answer_kana[2] = 0
            jump l2_2_q3AB
        "3.て":
            $chpt2_answer_kana[2] = 5
            jump l2_2_q3C

label l2_2_q3C:
    #选择3.て
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    TeacherTian "回答正确。"
    jump lesson2_2_q4

label l2_2_q3AB:
    #选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放se cuowu}
    TeacherTian "好像不太对哦，再听一遍。"
    #循环到第三题的位置
    jump lesson2_2_q3

label lesson2_2_q4:
    #循环到此处
    #{播放se disiti}
    TeacherTian "第四题。"
    play sound "audio/se/sushiyin/ta.mp3"
    pause 1.5
    #{播放SE ta}
    menu l2_2_q4:
        "1.と":
            $chpt2_answer_kana[3] = 0
            jump l2_2_q4AC
        "2.た":
            $chpt2_answer_kana[3] = 5
            jump l2_2_q4B
        "3.し":
            $chpt2_answer_kana[3] = 0
            jump l2_2_q4AC

label l2_2_q4B:
    #选择2.た
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    TeacherTian "回答正确。"
    jump lesson2_2_q5

label l2_2_q4AC:
    #选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放se cuowu}
    TeacherTian "好像不太对哦，再听一遍。"
    #循环到第四题的位置
    jump lesson2_2_q4

label lesson2_2_q5:
    #循环到此处
    #{播放se diwuti}
    TeacherTian "第五题。"
    play sound "audio/se/sushiyin/sa.mp3"
    pause 1.5
    #{播放SE sa}
    menu l2_2_q5:
        "1.か":
            $chpt2_answer_kana[4] = 0
            jump l2_2_q5AC
        "2.さ":
            $chpt2_answer_kana[4] = 5
            jump l2_2_q5B
        "3.う":
            $chpt2_answer_kana[4] = 0
            jump l2_2_q5AC

label l2_2_q5B:
    #选择2.さ
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    TeacherTian "回答正确。"
    jump lesson2_3

label l2_2_q5AC:
    #选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放se cuowu}
    TeacherTian "好像不太对哦，再听一遍。"
    #循环到第五题的位置
    jump lesson2_2_q5


label lesson2_3:
    # TODO
    TeacherTian "这十个假名大家都已经掌握了，接下来我们来看一下它们可以组成哪些单词。"
    TeacherTian "智子ちゃん、こちらの単語を読んでもらえますか。（智子，能请你读一下这些单词吗？）"
    #{显示立绘ZZ 11wx}
    show ZZ 11wx at right with dissolve
    Zhizi "はい。読みます。（好的，我读了。）"

    hide TJ with dissolve
    if chpt2_C_answer_tango_index < 1:
        $ chpt2_C_answer_tango_index = 1

    # TODO: 021sushi2
    if chpt2_C_answer_tango_index < 1:
        $ chpt2_C_answer_tango_index = 1
    show 021sushi2 at middle with dissolve
    play sound "audio/se/sushiyin/021sushi2.mp3"
    Zhizi "寿司（すし）。"
    hide 021sushi2 with dissolve

    # TODO: 022suki2
    if chpt2_C_answer_tango_index < 2:
        $ chpt2_C_answer_tango_index = 2
    show 022suki2 at middle with dissolve
    play sound "audio/se/sushiyin/022suki2.mp3"
    Zhizi "好き（すき）。"
    hide 022suki2 with dissolve

    # TODO: 023uta2
    if chpt2_C_answer_tango_index < 3:
        $ chpt2_C_answer_tango_index = 3
    show 023uta2 at middle with dissolve
    play sound "audio/se/sushiyin/023uta2.mp3"
    Zhizi "唄（うた）。"
    hide 023uta2 with dissolve

    # TODO: 024tuki2
    if chpt2_C_answer_tango_index < 4:
        $ chpt2_C_answer_tango_index = 4
    show 024tuki2 at middle with dissolve
    play sound "audio/se/sushiyin/024tuki2.mp3"
    Zhizi "月（つき）。"
    hide 024tuki2 with dissolve

    show TJ 1wx at tjleft with dissolve
    TeacherTian "大家可以跟读练习一下哦。"
    hide TJ with dissolve
    hide ZZ with dissolve

    #{TODO: 显示图片1-4  点击可以发音}
    call screen Dango(Dango_L2)
    # 点击图片可以确认发音，完成学习后点击“结束学习”按钮。


    show TJ 1wx at tjleft with dissolve
    TeacherTian "既然大家都学会了，那么我们来做一个小测试吧。请大家根据听到的读音选择正确的单词。"

    hide ZZ with dissolve

    jump lesson2_3_q1

label lesson2_3_q1:
    #{播放se diyiti}
    show TJ 1wx
    TeacherTian "第一题。"
    #{播放se 021sushi}
    pause 1.5
    play sound "audio/se/sushiyin/021sushi2.mp3"
    pause 1.0
    menu l2_3_q1:
        "1.寿司（すし）":
            $chpt2_answer_tango[0] = 5
            jump l2_3_q1A
        "2.唄（うた）":
            $chpt2_answer_tango[0] = 0
            jump l2_3_q1BC
        "3.月（つき）":
            $chpt2_answer_tango[0] = 0
            jump l2_3_q1BC

label l2_3_q1A:
    #选择1.寿司（すし）
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    TeacherTian "回答正确。"

    jump lesson2_3_q2

label l2_3_q1BC:
    #选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放se cuowu}
    TeacherTian "好像不太对哦，再听一遍。"
    #循环到本题上方

    jump lesson2_3_q1

label lesson2_3_q2:
    #{播放se dierti}
    show TJ 1wx
    TeacherTian "第二题。"
    #{播放se 022suki}
    pause 1.5
    play sound "audio/se/sushiyin/022suki2.mp3"
    pause 1.0
    menu l2_3_q2:
        "1.好き（すき）":
            $chpt2_answer_tango[1] = 5
            jump l2_3_q2A
        "2.月（つき）":
            $chpt2_answer_tango[1] = 0
            jump l2_3_q2BC
        "3.寿司（すし）":
            $chpt2_answer_tango[1] = 0
            jump l2_3_q2BC

label l2_3_q2A:
    #选择1.好き（すき）
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    TeacherTian "回答正确。"
    jump lesson2_3_q3

label l2_3_q2BC:
    #选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放se cuowu}
    TeacherTian "好像不太对哦，再听一遍。"
    #循环到本题上方
    jump lesson2_3_q2

label lesson2_3_q3:
    #{播放se disanti}
    show TJ 1wx
    TeacherTian "第三题。"
    #{播放se 023uta}
    pause 1.5
    play sound "audio/se/sushiyin/023uta2.mp3"
    pause 1.0
    menu l2_3_q3:
        "1.月（つき）":
            $chpt2_answer_tango[2] = 0
            jump l2_3_q3AB
        "2.好き（すき）":
            $chpt2_answer_tango[2] = 0
            jump l2_3_q3AB
        "3.唄（うた）":
            $chpt2_answer_tango[2] = 5
            jump l2_3_q3C

label l2_3_q3C:
    #选择3.唄（うた）
    #{显示立绘 TJ 1gx}
    show TJ 1gx
    #{播放 SE zhengque}
    TeacherTian "回答正确。"
    jump lesson2_4

label l2_3_q3AB:
    #选择 其他选项
    #{显示立绘 TJ 1ng}
    show TJ 1ng
    #{播放se cuowu}
    TeacherTian "好像不太对哦，再听一遍。"
    #循环到本题上方
    jump lesson2_3_q3

label lesson2_4:
    # #{播放BGM b0206}
    # play music "audio/bgm/b0206.mp3" fadein 2.0
    #{显示立绘TJ 1gx}
    show TJ 1gx
    TeacherTian "今天的内容就是这些，同学们都掌握了吗？"
    TeacherTian "希望大家在睡前用5分钟的时间回顾一下今天所学的内容，不要忘记了哦。"
    TeacherTian "本节课到此结束，明天见。"

    jump lesson2_5

label lesson2_5:
    #（回到寝室）
    # TODO: {播放BGM b0207}
    play music "audio/bgm/b0110 sushe.mp3" fadein 2.0
    #{显示背景  p06 qinshi }
    scene p06 qinshi with dissolve
    "晚自修结束后，回到宿舍。躺在床上，我的心情有些复杂。"
    "这一次神奇的穿越，让我带着所有的记忆回到了智子身边。"
    #{显示立绘WH 11zm}
    show WH 11zm at middle with dissolve
    "虽然很高兴能走近智子，愉快地和她交流。但我总觉得自己像个小偷，偷走了本应该属于智子和刘洋的故事。而且，现在的自己还是那个浑浑噩噩的状态，又如何能够给她幸福呢。"
    "此时，我忽然想起了周小雨。中午吃饭的时候她那欲言又止的样子，好像是遇到了什么烦心事，而且似乎和刘洋有关。于是我忍不住拿出手机给周小雨发了短信。"
    #{显示立绘WH 12rz}
    show WH 12rz at MidToRight
    me "小雨，在吗？"
    #{显示立绘XY 13jy}
    show XY 13jy at left with dissolve
    ZhouXiaoyu "怎么了，王浩？有什么事吗？"
    "我的短信也许会让周小雨感到意外。我高中的时候几乎不会主动和女生发消息。对于高中生来说，称呼好像也过于亲昵了。"
    #{显示立绘WH 13rz}
    show WH 13rz
    me "是这样的，中午看你有些失落，所以想来问问。"
    "周小雨很久没有回复，我有些焦急，又发了一条消息。"
    #{显示立绘WH 11zm}
    show WH 11zm
    me "你是不是喜欢刘洋啊？"
    "出于成年人的直觉，以及对高中生活的八卦和好奇，我直截了当地向周小雨确认她的心情。"
    "这次她秒回了。"
    #{显示立绘XY 13jy}
    show XY 13jy
    ZhouXiaoyu "有……那么明显吗？"
    "周小雨毫不避讳的回答，反而让我感到有些诧异。当时只觉得他们是关系很好的朋友，完全没想到这一层。随即，对话框接连跳了出来。"
    #{显示立绘XY 13wx}
    show XY 13wx
    ZhouXiaoyu "我和刘洋一起长大的，初中时我们还是同桌。"
    ZhouXiaoyu "他可能一直只是把我当成朋友吧。"
    #{显示立绘WH 12rz}
    show WH 12rz
    me "为什么这么说呢？"
    #{显示立绘XY 12bx}
    show XY 12bx
    ZhouXiaoyu "女生的第六感吧(*^-^)。初中的时候，有一次我的手不小心受伤了，他主动来帮我拿书包，课间还帮我倒水，班里同学起哄说我们两个人在谈恋爱。"
    #{显示立绘XY 13bx}
    show XY 13bx
    ZhouXiaoyu "你猜刘洋怎么着？"
    #{显示立绘WH 11rz}
    show WH 11rz
    me "他让你别放心上？"
    #{显示立绘XY 11bx}
    show XY 11bx
    ZhouXiaoyu "他把造谣的人打了一顿。坚持说和我只是普通朋友，让造谣的人闭嘴。"
    ZhouXiaoyu "在那之后就没有人再开玩笑了。不过我们俩的关系也变得有点古怪，好像都在避免尴尬。"
    me "所以你还是挺在乎他的咯？"
    #{显示立绘XY 13zm}
    show XY 13zm
    ZhouXiaoyu "上高中以后，我发现原来自己有点喜欢他。看到他和别的女生聊天，心里也会觉得有些不开心，想想自己也挺小家子气的……"
    #{显示立绘WH 12zm}
    show WH 12zm
    me "我看刘洋其实一直都很关心你啊，只是不善于表达吧。"
    #{显示立绘XY 13jy}
    show XY 13jy
    ZhouXiaoyu "诶(´•༝•`)，有时候觉得他挺懂我的，但有时候却感觉很疏远。"
    #{显示立绘WH 11wx}
    show WH 11wx
    me "男生的喜欢，有时候可能自己也未必能察觉。"
    me "对了，中午说起梦想的事情，你遇到了什么困难吗？"
    #{显示立绘XY 13wx}
    show XY 13wx
    ZhouXiaoyu "你真细心，没想到这也被你发现了。刘洋觉得我想成为一名钢琴家，但其实我并没有那么高的天赋，对自己也没什么信心。"
    ZhouXiaoyu "我很想大学有机会和刘洋一起去日本，但是家里的经济条件不允许。"
    #{显示立绘WH 12rz}
    show WH 12rz
    me "那或许他愿意留在国内和你一起上大学呢？不问问怎么知道。"
    #{显示立绘XY 13dy}
    show XY 13dy
    ZhouXiaoyu "说了要是被拒绝了，还要一起上课，多尴尬呀。而且，我不能那么自私，让刘洋放弃去日本的机会……"
    #{显示立绘WH 12zm}
    show WH 12zm
    me "有道理。不过，我相信会有一个两全其美的方案的。"
    "小雨和刘洋两个人最终选择在国内读大学。一个读了音乐教育，一个学了社会学。说不定当时刘洋就是为了小雨才放弃了去日本的机会。站在上帝视角的我自信满满地为小雨打气。"
    me "即使在国内读本科，研究生也还有机会一起去日本嘛。"
    "我想起了小雨说的她后来去日本读研究生的事情，便补充了一句。"
    #{显示立绘XY 13wx}
    show XY 13wx
    ZhouXiaoyu "确实，你说得对。人生有很多选择。(＾ω＾) "
    "小雨回复了我一个笑脸。我看着自己发给小雨的话语，仿佛看到了另一个自己在说话。这些话或许也是对我自己说的，人生真的有很多可能性。或许我应该更真诚地面对自己的感情。"
    #{显示立绘XY 12bx}
    show XY 12bx
    ZhouXiaoyu "对了对了，明天是什么日子你记得吗？"
    #{显示立绘WH 11zm}
    show WH 11zm
    me "你是说社团招新对吧。"
    #{显示立绘XY 11wx}
    show XY 11wx
    ZhouXiaoyu "你要不要带智子去逛逛？"
    #{显示立绘WH 12zm}
    show WH 12zm
    me "你明天不去吗？"
    #{显示立绘XY 12wx}
    show XY 12wx
    ZhouXiaoyu "帮你创造机会呀，你不想要和智子独处的机会？"
    "周小雨已从自己的故事里抽出身来，切换了频道，开始考虑起了帮我助攻的事情。"
    "当年的社团招新活动我并没有参加，或许这次能创造一些新的回忆。"
    #{显示立绘WH 11wx}
    show WH 11wx
    me "好啊，那我就陪智子去逛逛吧。"
    #{显示立绘XY 13wx}
    show XY 13wx
    ZhouXiaoyu "好嘞，包在我身上吧。晚安。(〃'▽'〃) "
    hide XY with dissolve
    show WH at middle with dissolve
    "又是一个笑脸，我仿佛看到了手机那一端周小雨的坏笑。"

    #{显示立绘WH 12rz}
    show WH 12rz
    me "对了，田老师说过睡前要复习一下今天上课的内容，看一下笔记吧。"
    #{打开复习回顾界面，添加第二课的内容。}

    #{停止播放BGM}

    #{显示立绘 WH 13rz}
    show WH 13rz
    me "复习了一下，果然思路清晰多了。"

    #（打开复习回忆界面、增加第二课内容，文化常识、假名）
    me "好了，时间不早了，先休息吧……"

    hide WH with dissolve

    return