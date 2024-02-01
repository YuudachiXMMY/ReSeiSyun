#第二章
label chpt2_1:

    # 显示第二章过渡幕间图片
    #{显示背景  pz 02 }
    scene pz 02 with Dissolve(4)
    pause 0.5
    #（画面黑屏）
    scene black_bg with dissolve
    # （手机闹钟响起的声音）
    play music "audio/se/s0101 naozhong.mp3"
    # TODO: {显示立绘WH12my}
    # show WH 12my at middle with dissolve
    me "……"
    me "今天是……"
    hide WH with dissolve
    stop music
    # TODO:（画面逐渐变亮 睁眼动画）
    #{显示背景  p06 qinshi zao }（这个是新的背景）
    scene p06 qinshi zao with dissolve
    me "……"
    "缓缓睁开眼，映入眼帘的是熟悉而又陌生的天花板。"
    #{播放BGM b0201 }
    play music "audio/bgm/b0201.mp3"
    #{显示立绘WH12rz}
    show WH 12rz at middle with dissolve
    "从床上坐起，环顾四周，发现自己仍置身于高中寝室。"
    me "原来不是做梦啊……"
    "原以为回到高中时代不过是昨日的黄粱一梦，没想到这样的奇迹确确实实地发生在了我身上。这样的话，今天和智子约好共进午餐的事……"
    #{显示立绘LY11qx}
    show WH at MidToRight
    show LY 11qx at left with dissolve
    LiuYang "早上好啊。"
    "正在我恍惚之际，室友刘洋向我打了招呼，将我的思绪拉回了现实。"
    #{显示立绘WH13my}
    show WH 13my
    me "……嗯，早上好。"
    #{显示立绘LY11jy}
    show LY 11jy
    LiuYang "怎么了？你看上去好像没有什么精神。"
    me "没什么，还没缓过神来。哈哈。"
    "十年前每个相似的早晨又一下子闪回到我的眼前。"
    "刘洋很习惯早睡早起的生活，从没在脸上表现出困倦。而我则是一名不折不扣的起床困难户。熟悉又怀念的记忆向我不断涌来。"
    "洗漱完毕，我收拾收拾书包，和刘洋一同出门走向教室。"

    #{播放BGM b0202 }
    play music "audio/bgm/b0202.mp3"
    #{显示背景  p05 jiaoshijiu }
    scene p05 jiaoshijiu with dissolve
    "时间转眼就到了上午最后一节课。我看了一眼黑板上的课表，是体育课。"
    #{显示立绘WH12wx}
    show WH 12wx at middle with dissolve
    "我看到不远处独自坐着的智子。看到班里的同学接二连三地离开教室，智子会很不安吧"
    #{显示立绘ZZ13ys}
    show WH at MidToRight
    show ZZ 13ys at left with dissolve
    me "智子不认识去操场的路，要不要和她打个招呼？"
    jump chpt2_2

label chpt2_2:
    #{显示选项  文本框居中，选项竖排1 2}
    menu chpt2_choice_1:
        "1.一緒に食べましょうか。":
            $chpt2_select[0] = 0
            jump chpt2_choice_1A
        "2.一緒に行きましょうか。":
            $chpt2_select[0] = 10
            jump chpt2_choice_1B

label chpt2_choice_1B:
    if chpt2_C_answer_kaiwa_index < 1:
        $ chpt2_C_answer_kaiwa_index = 1
    #选择1.
    #好感度参数 +10
    me "次は体育の授業ですよ。一緒に行きましょうか。（下节是体育课，我们一起去吧。）"

    jump chpt2_3

label chpt2_choice_1A:
    if chpt2_C_answer_kaiwa_index < 1:
        $ chpt2_C_answer_kaiwa_index = 1
    #选择2.
    me "不对，不对。食べましょう是邀请一起吃饭的意思，应该说……"
    me "次は体育の授業ですよ。一緒に行きましょうか。（下节是体育课，我们一起去吧。）"

    jump chpt2_3

