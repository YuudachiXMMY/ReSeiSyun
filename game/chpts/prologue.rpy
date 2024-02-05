# 序章
label prologue_scene_1_1:

    scene black_bg with Dissolve(2)
    scene pz 00 with Dissolve(2)
    pause 1
    #{黑屏}
    scene black_bg with Dissolve(2.5)
    #{播放SE s0101手机闹钟响起的声音}（所有se的播放都设定画面停止到播放结束以后）
    play music "audio/se/s0101 naozhong.mp3"
    me "……"
    me "我是谁……我在哪里……"
    me "眼前闪过熟悉的画面，却又稍纵即逝……"
    me "曾几何时，慢慢地开始淡忘了自我……"
    #{画面逐渐变亮  睁眼动画}
    #{显示背景 P01 woshi}
    scene p01 woshi with dissolve
    #{手机闹铃停止}
    stop music fadeout 1.0
    #{播放BGM b0101 }
    play music "audio/bgm/b0101 yume.mp3"
    me "……"
    #{显示立绘 WH 22kx}
    show WH 22kx at middle with dissolve
    me "原来是场梦。"
    "我只是这个世界上最平凡不过的一个路人。"
    "都说90后是娇生惯养的一代人，脆弱、敏感而自私。"
    "没想到工作了以后，也不得不坦然接受社会的捶打。"
    "因为工作的调动，又要搬家了。毕业以来，这已经是第三次了……"
    #{显示立绘 WH 23wx}
    show WH 22wx
    me "算了，既然已经醒了，就起来整理一下房间吧。"
    #{播放SE s0102整理东西的特效}
    play sound "audio/se/s0102 zhengli.mp3"
    "书架上塞满了各种书，有《销售葵花宝典》《成功人士守则100条》《创业不死秘诀》……"
    "并非喜欢创业经商，只是想有一份自己的事业，摆脱浑浑噩噩的“工具人”生活。"
    "然而，书里这些人物的“小目标”已经是普通人无法触及的天花板。"
    #{显示立绘 WH 23kx}
    show WH 22kx
    me "卖了换杯奶茶吧……"
    #{播放SE s0103书摔下来的音效}
    play sound "audio/se/s0103 book.mp3"
    #{ BGM停止}
    stop music fadeout 1.0
    #{显示立绘 WH 22jy}
    show WH 22jy
    me "这是……"
    "掉落下来的是一堆高中时代的学习资料。"
    "几次搬家，当年的教科书、教辅书几乎都已经换了奶茶。"
    "唯有几本日语书还一直留着……"
    #{显示一本日语书的图片 w01}
    show w01 at left
    #{播放BGM b0101 }
    play music "audio/bgm/b0101 yume.mp3"
    #{显示立绘 WH 22rz}
    show WH 22rz
    me "《中学生日语》……这是我们当年学日语的入门书。"
    "翻开书页，熟悉的题目映入眼帘。"
    me "这些都是当年学过的，应该还想得起来。"
    #{图片 w01消失}
    hide w01 with dissolve

    #{显示题目  文本框居中，选项竖排A B C}
    menu prologue_scene_1_choice_1:
        '日本的(____)起源于中国，其核心精神为“和、敬、清、寂”。'
        "A.花道":
            $ prologue_answer[0] = 0
            jump prologue_scene_1_choice_1AC
        "B.茶道":
            $ prologue_answer[0] = 10
            jump prologue_scene_1_choice_1B
        "C.柔道":
            $ prologue_answer[0] = 0
            jump prologue_scene_1_choice_1AC

label prologue_scene_1_choice_1B:
    # 选择答案后跳转
    #选择2.茶道
    #好感度参数 +10
    me "嗯，确实是这个答案。日本的茶道起源于中国。“和”指祥和，“敬”指尊敬，“清”指清洁，“寂”指幽寂。"

    jump prologue_scene_1_2

label prologue_scene_1_choice_1AC:
    # 选择 其他选项
    me "唉，好像不太对。"
    me "应该是2.茶道。日本的茶道起源于中国。“和”指祥和，“敬”指尊敬，“清”指清洁，“寂”指幽寂。"

    jump prologue_scene_1_2

label prologue_scene_1_2:
    if chpt1_C_answer_bunka_index < 1:
        $ chpt1_C_answer_bunka_index = 1
    me "再来做一题试试看。"

    menu prologue_scene_1_choice_2:
        '日本的和服最早受到古代中国的哪种服装的影响？'
        "A.汉服":
            $prologue_answer[1] = 10
            jump prologue_scene_1_choice_2A
        "B.唐装":
            $prologue_answer[1] = 0
            jump prologue_scene_1_choice_2BC
        "C.旗袍":
            $prologue_answer[1] = 0
            jump prologue_scene_1_choice_2BC

label prologue_scene_1_choice_2A:
    #选择1.汉服
    #好感度参数 +10
    me "嗯，确实是这个答案。日本和服，初仿中国魏晋隋唐时期吴地的汉服，称为“吴服”，后又学习唐初衣冠制度，称为“唐衣”。"

    jump prologue_scene_1_3

label prologue_scene_1_choice_2BC:
    #选择 其他选项
    me "唉，好像不太对。"
    me "应该是1.汉服。日本和服，初仿中国魏晋隋唐时期吴地的汉服，称为“吴服”，后又学习唐初衣冠制度，称为“唐衣”。"

    jump prologue_scene_1_3

