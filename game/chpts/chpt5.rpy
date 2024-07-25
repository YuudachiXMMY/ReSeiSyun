#第五章
label chpt5_1:
    #{播放bgm0502}
    play music "audio/bgm/b0502.mp3"
    #{显示背景  p05 jiaoshijiu }
    scene p05 jiaoshijiu with dissolve
    #{显示立绘XY 11wx}
    show XY 11wx at middle with dissolve
    ZhouXiaoyu "王浩，日语歌词搞定了没？"
    #{显示立绘WH 11jy}
    show XY at MidToLeft
    show WH 11jy at t_right with dissolve
    me "啊，小雨啊。吓我一跳。写好了，你看这样行不？"
    "昨天晚上小雨突然来让我写日语歌词，结果我忙了一个晚上没睡好觉。"
    "当年读高中的时候没写过歌，工作了以后更是没有这种闲情雅致。这次的穿越让我体验到了很多高中生独有的浪漫。"
    #{显示立绘XY 13cx}
    show XY 13cx
    ZhouXiaoyu "哎哟，还挺靠谱啊。果然是找对人了。"
    #{显示立WH 11my}
    show WH 11my
    me "哈哈哈，只是被你激发了潜能而已。说实话，连我自己都没想到有生之年还能写歌。"
    #{显示立绘XY 12bx}
    show XY 12bx
    ZhouXiaoyu "说什么呢，怎么把自己说得像个老年人一样，你还是个高中生啊。"
    "老年倒还不至于，不过确实已经快要步入中年了……我心里暗想。"
    #{显示立绘WH 12wx}
    show WH 12wx
    me "我都标注好假名了，大家照着假名应该就能唱。"
    #{显示立绘XY 13wx}
    show XY 13wx
    ZhouXiaoyu "哇哦！真是贴心暖男。我和小伙伴们先去音乐教室准备一下，20分钟后你把智子带过来吧。拜托啦！"
    "丢下一句感谢，小雨便匆匆跑出了教室。"
    "十年前，因为小雨的手受了伤，所以大家没有一起为智子举办过什么活动。现在给智子准备的这份惊喜，变成了原来的世界线上没有发生过的事……"

    scene p05 jiaoshijiu with dissolve
    "我按照小雨的安排，带智子去音乐教室。"
    "不知不觉我们已经走到了音乐教室的门口，小雨正在音乐教室里练习自己的原创歌曲。"

    #{播放bgm0503 shinianhou}歌曲强制播放完毕，下面的台词和图片都自动定时播放

    #场景在音乐教室门口
    #{显示背景  p11 yinyue}
    scene p11 yinyue with dissolve
    #{显示立绘XY13wx}
    show XY 13wx at left with dissolve
    play music "audio/bgm/b0503 shinianhou.mp3" fadein 0.5

    # Total 102 seconds
    # $ renpy.pause(102, hard=True)
    $ _skipping = False
    show screen stop_scr

    $ pauseTime = 2.4
    $ blackPauseTime = 0.4

    #{显示立绘ZZ 14xf}
    $ renpy.pause(3.3, hard=True)
    show ZZ 14xf at t_right with dissolve
    Zhizi "綺麗な歌声ですね。（好动听的歌声啊）。{w=3}{nw}"
    "小雨的歌声透过微微开启的大门传了出来。{w=3}{nw}"
    "为了不打扰小雨，智子静静地站在门口示意我不要打扰她。{w=3}{nw}"
    "在这首歌是我们高中时代的种种回忆……{w=3}{nw}"

    scene black_bg with dissolve
    $ renpy.pause(blackPauseTime, hard=True)
    scene huiyi (1) with dissolve
    $ renpy.pause(pauseTime, hard=True)

    scene black_bg with dissolve
    $ renpy.pause(blackPauseTime, hard=True)
    scene huiyi (2) with dissolve
    $ renpy.pause(pauseTime, hard=True)

    scene black_bg with dissolve
    $ renpy.pause(blackPauseTime, hard=True)
    scene huiyi (3) with dissolve
    $ renpy.pause(pauseTime, hard=True)

    scene black_bg with dissolve
    $ renpy.pause(blackPauseTime, hard=True)
    scene huiyi (4) with dissolve
    $ renpy.pause(pauseTime, hard=True)

    scene black_bg with dissolve
    $ renpy.pause(blackPauseTime, hard=True)
    scene huiyi (5) with dissolve
    $ renpy.pause(pauseTime, hard=True)

    scene black_bg with dissolve
    $ renpy.pause(blackPauseTime, hard=True)
    scene huiyi (6) with dissolve
    $ renpy.pause(pauseTime, hard=True)

    scene black_bg with dissolve
    $ renpy.pause(blackPauseTime, hard=True)
    scene huiyi (7) with dissolve
    $ renpy.pause(pauseTime, hard=True)

    scene black_bg with dissolve
    $ renpy.pause(blackPauseTime, hard=True)
    scene huiyi (8) with dissolve
    $ renpy.pause(pauseTime, hard=True)

    scene black_bg with dissolve
    $ renpy.pause(blackPauseTime, hard=True)
    scene huiyi (9) with dissolve
    $ renpy.pause(pauseTime, hard=True)

    scene black_bg with dissolve
    $ renpy.pause(blackPauseTime, hard=True)
    scene huiyi (10) with dissolve
    $ renpy.pause(pauseTime, hard=True)

    scene black_bg with dissolve
    $ renpy.pause(blackPauseTime, hard=True)
    scene huiyi (11) with dissolve
    $ renpy.pause(pauseTime, hard=True)

    scene black_bg with dissolve
    $ renpy.pause(blackPauseTime, hard=True)
    scene huiyi (12) with dissolve
    $ renpy.pause(pauseTime, hard=True)

    scene black_bg with dissolve
    $ renpy.pause(blackPauseTime, hard=True)
    scene huiyi (13) with dissolve
    $ renpy.pause(pauseTime, hard=True)

    scene black_bg with dissolve
    $ renpy.pause(blackPauseTime, hard=True)
    scene huiyi (14) with dissolve
    $ renpy.pause(pauseTime, hard=True)

    scene black_bg with dissolve
    $ renpy.pause(blackPauseTime, hard=True)
    scene huiyi (15) with dissolve
    $ renpy.pause(pauseTime, hard=True)

    scene black_bg with dissolve
    $ renpy.pause(blackPauseTime, hard=True)
    scene huiyi (16) with dissolve
    $ renpy.pause(pauseTime, hard=True)

    scene black_bg with dissolve
    $ renpy.pause(blackPauseTime, hard=True)
    scene huiyi (17) with dissolve
    $ renpy.pause(pauseTime, hard=True)

    scene black_bg with dissolve
    $ renpy.pause(blackPauseTime, hard=True)
    scene huiyi (18) with dissolve
    $ renpy.pause(pauseTime, hard=True)

    scene black_bg with dissolve
    $ renpy.pause(blackPauseTime, hard=True)
    scene huiyi (19) with dissolve
    $ renpy.pause(pauseTime, hard=True)

    scene black_bg with dissolve
    $ renpy.pause(blackPauseTime, hard=True)
    scene huiyi (20) with dissolve
    $ renpy.pause(pauseTime, hard=True)

    scene black_bg with dissolve
    $ renpy.pause(blackPauseTime, hard=True)
    scene huiyi (21) with dissolve
    $ renpy.pause(pauseTime, hard=True)

    scene black_bg with dissolve
    $ renpy.pause(blackPauseTime, hard=True)
    scene huiyi (22) with dissolve
    $ renpy.pause(pauseTime, hard=True)

    scene black_bg with dissolve
    $ renpy.pause(blackPauseTime, hard=True)

    #固定时间显示图片回忆集（之后补），每张图片之间进行切换（渐暗渐明）
    #音乐结束以后可以开始自由操控

    stop music fadeout 1.0
    hide screen stop_scr
    $ _skipping = True

    scene p11 yinyue with dissolve

    #{播放bgm0502}
    play music "audio/bgm/b0502.mp3" fadein 0.5
    #{显示立绘XY 13dx}
    hide ZZ
    show XY 13dx at middle
    with dissolve
    ZhouXiaoyu "智子ちゃん！你已经来了啊。"
    #{显示立绘WH 11rz}
    hide XY
    show WH 11rz at middle
    with dissolve
    me "みんなで感謝の気持ちを込めて、智子ちゃんへの唄を書いたの。（大家为了表达感谢，写了一首歌送给你。）"
    #{显示立绘ZZ 13jy}
    hide WH
    show ZZ 13jy at middle
    with dissolve
    Zhizi "私のために歌を書いてくれたの？（是写给我的歌吗？）"
    #{显示立绘QQ 13xf}
    hide ZZ
    show QQ 13xf at t_right
    with dissolve
    YuanQiaoqiao "谢谢智子这几天给我们带来了那么多的快乐。"
    #{显示立绘ZH 12wn}
    hide ZZ
    show ZH 12wn at left
    with dissolve
    ZhengHui "是啊，能够认识智子同学真的很开心。"
    #{显示立绘LY 13gx}
    hide QQ
    show LY 13gx at right
    with dissolve
    LiuYang "这首歌是小雨亲自作词作曲的原创歌曲哦。"
    #{显示立绘XY 12dx}
    hide ZH
    show XY 12dx at left
    with dissolve
    ZhouXiaoyu "哈哈哈水平有限，日语歌词是王浩写的，希望你能喜欢哦。"
    #{显示立绘ZZ 13xf}
    hide XY
    hide LY
    show ZZ 13xf at middle
    with dissolve
    Zhizi "みんな……ありがとう。私のために歌まで書いてくれて、本当にうれしいです。（谢谢大家，还专门为我写歌，我真的很高兴。）"
    #{显示立绘WH 12wx}
    hide ZZ
    show WH 12wx at middle
    with dissolve
    "这次穿越，真的改变了很多事情。也正是因为有这些改变，才有了这首歌曲。"
    me "原以为高中生活就是无尽的刷题与考试，其实是我忽略了那么多值得回味的快乐。"
    me "谢谢智子让我们真实地感受到了高中生活的意义……"
    #{显示立绘ZZ1xf}
    show WH at MidToRight
    show ZZ 11xf at left with dissolve
    Zhizi "王さんのおかげだよ。本当にありがとう。（这一切多亏了你，谢谢你。）"
    #{显示立绘WH 11my}
    show WH 11my
    me "いえいえ、そんな……（不，不。哪有……）"
    "智子突然向我道谢，仿佛她看透了我的想法，让我不知所措。"

    #{播放bgm0302}
    #{显示立绘TJ 1gx}
    hide WH
    hide ZZ
    show TJ 1gx at middle with dissolve
    TeacherTian "你们怎么还没走啊。我们要出发了哦。"
    #{显示立绘XY 13bx}
    hide TJ
    show XY 13bx at middle
    with dissolve
    ZhouXiaoyu "好的，田老师。马上来。"
    hide XY with dissolve
    "要不是田老师的提醒，差点忘了下午要去七宝老街。"

    scene black_bg with dissolve
    #屏幕渐暗渐明
    #{播放bgm0501}
    play music "audio/bgm/b0501.mp3" fadein 1

    "一行人上了公交车，准备前往七宝老街开展文化体验活动。"

    #{显示背景  p12 gongjiao}
    scene p12 gongjiao with dissolve
    #{显示立绘XY 12zm}
    show XY 12zm at left with dissolve
    ZhouXiaoyu "刘洋，等下我们组去玩什么呀？"
    #{显示立绘LY 12wx}
    show LY 12wx at right with dissolve
    LiuYang "要不还是问问智子吧。"
    #{显示立绘WH 11gx}
    hide LY
    hide XY
    show WH 11gx at middle
    with dissolve
    "对了，我们当年参加文化体验活动的时候干了什么？"
    "记得那时去的也是七宝老街，智子一路上都表现得非常开心。大家一起吃了汤圆，去了七宝塔，还买了一些有中国特色的纪念品……"
    #{显示立绘QQ 11gx}
    hide WH
    show QQ 11gx at left
    with dissolve
    YuanQiaoqiao "当然是买买买啦。"
    #{显示立绘ZH 11zj}
    show ZH 11zj at t_right with dissolve
    ZhengHui "这是文化体验活动，我们可不是来购物的。"
    #{显示立绘QQ 11sq}
    show QQ 11sq
    YuanQiaoqiao "嘁，就你认真。"
    #{显示立绘WH 12jy}
    hide QQ
    hide ZH
    show WH 12jy at middle
    with dissolve
    "话说当年来七宝老街的时候，智子好像说过想去什么地方……。"
    #{显示立绘LY 13wx}
    show WH at MidToRight
    show LY 13wx at left with dissolve
    LiuYang "不如咱们先带智子品尝一下七宝老街的小吃，再带智子逛逛，买一些纪念品留作纪念吧。"
    #{显示立绘WH 11rz}
    show WH 11rz
    me "好啊，边逛边看吧。"
    "大约20几分钟的车程便到老街门口。"

    #{显示背景  p13 laojie}
    scene p13 laojie with dissolve
    "公交车门还没来记得完全打开，一行人便鱼贯而出地走了出去。"
    "七宝老街不愧是上海有名的景点，即使是周五还是有很多游客。和十年前一样，我们一起吃了一些特色小吃，接着开始逛路边的小店。"
    "智子兴奋地看着周围各式各样的店铺，忽然转过头来。"
    #{显示立绘ZZ 13wx}
    show ZZ 13wx at middle with dissolve
    Zhizi "中国の雰囲気が漂っているね。そういえば、この街はどうして「七宝老街」と呼ぶの？（这里非常有中国风情啊。话说，这里为什么叫“七宝老街”呢？）"
    #{显示立绘LY 13qx}
    show ZZ at MidToLeft
    show LY 13qx at right with dissolve
    LiuYang "地元の寺院「七宝寺」に由来していると思うよ。（应该是源于当地的“七宝寺”吧。）"
    #{显示立绘XY 12bx}
    hide LY
    show XY 12bx at t_right
    with dissolve
    ZhouXiaoyu "传说这里有古时候留下来的七件宝物哦。"
    #{显示立绘ZZ 14wx}
    show ZZ 14wx with dissolve
    Zhizi "そうなんだ。確かにここを歩いていると、歴史を感じるね。（原来如此，确实在这里漫步，能感受到历史的气息。）"
    #{显示立绘WH 12my}
    hide XY
    show WH 12my at t_right
    with dissolve
    me "ここには、中国のお土産などを売っているお店もたくさんあるよ。（这里还有很多卖中国特产的小店哦。）"
    #{显示物品 w20}
    hide ZZ
    hide WH
    show w20 at middle
    show ZZ 13jy at t_right
    with dissolve
    "智子的目光落在商店里一个个精美的小盒子上，好奇地停下了脚步。"
    #{显示立绘ZZ 13jy}
    Zhizi "これって、お茶？（这是……茶叶吗？）"
    #{显示立绘QQ 12gx}
    show QQ 12gx at left
    with dissolve
    YuanQiaoqiao "对啊，这是中国的茶叶。"
    #{显示立绘ZZ 14jy}
    show ZZ 14jy at t_right
    Zhizi "なんか日本のお茶とちょっと違う感じがするね。（和日本的茶感觉不太一样呢。）"
    #{显示立绘LY 12rz}
    hide QQ
    show LY 12rz at left
    with dissolve
    LiuYang "実は……（其实……）"
    #{显示立绘XY 12cx}
    hide w20
    hide ZZ
    show XY 12cx at t_right
    with dissolve
    ZhouXiaoyu "咳咳。"
    "刘洋刚要开口，就被小雨打断了。她朝我使了个眼色，暗示我来介绍。"
    "关于中日茶道文化的知识应该在高中课本中学习过，让我想想……"
    #{显示立绘WH 13gx}
    hide XY
    hide LY
    show WH 13gx at middle
    with dissolve
    me "日本でよく飲まれている抹茶は緑茶の一種で、乾燥させた緑茶を擦って粉末にしたものなんだよね。実は抹茶の製法は、中国から伝わったらしいよ。（日本人常喝的抹茶也是绿茶的一种，是把绿茶烘干后磨成粉末制成的。其实抹茶的制作方法也是从中国传入日本的。）"
    #{显示立绘ZZ 12ys}
    show WH at MidToRight
    show ZZ 11jy at left
    with dissolve
    Zhizi "確か、お茶は今から800年ほど前、中国から伝わったって本で読んだことがある。（我在书中读到过，茶好像是在大约800年前从中国传入的。）"
    #{显示立绘WH 12zm}
    show WH 12zm with dissolve
    me "栄西という日本の僧侶が中国に渡ってお茶の種を持ち帰って栽培したのが始まりみたい。（据说是一位叫做荣西的日本僧侣来到中国，把中国的茶叶种子带回了日本，之后日本开始栽培茶树。）"
    #{显示立绘ZZ 14xf}
    show ZZ 14xf with dissolve
    Zhizi "そうなんだ。やっぱり中国ってすごいね。（原来如此，中国真的很厉害啊。）"
    #{显示立绘XY 12dx}
    hide ZZ
    hide WH
    show XY 12dx at middle
    with dissolve
    "小雨朝我笑了笑，比划了一个胜利的手势。真是贴心的助攻。"
    #{显示物品 w21}
    hide XY
    show w21 at middle
    with dissolve
    #{显示立绘QQ 13gx}
    show QQ 13gx at left
    with dissolve
    YuanQiaoqiao "快来看啊，这件汉服好漂亮，智子穿上一定很好看！"
    #{显示立绘ZZ 13wx}
    show ZZ 13wx at t_right
    with dissolve
    Zhizi "かんふくですね。（这是汉服吧。）"
    #{显示立绘LY 13wx}
    hide QQ
    show LY 13wx at left
    with dissolve
    LiuYang "そう。中国の伝統的な服装だよ。（是的，这是中国的传统服饰。）"
    #{显示立绘ZZ 14wx}
    show ZZ 14wx at t_right
    with dissolve
    Zhizi "よく見ると、日本の着物と似てるところがあるね。（仔细一看，和日本的和服有些相似呢。）"
    #{显示立绘ZZ 14sq}
    hide w21
    hide LY
    show ZZ 14sq at middle
    with dissolve
    Zhizi "あ、あそこは？（啊，那里是？）"
    #{显示立绘WH 11rz}
    show ZZ at MidToLeft
    show WH 11rz at t_right with dissolve
    me "何？（什么？）"
    #{显示立绘ZZ 13jy}
    show ZZ 13jy
    Zhizi "ううん。何でもない。（不，没什么。）"
    "朝着刚刚智子所指的地方望去，不远处有一家店，店内挂着一排排各式各样的中国结。"
    #{显示立绘WH 13rz}
    show WH 13rz
    me "どうかしたの（有什么事吗？）"
    #{显示立绘ZZ 14wx}
    show ZZ 14wx
    Zhizi "ううん、大丈夫。（不用了，没事。）"
    "智子低着头小声说道。"
    "看得出智子对那家店铺很感兴趣。但是巧巧正在汉服店里精心挑选着衣服，或许智子担心扫了大家的兴致。"
    #{显示立绘WH 11zm}
    show WH 11zm
    "十年前好像也有过这样的场景。最终因为要和大家一起行动，智子没好意思提，也没有人注意到。"


    #{显示选项  文本框居中，选项竖排1 2}
    menu l5_4_q1:
        "1.行って見る？。":
            $chpt5_answer_kaiwa[0] = 0
            jump l5_4_q1A
        "2.……。":
            $chpt5_answer_kaiwa[0] = 10
            jump l5_4_q1B


