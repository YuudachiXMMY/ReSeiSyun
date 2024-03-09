#第三章
label chpt3_1:

    scene black_bg with Dissolve(2)
    #显示第二章过渡幕间图片
    #{显示背景  pz 03 }
    scene pz 03 with Dissolve(2)
    pause 1
    #{播放BGM b0301}
    play music "audio/bgm/b0301.mp3"  fadein 2.0
    #{显示背景  p05 jiaoshijiu }
    scene p05 jiaoshijiu with Dissolve(2.5)
    #{显示立绘WH 11kx}
    show WH 11kx at middle with dissolve
    "一晃穿越回这个世界已经三天了，内心渐渐地有些留恋这个地方。"
    "高中时代并没有觉得校园是个特别的地方。睁开眼就是上课、做题、无穷无尽的试卷，让人透不过气。"
    "但现在的我却能够感受到与同学们的关系在慢慢地变化，在这个微缩的小社会里，每个人都有自己精彩的人生，每个个体都在默默地改变着这个世界……"

    #{显示立绘ZZ 13jy}
    show WH at MidToRight
    show ZZ 13jy at left with dissolve
    Zhizi "鄭さんと袁さんはどこに行ったんですか。（郑辉和巧巧去哪儿了？）"
    "智子一脸疑惑地看着我，我的思绪被拉回了现实中。"
    #{显示立绘LY 13wx}
    hide WH
    show LY 13wx at right
    with dissolve
    LiuYang "今日は新入生を勧誘するためのサークル活動日なんです。（今天是学校的社团招新日。）"
    "在一旁的刘洋见我愣在原地，便回复了智子。"
    #{显示立绘LY 11wx}
    show LY 11wx
    LiuYang "鄭さんと袁さんは部長なので、今準備しているところです。（郑辉和巧巧都是社团部长，现在正在做准备。）"
    #{显示立绘ZZ 13gx}
    show ZZ 13gx
    Zhizi "面白そうですね。私も行きたいです。（听上去很有趣，我也想去看看。）"
    "在一旁的周小雨看了看刘洋，又狠狠地瞪了我一眼。"
    "当年的社团招新我没去参加，这次……"
    #{显示立绘XY 12dx}
    hide ZZ
    show XY 12dx at left
    with dissolve
    ZhouXiaoyu "啊呀，田老师让我中午去整理资料。让王浩带你去逛逛吧。"
    #{显示立绘LY 12qx}
    show LY 12qx
    LiuYang "那我也一起去吧。"
    #{显示立绘XY 11zm}
    show XY 11zm
    ZhouXiaoyu "不行不行，刘洋你得过来帮我，我一个人可应付不过来。"
    hide ZZ
    hide LY
    hide XY
    #{显示立绘WH 11zm}
    show WH 11zm at middle
    with dissolve
    "小雨竭力帮我助攻，不抓住这个机会实在说不过去。"
    jump chpt3_2

label chpt3_2:
    #{显示选项  文本框居中，选项竖排1 2}
    menu chpt3_choice_1:
        "1.私でよければ、案内します。":
            $chpt3_select[0] = 10
            $chpt3_answer_kaiwa[0] = 10
            jump chpt3_choice_1A
        "2.私はちょっと……":
            $chpt3_select[0] = 0
            $chpt3_answer_kaiwa[0] = 0
            jump chpt3_choice_1B

label chpt3_choice_1A:
    #选择1.
    #好感度参数 +10
    #{显示立绘WH 11wx}
    show WH 11wx
    me "私でよければ、案内します。（可以的话，我带你去吧。）"
    jump chpt3_3

label chpt3_choice_1B:
    #选择2.
    me "不对，不对。ちょっと……是委婉拒绝的意思，应该说……"
    me "私でよければ、案内します。（可以的话，我带你去吧。）"
    jump chpt3_3