label prologue_scene_1_3:
    if chpt1_C_answer_bunka_index < 2:
        $ chpt1_C_answer_bunka_index = 2
    me "真是令人怀念，没想到高中时代学的一些知识现在都还记得。"
    "那时候最喜欢上日语课， 只可惜没有认真学习……"
    #{播放s0105钥匙掉在地上的声音}
    play sound "audio/se/s0105 yaochi.mp3"
    #{显示立绘 WH 23jy}
    show WH 23jy
    me "这是……"
    #{显示钥匙的图片 w02}
    show w02 at left
    "突然，从书里掉落了一把钥匙。"
    "好像在哪里见到过，一时又想不起来。"
    "拿起钥匙，回忆里的一些碎片仿佛被唤醒了……"
    #{ BGM b0101 停止}
    stop music
    #{图片 w02消失}
    hide w02 with dissolve
    #{播放SE s0104 手机铃声响起}
    play music "audio/se/s0104 Harmony.mp3"

    menu prologue_scene_1_choice_3:
        # {显示选项  文本框居中，选项竖排1 2}
        "A.马上接电话。":
            $prologue_select[0] = 10
            jump prologue_scene_1_choice_3A
        "B.懒得接电话。":
            $prologue_select[0] = 0
            jump prologue_scene_1_choice_3B

label prologue_scene_1_choice_3A:
    #选择1.
    #好感度参数 +10
    stop music
    "脑海里的回忆被铃声打断，匆忙之间，把钥匙塞进了口袋。"

    jump prologue_scene_1_4

label prologue_scene_1_choice_3B:
    #选择2.
    stop music
    me "估计是骚扰电话，不管它……"
    #{播放SE s0104 手机铃声响起}（所有se的播放都设定画面停止到播放结束以后）
    play music "audio/se/s0104 Harmony.mp3"
    "铃声再次响起，无奈地接起电话。"

    jump prologue_scene_1_4

label prologue_scene_1_4:
    stop music
    question "喂，请问是王浩吗？"
    "一个陌生的来电号码"
    #{显示立绘 WH 21wx}
    show WH 21wx at middle
    me "是的，请问您是哪位？"
    question "我是周小雨呀，连老同学的声音都听不出来了吗？"
    me "原来是班长（笑），许久不联系，有什么事吗？"
    #{播放BGM b0102  音乐替换}
    play music "audio/bgm/b0102 houkagonoyuzora.mp3"
    ZhouXiaoyu "当然，你还记得明天是什么日子吗？"
    "今天是礼拜六，明天自然是礼拜天……。"
    "对于一个没有女朋友的单身狗来说，从来没有必要去记一些特殊的节日。我努力回想了一下，最终还是放弃了。"
    #{显示立绘 WH 22my}
    show WH 22my
    me "是你的生日吗？"
    ZhouXiaoyu "哈哈哈，你怎么变得那么油了？"
    #{显示立绘 WH 22kx}
    show WH 22kx
    me "……"
    ZhouXiaoyu "十年之约啊，你忘了？"
    #{显示立绘 WH 21jy}
    show WH 21jy
    me "十年之约？"
    "经周小雨这么一说，才发现距离高中入学已经十年了，没想到时间过得那么快。"
    "正是在十年前，我们学校开设了第一届高中零起点日语班。"
    ZhouXiaoyu "时间定在明天上午8点，地点就在学校，能来参加吗，老同学？"
    #{显示立绘 WH 21ng}
    show WH 21ng
    me "我……"
    "高中时代，我就是存在感很弱的角色，工作以后更是像患了社恐，什么聚会活动都能躲则躲，每到周末，除了加班就只想躺平。况且，我也没有特别想见的人。"
    "想到自己还要打包搬家的行李，下意识地想要拒绝……"
    ZhouXiaoyu "那么晚才通知你，你别生气啊。"
    ZhouXiaoyu "谁让你当年不用QQ也不用微信，电话号码也换了。好不容易才打听到了你的新号码。"
    "还没来得及等我回答，周小雨又像想起了什么似的，接着往下说。"
    ZhouXiaoyu "就我们组的小聚会。"
    ZhouXiaoyu "对了，智子也会来参加哦，你还记得她吗？说是坐今天晚上的飞机过来。"
    #{播放BGM b0103 }
    play music "audio/bgm/b0103 toikioku_healing.mp3"
    "听到这个名字，我一瞬间有些恍惚。"
    "智子是当年我们班里的日本交换留学生。"
    "或许是因为少年时代的懵懂，我对她有种莫名的好感。"
    "“十年之约”就是她回国之前与我们做的约定。但是都过了十年了，她还记得吗？"
    #{显示立绘 WH 23rz}
    show WH 23rz
    me "你确定……她会来？"
    ZhouXiaoyu "嘻嘻，明天你就知道啦！果然你还是对智子念念不忘呢。"
    #{显示立绘 WH 23jy}
    show WH 23jy
    me "哪里……我是……"
    ZhouXiaoyu "那就这样，明天见啦。"
    "周小雨不由分说地挂断了电话。"
    #{显示立绘 WH 23kx}
    show WH 22kx
    "她的性格还是和高中时代一样，干脆、利落、让人难以拒绝。"
    "当年周小雨和智子住同一个寝室，两个人总是形影不离。"
    "课上我偷偷看智子的时候，总是被周小雨发现，还被调侃了许久。"
    "我的心中莫名产生了一种复杂的情绪。"
    "仿佛按下了回忆的开关，那些有关青春的美好记忆一股脑地涌上心头。"
    "不知道智子现在怎么样了……"
    "或许我心里对这个十年之约有些许期待，但是一想到自己窘迫的样子，还是不由地打退堂鼓。"
    #{显示立绘 WH 23kx}
    show WH 22kx
    "算了，去就去吧，也算是给自己的青春画一个句号。"
    #{ BGM停止}
    stop music
    #{黑屏}
    scene black with Dissolve(2)

    jump prologue_scene_2_1