label l5_4_q1A:
    if chpt5_C_answer_kaiwa_index < 1:
        $ chpt5_C_answer_kaiwa_index = 1
    #选择1.
    #好感度参数 +10
    #{显示立绘WH 13gx}
    show WH 13gx
    me "あそこ、行ってみる？（要去那里看看吗？）"
    jump chpt5_2

label l5_4_q1B:
    if chpt5_C_answer_kaiwa_index < 1:
        $ chpt5_C_answer_kaiwa_index = 1
    #选择2.
    me "……。虽然会耽误大家的行程，还是带智子去看看吧。"
    me "あそこ、行ってみる？（要去那里看看吗？）"
    jump chpt5_2

label chpt5_2:
    #{显示立绘ZZ 13wx}
    show ZZ 13wx
    Zhizi "ええ。いいの。（啊，可以吗？）"
    #{显示立绘WH 12rz}
    show WH 12rz
    me "巧巧，小雨，我带智子去对面的店看看哦。"
    #{显示立绘XY 11bx}
    hide ZZ
    show XY 11bx at left
    with dissolve
    ZhouXiaoyu "哇哦，王浩什么时候变得这么主动了。"
    #{显示立绘WH 11ng}
    show WH 11ng
    me "别取笑我了，智子有想看的东西。"
    hide WH
    hide XY
    with dissolve
    "说罢，我便带着智子来到了那家小店的门口。"
    #{显示立绘ZZ 11wx}
    show ZZ 11wx at left with dissolve
    Zhizi "気を使ってくれて、ありがとう。（不好意思，让你费心了。）"
    #{显示立绘WH 11gx}
    show WH 11gx at t_right with dissolve
    me "ぜんぜん気にしないで。いつも智子ちゃんに助けてもらってるし。（别介意。而且平时是你一直在帮助我。）"
    "智子脸上露出了灿烂的笑容。"
    "一直为他人着想、为他人考虑的性格，或许让智子少了很多她这个年龄的女孩应该有的自由和快乐。"

    #{播放bgm0301}
    play music "audio/bgm/b0301.mp3"
    hide WH
    hide ZZ
    show dianzhu at middle
    with dissolve
    "店主" "这位小哥，给女朋友买个中国结吧，讨个口彩。"
    #{显示立绘WH 11jy}
    hide dianzhu
    show WH 11jy at middle
    with dissolve
    me "不，不是女朋友啦。这位是日本来的朋友。"
    hide WH
    show dianzhu at middle
    with dissolve
    "店主" "哎哟，还是个日本女孩子，看你们挺般配啊。"
    "被店主这么一说，我有些手足无措。"
    #{显示立绘ZZ 11jy}
    hide dianzhu
    show ZZ 11jy at middle
    with dissolve
    Zhizi "え、何？（啊，什么？）"
    "看到我和店主攀谈起来，智子很好奇我们在说些什么。"
    #{显示立绘WH 11rz}
    show ZZ at MidToLeft
    show WH 11rz at t_right with dissolve
    me "あ、今日はいい天気ですねって。（啊，他说今天的天气很好……）"
    "刚刚的话自然不好意思翻译给智子听，我便撒了个小谎。"
    hide WH
    hide ZZ
    show dianzhu at middle
    with dissolve
    "店主" "ちゅうごくむすび、かわいい。どうぞ、どうぞ。（中国结，可爱。请，请。）"
    #{显示立绘ZZ 14wx}
    hide dianzhu
    show ZZ 14wx at middle
    with dissolve
    Zhizi "あ、ありがとうございます。（谢，谢谢。）"
    "店主突然用日语大声吆喝起来，我也着实吃了一惊。"
    "虽然是半吊子的日语，却充满了感染力。他一边说着卡哇伊，一边从架子上取下一个中国结，塞到智子手里。也不知道他是在夸中国结可爱，还是在夸智子。"
    #{显示立绘WH 13jy}
    hide ZZ
    show WH 13jy at middle
    with dissolve
    me "老板，你还会说日语啊，厉害厉害。"
    hide WH
    show dianzhu at middle
    with dissolve
    "店主" "这有啥，现在日本客人多。听多了也就能说一些。"
    #{显示立绘ZZ 13wx}
    hide dianzhu
    show ZZ 13wx at left
    #{显示物品 w22}
    show w22 at middle
    with dissolve
    Zhizi "とてもかわいい飾りですね。これにはどんな意味が込められているの？（好可爱的吊饰。这个吊饰有什么含义吗？）"
    #{显示立绘WH 12gx}
    show WH 12gx at t_right with dissolve
    me "「中国結び」といって、古くから伝わったものみたいだけど……（这个叫做“中国结”，好像是从古代流传下来的……）"
    "说到这里，突然卡壳了。我才意识到，虽然经常看到中国结这个饰品，但我从来没想过它的由来和意义。"
    hide w22
    hide ZZ
    hide WH
    show dianzhu at middle
    with dissolve
    "店主" "嘿嘿，中国结的由来你们不知道了吧。其实早在远古时代，人们为了不遗忘事情，就用结绳的方式来记录。小事则小结其绳，大事便大结其绳。"
    #{显示立绘ZZ 11jy}
    show dianzhu at MidToLeft
    show ZZ 11jy at t_right with dissolve
    Zhizi "大事なことを忘れないために糸で「結ぶ」のですね。（原来是为了不忘记重要的事情，而用绳子打结啊。）"
    "店主" "正是如此。随着历史演变，后来结也被用来表达人的感情，例如男女之间的情思。"
    #{显示立绘ZZ 11gx}
    show ZZ 11gx
    Zhizi "なるほど。日本には「縁を結ぶ」という言葉がありますが、そこから由来しているのかもしれませんね。（原来如此，日语中也有“结缘”这样的说法，或许就是从这里来的呢。）"
    "智子认真欣赏着手中的红色中国结，我突然意识到好像在哪里看到过……"
    #{显示立绘WH 12jy}
    hide ZZ
    hide dianzhu
    # hide w22
    show WH 12jy at middle
    with dissolve
    "啊，就是挂在那把钥匙上的中国结！"
    "打开回忆大门的钥匙上的中国结为什么会出现在这里？或许这是冥冥中注定的？它是不是也能帮我回到现实呢？"
    "看到智子如此喜欢这个中国结，我便转向店主。"
    #{显示立绘WH 13kx}
    show WH 13kx
    me "老板，这个中国结多少钱？"
    show WH at MidToRight
    show dianzhu at left with dissolve
    "店主" "哈哈哈，我跟你们这么投缘，又是日本客人。就送给你们吧，记得以后给我介绍点生意哦。"
    #{显示立绘WH 13jy}
    show WH 13jy
    me "这，这怎么好意思……"
    me "プレゼントしてくれるって。（他说送给你。）"
    #{显示立绘ZZ1jy}
    show WH at MidToRight
    hide dianzhu
    show ZZ 11jy at left with dissolve
    Zhizi "え、いいんですか。すみません、ありがとうございます。（啊，可以吗？真不好意思，谢谢！）"
    "智子脸微微发红，很高兴地收下了这份礼物。"

    #{播放bgm0504}
    play music "audio/bgm/b0504.mp3"
    #{显示立绘XY 11jy}
    hide WH
    hide ZZ
    show XY 11jy at middle
    with dissolve
    ZhouXiaoyu "王浩，你们还在这里啊。"
    #{显示立绘WH 11jy}
    show XY at MidToLeft
    show WH 11jy at t_right with dissolve
    "小雨从背后走来，拍了一下我的右肩。我这才意识到我们在店里待了挺长时间。抬头望去，夕阳映红了老街上的店铺招牌。"
    #{显示立绘XY 12wx}
    show XY 12wx
    ZhouXiaoyu "智子ちゃん、这盒茶叶是送你的礼物。"
    #{显示立绘ZZ 14gx}
    hide WH
    show ZZ 14gx at t_right
    with dissolve
    Zhizi "ありがとう。本当にもらっていいの？（谢谢，我真的可以收下吗？）"
    #{显示立绘QQ 11gx}
    hide XY
    hide ZZ
    show QQ 11gx at left
    with dissolve
    YuanQiaoqiao "快看我们买了什么。"
    show w21 at middle with dissolve
    "巧巧也从旁边蹿了出来，举起了一件红白相间的汉服。"
    #{显示物品 w21}
    #{显示立绘ZH 11gx}
    show ZH 11gx at t_right
    with dissolve
    ZhengHui "巧巧给智子挑了一套汉服。她可是把自己的零花钱都贡献出来了。"
    #{显示立绘LY 13wx}
    hide ZH
    show LY 13wx at right
    with dissolve
    LiuYang "怪不得之前巧巧在跳蚤市场要把画给卖了呢，原来是要给智子买礼物啊。"
    #{显示立绘QQ 11tq}
    hide w21
    show QQ 11tq at left
    with dissolve
    YuanQiaoqiao "说好了，一半算你出资的，以后要连本带利还哦。"
    #{显示立绘WH 12wx}
    hide QQ
    hide LY
    show WH 12wx at middle
    with dissolve
    me "一向省吃俭用的巧巧这次倒是挺大方。不过想想十年以后郑辉将要被她狠狠地敲一回竹杠，我不由地偷笑……"
    #{显示立绘ZZ 14gx}
    hide WH
    show ZZ 14gx at left
    with dissolve
    Zhizi "こんな素敵なもの。申し訳ないよ。（这么漂亮的礼物，实在不好意思。）"
    #{显示立绘WH 11my}
    show WH 11my at t_right with dissolve
    me "みんなの気持ちだから、受け取って。（这是大家的一片心意，收下吧。）"
    #{显示立绘ZZ 11xf}
    show ZZ 11xf
    Zhizi "みんな、本当にありがとう。とても嬉しいです。（真的非常感谢大家。我太高兴了。）"
    #{显示立绘ZH 12zj}
    hide ZZ
    hide WH
    show ZH 12zj at t_right
    with dissolve
    ZhengHui "对了，刚刚听到田老师在召集大家集合，我们是不是要回学校啦。"
    #{显示立绘XY 13dy}
    show XY 13dy at left with dissolve
    ZhouXiaoyu "确实，天都快黑了，我们去大门口集合吧。"
    "突然，智子好像想到了什么，露出抱歉的表情。"
    #{显示立绘ZZ 13ys}
    hide XY
    hide ZH
    show ZZ 13ys at middle
    with dissolve
    Zhizi "ごめん、ちょっと寄ってみたいところがあるから、みんな先に行ってて。（不好意思，我想去个地方，大家先走吧。）"
    #{显示立绘WH 11rz}
    show ZZ at MidToLeft
    show WH 11rz at t_right with dissolve
    me "大丈夫？一緒に行こうか。（没事吧？需要我陪你去吗？）"
    #{显示立绘ZZ 11ys}
    show ZZ 11ys
    Zhizi "ううん。大丈夫だよ。心配しないで。（没事，不用担心。）"

    #{停止播放bgm}
    stop music
    #{显示背景  p12 gongjiao}
    scene p12 gongjiao with dissolve
    "过了10分钟左右，智子和我们汇合，一起上了公交车准备回学校。"
    "回学校的路上，大家有说有笑。但是大家心里都知道，智子明天就要回国了，这一别不知道何时才能再见。"
    #{播放bgm0505}
    play music "audio/bgm/b0505.mp3" fadein 0.5
    "智子一言不发，静静地望着窗外，若有所思。"
    #{显示立绘WH 11ng}
    show WH 11ng at middle with dissolve
    me "智子ちゃん？（智子？）"
    #{显示立绘ZZ 13ys}
    show WH at MidToRight
    show ZZ 13ys at left with dissolve
    Zhizi "あ、ごめん。ちょっと考え事をしてた。明日になったら、みんなに会えなくなっちゃうの、寂しいなあ。（不好意思，刚刚走神了。明天就见不到大家了，好寂寞。）"
    #{显示立绘XY 13dy}
    hide WH
    show XY 13dy at t_right
    with dissolve
    ZhouXiaoyu "没事的，我们会去日本看你的。"
    #{显示立绘QQ 13xf}
    hide XY
    show QQ 13xf at t_right
    with dissolve
    YuanQiaoqiao "对呀，明年不就有夏令营活动吗？我们一定报名参加。"
    "智子的中国之旅即将结束，而我的人生旅程又将何去何从呢……"
    "高中生们对未来的梦想让我的心中也泛起了波澜。或许我的人生也能有所改变……"
    #{显示立绘ZZ 14xf}
    show ZZ 14xf
    Zhizi "うん、楽しみにしてるね。日本でまた一緒に遊ぼう。（我很期待大家来日本，我们再一起玩吧。）"
    #{显示立绘ZZ 14wx}
    show ZZ 14wx
    Zhizi "王さんも来てくれる？（王浩你也会来吗？）"

    #{显示选项  文本框居中，选项竖排1 2}
    menu l5_4_q2:
        "1.それは……まだ分からない。":
            $chpt5_answer_kaiwa[1] = 0
            jump l5_4_q5A
        "2.うん、必ず会いに行くよ。":
            $chpt5_answer_kaiwa[1] = 10
            jump l5_4_q2B