label chpt3_3:
    if chpt3_C_answer_kaiwa_index < 1:
        $ chpt3_C_answer_kaiwa_index = 1
    show WH at MidToRight
    #{显示立绘ZZ 13xf}
    show ZZ 13xf at left with dissolve
    Zhizi "よかった。王さんがいてくれると、心強いです。（太棒了。有你在，我就安心了。）"
    #{显示立绘WH 12zm}
    show WH 11kx
    "第一次拥有和智子独处的机会，这感觉真奇妙。虽然内心已经是一个二十几岁的成年人了，但我还是不由得有些紧张。"

    #{显示背景  p09 shetuan }
    scene p09 shetuan with dissolve
    #{播放BGM b0302}
    play music "audio/bgm/b0302.mp3"  fadein 2.0
    #{显示立绘WH 13wx}
    show WH 13wx at middle with dissolve
    "不一会儿，我和智子就一起来到了社团招新的广场上。我们穿行在不同的展台间，她好奇地四处打量着，我用日语向智子一一介绍。"
    me "ここは書道部です。（这里是书法社。）"
    me "ここは武道部です。（这里是武术社。）"
    me "ここは文化創意部です。（这里是文化创意社。）"
    #{显示立绘ZZ 13ys}
    show WH at MidToRight:
        xoffset 75
    show ZZ 13jy at left with dissolve
    Zhizi "文化創意部ってどんなことをする部活なんですか。（文化创意社是做什么的呢？）"
    #{显示立绘WH 12gx}
    show WH 12gx
    me "そうですね。学校の文化関連グッズを作ったりバザーで売ったりするクラブかなあ。ほら、あの校章のついたバッグみたい。（嗯，主要是制作和售卖学校文化周边产品的。比如说，你看，那个印着校徽的包包。）"

    #{显示立绘ZZ 11gx}
    show ZZ 11gx
    Zhizi "へえ、面白そう！ちょっと参加してみたいな。（很有趣的样子，我也想参加看看。）"
    "我突然意识到刚才和智子说话时从敬体变成了简体，而她也丝毫没有介意，自然而然地开始用简体和我对话了。这是不是意味着我们的关系悄悄地近了一步？"
    #{显示立绘ZZ 12jy}
    show ZZ 12jy
    Zhizi "王さん、どうしたの？（王浩，你怎么了？）"
    #{显示立绘WH 12ng}
    show WH 11my
    "我急忙摇摇头，低下头加快脚步向前走，掩饰心中的羞涩。"
    #{显示立绘ZZ 13jy}
    show ZZ 13jy
    Zhizi "あれ、日本アニメじゃない？すごい！（那不是日本的动漫吗？好厉害呀！）"
    hide ZZ
    hide WH
    show QQ 12wx at middle
    with dissolve
    "我顺着她的目光看去，原来是袁巧巧担任部长的动漫社。"
    "她正站在台前拿着宣传单招呼着同学们，台子上挂着许多日本动漫的手绘图，还有中日文对照的宣传海报。"
    "有不少男生都围过来看热闹。"
    show QQ 13wx
    "面对那些男生的调侃，巧巧并不搭理，还在专注地宣传动漫社。"
    #{显示立绘WH 11wx}
    hide QQ
    show WH 11wx at middle
    with dissolve
    "看到巧巧被那么多狂热的粉丝包围着，我犹豫要不要去和她打招呼。"
    "这时，巧巧突然看到了智子，便快步走到智子身边，一把拉住她的手。"
    #{显示立绘QQ 11gx}
    hide WH
    show QQ 11gx at left
    with dissolve
    YuanQiaoqiao "智子，来我们这里看看呀。你那么可爱，来给我们做模特吧。"
    #{显示立绘ZZ 14ys}
    show ZZ 14ys at t_right with dissolve
    "智子有点被她的热情吓到了，红着脸怯怯地看了看我，我急忙向她解释。"
    #{显示立绘WH 12gx}
    hide QQ
    hide ZZ
    show WH 12gx at middle
    with dissolve
    me "袁さんはアニメの話になると、いつもハイテンションだから。（袁巧巧一提到动漫的话题，兴致就很高。）"
    #{显示立绘ZZ 11xf}
    hide WH
    show ZZ 11xf at right
    with dissolve
    "智子回握住袁巧巧的手，开心地笑了。"
    Zhizi "いえいえ、そんなことないです。袁さんこそ可愛いですよ。（哪里，巧巧你才很可爱呢。）"
    #{显示立绘QQ 13tq}
    show QQ 13wx at left with dissolve
    YuanQiaoqiao "哈哈哈，我听懂了卡哇伊。谢谢你呀！"
    YuanQiaoqiao "对了，能让我给你画张肖像画吗？"
    #{显示立绘WH 12rz}
    hide QQ
    hide ZZ
    show WH 12rz at middle
    with dissolve
    "我这才发现放在台子上的图都是动漫人物的肖像画。"
    #{显示立绘ZZ 14jy}
    hide WH
    show ZZ 14jy at t_right
    with dissolve
    Zhizi "ええ？似顔絵ですか。私でいいんですか…（啊，肖像画吗？我做模特没问题吗……）"
    #{显示立绘QQ 13dy}
    show QQ 13dy at left with dissolve
    YuanQiaoqiao "当然可以啊，画出来一定很好看，对不对王浩？"
    #{显示立绘WH 11zm}
    hide ZZ
    show WH 11kx at t_right
    with dissolve
    "巧巧的眼睛却瞟向我，等待我的回应。一下子有点手足无措。"
    "智子捕捉到我的窘态，噗嗤笑了。"
    #{显示立绘ZZ 11xf}
    hide WH
    show ZZ 11xf at t_right
    with dissolve
    "智子不好意思地坐到椅子上，安静地等袁巧巧画画……"
    #{显示立绘QQ 11gx}
    show QQ 11gx
    "过了好一会儿，巧巧画好了。她得意洋洋地把画展示给我和智子看。"
    YuanQiaoqiao "怎么样，我画的不错吧？"
    # TODO:{显示智子的肖像画 w11}
    jump chpt3_4