label prologue_scene_2_1:
    #{显示章节背景  序 约定}
    #{黑屏}
    #{显示背景 P02 xiaomen}
    scene p02 xiaomen with dissolve
    #{播放BGM b0104 }
    play music "audio/bgm/b0104 xiaomen.mp3"
    "周日的校园安静得令人感到陌生。"
    "时隔多年回到母校，往日种种恍若昨日，历历在目。"
    "当年为了省下一些零花钱，每天骑自行车上学，即便是下雨天也不舍得打车。"
    MenWei "你好，有什么事吗？"
    "门卫师傅的话打断了回忆的思绪。"
    #{显示立绘 WH 21gx}
    show WH 21gx at middle
    me "我是这里的毕业生，是来参加同学聚会的。"
    MenWei "同学聚会？没听说啊。"
    "不应该啊。是今天，时间也没有错。"
    #{显示立绘 WH 21jy}
    show WH 21jy
    me "师傅，我确实跟老同学约了今天在这儿聚会。"
    me "要不我先进去等她可以吗？"
    MenWei "不行，学校有规定，没有相关证明，外来人员一律不许入校。"
    #{显示立绘 WH 21kx}
    show WH 21kx
    me "那我在门口等她吧。"
    me "小雨也真是的，说好的8点，自己却没到。"
    "打个电话给她问一下吧。"
    #{显示华为智能手机正在拨号的图片，2022年的手机  w03}
    show w03 at left
    #{BGM 暂停 }
    stop music fadeout 1.0
    #{播放SE s0106}
    play sound "audio/se/s0106 dadianhua.mp3"
    me "怎么回事，电话也不接。"
    #{图片 w03消失}
    hide w03 with dissolve

    menu prologue_scene_1_choice_4:
        #{显示选项  文本框居中，选项竖排1 2}
        "A.要不先回家吧。":
            $prologue_select[1] = 0
            jump prologue_scene_1_choice_4A
        "B.要不再等等吧。":
            $prologue_select[1] = 10
            jump prologue_scene_1_choice_4B

label prologue_scene_1_choice_4A:
    #选择1.
    me "先回家再说吧。"
    "刚转身准备走。"

    jump prologue_scene_2_2

label prologue_scene_1_choice_4B:
    #选择2.
    #好感度参数 +10
    me "再等等吧，小雨可能被什么事情耽搁了。"

    jump prologue_scene_2_2