label chpt2_3:
    #{显示立绘ZZ13xf}
    show ZZ 13xf
    Zhizi "助かります。誘ってくれてありがとう。（帮大忙了，谢谢你邀请我。）"
    "智子点点头并露出了安心的微笑。"
    #{显示立绘XY11dy}
    hide WH
    hide ZZ
    show XY 11dy at t_left with dissolve
    ZhouXiaoyu "王浩，你刚才说了什么吗？"
    #{显示立绘LY13jy}
    show LY 13jy at t_right with dissolve:
        xoffset 250
    LiuYang "他邀请智子和我们一起走。"
    #{显示立绘XY11zm}
    show XY 11zm
    ZhouXiaoyu "哎哟，没看出来王浩还是个暖男嘛。不像某些人……"
    "周小雨朝着刘洋看了一眼，明显话里有话。刘洋却微微一笑，好像并没有察觉。"
    #{显示立绘QQ11jy}
    show QQ 11jy at middle with dissolve
    YuanQiaoqiao "不好，只剩两分钟啦，快走吧！"


    #{显示背景 p07 caochang }
    scene p07 caochang with dissolve
    "前半节体育课的集体训练结束后，老师便让我们原地解散自由活动了。"
    "我在操场跑道上漫无目的地逛了一会儿，想起了昨天和智子约好一起吃午餐的事情。"
    #{显示立绘WH 12zm}
    show WH 12zm at middle with dissolve
    me "要不然现在就去找她吧。"
    me "啊，在那儿。"
    show WH at t_MidToRight
    #{显示立绘ZZ 14xf}
    show ZZ 14xf at t_left with dissolve
    #{显示立绘XY 12dx}
    show XY 12dx at middle with dissolve
    "智子正从教学楼的方向走过来。周小雨陪在一旁，好像在向她介绍学校各处的场馆设施和同学们的学习生活。"
    "足球场上，校足球队正在训练。刘洋在场上带球过人的动作行云流水，英姿飒爽。"
    "周小雨陪着智子有说有笑地一起向足球场走去。"
    #{显示立绘ZZ 13gx}
    show ZZ 13gx
    #{显示立绘XY 11bx}
    show XY 11bx
    "智子和小雨正聚精会神地看着比赛。"
    "我停下脚步，心里不禁打起了退堂鼓。"
    #{显示立绘WH 11zm}
    show WH 11zm
    me "……要不还是别去打扰她们两个了。我也不懂足球，省得自讨没趣。"
    me "不对，这个场景之前也发生过……"

    scene black_bg with dissolve
    #{播放BGM b0203 }
    play music "audio/bgm/b0203.mp3"
    scene p07 caochang with dissolve
    #（回到过去的记忆 画面黄色）
    show ZZ 13gx at left with dissolve
    show XY 11bx at right with dissolve:
        xoffset -300
    show memory_cover onlayer over_screen with dissolve:
        alpha 0.5
    "智子和小雨正聚精会神地看着比赛。"
    "我停下脚步，心里不禁打起了退堂鼓。"
    me "……要不还是别去打扰她们两个了。我也不懂足球，省得自讨没趣。"
    "就在我打算转身离开的时候，突然听到了一声惊叫。"
    #{显示立绘ZZ 14jy}
    show ZZ 14jy
    Zhizi "あぶない！"
    "我猛地回头，发现一个足球失控飞出场外，直直地向智子的脸上飞去。"
    "智子想要侧身躲闪却已来不及，害怕地闭上了眼睛。"
    show ZZ with hpunch
    "情急之下，周小雨伸出左手挡在智子面前，足球重重地打在了她的手腕上。"
    ZhouXiaoyu "……啊！"
    #{显示立绘ZZ 14ys}
    show ZZ 14ys
    "一旁的智子脸上写满了自责，又因为语言不通，而不知所措，不住地说着……"
    Zhizi "すみません、すみません……（对不起，对不起……）"
    "足球队的队员们也赶过来查看情况。"
    hide ZZ
    #{显示立绘LY 11jy}
    show LY 11jy at left with dissolve
    "刘洋一脸紧张地看着周小雨被打中的手腕"
    LiuYang "小雨，你还好吗？都怪我……"
    #{显示立绘XY 13jy}
    show XY 13jy
    ZhouXiaoyu "还好……"
    "疼痛让周小雨的声音有些颤抖。刘洋想要伸手扶小雨，看到了她手腕上的黑色球印，显然伤得不轻。"
    LiuYang "疼得厉害吗？要不要去医务室？"
    "周小雨看似平静，但泪水却在眼眶里打转。"

    scene black_bg with dissolve
    hide memory_cover onlayer over_screen with dissolve
    #（结束回忆，画面恢复正常）
    scene p07 caochang with dissolve
    #{播放BGM b0204}
    play music "audio/bgm/b0204.mp3"
    "既然是回到了过去，那是不是马上就会……"
    "只见场上的刘洋正在和场外看球的智子和小雨打招呼，没注意到对手趁此机会发起了进攻。"
    "正如预想的那样，足球向场外飞过来……"

    #{显示立绘WH 13jy}
    show WH 13jy at middle with dissolve
    me "快躲开！"
    "我一边喊着一边向智子所在的地方冲了过去。我从未如此拼尽全力地奔跑过。"
    #{显示立绘XY 13jy}
    show WH at t_MidToRight
    show XY 13jy at t_left with dissolve
    show ZZ 14jy at middle with dissolve
    "周小雨听到我的声音愣在原地，有点不知所措。"
    me "小心！"
    "周小雨一惊，急忙拉着智子往旁边躲了一步。"
    # TODO: （声效扑球撞击声）
    show WH with hpunch
    "球啪的一声打在我的手掌上，我飞扑倒地……"
    #{显示立绘WH 11zm}
    show WH 11zm
    me "你们俩没事吧？"
    "我起身拍了拍身上的尘土。"
    #{显示立绘XY 13jy}
    show XY 13jy
    ZhouXiaoyu "王浩！你没事吧？"
    #{显示立绘ZZ 14jy}
    "智子握着小雨的手，好像也有点惊魂未定的样子。她看了看足球场，又将视线移到了我的脸上。"
    Zhizi "王さん、大丈夫ですか。ごめんなさい。（王浩，你没事吧？对不起！）"
    "智子惊慌失措地看着我，露出焦急而充满歉意的表情。"

    jump chpt2_4

