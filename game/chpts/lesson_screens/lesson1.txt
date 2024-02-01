#####################################################################
# 第一课 文化部分  课堂对话
label lesson1_1:
    # 第一课

    scene blackboard
    show lihui at middle
    # TODO {播放SE  上课铃声}
    TeacherTian "各位同学，欢迎大家开启学习日语的第一课。今天我们有三个学习任务。"
    # TODO {显示图片 学习目标}
    TeacherTian "一是了解日语中“万叶假名”的由来，二是学习「あ行～か行」的假名。最后教大家一些基础的日语对话。"
    TeacherTian "《隋书》中有一句对日本的记载：“无文字，唯刻木结绳。敬佛法，于百济求得佛经，始有文字。”"
    TeacherTian "也就是说，日本起初有自己的语言，却没有用于记载的文字，主要通过口耳相传。"
    ZhouXiaoyu "原来是这样啊。那日本什么时候开始有了文字呢？"
    TeacherTian "大约在公元三至五世纪，汉字逐渐从中国传入日本。"
    LiuYang "当时没有字典，也没有翻译软件，日本人是如何学习汉字的呢？"
    TeacherTian "这个问题问的很好。其实汉字传入日本后产生了两种用途。一种是“汉字的正用”，也就是严格遵循汉字的本义所使用。"
    # TODO {显示图片 山的两种发音}
    TeacherTian "例如日本人使用“山”这个汉字来表示山峰。但是有两种读音。一种是原本日语中的发音“yama”，另一种是中文中的发音“shan”。"
    ZhengHui "那不是很麻烦啊。"
    TeacherTian "哈哈，确实。尤其是“shan”这个读音日本人并不熟悉，因此汉字起初更多的是被当作“表音文字”来使用。于是日本人创造出了“万叶假名”。"
    TeacherTian "这里的“假”就是“假借(汉字)”的意思。“万叶假名”借用一部分汉字的读音来记录原本日语中的读音。"
    # TODO {显示图片 山的万叶假名}
    TeacherTian "例如日语中的“山”读作“yama”，就可以用“夜麻，野麻”等汉字来记录。这种使用方法就被称为“万叶假名”。"
    YuanQiaoqiao "原来如此。那既然有“假名”，那还有“真名”吗？"
    TeacherTian "当然有。“真名”就是指的汉字原来的用法啊。"
    TeacherTian "此后，在万叶假名的基础上，演化出平假名「ひらがな」和片假名「カタカナ」。"
    TeacherTian "今天我们就要来学习十个假名的读法与写法哦。"
    TeacherTian "对了，在这之前我们先做一个小测试吧。看看大家是否都掌握了。"

    jump lesson1_1_q1


label lesson1_1_q1:
    TeacherTian "第一题。"
    show lihui at left with dissolve #at MidToLeft
    menu l1_1_q1:
        '日本是先有语言还是先有文字？'
        "1.先有语言":
            jump lesson1_1_q1_c1
        "2.先有文字":
            jump lesson1_1_q1_c23
        "3.同时出现":
            jump lesson1_1_q1_c23

label lesson1_1_q1_c1:
    #选择1.语言
    show lihui at middle with dissolve #at LeftToMid
    TeacherTian "正确。日本起初有自己的语言，却没有用于记载的文字，主要通过口耳相传。"
    jump lesson1_1_q2

label lesson1_1_q1_c23:
    # 选择 其他选项
    show lihui at middle with dissolve #at LeftToMid
    TeacherTian "上课要认真听讲哦。日本起初有自己的语言，却没有用于记载的文字，主要通过口耳相传。"
    jump lesson1_1_q2


label lesson1_1_q2:
    TeacherTian "第二题。"
    show lihui at left with dissolve #at MidToLeft
    menu l1_1_q2:
        '日语中“汉字的正用”是指什么意思？'
        "1.正确地书写汉字":
            jump lesson1_1_q2_c12
        "2.把汉字正过来写":
            jump lesson1_1_q2_c12
        "3.按照汉字的原本的意思来使用":
            jump lesson1_1_q2_c3