label chpt3_4:
    #{显示选项  文本框居中，选项竖排1 2}
    menu chpt3_choice_2:
        "1.まあまあです。":
            $chpt3_select[1] = 0
            $chpt3_answer_kaiwa[1] = 0
            jump chpt3_choice_2A
        "2.とても可愛いですよ。":
            $chpt3_select[1] = 10
            $chpt3_answer_kaiwa[1] = 10
            jump chpt3_choice_2B

label chpt3_choice_2B:
    #选择2.
    #好感度参数 +10
    #{显示立绘WH 11wx}
    hide ZZ
    show WH 11wx at t_right
    with dissolve
    me "とってもかわいいですよ！（真的很可爱！）"
    jump chpt3_5

label chpt3_choice_2A:
    #选择1.
    me "虽然感觉有些不好意思，但是巧巧确实画的不错，还是真心夸赞吧。"
    #{显示立绘WH 11wx}
    hide ZZ
    show WH 11wx at t_right
    with dissolve
    me "とってもかわいいですよ！（真的很可爱！）"
    jump chpt3_5

label chpt3_5:
    if chpt3_C_answer_kaiwa_index < 2:
        $ chpt3_C_answer_kaiwa_index = 2
    #{显示立绘ZZ 14wx}
    hide WH
    show ZZ 14wx at t_right
    with dissolve
    Zhizi "（脸红）あ……ありがとう。"
    "智子突然显得很害羞。我本意是说巧巧的画，没想到一语双关。"
    #{显示立绘QQ 12wx}
    show QQ 12wx
    YuanQiaoqiao "（一把将画塞进我手里）喏，王浩你拿好了。"
    #{智子的肖像画消失 w11消失}
    #{显示立绘WH 11gx}
    hide ZZ
    show WH 11gx at t_right
    with dissolve
    me "啊？给我吗？"
    #{显示立绘QQ 11tq}
    show QQ 11xf
    YuanQiaoqiao "看在你懂得欣赏的份上，就送给你做为礼物吧。"
    "巧巧鬼灵精怪地冲我眨眨眼。"
    #{显示立绘ZZ 14ys}
    hide QQ
    show ZZ 14wx at left
    with dissolve
    "智子虽然听不懂中文，但也有些不好意思地低下头。"
    #{显示立绘WH 13wx}
    show WH 13wx at t_right
    me "でも、やっぱりこれは智子ちゃんにあげた方がいいと思うな。（可是，我想还是送给智子比较好。）"
    #{显示立绘ZZ 13sq}
    show ZZ 14wx
    Zhizi "（惊讶）え？"
    #{显示立绘WH 11my}
    show WH 11my
    me "だって、この絵を見る度に、今日ここで過ごした良い思い出が思い出せるでしょ。（每一次看到这幅画，相信你都能想起今时今日在这里度过的美好时光。）"
    #{显示立绘ZZ 11xf}
    show ZZ 11xf
    Zhizi "そうだね……絶対に忘れられない思い出になると思う。（嗯，这一定会是最难忘的回忆。）"

    #{显示立绘QQ 13wx}
    hide ZZ
    hide WH
    show QQ 13wx at middle
    with dissolve
    YuanQiaoqiao "你们再去别的地方逛逛吧。哦对了，那边是‘游戏制作社’。郑辉笨手笨脚的，、帮忙去捧个场呗？"
    "朝着巧巧手指的地方望去，游戏制作社的展台和动漫社比起来确实是门可罗雀。"

    #（以下的对话保留原来三个人同时出现的模式）
    #{播放BGM b0301}
    play music "audio/bgm/b0301.mp3"  fadein 2.0
    #{显示立绘ZH 12wx}
    scene p09 shetuan with dissolve
    show ZH 12wx at t_left
    with dissolve
    ZhengHui "王浩，我就知道你会来。"
    # TODO: {显示立绘WH 12zm}
    show WH 12zm at t_right with dissolve:
        xoffset 75
    me "要不是袁巧巧提醒，我还真没注意到这个社团。"
    #{显示立绘ZZ 13gx}
    show ZZ 13gx at middle with dissolve
    Zhizi "鄭さん、こんにちは。"
    #{显示立绘ZH 12gx}
    show ZH 12gx
    ZhengHui "智子也来啦。你好，快看看我设计的游戏吧。"
    "看到我和智子走上前去，郑辉赶忙向我们介绍他设计的游戏。"
    #{显示立绘ZH 11wx}
    show ZH 11wx
    ZhengHui "你看，我设计了一款日语学习游戏。"
    #{显示立绘WH 12gx}
    show WH 12gx
    me "哦？日语学习还能做游戏？"
    #{显示立绘ZZ11wn}
    ZhengHui "对，这是我和一个日语老师一起开发的，可以通过玩游戏来学日语。王浩，你不是玩过很多游戏吗？要不先给你体验一下？"
    #{显示游戏光盘封面 w12}
    #{显示立绘WH 11jy}
    show WH 11jy
    "郑辉兴致勃勃地把光盘放到我手里，我也不好推辞，于是敷衍着答应了。"
    "话说这款游戏当年郑辉也向我推荐过，但是回寝室以后我就把它丢在了一边，并没有点开。我瞥了一眼游戏名称：甘泉幻想物语。好像在哪里听说过。"
    #{显示立绘ZZ 13jy}
    show ZZ 13jy
    Zhizi "このゲームを自分で作ったんですか。すごいですね。（这个游戏是你自己做的吗？太厉害了。）"
    #{显示立绘ZH 11gx}
    show ZH 11gx
    ZhengHui "这有什么。我还打算设计一款沉浸式体验的游戏，模拟真实的环境，让大家能身临其境地学日语！"
    #{游戏光盘封面消失 w12}
    #{显示立绘WH 12kx}
    show WH 12kx
    me "身临其境？那可有点难吧。"
    #{显示立绘ZH 12zj}
    show ZH 12zj
    ZhengHui "现在VR技术已经取得很大的突破，将来肯定能应用到游戏上。"
    "我回忆起关于AI和VR的新闻，没想到郑辉当年这么有远见，难怪成了游戏公司的老板。"
    #{显示立绘WH 13my}
    show WH 13my
    me "郑辉，我觉得你说得很有道理，我相信你一定能做到。"
    #{显示立绘ZH 11zj}
    show ZH 11zj
    ZhengHui "哈哈，不管结果如何，现在不尝试一下的话，就会留下遗憾。"
    #{显示立绘ZZ 14xf}
    show ZZ 14xf
    Zhizi "夢を追い続ければ、きっとできますよ。（只要不放弃追梦，肯定会成功的。）"
    #{显示立绘WH 12ng}
    show WH 12ng
    "智子的话点醒了我，只要不放弃的话……我也曾有过很多想法，我却让它们在脑海中一闪而过，没有付诸行动。和郑辉、巧巧相比，我真是差得太远了……"
    # （上课铃声）
    #{显示立绘WH 11wx}
    show WH 11wx
    me "あっ、もうこんな時間。日本語の授業が始まるから、そろそろ教室に戻ろうか。（啊，已经这个点了。日语课要开始了，我们回教室吧。）"
    #{显示立绘ZZ 13gx}
    show ZZ 13gx
    Zhizi "そうだね。今日はありがとう。楽しかった。（好的，今天谢谢你啊，我玩得很开心。）"

    jump lesson3_1