label l5_4_q2B:
    if chpt5_C_answer_kaiwa_index < 2:
        $ chpt5_C_answer_kaiwa_index = 2
    #选择2.
    #好感度参数 +10
    #{显示立绘WH 13gx}
    hide QQ
    hide ZZ
    show WH 13gx at middle
    with dissolve
    me "うん、必ず会いに行くよ。（嗯，我一定会去见你的。）"
    jump chpt5_3

label l5_4_q5A:
    if chpt5_C_answer_kaiwa_index < 2:
        $ chpt5_C_answer_kaiwa_index = 2
    #选择1.
    "虽然当年我没有参加那个夏令营活动，但如果还有一次机会的话……"
    hide QQ
    hide ZZ
    show WH 13gx at middle
    with dissolve
    me "うん、必ず会いに行くよ。（嗯，我一定会去见你的。）"
    jump chpt5_3

label chpt5_3:
    #{显示立绘XY 11bx}
    hide WH
    show XY 11bx at middle
    with dissolve
    ZhouXiaoyu "哈哈哈，这句我听懂了。好像是电影里的告白台词嘛。"
    #{显示立绘WH 11rz}
    hide XY
    show WH 11rz at middle
    with dissolve
    "小雨的这句话点醒了我。这次穿越回来圆了很多梦，但是我最终还是没有勇气告白。"
    "当年可能是觉得自己不够优秀，会被智子拒绝。而现在却有了更多复杂的感情。我希望智子能够完成她自己的梦想，我的存在或许会成为她成功路上的绊脚石……"
    "是否没有我的存在，她反而会有更幸福的人生呢……"
    #{显示立绘WH 11jy}
    show WH 11jy
    me "智子ちゃんの夢はアナウンサーになることだよね。（智子你的梦想是做电视台主持人对吧。）"
    #{显示立绘ZZ 11gx}
    show WH at MidToRight
    show ZZ 11gx at left with dissolve
    Zhizi "うん。中国の素晴らしいところを、もっと日本人に伝えたい。（是的，我想向日本人传递更多中国的精彩故事。）"
    #{显示立绘ZZ 11wx}
    show ZZ 11wx
    Zhizi "それに、もう一つ……あ、それはまだ言えないかなあ。（另外，还有一个原因……那个现在还不能说。）"
    "讲到关键之处，智子却欲言又止。"
    #{显示立绘XY 11zm}
    hide WH
    show XY 11zm at t_right
    with dissolve
    ZhouXiaoyu "哈哈哈，智子怎么说话也神神秘秘的。"
    #{显示立绘QQ 12tq}
    hide XY
    show QQ 12tq at t_right
    with dissolve
    YuanQiaoqiao "对了，要不我们定一个十年之约吧？"
    #{显示立绘ZZ 14gx}
    show ZZ 14gx
    Zhizi "十年後の約束？とてもいい響きね。（十年后的约定？听上去很不错。）"
    Zhizi "みんな自分の願いを書いて、再会した時に一緒に打ち明けるっていうのはどうかな。（大家把自己的心愿写在纸上，再会的时候各自说出自己的心愿怎么样？）"
    #{显示立绘XY 12wx}
    hide QQ
    show XY 12wx at t_right
    with dissolve
    ZhouXiaoyu "哇，这个提议很棒! "
    #{显示立绘ZZ 13wx}
    show ZZ 13wx
    Zhizi "紙とペンがあるから、使って。（我这里有纸和笔，大家可以用。）"
    #{显示立绘LY 11hz}
    hide ZZ
    hide XY
    show LY 11hz at right
    with dissolve
    LiuYang "有点时光宝盒的感觉，真有意思啊。"
    #{显示立绘ZH 11wn}
    show ZH 11wn at left
    with dissolve
    ZhengHui "哪里去找个盒子呢？"
    #{显示立绘ZZ 14wx}
    hide LY
    show ZZ 14wx at t_right
    with dissolve
    Zhizi "これ、使ってもいいかなあ。とてもきれいな箱だけど。（用这个可以吗？虽然这个盒子这么漂亮，有点可惜。）"
    #{显示物品w20}
    hide ZH
    show w20 at middle
    with dissolve
    "智子指着刚刚收到的礼物——茶叶，取出里面的茶叶罐，放在大家面前。"
    #{显示立绘XY 13dx}
    show XY 13dx at left
    with dissolve
    ZhouXiaoyu "当然可以啊。"
    #{显示立绘ZZ 13wx}
    show ZZ 13wx
    Zhizi "じゃあ、決まりね。（好，那就这么定了。）"
    #{显示立绘QQ 11wx}
    hide w20
    hide XY
    show QQ 11wx at left
    with dissolve
    YuanQiaoqiao "可是，我们要把它藏在什么地方呢？"
    #{显示立绘LY 12hz}
    hide ZZ
    show LY 12hz at right
    with dissolve
    LiuYang "我们学校不是有棵大树吗？埋在树下怎么样？"
    #{显示立绘XY 11dy}
    hide QQ
    show XY 11dy at left
    with dissolve
    ZhouXiaoyu "不行，不行，万一我们埋的时候不小心破坏了树根怎么办？而且埋在土里，这个盒子恐怕会腐烂吧。"
    #{显示立绘WH 12rz}
    hide XY
    hide LY
    show WH 12rz at middle
    with dissolve
    "怪不得之前觉得这个盒子有些眼熟，原来是当年的月光宝盒啊。藏的地方我自然是知道的……"
    me "不如我们放在教室的书架后面吧。那里好像有个不用工具箱。"
    #{显示立绘ZH 11wx}
    hide WH
    show ZH 11wx at t_right
    with dissolve
    ZhengHui "对，这个主意好。钥匙一直由我保管着，重新装修后那个工具箱就闲置了。"
    #{显示立绘XY 12wx}
    show XY 12wx at left
    with dissolve
    ZhouXiaoyu "行，那等一下回学校以后，我们一起回一趟教室吧。"
    #{显示立绘LY 12jy}
    hide ZH
    show LY 12jy at right
    with dissolve
    LiuYang "田老师不是说在校门口解散吗？"
    #{显示立绘XY 13cx}
    hide XY
    show XY 13cx at left
    with dissolve
    ZhouXiaoyu "真是死脑筋。交给我吧，嘿嘿。"

    #{停止播放bgm}
    stop music
    #{显示背景  p14 xiaomen}
    scene black_bg with Dissolve(2.5)
    # scene white_bg with Dissolve(1.5)
    scene p14 xiaomen with dissolve
    "没过多久，校车在校门口停下了。"
    #{显示立绘TJ 1gx}
    show TJ 1gx at middle with dissolve
    TeacherTian "同学们，感谢大家参与今天的活动。请大家回家注意安全，也祝福智子同学明天回国的旅途一路顺利哦。"
    #{显示立绘ZZ 13wx}
    show TJ at MidToLeft
    show ZZ 13wx at t_right with dissolve
    Zhizi "田先生、いろいろご親切にしていただき、本当にありがとうございました。（田老师，您一直对我照顾有加，真的非常感谢。）"
    #{显示立绘XY 12wx}
    hide ZZ
    show XY 12wx at t_right
    with dissolve
    ZhouXiaoyu "啊，田老师，我们小组想送智子一个小礼物，忘在教室里了。我们能回去拿一下吗？"
    #{显示立绘TJ 1jy}
    show TJ 1jy
    TeacherTian "哦，这样啊。好吧，别回家太晚了哦。王浩，你要照顾好大家哦。"
    "田老师突然看向我，给我使了个眼色。我感觉到背脊一阵凉意，好像所有事情都被她看透了一般……"
    #{显示立绘WH12ky}
    hide TJ
    hide XY
    show WH 12kx at middle with dissolve
    me "哦，好的。"
    "确实，高中生的这些小把戏，哪有老师看不出来的，老师们只是睁一只眼闭一只眼而已……"

    #{显示背景  p15 wanshang}
    scene p15 wanshang with dissolve
    #{播放bgm0506}
    play music "audio/bgm/b0506.mp3"
    "我们几个回到了教室，小雨得意地看了看刘洋。"
    #{显示立绘XY 12cx}
    show XY 12cx at middle with dissolve
    ZhouXiaoyu "嘻嘻，这不就搞定了嘛。大家赶快写吧。"
    hide XY with dissolve
    "小雨果然有做班长的天赋。和老师同学都能相处融洽，也懂得变通。"
    "大家从智子手里接过彩纸，便开始写下自己的心愿。"
    "大家在写的时候遮遮挡挡，还不时抬起头来若有所思。"
    "十年来，大家都没有放弃自己的梦想，并通过努力不断成就自己的梦想。"
    "不知道智子写的心愿是什么。面对这第二次机会，我又应该写什么呢……"
    #{显示立绘XY 12dy}
    show XY 12dy at middle with dissolve
    ZhouXiaoyu "王浩，你写好了没？就差你的了。"
    #{显示立绘WH 11wx}
    hide XY
    show WH 11wx at middle
    with dissolve
    me "哦，好了好了。"
    "我慌忙把写好的纸条放进盒子里，智子盖上了盖子。"
    "刘洋和郑辉对视一眼，合力推开了书架。郑辉用钥匙打开盖板，智子将时光宝盒郑重地放在里面。"
    #{显示立绘ZH 11zj}
    hide WH
    show ZH 11zj at t_right
    with dissolve
    ZhengHui "我们这样随便占用教室里的东西不太好吧……"
    #{显示立绘QQ 13sq}
    show QQ 13sq at left with dissolve
    YuanQiaoqiao "胆小鬼，怕什么。期待我们十年后再回到这里探宝吧。嘻嘻。"
    "虽说是闲置的工具箱，但随便占用确实不太妥当。而且总觉得哪里怪怪的……"
    #{显示立绘WH 11rz}
    hide QQ
    hide ZH
    show WH 11rz at t_right
    with dissolve
    me "いや、ちょっと待って。（不对，稍等一下。）"
    #{显示立绘ZZ 13ys}
    show ZZ 13ys at left
    with dissolve
    Zhizi "どうしたの？（怎么了？）"
    #{显示物品 w20}
    hide ZZ
    show w20 at wleft
    #{显示立绘WH 11jy}
    show WH 11jy
    with dissolve
    "我十年后看到的时光宝盒，明明是使用密码锁的。但现在用的是茶叶罐，并没有密码锁。"
    "而且，外观上好像也有一些差异，这到底是怎么回事？"
    "怎么回事？难道不是穿越而是平行时空？还是说只是我想多了而已？"
    #{显示立绘LY 11jy}
    hide w20
    show LY 11jy at left
    with dissolve
    LiuYang "王浩，没事吧？怎么看你一脸紧张的样子。"
    #{显示立绘WH 13zm}
    show WH 13zm
    me "我……没……没事。"
    #{显示立绘XY 12wx}
    hide WH
    hide LY
    show XY 12wx at left
    with dissolve
    ZhouXiaoyu "那钥匙就交给智子吧。"
    #{显示立绘ZZ 13gx}
    show ZZ 13gx at t_right
    with dissolve
    Zhizi "分かった。とりあえず預かっておくね。（好的，那就由我负责保管吧。）"
    #{显示物品 w02}
    hide XY
    show w02 at wleft
    with dissolve
    "智子很认真地在钥匙上系上了中国结，微笑着挥了挥。"
    "窗外的月光映照在智子的脸上，格外皎洁。"
    "我看到眼前的画面，脱口而出……"
    #{显示立绘WH 12wx}
    hide w02
    hide ZZ
    show WH 12wx at middle
    with dissolve
    me "今夜は月が綺麗ですね。（今天的月亮真美啊。）"
    #{显示立绘ZZ 14jy}
    hide WH
    show ZZ 14jy at middle
    with dissolve
    Zhizi "え？答え分かったの（咦？你知道了（夏目漱石）所说的答案了吗？）"
    "智子露出惊讶的表情，脸颊微微红起来……"
    "就在此时……"

    # {停止播放bgm}
    stop music
    hide ZZ with vpunch
    "保安" "谁啊，还在教室里？"
    "保安的一声大喊打破了平静。"
    #{显示立绘XY 13zm}
    show XY 13zm at left with dissolve
    ZhouXiaoyu "糟糕！被保安叔叔发现了。"
    #{显示立绘ZH 12zj}
    show ZH 12zj at t_right with dissolve
    ZhengHui "快跑！"
    "随着郑辉的一声大喊，大家一股脑地向教室门口冲去。"
    #{显示立绘WH 12zm}
    hide ZH
    hide XY
    show WH 13zm at middle
    with dissolve
    "不知怎么的，我的心底蓦然生出一丝不安。好像直觉在催促着我，告诉我周围的一切很快就要消失……"
    "我下意识地牵起智子的手，向教室外面跑去……"
    "回忆起这几天发生的故事，想起初次见面时微笑的智子，想起和大家一起参加社团活动的体验，想起在老街度过的时光……或许这一切都只是一场梦吧。"
    "但是，现在智子就在我的身后，那么真实。即将冲出教室后门的那一刻，我不禁回头看了一眼，没注意到前方…… "
    #{显示立绘QQ 13jy}
    hide WH
    show QQ 13jy at middle with vpunch
    YuanQiaoqiao "啊！"

    #{播放bgm0507}
    play music "audio/bgm/b0507.mp3"
    #黑屏
    scene black_bg with Dissolve(2)
    "在黑暗中，我轻轻握住智子的手，一束光线照亮了智子的面孔。她在微笑，眼神闪烁，似乎在说着什么，但又听不见，最终白光吞噬了一切。"

    "再次睁开眼睛，看到模糊的天花板。揉了揉眼睛，才发现眼里似乎有泪水。耳边听到呼喊着我名字的声音。"
    #{显示立绘LY 21rz}
    show LY 21rz at middle with dissolve
    LiuYang "王浩，王浩！"

    #{显示背景  p05 jiaoshixin2 }
    scene p05 jiaoshixin2 with Dissolve(2)
    #{显示立绘ZH 21gg}
    show ZH 21gg at middle with dissolve
    ZhengHui "王浩！你可算醒了。"
    #{显示立绘XY 23zm}
    hide ZH
    show XY 23zm at middle
    with dissolve
    ZhouXiaoyu "你把我们都给吓坏了，刘洋差点要叫救护车了。"
    #{显示立绘QQ 22jy}
    hide XY
    show QQ 22jy at middle
    with dissolve
    YuanQiaoqiao "对不起啊，我不该来和你抢。"
    hide QQ
    with dissolve
    "一脸委屈的巧巧和大家围在我身边。"
    "然而，这里已经不是十年前的教室了。"
    "周围的人七嘴八舌把刚才发生的事情讲了一遍。原来刚才巧巧追着来抢我手中的彩纸，我因躲避不及被撞倒在地上，昏了过去……"
    "阴差阳错，我又回到了十年后的教室。"
    #{显示立绘XY 21zm}
    show XY 21zm at left with dissolve
    ZhouXiaoyu "没事吧，王浩？你怎么不说话啊？"
    #{显示立绘WH 21zm}
    show WH 21zm at t_right with dissolve
    me "啊，我没事。"
    hide WH
    hide XY
    with dissolve
    "终于……"
    "还是回来了……"
    "之前所有的体验难道都是梦吗？但一切为何如此真实？"

    #{显示立绘XY 22wx}
    show XY 22wx at middle with dissolve
    ZhouXiaoyu "智子还没来，她的心愿我们就先别看了。"
    ZhouXiaoyu "王浩，你的心愿是什么呀？和大家说说呗。"
    #{显示立绘WH 21wx}
    hide XY
    show WH 21wx at middle
    with dissolve
    me "我的心愿？"
    "被周小雨冷不丁地一问，我才意识到自己手里捏着两张纸条。一张是智子的，还有一张是我自己的。"
    "当年的自己到底写了什么？我已经记不得了，或许是没有勇气去回忆……"
    #{显示立绘LY 22wx}
    hide WH
    show LY 22wx at middle with dissolve
    LiuYang "哎呀，都快要而立之年了，怎么还扭扭捏捏的。"
    "刘洋也跟着起哄……"
    hide LY
    #{显示立绘WH 22gx}
    show WH 22gx at middle
    with dissolve
    me "你自己的事和小雨说了吗？"
    "我有些赌气地反问刘洋。"
    #{显示立绘LY 22rz}
    hide WH
    show LY 22rz at middle
    with dissolve
    LiuYang "我，我的什么事？"
    #{显示立绘XY 21jy}
    show LY at MidToRight
    show XY 21jy at left with dissolve
    "小雨略带疑惑地看了一眼我和刘洋。"
    #{显示立绘WH 22rz}
    hide LY
    hide XY
    show WH 22rz at middle
    with dissolve
    me "哎，都过去10年了，你还没抓住机会啊。"
    me "「彼女に本当の気持ちを伝える」でしょ。（你不是说‘要告诉她自己的心意’吗？）"
    #停止播放bgm
    stop music fadeout 1.0
    #{显示立绘LY 23rz}
    hide WH
    show LY 23rz at middle
    with dissolve
    "刘洋看了看小雨，一言不发，涨红了脸。手里捏着当年写下的心愿。"
    "刘洋的心愿里写的那个喜欢的女孩，正是眼前的周小雨。而经过方才的记忆之旅，我也知晓了周小雨的心意。只是他们中必须有一个人先迈出一步才行。"
    LiuYang "那个，小雨……你有男朋友了吗？"
    #{显示立绘XY 23zm}
    show LY at MidToRight
    show XY 23zm at left with dissolve
    ZhouXiaoyu "啊？"
    #{显示立绘LY 21rz}
    show LY 21rz
    LiuYang "你愿意做我女朋友吗？"
    "周小雨一脸不可置信，表情中夹杂了欣喜和责怪。"
    #{显示立绘XY 23zm}
    show XY 23zm
    ZhouXiaoyu "你，你这个人表白怎么也不挑个好点的时候。"
    #{显示立绘LY 21qx}
    show LY 21qx
    LiuYang "好时候是什么时候啊……"
    #{播放bgm0502}
    play music "audio/bgm/b0502.mp3" fadein 0.5
    #{显示立绘XY 22dx}
    show XY 22dx
    ZhouXiaoyu "哈哈哈。好吧好吧。那先给你一年见习期，好好表现哦。"
    #{显示立绘LY 22qx}
    show LY 22qx
    LiuYang "啊？我又不是当老师，还有见习期啊。"
    YuanQiaoqiao "哈哈哈哈……"
    hide XY
    hide LY
    with dissolve
    "刘洋这句话让在场的众人笑作一团，同时也为他们感到由衷的高兴。"
    "其他几个人还在兴致勃勃地互相调侃的时候，我瞥了一眼手中的彩纸条。"
    #{显示立绘WH 22rz}
    show WH 22rz at middle
    with dissolve
    "希望大家都能实现自己的梦想。——这是我当年在心愿纸上写下的愿望。"
    "原来，我的梦想也实现了……"
    "十年后的今天，巧巧穿上了自己设计的服装，成了一名玩cosplay的声优，郑辉做的日语学习游戏已经正式上线，小雨回母校做了一名音乐老师，刘洋也终于传递了自己真实心意，还有智子……"
    "她还会回来吗……"
    "门卫" "这里有同学叫王浩的吗？刚刚有人送来一封信。"
    #{显示立绘WH 21zm}
    show WH 21zm
    me "我，我是王浩。"
    "门卫的话让众人吃了一惊，怎么现在会有人把我的信寄到学校？"
    "这封信的信封已有些泛黄，背面落款处写的日期是2012年9月7日。"
    #{显示立绘XY 23zm}
    show WH at MidToRight
    show XY 23zm at left with dissolve
    ZhouXiaoyu "是谁寄来的啊？"
    "落款处清晰地写着「高橋　智子」。 "
    #{显示立绘WH 22zm}
    show WH 22zm
    me "是智子寄来的信。不，准确地说是十年前的智子寄来的信。"
    #{显示立绘QQ 23jy}
    hide XY
    show QQ 23jy at left
    with dissolve
    YuanQiaoqiao "十年前的信怎么会现在才寄到？"
    hide QQ
    hide WH
    with dissolve
    "9月7日，这天正好是大家一起去七宝老街的时候。那时候……"
    #{显示立绘WH 23zm}
    show WH 23zm at middle with dissolve
    me "哦，我明白了……"
    #{显示立绘ZH 22zj}
    show WH at MidToRight
    show ZH 22zj at left with dissolve
    ZhengHui "你明白什么了？"
    "那天智子在上车前去的地方是七宝老街的时光信件铺。只要把信交给店家，店家便会按照约定的时间来寄送。"
    #{显示立绘WH 21zm}
    show WH 21zm
    me "没什么……"
    hide WH
    hide ZH
    with dissolve
    "那么久以前的事情想必大家早已不记得了。现在更令我在意的是，智子到底在这封信里写了什么。"
    "我小心地打开尘封已久的信，里面有两张不同颜色的信纸。"

    #{播放bgm0508}
    play music "audio/bgm/b0508.mp3"

    #{显示物品 w23}
    show w23 at middle with dissolve
    #播放朗读以下内容的音频，中间不能打断
    Zhizi "（第一封信……）"

    $ _skipping = False
    show screen disable_Lmouse()

    "{cps=8}皆さんへ{/cps}{p=2}{nw}"
    "{cps=8}{space=25}一週間の短期留学の間、本当にお世話になりました。{/cps}{p=2}{nw}"

    "{cps=8}{space=40}初めての留学で、最初はちょっと不安でしたが、\n
    皆が優しくしてくれたおかげで、すぐに馴染むことができました。{/cps}{p=2}{nw}"

    "{cps=8}{space=35}一緒に勉強したり、遊びに行ったりして最高の思い出ができました。\n
    {space=30}本当にありがとうございました。この経験は一生忘れません。{/cps}{p=2}{nw}"

    "{cps=8}{space=25}いつか必ずまたどこかで会いましょう。\n \n
    {space=430}高橋智子{/cps}{p=2}{nw}"

    $ _skipping = True
    hide screen disable_Lmouse


    #{显示物品 w24}
    hide w23
    show w24 at middle
    with dissolve

    #播放朗读以下内容的音频，中间不能打断
    Zhizi "（第二封信……）"

    $ _skipping = False
    show screen disable_Lmouse()

    "{cps=8}王さんへ{/cps}{p=2}{nw}"
    "{cps=8}{space=25}いつも気を使ってくれてありがとう。{/cps}{p=2}{nw}"

    "{cps=8}{space=25}臆病な私をたくさん褒めてくれて、すごく自信がついた。{/cps}{p=2}{nw}"

    "{cps=8}{space=35}王さんは自分のことを取柄がないとか言っていたけど、\n
    本当はみんなのことを誰よりも大事に思っているよね。{/cps}{p=2}{nw}"

    "{cps=8}{space=25}そういうところがとても好きだよ。{/cps}{p=2}{nw}"

    "{cps=8}{space=35}いろいろ大変なことがあるかもしれないけど、\n
    皆と一緒にいれば、なんだか乗り越えられる気がする。{/cps}{p=2}{nw}"

    "{cps=8}{space=25}また、会えるといいね。さようなら。\n\n

    {space=420}智子より{/cps}{p=2}{nw}"

    $ _skipping = True
    hide screen disable_Lmouse


    hide w23 with dissolve

    "智子在信里写下了对大家的感谢和祝福，还有一段写给我的独白。"
    "智子感谢大家带给她的快乐，也感谢我给她带去信心和勇气。"

    #黑屏
    scene black_bg with Dissolve(2)
    stop music fadeout 2.0

    $ total_score = (sum(prologue_select) + sum(prologue_answer) + \
                    sum(chpt1_select) + sum(chpt1_answer_bunka) + sum(chpt1_answer_kana) + sum(chpt1_answer_tango) + sum(chpt1_answer_kaiwa) + \
                    sum(chpt2_select) + sum(chpt2_answer_bunka) + sum(chpt2_answer_kana) + sum(chpt2_answer_tango) + sum(chpt2_answer_kaiwa) + \
                    sum(chpt3_select) + sum(chpt3_answer_bunka) + sum(chpt3_answer_kana) + sum(chpt3_answer_tango) + sum(chpt3_answer_kaiwa) + \
                    sum(chpt4_select) + sum(chpt4_answer_bunka) + sum(chpt4_answer_kana) + sum(chpt4_answer_tango) + sum(chpt4_answer_kaiwa) + \
                    sum(chpt5_select) + sum(chpt5_answer_bunka) + sum(chpt5_answer_kana) + sum(chpt5_answer_tango) + sum(chpt5_answer_kaiwa) )

    if total_score > 300:
        jump End2
    else:
        jump End1

    # menu:
    #     "（由于数值还没确定，这里先直接进行结局选择）"
    #     "结局一":
    #         jump End1
    #     "结局二":
    #         jump End2


