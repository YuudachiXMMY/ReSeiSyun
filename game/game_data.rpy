#################################################################
## Hirakana & Katakana
define HiraKataKANA = {
    "a_o" : ["a","i","u","e","o"],
    "ka_ko" : ["ka","ki","ku","ke","ko"],
    "sa_so" : ["sa", "shi", "su", "se", "so"],
    "ta_to" : ["ta", "chi", "tu", "te", "to"],
    "na_no" : ["na","ni","nu","ne","no"],
    "ha_ho" : ["ha","hi","fu","he","ho"],
}

## Dango
define Dango_L1 = ["011ai2", "012au2", "013aki2", "014koi2"]
define Dango_L2 = ["021sushi2", "022suki2", "023uta2", "024tuki2"]
define Dango_L3 = ["031inu2", "032neko2", "033hana2", "034hoshi2"]


#################################################################
## Variables
default HaoGan = 0
# define persistent.lesson1_attempt = []
# Prologue
default prologue_select = [0, 0, 0, 0]
default prologue_answer = [0, 0, 0, 0, 0, 0]
default Baohe = 0

# Chpt 1
default chpt1_select = [0, 0, 0]
default chpt1_answer_bunka = [0, 0, 0]
default chpt1_answer_kana = [0, 0, 0, 0, 0]
default chpt1_answer_tango = [0, 0, 0]
default chpt1_answer_kaiwa = [0, 0, 0]

# Chpt 2
default chpt2_select = [0, 0]
default chpt2_answer_bunka = [0, 0, 0]
default chpt2_answer_kana = [0, 0, 0, 0, 0]
default chpt2_answer_tango = [0, 0, 0]
default chpt2_answer_kaiwa = []

# Chpt 3
default chpt3_select = [0, 0]
default chpt3_answer_bunka = [0, 0, 0]
default chpt3_answer_kana = [0, 0, 0, 0, 0]
default chpt3_answer_tango = [0, 0, 0]
default chpt3_answer_kaiwa = [0, 0]

#################################################################
## Chapter 1
default chpt1_C_answer_kana_index = 0
define chpt1_C_answer_kana = [
    "a","i","u","e","o",
    "ka","ki","ku","ke","ko"
]

default chpt1_C_answer_tango_index = 0
define chpt1_C_answer_tango = [
    "011ai2", "012au2", "013aki2", "014koi2"
]

default chpt1_C_answer_kaiwa_index = 0
define chpt1_C_answer_kaiwa = [

    "智子：“今日はありがとう。王さんはとても日本語がお上手ですね。\n（今天谢谢你的帮助。你的日语说得真好啊。）”我应该说……\n正确回答：{u}いえいえ。{/u}",
    "我：“智子打来的电话？！我应该如何回答……”\n正确回答：{u}こんばんは。{/u}"
]

default chpt1_C_answer_bunka_index = 0
define chpt1_C_answer_bunka = [
    '日本的(____)起源于中国，其核心精神为“和、敬、清、寂”。\n正确答案：{u}茶道{/u}',
    '日本的和服最早受到古代中国的哪种服装的影响？\n正确答案：{u}汉服{/u}',
    '日本人迎接新年的时候一般会吃 (____)。\n正确答案：{u}年糕{/u}',
    '日本人在搬家的时候，会赠予近邻 (____)，寄托了长久友好的希冀。\n正确答案：{u}荞麦面{/u}',
    '(____)是从中国传到日本的民间故事，深受日本人的喜爱。\n正确答案：{u}牛郎织女的传说{/u}',
    '七夕节时，日本的商店街和车站等地会悬挂长条的装饰物，这种装饰物叫作 (____)。\n正确答案：{u}风幡{/u}',
    "日本是先有语言还是先有文字？\n正确答案：{u}先有语言{/u}",
    "日语中“汉字的正用”是指什么意思？\n正确答案：{u}按照汉字原本的意思来使用{/u}",
    "“万叶假名”中的“假”指什么意思？\n正确答案：{u}假借{/u}"
]


#################################################################
## Chapter 2
default chpt2_C_answer_kana_index = 0
define chpt2_C_answer_kana = [
    "sa","shi","su","se","so",
    "ta","chi","tu","te","to"
]

default chpt2_C_answer_tango_index = 0
define chpt2_C_answer_tango = [
    "021sushi2", "022suki2", "023uta2", "024tuki2"
]

default chpt2_C_answer_kaiwa_index = 0
define chpt2_C_answer_kaiwa = [
    "如何用邀请他人和你一起同行？\n正确回答：{u}一緒に行きましょうか。{/u}",
    "如何安慰他人？\n正确回答：{u}大丈夫。気にしないで。{/u}"
]

default chpt2_C_answer_bunka_index = 0
define chpt2_C_answer_bunka = [
    "日本人为什么要在吃饭前要说「いただきます」（我吃咯）？\n正确回答：{u}表示对事物的敬意{/u}",
    '平假名为什么又被称为女手？\n正确答案：{u}早期平假名多为女性所用{/u}',
    '平假名的起源是？\n正确答案：{u}汉字的草书{/u}',
    "片假名现在的功能是什么？\n正确回答：{u}标注外国的人名和地名、突出需要强调的词{/u}"
]


#################################################################
## Chapter 3
default chpt3_C_answer_kana_index = 0
define chpt3_C_answer_kana = [
    "na","ni","nu","ne","no",
    "ha","hi","fu","he","ho"
]

default chpt3_C_answer_tango_index = 0
define chpt3_C_answer_tango = [
    "031inu2", "032neko2", "033hana2", "034hoshi2"
]

default chpt3_C_answer_kaiwa_index = 0
define chpt3_C_answer_kaiwa = [
    "如何主动提出帮别人带路？\n正确回答：{u}「私でよければ、案内します」（可以的话，我带你去吧）{/u}",
    "如何夸奖对方可爱？\n正确回答：{u}「とても可愛いですよ」（非常可爱哦）{/u}"
]

default chpt3_C_answer_bunka_index = 0
define chpt3_C_answer_bunka = [
    '徐福东渡的故事最早在哪本书中有记录？\n正确答案：{u}《史记·秦始皇本纪》中有相关的记载{/u}',
    '日本佐贺市金立神社举办的大型祭祀活动祭拜的人是谁？\n正确答案：{u}徐福{/u}',
    '中国的铁器、铜器、丝帛在哪个朝代传入了日本？\n正确答案：{u}在两汉时期，中国的铁器、铜器、丝帛等传入了日本{/u}'
]