label prologue_scene_2_2:
    question "王浩！"
    "身后响起了熟悉的声音。"
    "还没等我上前打招呼，门卫师傅迎了上去。"
    MenWei "周老师好。"
    #{播放BGM b0104 }
    play music "audio/bgm/b0104 xiaomen.mp3"
    #{显示立绘 XY 23wx}
    show WH at MidToRight
    show XY 23wx at left with dissolve
    ZhouXiaoyu "你好，张师傅。"
    ZhouXiaoyu "这是我的老同学。他是来帮忙布置校庆场地的。"
    MenWei "是这样啊。我还在想今天哪有什么同学聚会……"
    "周小雨看着一脸狐疑的门卫师傅，朝我眨了眨眼睛示意。"
    #{显示立绘 XY 23dx}
    show XY 23dx
    ZhouXiaoyu "别发呆啦，快走吧。"
    "我一头雾水地看了一眼门卫师傅。周小雨已经进了校门，在前面等着了，我只好跟着她走进了学校。"
    #{播放SE s0107 走路声}
    play sound 'audio/se/s0107 zoulu.mp3'
    #{显示背景 p03 xiaoyuan}
    scene p03 xiaoyuan with dissolve
    "学校还是十年前的模样，时间仿佛又回到了高中。"
    "不知道现在在这里学习的学生，又会是怎样的感受？"
    #{显示立绘 WH 23zm}
    show WH 23zm at right with dissolve:
        xoffset -400
    me "今天是布置校庆场地吗？没听你说啊。"
    #{显示立绘 XY 21cx}
    show XY 21cx at left with dissolve
    ZhouXiaoyu "哈哈，不这么说你怎么进得来呀。"
    "周小雨对我打趣。"
    #{显示立绘 WH 21gx}
    show WH 21gx
    me "没想到老班长现在也会耍小聪明了。"
    #{显示立绘 XY 21bx}
    show XY 21bx
    ZhouXiaoyu "切，这叫变通懂不懂。"
    #{显示立绘 WH 22jy}
    show WH 22jy
    me "对了，你当老师了？"
    #{显示立绘 XY 22dx}
    show XY 22dx
    ZhouXiaoyu "哈哈，你猜。"
    #{播放SE s0107 走路声}
    play sound "audio/se/s0107 zoulu.mp3"
    #{显示背景 p04 zoulang}
    scene p04 zoulang
    "跟着周小雨走进熟悉的教学楼，楼道里的环境也没什么变化。"
    #{显示立绘 WH 23rz}
    show WH 23rz at right with dissolve:
        xoffset -400
    me "这里是……"
    #{显示立绘 XY 23wx}
    show XY 23wx at left with dissolve
    ZhouXiaoyu "五班的教室还在老地方，还记得吗？"
    #{显示立绘 WH 23wx}
    me "当然记得。我们班离楼梯口最近，出操总是最快的。"
    #{显示立绘 XY 23wx}
    show XY 23wx
    ZhouXiaoyu "我们毕业了以后，班级的位置一直都没有变过。"
    "楼梯口的教室确实有地理优势，但是由于在转角处，经常会和在楼道里奔跑的学生迎面撞个踉跄。"
    #{显示立绘 XY 23wx}
    show XY 23wx
    ZhouXiaoyu "你看，谁来了！"
    "不知不觉已经走到了教室门口。"
    #{ BGM停止}
    stop music
    #{显示背景 p05 jiaoshixin}
    scene p05 jiaoshixin with dissolve
    "在前排的座位上，有一个熟悉的身影。"
    #{显示立绘 WH 22jy}
    show WH 22jy at middle with dissolve
    me "刘洋？"
    #{显示立绘 LY 21gx}
    show WH at t_MidToRight
    show LY 21gx at t_left with dissolve
    "刘洋一点都没变，还是学生时代的模样。"
    LiuYang "王浩，好久不见。"
    #{播放BGM b0105  }
    #{显示立绘 WH 21wx}
    show WH 21wx
    me "好久不见，你一点都没变。"
    "刘洋当年是班里的好学生，成绩出类拔萃，而且为人谦和，和班里的同学关系都不错。"
    "由于他爸爸在日企工作，我们开始学日语的时候，他已经超前学了很多。因此一直是大家膜拜的偶像。"
    #{显示立绘 WH 21gx}
    show WH 21gx
    me "怎么样，最近在哪里高就？"
    #{显示立绘 LY 21qx}
    show LY 21qx
    LiuYang "惭愧惭愧，还在家里啃老呢。"
    #{显示立绘 XY 21bx}
    show XY 21bx at middle with dissolve
    ZhouXiaoyu "听他瞎说。他现在可是在华师大读博呢。还拿了全额奖学金。"
    "说起华师大，我想起当年刘洋和周小雨同时考上了华师大。"
    "周小雨报考的是音乐教育专业，刘洋学的好像是社会学。"
    #{显示立绘 LY 23qx}
    show LY 23qx
    LiuYang "哪里哪里，我可比不上周老师啊，你现在可是人民教师。"
    #{显示立绘 XY 23wx}
    show XY 23wx
    ZhouXiaoyu "刚刚入职而已，别说得那么夸张。"
    #{显示立绘 WH 23my}
    me "看着已经很老练了。"
    #{显示立绘 XY 22wx}
    ZhouXiaoyu "哈哈，其实已经实习半年多了。我在日本读的研究生，3月份毕业的。国内9月才能入职，所以前面半年都是实习期……"
    hide LY
    hide WH
    hide XY
    "三个人正在聊天的时候，门口传来了熟悉的声音。"
    #{播放SE  s0108 开门的声音}
    play sound "audio/se/s0108 kaimen.mp3"
    #{ BGM停止}
    stop music
    #{显示立绘 ZH 21wx}
    show ZH 21wx at left with dissolve
    ZhengHui "好久不见啊，终于见面啦。"
    #{显示立绘 WH 23jy}
    show WH 23jy at right with dissolve:
        xoffset -400
    me "郑辉？"
    # TODO: {播放BGM b0106 }
    # play music "audio/bgm/b0105 jiaoshi.mp3"
    #{显示立绘 LY 21gx}
    show LY 21gx at middle with dissolve
    LiuYang "哈哈，是阿辉啊，别来无恙。旁边的这位是？"
    hide LY
    hide WH
    hide ZH
    "三个人在打趣中把目光转向了郑辉旁边的一位妆容精致、打扮得青春靓丽的女孩。"
    #{显示立绘 ZH 21zj}
    show ZH 21zj at left with dissolve
    ZhengHui "你不认识她啦？"
    #{显示立绘 XY 23dx}
    show XY 23dx at right with dissolve:
        xoffset -200
    ZhouXiaoyu "原来是巧巧大美女啊，越来越漂亮了。"
    hide ZH
    hide XY
    "袁巧巧，高中时代的同班同学。当时在班里就是班花级的人物，没想到时隔多年更加时髦了，难怪刘洋没有认出来……"
    #{显示立绘 QQ 22sq}
    show QQ 22sq at left with dissolve
    YuanQiaoqiao "老了老了，你看刘博士都不认得我了。"
    #{显示立绘 XY 21cx}
    show XY 21cx at right with dissolve:
        xoffset -200
    ZhouXiaoyu "哈哈，他就是个钢铁直男，别理他。对了对了，我之前在一个网站看过你的直播，粉丝人数可不少啊。"
    "说罢，周小雨就开启了八卦模式。"
    #{显示立绘 XY 21jy}
    show XY 21cx
    ZhouXiaoyu "你们两个人今天一起过来的吗？"
    #{显示立绘 QQ 23dy}
    show QQ 23dy
    YuanQiaoqiao "我这不是没有车嘛，过来不方便，就搭了顺风车。"
    #{显示立绘 XY 21dx}
    show XY 21dx
    ZhouXiaoyu "一开始我真没认出你来，我还以为阿辉今天带女朋友来撒狗粮呢。"
    #{显示立绘 ZH 21gg}
    show ZH 21gg at middle with dissolve
    ZhengHui "……"
    #{显示立绘 LY 22jy}
    hide XY
    hide QQ with dissolve
    show ZH 22wn at right with dissolve:
        xoffset -200
    show LY 22jy at left with dissolve:
        xoffset -200
    LiuYang "对了，你当年是学软件工程的吧。现在怎么样了？听说你开了公司？"
    #{显示立绘 ZH 22wn}
    show ZH 22wn at right
    ZhengHui "大学毕业之后在游戏公司待了一年吧，之后就出来单干了。想做点自己喜欢的游戏……"
    #{显示立绘 WH 22jy}
    hide LY with dissolve
    show WH 22jy at left with dissolve
    me "我记得高中的时候你就做过一个学日语的游戏……"
    #{显示立绘 ZH 22wx}
    show ZH 22wx
    ZhengHui "对，没想到你还记得。当年摸索着学编程，跟着一位日语老师一起做过一款学习日语的RPG游戏。"
    #{显示立绘 ZH 22wx}
    show ZH 22wx
    ZhengHui "现在VR技术也普及了，我正在制作一款学习日语的沉浸式VR游戏。"
    #{显示立绘 WH 23kx}
    show WH 22kx
    me "能够坚持自己的梦想太不容易了。"
    #{显示立绘 ZH21}
    show ZH 21gx
    ZhengHui "哈哈，期待你的试玩，多提宝贵意见啊。"
    #{显示立绘 WH 23gx}
    show  WH 23gx
    me "一定一定。"
    #{显示立绘 ZH 22gx}
    show ZH 22gx
    ZhengHui "其实这次还请巧巧参与了游戏的配音，她可是日本声优专业的科班出身，有百万粉丝呢。"
    #{显示立绘 QQ 21sq}
    show QQ 21sq at middle with dissolve
    YuanQiaoqiao "切，别光拍马屁，说好了游戏盈利三七开哦，你三我七。"
    #{显示立绘 ZH 21gg}
    show ZH 21gg
    ZhengHui "一定一定。"
    hide QQ with dissolve
    "郑辉不好意思地笑了笑，转头来和我搭话。"
    ZhengHui "你现在怎么样？说了一圈还没聊你呢。"
    #{显示立绘 WH21}
    show WH 21ng
    me "我没什么好聊的，在公司混混日子而已……"
    hide WH
    hide ZH
    "对于郑辉突如其来的问题，我不知该如何作答。看到大家都实现了自己当初的梦想，我越发觉得失去了方向，或者说我从来没有过自己的理想……"

    #{显示立绘 QQ 23jy}
    show QQ 23jy at middle with dissolve
    YuanQiaoqiao "智子怎么还没到啊，不是说今天要来的吗？"
    #{显示立绘 XY 23dy}
    show XY 23dy at right with dissolve:
        xoffset -200
    ZhouXiaoyu "是啊，我也联系不上她。说是昨天晚上的飞机，可能是晚点了吧。"
    #{显示立绘 LY 21wx}
    show LY 21wx at left with dissolve
    LiuYang "智子现在怎么样？"
    #{播放BGM b0105  }
    play music "audio/bgm/b0105 jiaoshi.mp3"
    #{显示立绘 XY 23dy}
    hide QQ
    hide LY
    show XY 23dy
    ZhouXiaoyu "在日本的时候，我跟她一直都有联系。她现在在日本一家电视台工作，天天录节目，这次回来也是推了很多工作。"
    #{显示立绘 LY 22wx}
    show LY 22wx at left with dissolve
    LiuYang "智子当年的梦想就是当记者，电视台的工作挺适合她的。"
    hide LY
    hide XY
    "看着刘洋满心欢喜地讲着智子，我的脑海中不由地浮现出十年前的画面。当年智子来中国留学的时候，刘洋是她的同桌。"
    "刘洋当年日语很好，所以和智子聊得很投缘。班里的同学也都看得出他们彼此有好感，看来刘洋果然很喜欢她。"
    #{显示立绘 QQ 22xf}
    show  QQ 22xf at right with dissolve:
        xoffset -200
    YuanQiaoqiao "对了，我们的十年之约大家都还记得吧？"
    #{显示立绘 XY 22dx}
    show XY 22dx at left with dissolve
    ZhouXiaoyu "你说的是那个时光宝盒吧。"
    "十年之约是当时智子回国前与我们的约定，大家将自己的梦想和心愿放在“时光宝盒”中，十年之后再一起打开。"
    #{显示立绘 XY 22jy}
    show XY 22jy
    ZhouXiaoyu "我记得当年好像是放在……"
    #{播放BGM b0107 }
    play music "audio/bgm/b0107 shiguangbaohe.mp3"
    #{显示立绘 LY 21hz}
    hide QQ with dissolve
    show LY 21hz at right with dissolve:
        xoffset -200
    LiuYang "应该不会已经被人打开了吧？过了这么久，还在那里吗？"
    #{显示立绘 ZH 21wx}
    hide XY with dissolve
    show ZH 21wx at left with dissolve
    ZhengHui "不会，不会，当年不是说了嘛，最危险的地方就是最安全的地方。"
    hide ZH
    hide LY
    "当年原本周小雨提议埋在校园的樱花树下，后来还是作罢了。一来担心破坏了树根，二来怕被人发现。"
    "不知道是谁提议说书架后面有一块盖板可以打开，可以放在那里面。盖板后面原本是多媒体设备的工具箱，更换了投屏系统以后就空置了。"
    "郑辉是当时班里的信息课代表，有工具箱的钥匙。于是大家便把“时光宝盒”藏在了那里面。"
    #{显示立绘 XY 22cx}
    show XY 22cx at right with dissolve
    #{显示书架特写图片 w04}
    show w04 at left with dissolve
    ZhouXiaoyu "嘿嘿，我来实习的第一天就检查过了，这个书架一直没有挪动过，应该没有人发现。"
    #{显示立绘 ZH 21gx}
    show ZH 21gx at middle with dissolve
    ZhengHui "刘洋，来搭把手。我们把书架推开吧。"
    #{图片 w04消失
    hide w04 with dissolve
    #{显示立绘 LY 23gx}
    show LY 23gx at left with dissolve
    LiuYang "好嘞。"
    #{播放SE s0109 推开书架声音}
    play sound "audio/se/s0109 shujia.mp3"
    #黑屏
    scene black_bg
    pause 1.0
    #{显示背景 p05 jiaoshixin2}
    scene p05 jiaoshixin2 with dissolve
    "书架上放满了书，加上原本就是钢制的，花了不少力气，终于推开一个人能进出的口子。"
    #{显示箱子背后的特写图片 w05}
    show w05 at left with dissolve
    pause
    #{显示立绘 XY 23wx}
    show XY 23wx at t_right with dissolve
    ZhouXiaoyu "哈哈，就是这里了。"
    #{显示立绘 QQ 21tq}
    show QQ 21tq at middle with dissolve
    YuanQiaoqiao "啊呀！我们没有钥匙啊。"
    #{图片 w05消失}
    hide w05 with dissolve
    hide WH
    hide QQ
    hide XY
    "大家突然想起来，当年为了十年之内不开启这扇回忆之门，大家把钥匙交给了智子保管……"
    "这时，我突然想起了口袋里的那把钥匙。昨天整理房间时，从日语书中掉出来的……"
    #{显示立绘 WH 22rz}
    show WH 22rz at right with dissolve:
        xoffset -200
    me "是不是这把？"
    #{显示钥匙的图片 w02}
    show w02 at left with dissolve
    #{显示立绘 XY 23jy}
    show XY 23jy at middle with dissolve
    ZhouXiaoyu "咦，为什么在你那儿？"
    #{显示立绘 QQ 21xf}
    show QQ 21xf at left with dissolve
    YuanQiaoqiao "别管这些了，赶快试试吧。"
    #{图片 w02消失}
    hide w02 with dissolve
    hide WH
    hide XY
    hide QQ
    "大家都感到很诧异。正准备追问的时候，袁巧巧已经一把抢过钥匙，打开了工具箱。"
    #{显示立绘 QQ 22gx}
    show QQ 22gx at middle with dissolve
    YuanQiaoqiao "果然就是这把钥匙！太棒了！"
    YuanQiaoqiao "哇，在里面！没想到真的能保存那么久，太好玩了，像密室逃脱游戏一样。"
    #{显示立绘 XY 21jy}
    hide QQ with dissolve
    show XY 21jy at right with dissolve:
        xoffset -200
    ZhouXiaoyu "这就是……"
    #{显示时光宝盒的图片 w06}
    show w06 at left with dissolve
    "周小雨拿起略带灰尘的盒子，上面有一把密码锁。"
    #{显示立绘 WH 22zm}
    show WH 22zm at left with dissolve
    me "好熟悉的盒子……"
    me "唉，当年好像没有密码锁啊……。"
    #{显示立绘 XY 21zm}
    show XY 21zm
    ZhouXiaoyu "是个四位数的密码，有多少种组合呢……"
    #{图片 w06消失}
    hide w06 with dissolve

    #{显示选项  文本框居中，选项竖排1 2}
    menu prologue_scene_2_choice_1:
        "A.6561种组合。":
            $ prologue_select[2] = 0
            jump prologue_scene_2_choice_1A
        "B.10000种组合。":
            $ prologue_select[2] = 10
            jump prologue_scene_2_choice_1B