label lesson1_1_q2_c3:
    #选择3.按照汉字的原本的意思来使用
    show lihui at middle with dissolve #at LeftToMid
    TeacherTian "正确。“汉字的正用”，也就是严格遵循汉字的本义所使用。例如日语中的“山”读作“yama”，写作“山”。"
    jump lesson1_1_q3

label lesson1_1_q2_c12:
    # 选择 其他选项
    show lihui at middle with dissolve #at LeftToMid
    TeacherTian "上课要认真听讲哦。“汉字的正用”，也就是严格遵循汉字的本义所使用。例如日语中的“山”读作“yama”，写作“山”。"
    jump lesson1_1_q3


label lesson1_1_q3:
    TeacherTian "第三题。"
    show lihui at left with dissolve #at MidToLeft
    menu l1_1_q3:
        '“万叶假名”中的”假指什么意思？'
        "1.假冒":
            jump lesson1_1_q3_c13
        "2.假借":
            jump lesson1_1_q3_c2
        "3.假如":
            jump lesson1_1_q3_c13

label lesson1_1_q3_c2:
    #选择2.假借
    show lihui at middle with dissolve #at LeftToMid
    TeacherTian "正确。“日本人把汉字称为“真名”，“假名”中的“假”就是“假借(汉字)”的意思。“万叶假名”是一种表音文字，借用汉字的读音记录原本日语中的读音。"
    jump lesson1_2

label lesson1_1_q3_c13:
    # 选择 其他选项
    show lihui at middle with dissolve #at LeftToMid
    TeacherTian "上课要认真听讲哦。日本人把汉字称为“真名”，“假名”中的“假”就是“假借(汉字)”的意思。“万叶假名”是一种表音文字，借用汉字的读音记录原本日语中的读音。"

    jump lesson1_2


#####################################################################
# 第一课 假名部分 对话
label lesson1_2:
    TeacherTian "接下来我们讲学习本课的第二个内容，「あ行～か行」的十个假名。"
    # TODO {显示图片 十个假名}
    show lihui at left with dissolve
    show screen HiraKataKANA("a_o","ka_ko", False)
    TeacherTian "请智子同学为我们读一下吧。"
    TeacherTian "智子ちゃん、ちょっと読んでもらえますか。"
    Tomoko "はい。"
    Tomoko "あ、い、う、え、お。\nか、き、く、け、こ。"
    TeacherTian "もう一度お願いします。"
    Tomoko "あ、い、う、え、お。\nか、き、く、け、こ。"
    hide screen HiraKataKANA
    show lihui at middle with dissolve
    TeacherTian "大家可以再练习跟读一下哦。"
    # TODO {显示图片 十个假名 点击可以发音}
    # 点击图片可以确认发音，学习完成以后点击“结束学习”按钮。
    hide lihui
    call screen HiraKataKANA("a_o","ka_ko")
    show lihui at middle with dissolve #at MidToLeft
    TeacherTian "既然大家都会了，我们来做一个小测试吧。根据听到的读音选择正确的假名"

    jump lesson1_2_q1

label lesson1_2_q1:
    TeacherTian "第一题。"
    show lihui at left with dissolve #at MidToLeft
    # TODO {播放SE  u}
    menu l1_2_q1:
        "1.あ":
            jump lesson1_2_q1_c12
        "2.お":
            jump lesson1_2_q1_c12
        "3.う":
            jump lesson1_2_q1_c3

label lesson1_2_q1_c3:
    #选择3.う
    show lihui at middle with dissolve #at LeftToMid
    TeacherTian "正确。"
    jump lesson1_2_q2

label lesson1_2_q1_c12:
    # 选择 其他选项
    show lihui at middle with dissolve #at LeftToMid
    TeacherTian "要仔细听哦。这道题是3.う"
    # TODO {播放SE  u}
    jump lesson1_2_q2


label lesson1_2_q2:
    TeacherTian "第二题。"
    show lihui at left with dissolve #at MidToLeft
    # TODO {播放SE  ki}
    menu l1_2_q2:
        "1.か":
            jump lesson1_2_q2_c13
        "2.き":
            jump lesson1_2_q2_c2
        "3.け":
            jump lesson1_2_q2_c13