label End1:

    #{播放bgm bokunosekai}
    # play music "audio/bgm/b0406 xiaoyu.mp3" fadein 1.0
    stop music fadeout 3.0
    #结局一 好感度XXX分以下结局
    #{显示立绘WH 23gx}
    # show WH 23gx at middle with dissolve
    "虽然过去无法改变，但通过重启青春的经历，我弥补了很多青春岁月中留下的遗憾。"
    "但是我依然没有勇气坦白自己对智子的情感。"
    "或许有一天，我会成长为一个勇敢的男子汉，期待那时候能够再次与智子重逢……"

    jump EndingSubtitle


label End2:
    #结局二 好感度达到XX以上触发
    #{停止播放bgm }
    #{显示立绘WH 23gx}
    show WH 23gx at middle with dissolve
    "看到智子给自己的留言，我思绪万千。没有想到一无是处的自己还能够给周围的人带来改变。"
    "她现在又在何处，我们如何才能再次相见呢……"
    # 手机铃声响起
    play music "audio/se/s0104 Harmony.mp3"
    #{显示立绘XY 21dy}
    hide WH
    show XY 21dy at middle
    with dissolve
    ZhouXiaoyu "是王浩的手机，要不要叫他起来接电话啊？"
    "我突然听到了周小雨的声音。"
    stop music fadeout 2.0
    #{显示立绘LY 21rz}
    hide XY
    show LY 21rz at middle
    with dissolve
    LiuYang "王浩，王浩！起来咯。"
    #{显示立绘ZH 12zj}
    hide LY
    show ZH 22zj at middle
    with dissolve
    ZhengHui "哎，奇怪了。游戏应该已经结束了呀，他怎么还没醒。"
    #{显示立绘QQ 23jy}
    hide ZH
    show QQ 23jy at middle
    with dissolve
    YuanQiaoqiao "是不是你设计的这个游戏程序有问题啊？"
    #{显示立绘ZH 12zj}
    hide QQ
    show ZH 22zj at middle
    with dissolve
    ZhengHui "不应该啊……"
    "耳边传来很多熟悉的声音。这时我才注意到周围一片漆黑，头上好像套着一个重重的头盔。"

    #屏幕亮起
    #{显示背景  p16 xinjia}
    scene p16 xinjia with Dissolve(2)
    #{播放bgm 0509}
    play music "audio/bgm/b0509.mp3"
    #{显示立绘WH 22wx}
    show WH 22wx at middle with dissolve
    me "这里是……"
    "摘掉头盔后，我看着周围有些陌生的景象。看到窗外的场景，我这才意识到这里是刚刚搬进来的新家。昔日的同学围在我身边。"
    #{显示立绘ZH 22wx}
    show WH at MidToRight
    show ZH 22wx at left with dissolve
    ZhengHui "这么样，我做的新游戏还行吧？"
    "郑辉满怀期待地凑了过来。"
    #{显示立绘WH 23jy}
    show WH 23jy
    me "新游戏？"
    #{显示立绘ZH 22wn}
    show ZH 22wn
    ZhengHui "对啊，就是你刚刚体验的《重启青春》。"
    #{显示立绘WH 22jy}
    show WH 22jy
    me "刚刚体验的游戏？"
    hide ZH
    hide WH
    with dissolve
    "我从什么时候开始玩的游戏？不是应该在学校参加同学聚会吗？"
    "不对，今天确实是同学聚会。但是因为学校正好在装修，于是便定在我的新家聚会。"
    "然后郑辉带来了一个类似头盔的装置，说是他做的新游戏《重启青春》，可以使用VR技术进行沉浸式体验……"
    "再然后……"

    #{显示立绘WH 23jy}
    show WH 23jy at middle with dissolve
    "我这才意识到，原来从头到尾都是发生在郑辉设计的VR游戏里的故事。这款游戏会调动玩家潜意识里的记忆，根据他们的经历，生成不同的剧情，来帮他们完成自己的心愿。"
    "完全沉浸式的体验让我分不清哪个是现实，哪个是虚拟世界。"
    "我突然意识到，智子她早已经回国……"
    "此时，门外传来了敲门声……"

    #{显示立绘ZZ21xf}
    hide WH
    show ZZ 21xf at middle
    with dissolve
    Zhizi "ただいま。（我回来了。）"
    "智子一脸微笑地走了进来，包上挂着当年的那个中国结……"
    # hide ZZ with dissolve
    "是的，一年前智子回国的时候，接受了我的告白。"
    "在经历了一年的交往以后，我们得到了大家的祝福，走入了婚姻的殿堂。这里是我和智子的新家。"
    "这次的时光穿越让我想起了当年的那个胆小而不敢向前看的自己，也让我再次体会到了要想成功必须变得勇敢、坦率和真诚。"
    "给周围的人带去幸福的人，最终也能找到属于自己的幸福……"
    hide ZZ with dissolve

    jump EndingSubtitle

label EndingSubtitle:
    #{播放bgm bokunosekai}
    play music "audio/bgm/bokunosekai.mp3" fadein 0.5

    window hide

    show screen stop_scr
    $ _skipping = False

    #片尾字幕
    show ending_script with dissolve:
        ypos 0
        linear 208 ypos -(9537-1180)

    $ renpy.pause(208, hard=True)

    hide screen stop_scr

    stop music
    pause

    return