label prologue_scene_2_choice_1A:
    #选择1.
    #{显示立绘 WH 22rz}
    show WH 22rz at middle
    me "大概有6561种组合？"
    #{显示立绘 XY 21zm}
    ZhouXiaoyu "应该不止吧，得有10000种组合吧，这要试到地老天荒了。"
    ZhouXiaoyu "这里还有一张纸条，先看看纸上写了什么吧。"

    jump prologue_scene_2_3

label prologue_scene_2_choice_1B:
    #选择2.
    #好感度参数 +10
    #{显示立绘 WH 22rz}
    show WH 22rz
    me "应该有10000种组合吧。"
    #{显示立绘 XY 21wx}
    ZhouXiaoyu "果然是理工男，算得真快。这要试到地老天荒了。"
    ZhouXiaoyu "这里还有一张纸条，先看看纸上写了什么吧。"

    jump prologue_scene_2_3

label prologue_scene_2_3:
    #{显示立绘 LY 22wx}
    hide XY
    hide WH
    show LY 22wx at left with dissolve
    LiuYang "都是一些文化测试题。看来是有人要考我们。王浩，你来看看。"
    #{显示立绘 WH 22rz}
    show WH 22rz at right with dissolve:
        xoffset -400
    me "这些问题好像在哪里见过……"
    hide WH
    hide LY

    jump prologue_scene_2_3_Baohe