label chpt2_4:
    #{停止BGM }
    stop music

    #{显示立绘WH 11rz}
    show WH 11rz
    "我想安慰一下智子不必担心，应该说……"
    #{显示选项  文本框居中，选项竖排1 2}
    menu chapt2_choice_2:
        "1.すみません。":
            $chpt2_select[1] = 0
            jump chpt2_choice_2A
        "2.大丈夫。気にしないで。":
            $chpt2_select[1] = 10
            jump chpt2_choice_2B

label chpt2_choice_2A:
    if chpt2_C_answer_kaiwa_index < 2:
        $ chpt2_C_answer_kaiwa_index = 2
    #选择1.
    me "不对，すみません是道歉的意思。应该说……"
    me "大丈夫。気にしないで。（没事，别介意。）"

    jump chpt2_5

label chpt2_choice_2B:
    if chpt2_C_answer_kaiwa_index < 2:
        $ chpt2_C_answer_kaiwa_index = 2
    #选择2.
    #好感度参数 +10
    me "大丈夫。気にしないで。（没事，别介意。）"

    jump chpt2_5

label chpt2_5:
    #{播放BGM b0202}
    play music "audio/bgm/b0202.mp3"
    #{显示立绘LY 11jy}
    show WH at f_rright
    show ZZ at f_right:
        xoffset -75
    show XY at f_left:
        xoffset 75
    show LY 11jy at f_lleft with dissolve
    "这时，刘洋也从足球场上跑过来，在我们三人面前停住了脚步。"
    LiuYang "你们没事吧？都怪我分了神，没注意到球被踢飞了。不好意思啊！"
    #{显示立绘XY 12dy}
    show XY 12dy
    ZhouXiaoyu "我和智子没事，多亏了王浩。"
    #{显示立绘LY 11gx}
    show LY 11gx
    LiuYang "谢谢你啊王浩，幸亏有你在。"
    #{显示立绘WH 12my}
    show WH 12my
    me "没事没事，别介意。"
    #{显示立绘WH11hz}
    "刘洋看了看小雨，又低头向智子表示歉意。"
    #{显示立绘XY 12wx}
    show XY 12wx
    ZhouXiaoyu "你俩可是来对了。我刚刚和智子说了半天鸡同鸭讲。两位大神帮我翻译一下呗？"
    #{显示立绘LY 13gx}
    show LY 13gx
    "我和刘洋对视了一眼。刘洋随即点了点头。"
    LiuYang "可以啊，我没问题。"
    #（后文中默认王浩和刘洋会为其他小伙伴进行翻译，对话中就不以转述的形式出现。）
    "我想起昨晚智子邀我和她一起吃午餐的短信。"
    #{显示立绘WH 11rz}
    show WH 11rz
    me "……行呀，我也没问题。要不中午一起吃饭吧。"
    "见智子一脸迷茫，我赶忙向她解释。"
    me "四人で一緒に昼ご飯を食べましょうか。（我们四个人一起吃吧。）"
    #{显示立绘ZZ 11xf}
    show ZZ 11xf
    Zhizi "もちろんです。うれしい。（当然可以啦。我很乐意。）"
    me "智子也说可以。"
    #{显示立绘XY 13dx}
    show XY 13dx
    ZhouXiaoyu "那太好了！"

    #{播放BGM b0205}
    play music "audio/bgm/b0205.mp3"
    # （食堂）
    #{显示背景 p08 shitang }
    scene p08 shitang
    "四个人同坐一张桌子，我和智子面对面，刘洋和周小雨面对面。"
    #{显示立绘ZZ 11gx}
    show ZZ 11gx at f_lleft with dissolve:
        xoffset 75
    Zhizi "いただきます。（我开始吃了。）"
    #{显示立绘WH 13rz}
    show WH 13rz at f_rright with dissolve
    me "いただきます。（我开始吃了。）"
    "智子双手合十，小声地说了这样一句。我也跟着说了一句，周小雨看着我俩笑开了花。"
    #{显示立绘XY 12dx}
    show XY 12dx at f_left with dissolve
    ZhouXiaoyu "你们在干什么？"
    #{显示立绘LY 12wx}
    if chpt2_C_answer_bunka_index < 1:
        $ chpt2_C_answer_bunka_index = 1
    show LY 12wx at f_right with dissolve
    LiuYang "这是日本人的习惯，在吃饭前要说「いただきます」，表示对食物的敬意。"
    #{显示立绘XY 11zm}
    show XY 11zm
    ZhouXiaoyu "哦，为什么要对食物表示敬意呢？"
    #{显示立绘ZZ 13wx}
    show ZZ 13wx
    Zhizi "実は「いただきます」には意味が二つあります。（其实‘我开始吃了’这句话里有两层含义。）"
    Zhizi "一つは食事を作ってくれる人や飼育、栽培をしている人に感謝の気持ちを伝えること。（第一层含义是向给我们做菜和饲养动物、栽培作物的人们表达感谢。）"
    #{显示立绘WH 12wx}
    show WH 12wx
    me "もう一つは「尊い命をいただく」という意味だね。（另一层含义是向我们索取的尊贵生命表示感谢，对吧？）"
    #{显示立绘ZZ 14xf}
    show ZZ 14xf
    Zhizi "そうそう、日本の文化もよく知っているね。（是的，你很了解日本文化啊。）"

    # TODO: （出现选项）
    #{显示立绘WH 11my}
    show WH 11my
    me "いえいえ、まだまだです。（哪里，略知一二而已。）"

    "看到小雨听得有些云里雾里，刘洋便岔开了话题。"
    #{显示立绘LY 12gx}
    show LY 12gx
    LiuYang "对了，大家想过将来要做什么吗？"
    #{显示立绘XY 11wx}
    show XY 11wx
    ZhouXiaoyu "我想做的事可多了。"
    LiuYang "哈哈哈，你不是想做钢琴演奏家吗？"
    #{显示立绘ZZ 14xf}
    show ZZ 14xf
    Zhizi "すごい。（太厉害了。）"
    #{显示立绘XY 13zm}
    show XY 13zm
    ZhouXiaoyu "别听他瞎说，我还没想好呢。有很多要考虑的事……"
    #{显示立绘LY 12hz}
    show LY 12hz
    LiuYang "有什么好多想的，有梦想就努力去实现呗！"
    "听到刘洋的话，周小雨张了张嘴想说些什么，又沉默了。"
    #{显示立绘WH 11rz}
    show WH 11rz
    "周小雨欲言又止，气氛有些尴尬，于是我把话题抛给了智子。"
    me "智子ちゃん、いや、高橋さんはどうですか。（智子，哦不对，高桥你的梦想是什么呢？）"
    #{显示立绘ZZ 13wx}
    show ZZ 13wx
    Zhizi "夢ですか。私はアナウンサーになりたいです。（梦想啊，我想成为一个电视台主持人。）"
    #{显示立绘XY 11dx}
    show XY 11dx
    ZhouXiaoyu "好棒啊。"
    "我不由得想起周小雨说智子在日本电视台录制节目的事情。虽然穿越到高中时代，看到智子在眼前让我非常高兴。但不知道现在的她怎么样了……"
    #{显示立绘ZZ 11xf}
    show ZZ 11xf
    "智子冲我微笑了一下，又看向旁边的刘洋。"
    #{显示立绘ZZ 13wx}
    show ZZ 13wx
    Zhizi "劉さんと王さんはどうですか。（刘洋、王浩，你们的梦想是什么呢？）"
    #{显示立绘LY 11rz}
    show LY 11rz
    LiuYang "外交官になりたいかな。日本に留学するとか。（我以后想做一个外交官吧，可能会去日本留学。）"
    #{显示立绘XY 11dy}
    show XY 11dy
    "或许是我的错觉，听到刘洋的话，小雨的脸上露出了些许担忧的表情。"
    #{显示立绘ZZ 13wx}
    show ZZ 13wx
    Zhizi "そうなんですか。さすがですね。（这样啊，真是了不起）"
    "智子又笑着望向我。"
    #{显示立绘ZZ 11xf}
    show ZZ 11xf
    Zhizi "王さんはどうですか。（王浩，你呢？）"
    #{显示立绘WH 11zm}
    show WH 11zm
    "原来只剩我还没有说自己的梦想了，我一下有点不知所措。"
    me "私、私は無職になるかも。（我……我可能要在家啃老了。）"
    "说起将来的事情，想到刚刚辞职的经历，我不由得感到前途渺茫，感伤了起来，不敢看智子的眼睛。"
    #{显示立绘ZZ 13wx}
    show ZZ 13wx
    Zhizi "そんなことないですよ。王さんは優しいから、きっとうまくいきますよ。（怎么会，你这么善良，一定会很顺利的。）"
    "得到智子的宽慰，我心里好受了一些。但是在成人的世界里善良或许反而是最大的弱点吧。"
    "我再次思考起自己的梦想。高中时代的我，只觉得顺其自然就好，船到桥头自然直。可是后来的生活却仿佛是踩着西瓜皮过日子，自己的人生永远在别人的指挥之下。如果再给我一次机会的话，我又该如何选择呢……"
    Zhizi "ご馳走さまでした。（感谢款待。）"
    "智子吃完饭后，很有礼貌地说了一句‘感谢款待’，便又认真地听我们说话。不知不觉中，我们四个人度过了愉快的午休时间……"

    jump lesson2_1