label lesson1_2_q2_c13:
    #选择2.き
    show lihui at middle with dissolve #at LeftToMid
    TeacherTian "正确。"
    jump lesson1_2_q3

label lesson1_2_q2_c2:
    # 选择 其他选项
    show lihui at middle with dissolve #at LeftToMid
    TeacherTian "要仔细听哦。这道题是2.き"
    # TODO {播放SE  ki}
    jump lesson1_2_q3


label lesson1_2_q3:
    TeacherTian "第三题。"
    show lihui at left with dissolve #at MidToLeft
    # TODO {播放SE  ko}
    menu l1_2_q3:
        "1.お":
            jump lesson1_2_q3_c12
        "2.か":
            jump lesson1_2_q3_c12
        "3.こ":
            jump lesson1_2_q3_c3

label lesson1_2_q3_c3:
    #选择3.こ
    show lihui at middle with dissolve #at LeftToMid
    TeacherTian "正确。"
    jump lesson1_2_q4

label lesson1_2_q3_c12:
    # 选择 其他选项
    show lihui at middle with dissolve #at LeftToMid
    TeacherTian "要仔细听哦。这道题是3.こ"
    # TODO {播放SE  ko}
    jump lesson1_2_q4


label lesson1_2_q4:
    TeacherTian "第四题。"
    show lihui at left with dissolve #at MidToLeft
    # TODO {播放SE  e}
    menu l1_2_q4:
        "1.く":
            jump lesson1_2_q4_c12
        "2.い":
            jump lesson1_2_q4_c12
        "3.え":
            jump lesson1_2_q4_c3

label lesson1_2_q4_c3:
    #选择3.え
    show lihui at middle with dissolve #at LeftToMid
    TeacherTian "正确。"
    jump lesson1_2_q5

label lesson1_2_q4_c12:
    # 选择 其他选项
    show lihui at middle with dissolve #at LeftToMid
    TeacherTian "要仔细听哦。这道题是3.え"
    # TODO {播放SE  e}
    jump lesson1_2_q5


label lesson1_2_q5:
    TeacherTian "第五题。"
    show lihui at left with dissolve #at MidToLeft
    # TODO {播放SE  ku}
    menu l1_2_q5:
        "1.く":
            jump lesson1_2_q5_c1
        "2.け":
            jump lesson1_2_q5_c23
        "3.お":
            jump lesson1_2_q5_c23

label lesson1_2_q5_c1:
    #选择1.く
    show lihui at middle with dissolve #at LeftToMid
    TeacherTian "正确。"
    jump lesson1_3

label lesson1_2_q5_c23:
    # 选择 其他选项
    show lihui at middle with dissolve #at LeftToMid
    TeacherTian "要仔细听哦。这道题是1.く"
    # TODO {播放SE  ku}
    jump lesson1_3



label lesson1_3:
    TeacherTian "这十个假名大家都已经掌握的不错了，我们来看一下他们可以组成那些单词。"
    TeacherTian "智子ちゃん、こちらの単語を読んでもらえますか。"
    Tomoko "はい。読みます。"
    # TODO {显示图片 单词1}
    Tomoko "愛（あい）"
    # TODO {显示图片 单词2}
    Tomoko "会う（あう）"
    # TODO {显示图片 单词3}
    Tomoko "秋（あき）"
    # TODO {显示图片 单词4}
    Tomoko "聞く（きく）"
    # TODO {显示图片 单词5}
    Tomoko "恋（こい）"
    TeacherTian "大家可以再练习跟读一下哦。"
    # TODO {显示图片1-5  点击可以发音}
    # 点击图片可以确认发音，学习完成以后点击“结束学习”按钮。
    TeacherTian "既然大家都会了，我们来做一个小测试吧。根据听到的读音选择正确的单词"

    jump lesson1_3_q1

label lesson1_3_q1:
    TeacherTian "第一题。"
    show lihui at left with dissolve #at MidToLeft
    # TODO {播放SE  koi}
    menu l1_3_q1:
        "1.秋（あき）":
            jump lesson1_3_q1_c13
        "2.恋（こい）":
            jump lesson1_3_q1_c2
        "3.聞く（きく）":
            jump lesson1_3_q1_c13