label prologue_scene_2_3_Baohe:
    #{显示题目  文本框居中，选项竖排A B C}
    menu prologue_scene_2_choice_2:
        '日本人迎接新年的时候一般会吃 (____)。'
        "A.年糕":
            $ prologue_answer[2] = 10
        "B.饺子":
            $ prologue_answer[2] = 0
        "C.汤圆":
            $ prologue_answer[2] = 0

    #选择1.年糕
    #好感度参数 +10
    #打开宝盒参数 +1
    #选择 其他选项
    #（直接跳到下一题）

    #{显示题目  文本框居中，选项竖排A B C}
    menu prologue_scene_2_choice_3:
        '日本人在搬家的时候，会赠予近邻 (____)，寄托了长久友好的希冀。'
        "A.年糕":
            $ prologue_answer[3] = 0
        "B.饺子":
            $ prologue_answer[3] = 0
        "C.荞麦面":
            $ prologue_answer[3] = 10

    #选择3.荞麦面
    #好感度参数 +10
    #打开宝盒参数 +1
    #选择 其他选项
    #（直接跳到下一题）

    #{显示题目  文本框居中，选项竖排A B C}
    menu prologue_scene_2_choice_4:
        '(____)是从中国传到日本的民间故事，深受日本人的喜爱。'
        "A.牛郎织女的传说":
            $ prologue_answer[4] = 10
        "B.桃太郎的传说":
            $ prologue_answer[4] = 0
        "C.辉夜姬的传说":
            $ prologue_answer[4] = 0

    #选择答案后跳转
    #选择1. 牛郎织女的传说
    #好感度参数 +10
    #打开宝盒参数 +1
    #选择 其他选项
    #（直接跳到下一题）

    #{显示题目  文本框居中，选项竖排A B C}
    menu prologue_scene_2_choice_5:
        '七夕节时，日本的商店街和车站等地会悬挂长条的装饰物，这种装饰物叫作 (____)。'
        "A.鲤鱼旗":
            $ prologue_answer[5] = 0
        "B.风幡":
            $ prologue_answer[5] = 10
        "C.灯笼":
            $ prologue_answer[5] = 0

    $ Baohe = (prologue_answer[2] + prologue_answer[3] + prologue_answer[4] + prologue_answer[5]) / 10
    if Baohe == 4:

        if chpt1_C_answer_bunka_index < 6:
            $ chpt1_C_answer_bunka_index = 6
        jump prologue_scene_2_3_Baohe_Opened

    jump prologue_scene_2_3_Baohe_NotOpened

    #选择2.prologue_scene_1_1（吹き流し）
    #好感度参数 +10
    #打开宝盒参数 +1
    #选择 其他选项
    #（直接跳到下一题）

label prologue_scene_2_3_Baohe_NotOpened:
    #如打开宝盒参数 不等于4
    #{显示立绘 WH 22rz}
    show WH 22rz at right with dissolve:
        xoffset -200
    me "我来试试是不是这个密码……"
    #{播放SE s01092锁没打开的声音}
    play sound 'audio/se/s01092 dabukaisuo.mp3'
    #{显示立绘 QQ 21tq}
    show QQ 21tq at left with dissolve
    YuanQiaoqiao "好像不对，再检查一下吧。"
    hide QQ
    hide WH
    #宝盒参数归零
    $ Baohe = 0

    jump prologue_scene_2_3_Baohe

label prologue_scene_2_3_Baohe_Opened:
    #如打开宝盒参数 等于4
    #{显示立绘 WH 22rz}
    show WH 22rz at right with dissolve:
        xoffset -200
    me "嗯……题目的答案应该是1312……"
    #{显示立绘 QQ 23wx}
    show QQ 23wx at left with dissolve
    YuanQiaoqiao "或许这个就是密码，赶快试一下。"
    play sound 'audio/se/s0110 kaisuo.mp3'
    hide QQ
    hide WH
    "周小雨转动密码“1312”，密码锁打开了……"
    #{播放SE s0110锁被打开的声音}
    play sound "audio/se/s0110 kaisuo.mp3"
    #{BGM 停止 }
    stop music
    jump prologue_scene_2_4