label lesson1_3_q1_c2:
    #选择 2.恋（こい）
    show lihui at middle with dissolve #at LeftToMid
    TeacherTian "正确。"
    jump lesson1_3_q2

label lesson1_3_q1_c13:
    # 选择 其他选项
    show lihui at middle with dissolve #at LeftToMid
    TeacherTian "要仔细听哦。这道题是2.恋（こい）"
    # {播放SE  koi}
    jump lesson1_3_q2


label lesson1_3_q2:
    TeacherTian "第二题。"
    show lihui at left with dissolve #at MidToLeft
    # TODO {播放SE  ai}
    menu l1_3_q2:
        "1.愛（あい）":
            jump lesson1_3_q2_c1
        "2.会う（あう）":
            jump lesson1_3_q2_c23
        "3.聞く（きく）":
            jump lesson1_3_q2_c23

label lesson1_3_q2_c1:
    #选择 1.愛（あい）
    show lihui at middle with dissolve #at LeftToMid
    TeacherTian "正确。"
    jump lesson1_3_q3

label lesson1_3_q2_c23:
    # 选择 其他选项
    show lihui at middle with dissolve #at LeftToMid
    TeacherTian "要仔细听哦。这道题是1.愛（あい）"
    # TODO {播放SE  ai}
    jump lesson1_3_q3


label lesson1_3_q3:
    TeacherTian "第三题。"
    show lihui at left with dissolve #at MidToLeft
    # TODO {播放SE  aki}
    menu l1_3_q3:
        "1.恋（こい）":
            jump lesson1_3_q3_13
        "2.秋（あき）":
            jump lesson1_3_q3_2
        "3.会う（あう）":
            jump lesson1_3_q3_13

label lesson1_3_q3_2:
    #选择 2.秋（あき）
    show lihui at middle with dissolve #at LeftToMid
    TeacherTian "正确。"
    jump lesson1_4

label lesson1_3_q3_13:
    # 选择 其他选项
    show lihui at middle with dissolve #at LeftToMid
    TeacherTian "要仔细听哦。这道题是2.秋（あき）"
    # TODO {播放SE  aki}
    jump lesson1_4



#####################################################################
# 第一课 问候语部分  对话
label lesson1_4:
    TeacherTian "前面的内容大家都学的不错，今天正好有机会，请高桥同学来为大家介绍一些日语中的打招呼用语吧。"
    TeacherTian "智子ちゃん、日本語の中での挨拶の言葉を皆さんに紹介してもらえますか。"
    Tomoko "はい。わかりました。私でよければ、紹介します。"
    # TODO {显示图片 1}
    show lihui at left with dissolve
    show l1 picture1 with dissolve:
        zoom 1.2 xalign 0.6 yalign 0.2
    Tomoko "朝の時は「おはよう（o ha yo）」と言います。"
    # TODO {显示图片 2}
    show l1 picture2 with dissolve:
        zoom 1.2 xalign 0.6 yalign 0.2
    Tomoko "昼の時は「こんにちは（kon ni chi wa）」と言います。"
    Tomoko "「こんにちは（kon ni chi wa）」一日中使えます。"
    # TODO {显示图片 3}
    show l1 picture3 with dissolve:
        zoom 1.2 xalign 0.6 yalign 0.2
    Tomoko "夜の時は「こんばんは（kon ban wa）」と言います。"
    # TODO {显示图片 4}
    show l1 picture4 with dissolve:
        zoom 1.2 xalign 0.6 yalign 0.2
    Tomoko "寝る前には「おやすみ（o ya su mi）」と言います。"
    TeacherTian "ありがとうございます。皆さん練習してね。"
    # TODO {显示图片 1-4}
    # 点击图片可以确认发音，学习完成以后点击“结束学习”按钮。
    hide l1
    hide lihui
    call screen L1_Greetings()
    # TODO {播放SE  下课铃声}
    show lihui at middle with dissolve
    TeacherTian "今天学习内容就到此结束了，大家回去好好复习，明天见。"

    return