label prologue_scene_2_4:
    #{显示立绘 QQ 23xf}
    show QQ 23xf at right with dissolve:
        xoffset -200
    YuanQiaoqiao "果然是这个数字，王浩你太厉害了！"
    #{显示立绘 XY2jy}
    show XY 22jy at left with dissolve
    ZhouXiaoyu "啊，是我们当年留下的东西……"
    show w07 at left with dissolve
    hide XY
    hide QQ
    "开启尘封已久的“时光宝盒”，里面有六张颜色各异的彩纸。上面写着每个人的名字：周小雨、刘洋、郑辉、袁巧巧、王浩、高桥智子。"
    #{显示6张颜色不同的彩纸的图片 w07}
    "大家小心翼翼地拿起写着自己名字的彩纸，并打开阅读了起来。"
    hide w07 with dissolve
    #{播放BGM b0102  }
    play music "audio/bgm/b0102 houkagonoyuzora.mp3"
    #{显示立绘 QQ 21gx}
    show QQ 21gx at right with dissolve:
        xoffset -200
    YuanQiaoqiao "说好了大家要公开的，别自己看啊，分享一下嘛。班长，要不你先来吧。"
    #{显示立绘 XY 23bx}
    show XY 23bx at left with dissolve
    ZhouXiaoyu "行啊。我的太普通了。我写的梦想就是“将来成为一名音乐老师”。没想梦想成真，还回到了母校。"
    #{显示立绘 XY 23wx}
    show XY 23wx
    ZhouXiaoyu "大家也来说说吧。"
    hide XY
    hide QQ
    "周小雨催促大家分享自己的梦想和心愿。"
    #{显示立绘 ZH 22gg}
    show ZH 22gg at right with dissolve:
        xoffset -200
    ZhengHui "我的梦想是“做一款自己开发的游戏”，不过现在还在努力中，嘿嘿。"
    #{显示立绘 WH 21my}
    show WH 21my at left with dissolve
    me "马上就会实现了。大家都能坚持自己的梦想，太厉害了。"
    #{显示立绘 XY 23wx}
    hide WH
    hide ZH
    show XY 23wx at right with dissolve:
        xoffset -200
    ZhouXiaoyu "你呢，巧巧？也说说你的梦想呗。"
    #{显示立绘 QQ 22wx}
    show QQ 22wx at left with dissolve
    YuanQiaoqiao "嘻嘻，我当年想做一个“职业coser”，现在想想还挺幼稚的。"
    #{显示立绘 LY 23qx}
    hide XY with dissolve
    show LY 23qx at right with dissolve:
        xoffset -200
    LiuYang "做配音演员不也是二次元嘛，都一样。"
    #{显示立绘 QQ 21sq}
    show QQ 21sq at left with dissolve
    YuanQiaoqiao "拜托，那叫“声优”，可不光配动画作品。"
    #{显示立绘 QQ 21dy}
    show QQ 21dy
    YuanQiaoqiao "别说我了，你的梦想呢，刘洋？"
    #{显示立绘 LY 21hz}
    show LY 21hz
    LiuYang "我……"
    LiuYang "我没什么特别的，就是好好学习天天向上呗。"
    hide LY
    hide QQ
    "突然被袁巧巧这么一问，刘洋显得有些不好意思。"
    #{显示立绘 XY 21jy}
    show XY 21jy at right with dissolve:
        xoffset -200
    ZhouXiaoyu "「彼女に本当の気持ちを伝える」（想告诉她我的心意）。"
    #{显示立绘 XY 21cx}
    show XY 21cx
    ZhouXiaoyu "哈哈，还写日文呢。“她”是谁啊？"
    hide XY with dissolve
    "周小雨偷偷瞄到了刘洋手里彩纸上的内容。"
    #{播放SE s1011 团纸头的声音}
    play sound "audio/se/s0111 zhituan.mp3"
    #{显示立绘 LY 21hz}
    show LY 21hz at right with dissolve:
        xoffset -200
    "刘洋显得有些慌乱，急忙把刚刚打开的彩纸塞进了口袋。"
    #{显示立绘 XY 23cx}
    show XY 23cx at left with dissolve
    ZhouXiaoyu "哎呀，别不好意思了，又不是高中生了，扭扭捏捏的干什么。没想到当年你有暗恋的对象啊。"
    #{显示立绘 LY 22rz}
    show LY 22rz
    LiuYang "别瞎说，没那回事。"
    #{显示立绘 QQ 21xf}
    hide XY
    show QQ 21xf at left with dissolve
    YuanQiaoqiao "哎哟，看来当年的传闻是真的咯。"
    #{显示立绘 ZH 21zj}
    hide LY
    show ZH 21zj at right with dissolve:
        xoffset -200
    ZhengHui "谁啊谁啊，我怎么不知道？"
    #{显示立绘 QQ 21sq}
    show QQ 21sq
    YuanQiaoqiao "切，你这个木瓜脑袋怎么会知道。"
    hide QQ
    hide ZH
    "袁巧巧说的那个传闻应该和智子有关。当年智子和刘洋是同桌，两个人平时就很默契，也一直聊得很开心。"
    "不知是谁说有一天晚上看到刘洋和智子在校园里卿卿我我，你一句我一句便传开了。"
    "但刘洋矢口否认，谣言也就不了了之。"
    "现在看到刘洋在彩纸上写下的心愿，想必当年的传闻……"
    #{显示立绘 LY 23hz}
    show LY 23hz at middle with dissolve
    LiuYang "别瞎猜啦，不是你们想的那样。"
    hide LY with dissolve
    "看到大家都在调侃起哄，刘洋急忙否认。"
    #{停止BGM  }
    stop music
    #{显示立绘 QQ 21xf}
    show QQ 21xf at right with dissolve:
        xoffset -200
    show w08 at left with dissolve
    YuanQiaoqiao "行了行了，别狡辩了。看看智子的心愿不就知道了。"
    hide QQ with dissolve
    "袁巧巧突然从时光宝盒里拿走了智子的心愿纸。"
    hide w08 with dissolve
    #{显示打开的宝盒里只剩下 1张彩纸的图片 w08}

    #{显示立绘 WH 21kx}
    show WH 21kx at right with dissolve:
        xoffset -200
    me "这样不好吧，应该由智子自己来打开才对。"
    #{显示立绘 QQ 21xf}
    show QQ 21xf at left with dissolve
    YuanQiaoqiao "哈哈，该不会你也喜欢智子吧？"
    #{显示立绘 WH 23kx}
    show WH 22kx
    me "哪……哪有……我……"
    #{播放SE s0112跑步的声音}
    play sound 'audio/se/s0112 paobu.mp3'
    hide WH
    hide QQ
    "袁巧巧眼看我要去抢她手中的彩纸，一边转身往走廊上跑，一边打开纸片准备读。"

    #{显示选项  文本框居中，选项竖排1 2}
    menu prologue_scene_2_choice_6:
        "A.抢过袁巧巧手中的彩纸。":
            $ prologue_select[3] = 10
            jump prologue_scene_2_choice_6A
        "B.……":
            $ prologue_select[3] = 0
            jump prologue_scene_2_choice_6B

label prologue_scene_2_choice_6A:
    #选择1.
    #好感度参数 +10
    "或许是不敢面对真相，我不由自主地追了上去……"

    jump prologue_scene_2_5

label prologue_scene_2_choice_6B:
    #选择2.
    #{显示立绘 WH 23jy}
    show WH 23jy at middle with dissolve
    me "……"
    hide WH
    "虽然极力想抑制住自己内心的激动，但我还是不由自主地追了上去……"

    jump prologue_scene_2_5

label prologue_scene_2_5:
    me "等等！"
    #{显示立绘 QQ 22jy}
    show QQ 22jy at middle with dissolve
    YuanQiaoqiao "啊！"
    #{播放SE s0113倒在地上的撞击声 }
    play sound 'audio/se/s0113 zhuangdao.mp3'
    scene black_bg with dissolve
    "伴随着袁巧巧的一声尖叫，不知怎么回事，我突然感觉到身体向前倾斜……
    随后眼前一黑……"

    jump chpt1_1
