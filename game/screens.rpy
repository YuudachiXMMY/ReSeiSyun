################################################################################
## Initialization
################################################################################

init offset = -1

define config.auto_voice = "audio/voice/{id}.mp3"


################################################################################
## Variables
################################################################################

default persistent.agreements_yes = False

default persistent.ug = False
# default persistent.favorability_chpt1 = 0
# default persistent.favorability_chpt2 = 0
# default persistent.favorability_chpt3 = 0
# default persistent.favorability_chpt4 = 0
# default persistent.favorability_chpt5 = 0
# default persistent.favorability_chpt6 = 0
# default persistent.favorability_chpt7 = 0


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


label splashscreen: # before_main_menu:
    if not persistent.agreements_yes:
        call screen agreements

# AGM
screen agreements_menu(title, yinitial=0.0):

    # style_prefix "agreements_menu"

    # frame:
    #     background "sl_bg" align(0.5,0.5)

    #     hbox:

    frame:
        background "sl_bg"
        left_margin 214
        right_margin 214
        top_margin 82
        bottom_margin 82

        frame:
            # style "agreements_menu"
            background None
            left_margin 50
            right_margin 50
            top_margin 20
            bottom_margin 20

            viewport:
                yinitial yinitial
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True

                side_yfill True

                vbox:
                    transclude


    # textbutton _("Return"):
    #     style "return_button"

    #     action Return()


screen agreements():
    zorder 102
    modal True
    predict False

    # add "sl_bg" align(0.5,0.5)

    ## This use statement includes the agreements_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the agreements_menu
    ## screen.
    use agreements_menu(_("Agreements")):

        style_prefix "about"

        vbox:

            label "用户服务协议"
            null height 20

            hbox:
                text _("在此特别提醒各位用户认真阅读、充分理解本《用户服务协议》（下称《协议》）——用户应认真阅读充分理解本《协议》中各条款。您的安装、使用、获取和登录“重启青春”等行为将视为对本《协议》的接受，并同意接受本《协议》各项条款的约束。") style "about_small"

            null height 20

            hbox:
                text _("“重启青春”是由郭侃亮制作、华东理工大学出版社有限公司出品，并由上海海笛数字出版科技有限公司上架发行同时提供运营支持和客户服务支持的。") style "about_small"

            null height 20

            hbox:
                text _("本《协议》是您（下称“用户”）与华东理工大学出版社有限公司（以下又称“出品方”）之间关于用户下载、安装、注册、使用软件；以及使用出品方提供的相关服务所订立的协议。本《协议》描述出品方与用户之间关于“软件”知识产权、许可使用及服务相关方面的权利义务。“用户”是指通过出品方提供的获取软件授权的途径获得软件产品授权许可以及使用出品方提供的相关服务的个人或组织。") style "about_small"

            null height 20

            hbox:
                text _("本《协议》可由出品方随时更新，更新后的协议条款一旦公布即代替原来的协议条款，恕不再另行通知。用户可重新下载安装本软件查阅最新版协议条款。在出品方修改《协议》条款后，如果用户不接受修改后的条款，请立即停止使用出品方提供的软件和服务，用户继续使用出品方提供的软件和服务将被视为已接受了修改后的协议。") style "about_small"

            null height 20

            hbox:
                text _("1. 知识产权声明") style "about_small"

            null height 20

            hbox:
                text _("本“软件”的一切版权、商标权、专利权、商业秘密等知识产权，以及与“软件”相关的所有信息内容，包括但不限于：文字表述及其组合、图标、图饰、图表、色彩、界面设计、版面框架、录像、动画、录音、文字、图像、有关数据、印刷材料、或电子文档等均受中华人民共和国著作权法、商标法、专利法、反不正当竞争法和相应的国际条约以及其他知识产权法律法规的保护，除涉及第三方授权的软件或技术外，归制作方所有。用户不得修改、改编、翻译本软件提供的内容，不得通过反编译、反向工程、反汇编或其它方式从本软件得到源代码。") style "about_small" color "#555"

            null height 20

            hbox:
                text _("2. 软件授权范围") style "about_small"

            null height 20

            hbox:
                text _("2.1 用户可以在手机或移动设备上安装、使用、显示、运行本软件。") style "about_small" color "#555"

            null height 20

            hbox:
                text _("2.2 保留权利：未明示授权的其他一切权利仍归制作方所有，用户使用其他权利时须另外取得制作方的书面同意。") style "about_small" color "#555"

            null height 20

            hbox:
                text _("3. 隐私保护") style "about_small"

            null height 20

            hbox:
                text _("本“软件”并未收集任何个人信息，用户在使用过程中产生的一切数据均存储在用户自身设备上，并由其承担系统受损、资料丢失以及其它任何风险。") style "about_small" color "#555"

            null height 20

            hbox:
                text _("4. 服务内容") style "about_small"

            null height 20

            hbox:
                text _("4.1 出品方服务的具体内容由出品方根据实际情况提供。") style "about_small" color "#555"

            null height 20

            hbox:
                text _("4.2 除非本服务协议另有其它明示规定，出品方所推出的新产品、新功能、新服务，均受到本服务协议之规范。") style "about_small" color "#555"

            null height 20

            hbox:
                text _("4.3 用户明确同意其使用出品方服务所存在的风险将完全由其自己承担。用户理解并接受下载或通过出品方服务取得的任何信息资料取决于用户自己，并由其承担系统受损、资料丢失以及其它任何风险。") style "about_small" color "#555"

            null height 20

            hbox:
                text _("4.4 出品方保留随时地、不事先通知地、不需要任何理由地、单方面地中止、终止提供相关服务的权利。该等中止、终止，可能是因为出品方解散、注销、合并、分立，也可能是因为出品方将软件运营权转让给了第三方，还可能是因为软件使用的内容版权到期，还可能是因为国家法律、法规、政策及国家机关的命令或者其他的诸如地震、火灾、海啸、台风、罢工、战争等不可抗力事件，还可能是上列原因之外的其他原因。若出品方的该等中止、终止行为给你造成任何损失的，您同意不向出品方主张任何赔偿或其他责任。") style "about_small" color "#555"

            null height 20

            hbox:
                text _("5. 法律责任与免责") style "about_small"

            null height 20

            hbox:
                text _("5.1 用户违反本《协议》或相关的服务条款的规定，导致或产生的任何第三方主张的任何索赔、要求或损失，包括合理的律师费，用户同意赔偿出品方与出品方关联公司及合作公司，并使之免受损害。") style "about_small" color "#555"

            null height 20

            hbox:
                text _("5.2 使用本“软件”由用户自己承担风险，出品方对本“软件”不作任何类型的担保，不论是明示的、默示的或法令的保证和条件，包括但不限于本“软件”的适销性、适用性、无病毒、无疏忽或无技术瑕疵问题、所有权和无侵权的明示或默示担保和条件，对在任何情况下因使用或不能使用本“软件”所产生的直接、间接、偶然、特殊及后续的损害及风险，出品方及合作单位不承担任何责任。") style "about_small" color "#555"

            null height 20

            hbox:
                text _("5.3 使用本“软件”涉及到互联网服务，可能会受到各个环节不稳定因素的影响，存在因不可抗力、计算机病毒、黑客攻击、系统不稳定、非法内容信息、骚扰信息屏蔽以及其他任何网络、技术、通信线路、信息安全管理措施等原因造成的用户的经济损失，出品方不承担任何责任。") style "about_small" color "#555"

            null height 20

            hbox:
                text _("5.4 用户因第三方如电信部门的通讯线路故障、技术问题、网络、电脑故障、系统不稳定性及其他各种不可抗力原因而遭受的一切损失，出品方不承担责任。") style "about_small" color "#555"

            null height 20

            hbox:
                text _("5.5 因技术故障等不可抗事件影响到服务的正常运行的，出品方承诺在第一时间内与相关单位配合，及时处理进行修复，但用户因此而遭受的一切损失，出品方及合作单位不承担责任。") style "about_small" color "#555"

            null height 20

            hbox:
                text _("6. 其他条款") style "about_small"

            null height 20

            hbox:
                text _("6.1 本《协议》所定的任何条款的部分或全部无效者，不影响其它条款的效力。") style "about_small" color "#555"

            null height 20

            hbox:
                text _("6.2 本《协议》的解释、效力及纠纷的解决，适用于中华人民共和国法律。若用户和服务方之间发生任何纠纷或争议，首先应友好协商解决，协商不成的，用户在此完全同意将纠纷或争议提交出品方公司所在地即上海有管辖权的人民法院管辖。") style "about_small" color "#555"

            null height 20

            hbox:
                text _("6.3 本《协议》版权由出品方所有，出品方保留一切解释权利。本文中提及的软件和服务名称有可能为出品方的注册商标或商标，受法律保护。") style "about_small" color "#555"

            null height 20

            label "用户隐私政策"
            null height 20


            hbox:
                text _("发布时间：2023年5月14日") style "about_small_alignLast" color "#555" xalign 1.0
            null height 20
            hbox:
                text _("生效时间：2023年5月14日") style "about_small_alignLast" color "#555"
            null height 20

            hbox:
                text _("本用户隐私政策所适用的“重启青春” 移动应用，是由郭侃亮制作、华东理工大学出版社有限公司（地址：上海市徐汇区梅陇路130号）出品，并由上海海笛数字出版科技有限公司（地址：上海市郭守敬路498号22号楼）上架发行同时提供运营支持和客户服务支持的。本隐私政策所适用的用户（以下称“用户”或“您”）是指通过“重启青春” 移动应用以及相关软件及网络服务获得各种在线的和线下的服务（以下统称“重启青春”）的用户。非常感谢您对郭侃亮制作团队、华东理工大学出版社有限公司、上海海笛数字出版科技有限公司（以下统称“我们”）的信任和支持，我们尊重并保护您的隐私。本政策与您使用“重启青春”的服务关系紧密，我们建议您仔细阅读并理解本政策全部内容，在确认充分理解并同意后使用“重启青春”产品或服务。{b}如您对本政策内容有任何疑问、意见或建议，请及时通过客服热线（4000213100）咨询，如果不同意本政策的任何内容或者无法理解本政策相关内容，请您立即停止访问和使用“重启青春”。{/b}") style "about_small"

            null height 20

            hbox:
                text _("{b}一、我们如何收集个人信息：{/b}") style "about_small"
            null height 20

            hbox:
                text _("  重启青春App为纯离线应用，无需创建账号，我们也未收集任何用户相关个人信息。") style "about_small" color "#555"

            null height 20

            hbox:
                text _("{b}（一）系统权限说明{/b}") style "about_small"
            null height 20

            hbox:
                text _("您在使用“重启青春”对应服务时不需要调用您的设备功能权限。如出现调用设备功能权限的申请，您可能下载了非正版软件，请您立即停止访问和使用“重启青春”。") style "about_small" color "#555"

            null height 20

            hbox:
                text _("{b}（二）其他{/b}") style "about_small"
            null height 20

            hbox:
                text _("请您理解，我们向你提供的服务是不断更新和发展的。如您选择使用了前述说明当中尚未涵盖的其他服务，基于该服务我们需要收集您的信息的，我们会通过页面提示、交互流程或协议约定的方式另行向您说明信息收集的范围与目的，并征得您的同意。") style "about_small" color "#555"

            null height 20

            hbox:
                text _("{b}二、对第三方责任的声明{/b}") style "about_small"
            null height 20

            hbox:
                text _("  “重启青春”本未接入任何第三方SDK。") style "about_small" color "#555"

            null height 20

            hbox:
                text _("三、未成年人隐私权特别约定") style "about_small"

            null height 20

            hbox:
                text _("1、我们期望父母或监护人指导未成年人使用我们的服务。我们承诺未收集任何未成年人的个人信息。") style "about_small" color "#555"

            null height 20

            hbox:
                text _("2、{color=#111}{b}如您为未成年人，建议请您的父母或监护人阅读本政策，并在征得您父母或监护人同意的前提下使用我们的服务。{/b}如您的监护人不同意您按照本政策使用我们的服务，请您立即终止使用我们的服务。") style "about_small" color "#555"

            null height 20

            hbox:
                text _("{b}四、本政策的适用及更新{/b}") style "about_small"

            null height 20

            hbox:
                text _("{b}1、本隐私政策适用于“重启青春”向您提供的所有服务。{/b}") style "about_small"

            null height 20

            hbox:
                text _("需要特别说明的是，本隐私政策不适用“重启青春”关联方、“重启青春”合作机构或其他第三方向你提供的服务。“重启青春”也可能含有到其他网站的链接，我们会依据法律法规的要求采取必要措施对相关网站进行审查（包括审查网站经营资质、通过技术手段对相关网站的安全情况进行合理且初步识别、督促该网站经营者根据法律规定保护您的个人信息安全），但我们无法保证该链接网站的运营方会按照我们的要求采取保护措施。{color=#111}{b}我们建议您查看该网站的隐私权政策，了解他们如何处理你的信息，以便审慎决策。{/b}") style "about_small" color "#555"

            null height 20

            hbox:
                text _("2、我们与您达成的其他关于个人信息和隐私的条款视为对本政策的补充，本政策存在未涉及内容的，适用其他条款的约定。若因新增产品、服务、功能且需收集、使用、提供您的个人信息的，我们将另行获取您的同意。") style "about_small" color "#555"

            null height 20

            hbox:
                text _("{b}发生下列重大变化情形并可能导致您在本政策项下权利的实质减损或产生重大影响时，我们会适时对本政策进行更新：{/b}") style "about_small"

            hbox:
                text _("""{b}
（1）我们的基本情况发生变化，例如：兼并、收购、重组引起的所有者变更；
（2）收集、存储、使用个人信息的范围、目的、规则发生变化；
（3）对外提供个人信息的对象、范围、目的发生变化；
（4）您访问和管理个人信息的方式发生变化；
（5）数据安全能力、信息安全风险发生变化；
（6）用户询问、投诉的渠道和机制，以及外部纠纷解决机构及联络方式发生变化；
（7）其他可能对您的个人信息权益产生重大影响的变化。{/b}""") style "about_small"

            null height 20

            hbox:
                text _("{b}如本政策发生更新，我们将以“重启青春”页面公告的方式来通知您。为了您能及时接收到通知，建议您在联系方式更新时及时通知我们。如您在本政策更新生效后继续使用“重启青春”服务，即表示您已充分阅读、理解并接受更新后的政策并愿意受更新后的政策约束。{/b}") style "about_small"

            null height 20

            hbox:
                text _("{b}您可以在“重启青春”查看本政策。我们鼓励您在每次使用“重启青春”时都查阅我们的隐私政策。{/b}") style "about_small"

            null height 20

            hbox:
                text _("{b}五、联系我们{/b}") style "about_small"

            null height 20

            hbox:
                text _("1、华东理工大学出版社的联系地址为：上海市徐汇区梅陇路130号，上海海笛数字出版科技有限公司的联系地址为：上海市郭守敬路498号22号楼。") style "about_small" color "#555"

            null height 20

            hbox:
                text _("2、我们成立了专门的个人信息保护小组，如有个人信息保护的相关问题，请与我们联系，邮箱地址：jacky@haidii.com。") style "about_small" color "#555"

            null height 20

            hbox:
                text _("{b}六、投诉反馈渠道{/b}") style "about_small"

            null height 20

            hbox:
                text _("{b}投诉反馈受理电话：4000213100 （工作日9:00-18:00）{/b}") style "about_small"

            null height 20

            hbox:
                text _("{b}邮箱地址：service@mingshukeji.com（受理书面投诉）{/b}") style "about_small"

            null height 20


            hbox:
                xalign 0.5
                textbutton _("拒绝"):
                    action Quit(confirm=False)
                textbutton _("同意"):
                    action SetVariable("persistent.agreements_yes", True), Hide("agreements"),Return()



style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    font "SourceHanSansCN-Bold.otf"
    size gui.label_text_size

style about_small:
    font "SourceHanSansHW-VF.ttf.ttc"
    color "#000"
    size 22
    minwidth 260
    text_align 0.0
    yalign 0.0

style about_small_title:
    font "SourceHanSansHW-VF.ttf.ttc"
    color "#000"
    size 24
    minwidth 260
    text_align 0.0
    yalign 0.0

style about_small_alignLast:
    font "SourceHanSansHW-VF.ttf.ttc"
    color "#000"
    size 24
    minwidth 260
    text_align 1.0
    yalign 0.0

## Review ##################################################################
##

screen kana_review():

    tag menu

    use review_slots(_("假名回顾"))


screen vocab_review():

    tag menu

    use review_slots(_("单词回顾"))


# Cancel
# screen conversation_review():

#     tag menu

#     use review_slots(_("对话回顾"))


screen bunka_review():

    tag menu

    use review_slots(_("文化常识"))


screen review_slots(title):

    tag menu

    # if main_menu:
    #     add "main_bg"

    add "bg_cover"

    # 假名回顾
    if renpy.get_screen("kana_review"):
        button:
            xysize(206, 68)
            idle_background "sl_sl_btn_idle"
            hover_background "sl_sl_btn_hover"
            text "单词回顾":
                align(.3, .5)
                style "sl_page"
                size 36 color "#ffffff"
            xalign 0.03 yalign 0.22
            action ShowMenu("vocab_review")
        button:
            xysize(206, 68)
            idle_background "sl_sl_btn_idle"
            hover_background "sl_sl_btn_hover"
            text "文化常识":
                align(.3, .5)
                style "sl_page"
                size 36 color "#ffffff"
            xalign 0.03 yalign 0.31
            action ShowMenu("bunka_review")
        add "sl_bg" align(0.5, 0.5)
        # add "sl_sl_btn_hover" xalign 0.03 yalign 0.22
        button:
            xysize(206, 68)
            idle_background "sl_sl_btn_hover"
            hover_background "sl_sl_btn_hover"
            text "假名回顾":
                align(.3, .5)
                style "sl_page"
                size 36 color "#50350f"
            xalign 0.03 yalign 0.13
            action NullAction()
    # 单词回顾
    elif renpy.get_screen("vocab_review"):
        button:
            xysize(206, 68)
            idle_background "sl_sl_btn_idle"
            hover_background "sl_sl_btn_hover"
            text "假名回顾":
                align(.3, .5)
                style "sl_page"
                size 36 color "#ffffff"
            xalign 0.03 yalign 0.13
            action ShowMenu("kana_review")
        button:
            xysize(206, 68)
            idle_background "sl_sl_btn_idle"
            hover_background "sl_sl_btn_hover"
            text "文化常识":
                align(.3, .5)
                style "sl_page"
                size 36 color "#ffffff"
            xalign 0.03 yalign 0.31
            action ShowMenu("bunka_review")
        add "sl_bg" align(0.5, 0.5)
        # add "sl_sl_btn_hover" xalign 0.03 yalign 0.13
        button:
            xysize(206, 68)
            idle_background "sl_sl_btn_hover"
            hover_background "sl_sl_btn_hover"
            text "单词回顾":
                align(.3, .5)
                style "sl_page"
                size 36 color "#50350f"
            xalign 0.03 yalign 0.22
            action NullAction()
    # 文化常识
    elif renpy.get_screen("bunka_review"):
        button:
            xysize(206, 68)
            idle_background "sl_sl_btn_idle"
            hover_background "sl_sl_btn_hover"
            text "假名回顾":
                align(.3, .5)
                style "sl_page"
                size 36 color "#ffffff"
            xalign 0.03 yalign 0.13
            action ShowMenu("kana_review")
        button:
            xysize(206, 68)
            idle_background "sl_sl_btn_idle"
            hover_background "sl_sl_btn_hover"
            text "单词回顾":
                align(.3, .5)
                style "sl_page"
                size 36 color "#ffffff"
            xalign 0.03 yalign 0.22
            action ShowMenu("vocab_review")
        add "sl_bg" align(0.5, 0.5)
        # add "sl_sl_btn_hover" xalign 0.03 yalign 0.13
        button:
            xysize(206, 68)
            idle_background "sl_sl_btn_hover"
            hover_background "sl_sl_btn_hover"
            text "文化常识":
                align(.3, .5)
                style "sl_page"
                size 36 color "#50350f"
            xalign 0.03 yalign 0.31
            action NullAction()

    if renpy.get_screen("kana_review"):
        $ review_tmp_lst = chpt1_C_answer_kana
        $ review_tmp_lst_index = chpt1_C_answer_kana_index
    elif renpy.get_screen("vocab_review"):
        $ review_tmp_lst = chpt1_C_answer_tango
        $ review_tmp_lst_index = chpt1_C_answer_tango_index
    elif renpy.get_screen("bunka_review"):
        $ review_tmp_lst = chpt1_C_answer_bunka
        $ review_tmp_lst_index = chpt1_C_answer_bunka_index
    else:
        $ review_tmp_lst = ["Error"]

    if review_tmp_lst_index != 0:
        use review_menu(_("Review"), scroll=("vpgrid" if 1010 else "viewport"), yinitial=0.0):

            style_prefix "review"

            if renpy.get_screen("kana_review") or renpy.get_screen("vocab_review"):
                for i in range(0, review_tmp_lst_index):
                    window:
                        xfill True yfill True
                        if renpy.get_screen("kana_review"):
                            xysize(273, 251)
                            imagebutton:
                                xysize(246, 251)
                                idle "images/HiraKataKANA/"+str(review_tmp_lst[i])+".png"
                                hover "images/HiraKataKANA/"+str(review_tmp_lst[i])+"2.png"
                                action Play("sound", "audio/se/sushiyin/"+str(review_tmp_lst[i])+".mp3")
                        else:
                            xysize(681, 356)
                            imagebutton:
                                xysize(601, 356)
                                idle "images/wupin/danci/"+str(review_tmp_lst[i])+"s.png"
                                hover "images/wupin/danci/"+str(review_tmp_lst[i])+"s.png"
                                action Play("sound", "audio/se/sushiyin/"+str(review_tmp_lst[i])+".mp3")
                        # window:
                        #     xysize(1336, 158)
                        #     xfill True yfill True
                        #     text str(i):
                        #         xoffset 40 yoffset 10
                        #         font "SourceHanSansCN-Bold.otf"
                        #         color "#000000"

            else:
                for i in review_tmp_lst:
                    window:
                        background "review_button_bg"
                        window:
                            xysize(1336, 158)
                            xfill True yfill True
                            text str(i):
                                xoffset 40 yoffset 10
                                font "SourceHanSansCN-Bold.otf"
                                color "#000000"

    imagebutton:
        xalign 0.87 yalign 0.1
        auto "sl_close_%s"
        action Return()


style review_window is empty

style review_window:
    xfill True
    yfill True
    xsize 1370
    ysize 158


screen review_menu(title, scroll=None, yinitial=0.0):

    frame:
        xysize(1623, 1010)
        background None
        align(0.5, 0.5)

        top_padding 130
        bottom_padding 100
        left_padding 130

        if scroll == "vpgrid":

            vpgrid:
                # xysize(1623, 1010)
                # yinitial yinitial

                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True

                side_yfill True

                transclude

                if renpy.get_screen("kana_review"):
                    cols 5
                    xspacing 0
                    yspacing 20
                elif renpy.get_screen("vocab_review"):
                    cols 2
                    # xspacing 40
                    yspacing 40
                else:
                    cols 1
                    spacing 40

        else:

            transclude


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

image textbox_bg:
    "gui/textbox.png"
    xalign 0.5
    yalign 1.0
    alpha 0.9

image namebox_bg:
    "gui/namebox.png"
    alpha 0.9

style window:
    xalign 0.5
    xfill True
    # yalign gui.textbox_yalign
    yalign 0.85
    ysize gui.textbox_height

    # background Image("gui/textbox.png", xalign=0.5, yalign=1.0, alpha=0.6)
    background "textbox_bg"

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize 285# gui.namebox_width
    ypos gui.name_ypos
    ysize 86# gui.namebox_height

    background Frame("namebox_bg", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign 0.55 # gui.name_xalign
    yalign 0.4

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5
    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    yalign 0.5


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu and renpy.get_screen("say"):

        window:
            xsize 520 ysize 81
            align(1.0, 0.98)
            background "quick_bg"

            imagebutton:
                yalign 0.5 xalign 0.125
                auto "quick_skip_%s"
                action Skip() alternate Skip(fast=False, confirm=True)

            imagebutton:
                yalign 0.5 xalign 0.32
                auto "quick_hist_%s"
                action ShowMenu("history")

            imagebutton:
                yalign 0.5 xalign 0.55
                auto "quick_quicksave_%s"
                # action QuickSave(message=u'已快速保存', newest=True)
                action ShowMenu("save")

            imagebutton:
                yalign 0.5 xalign 0.88
                auto "quick_system_%s"
                action Show("r_menu", dissolve)

    if not renpy.get_screen("save") or not renpy.get_screen("load"):
        key "right_click_menu" action Show("r_menu")


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True


## Right screen ###########################################################
##
## This screen is activated by clicking the settings button in quick menu

screen r_menu():
    zorder 101
    modal True

    imagebutton:
        auto "blank_%s"
        action Hide("r_menu",dissolve)

    style_prefix "r_menu"

    frame:

        vbox:
            xalign 0.7 yalign 0.5
            # spacing 16
            if not renpy.variant("small"):
                spacing 23
            else:
                spacing 23
            textbutton _("存档") action Hide("r_menu"), ShowMenu("save"):
                xalign 0.5
            textbutton _("读档") action Hide("r_menu"), ShowMenu("load"):
                xalign 0.5
            textbutton _("文本回放") action Hide("r_menu", transition=None), ShowMenu("history"):
                xalign 0.5
            textbutton _("复习回顾") action Hide("r_menu", transition=None), ShowMenu("kana_review"):
                xalign 0.5
            textbutton _("设置") action Hide("r_menu"), ShowMenu("preferences"):
                xalign 0.5
            textbutton _("返回标题") action Hide("r_menu"), MainMenu():
                xalign 0.5
            textbutton _("结束旅程") action Quit(confirm=True):
                xalign 0.5

        vbox:
            xalign 0.22 yalign 0.5
            spacing 25

            #存档
            hbox:
                imagebutton:
                    auto "r_menu_save_%s"
                    action Hide("r_menu"), ShowMenu("save")

            #读档
            hbox:
                imagebutton:
                    auto "r_menu_load_%s"
                    action Hide("r_menu"), ShowMenu("load")

            #文本回放
            hbox:
                imagebutton:
                    auto "r_menu_history_%s"
                    action Hide("r_menu", transition=None), ShowMenu("history")

            #复习回顾
            hbox:
                imagebutton:
                    auto "r_menu_review_%s"
                    # TODO
                    action Hide("r_menu", transition=None), ShowMenu("kana_review")

            #设置
            hbox:
                imagebutton:
                    auto "r_menu_setting_%s"
                    action Hide("r_menu"), ShowMenu("preferences")

            #返回标题
            hbox:
                imagebutton:
                    auto "r_menu_mainmenu_%s"
                    action Hide("r_menu"), MainMenu()

            #退出游戏
            hbox:
                imagebutton:
                    auto "r_menu_exit_%s"
                    action Quit(confirm=True)

style r_menu_frame:
    align(.85,.25)
    xysize(349, 520)
    background "r_menu_background"

style r_menu_textbutton:
    size 32


## Info screen ############################################################
##
## Game Infomation

screen info():
    zorder 101
    # tag main_menu

    add "gui/main/info_bg.png" zoom .74

    on 'show' action Play('music', "audio/bgm/ztq_zw.mp3")

    textbutton _("返回"):
        style "return_button"
        action Play('music', "audio/bgm/ztq_ry.mp3"), ShowMenu("main_menu"), Return() ,Hide("info")

    textbutton _("阅读 用户协议及隐私条款"):
        align(0.5,0.99)
        action Show("agreements")

################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

# define config.main_menu_music = 'audio/bgm/ztq_ry.mp3'
screen navigation():
    # tag main_menu

    on 'show' action Play('music', "audio/bgm/ztq_ry.mp3")

    if persistent.debug:
        text "debug: "+str(persistent.debug) xalign 0 yalign 0

        $tmp=""
        for i in prologue_select:
            $tmp += str(i)+" "
        text "prologue_select: "+tmp xalign 0 yalign 0.03

        $tmp=""
        for i in prologue_answer:
            $tmp += str(i)+" "
        text "prologue_answer: "+tmp xalign 0 yalign 0.06

        text "宝盒: "+str(Baohe) xalign 0 yalign 0.09
        text "基础好感: "+str(HaoGan) xalign 0 yalign 0.12

        $tmp=""
        for i in chpt1_select:
            $tmp += str(i)+" "
        text "chpt1_select: "+tmp xalign 0 yalign 0.15

        $tmp=""
        for i in chpt1_answer_bunka:
            $tmp += str(i)+" "
        text "chpt1_answer_bunka: "+tmp xalign 0 yalign 0.18

        $tmp=""
        for i in chpt1_answer_kana:
            $tmp += str(i)+" "
        text "chpt1_answer_kana: "+tmp xalign 0 yalign 0.21

        $tmp=""
        for i in chpt1_answer_tango:
            $tmp += str(i)+" "
        text "chpt1_answer_tango: "+tmp xalign 0 yalign 0.24

    if main_menu:
        # add "main_bg"
        add "gui/main/logo.png" xalign 1.0 yalign 1.0

    if main_menu:
        imagebutton:
            xalign 0.05 yalign 0.05
            idle "gui/main/start.png"
            hover "gui/main/start_hover.png"
            action Start()

        imagebutton:
            xalign 0.05 yalign 0.18
            idle "gui/main/load.png"
            hover "gui/main/load_hover.png"
            action ShowMenu("load")

        imagebutton:
            xalign 0.05 yalign 0.31
            idle "gui/main/info.png"
            hover "gui/main/info_hover.png"
            action ShowMenu("info")

        # if renpy.variant("small"):
        imagebutton:
            xalign 0.05 yalign 0.44
            idle "gui/main/quit.png"
            hover "gui/main/quit_hover.png"
            action Quit(confirm=True)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    # frame:
    #     style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu_test.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu_test.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45

style return_button_text:
    color "#fff"


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("保存"))


screen load():

    tag menu

    use file_slots(_("读取游戏"))


screen file_slots(title):

    fixed:

        if main_menu:
            add "main_bg"

        add "bg_cover"

        if renpy.get_screen("load"):
            if not main_menu:
                button:
                    xysize(206, 68)
                    idle_background "sl_sl_btn_idle"
                    hover_background "sl_sl_btn_hover"
                    text "存档":
                        align(.3, .5)
                        style "sl_page"
                        size 36 color "#ffffff"
                    xalign 0.03 yalign 0.13
                    action ShowMenu("save")
            # else:
            #     add "sl_save_btn_idle" xalign 0.25 yalign 0.09
            add "sl_bg" align(0.5, 0.5)
            # add "sl_sl_btn_hover" xalign 0.03 yalign 0.22
            button:
                xysize(206, 68)
                idle_background "sl_sl_btn_hover"
                hover_background "sl_sl_btn_hover"
                text "读档":
                    align(.3, .5)
                    style "sl_page"
                    size 36 color "#50350f"
                xalign 0.03 yalign 0.22
                action NullAction()
        elif renpy.get_screen("save"):
            button:
                xysize(206, 68)
                idle_background "sl_sl_btn_idle"
                hover_background "sl_sl_btn_hover"
                text "读档":
                    align(.3, .5)
                    style "sl_page"
                    size 36 color "#ffffff"
                xalign 0.03 yalign 0.22
                action ShowMenu("load")
            add "sl_bg" align(0.5, 0.5)
            # add "sl_sl_btn_hover" xalign 0.03 yalign 0.13
            button:
                xysize(206, 68)
                idle_background "sl_sl_btn_hover"
                hover_background "sl_sl_btn_hover"
                text "存档":
                    align(.3, .5)
                    style "sl_page"
                    size 36 color "#50350f"
                xalign 0.03 yalign 0.13
                action NullAction()

        imagebutton:
            xalign 0.47 yalign 0.9
            auto "sl_page_previous_%s"
            action FilePagePrevious(auto=False, quick=False)

        if FilePageName() == "10":
            text _(FilePageName()):
                xalign 0.5 yalign 0.905
                style "sl_page"
        else:
            text _(str(0) + FilePageName()):
                xalign 0.5 yalign 0.905
                style "sl_page"

        imagebutton:
            xalign 0.53 yalign 0.9
            auto "sl_page_next_%s"
            action FilePageNext(max=10, auto=False, quick=False)

        imagebutton:
            xalign 0.87 yalign 0.1
            auto "sl_close_%s"
            action Return()

        grid 3 3:
            style_prefix "slot"
            align(0.5, 0.5)
            xspacing 40
            yspacing 30

            for i in range (1, 10):
                button:
                    xysize(418, 256)
                    idle_background "sl_slot_bg"
                    hover_background "sl_slot_bg_hover"
                    action FileAction(i)
                    add "sl_slot_bg" align(0.5,0.5)
                    # text FileTime(i, format=_("{#file_time}%Y年%B%d日  %H:%M"), empty=_("")):
                    #     color "#fff" xalign 0.5 ypos 240 size 30
                    # # Delete Slot
                    # if FileLoadable(i):
                    #     imagebutton:
                    #         xalign 1.0
                    #         auto "sl_delete_%s"
                    #         action FileDelete(i)
                    # else:
                    if True:
                        # FileSlotName(i, int(FileCurrentPage()))
                        $ cur_page = FileCurrentPage()
                        if cur_page == "1":
                            $ num = i
                        else:
                            $ num = i - 1
                        $ res = str(int(cur_page) - 1) + "%s"%str(num)
                        text str(res):
                            align(0.5, 0.5)
                            style "sl_page"
                            size 56 bold True
                        # text "NO DATA":
                        #     align(0.5, 0.7)
                        #     style "sl_page"
                        #     size 18 bold True
                    add FileScreenshot(i) align(0.5,0.5) size(389, 230)
                    key "save_delete" action FileDelete(i)



style sl_page is text

style sl_page_text:
    xalign 0.5 yalign 0.845
    size 42
    # font "SourceHanSansCN-Bold.otf"
    color "#50350f"


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():


    if main_menu:
        add "main_bg"

    add "bg_cover"

    add 'sl_bg' align(0.5, 0.5)

    add 'bg_up' align(0.5, 0.19)
    add 'bg_down' align(0.5, 0.76)
    button:
        xysize(206, 68)
        idle_background "sl_sl_btn_hover"
        hover_background "sl_sl_btn_hover"
        text "设置":
            align(.3, .5)
            style "sl_page"
            size 36 color "#50350f"
        xalign 0.03 yalign 0.13
        action NullAction()

    imagebutton:
        xalign 0.87 yalign 0.1
        auto "sl_close_%s"
        action Return()

    # 上方
    hbox:
        style_prefix "sound_setting"
        xalign 0.5 yalign 0.2
        xoffset -20
        spacing 40

        vbox:
            yoffset 20
            xoffset -20
            spacing 60
            label _("文字显示速度")
            label _("自动播放速度")
            label _("快进设定")

        vbox:
            xoffset -30
            yoffset 20
            spacing 60
            # bar value Preference("music volume")
            # bar value Preference("music volume"):
            #     yoffset 10
            bar value Preference("text speed")
            bar value Preference("auto-forward time")
            hbox:
                xalign 0
                spacing 150
                hbox:
                    spacing 15
                    imagebutton:
                        auto "setting_click_%s"
                        action Preference("skip", "seen")
                    text _("仅限已读"):
                        style_prefix "mute_setting"
                        yoffset -5
                        if not preferences.skip_unseen:
                            bold True
                        else:
                            bold False
                hbox:
                    spacing 15
                    imagebutton:
                        auto "setting_click_%s"
                        action Preference("skip", "all")
                    text _("全部"):
                        style_prefix "mute_setting"
                        yoffset -5
                        if preferences.skip_unseen:
                            bold True
                        else:
                            bold False

    # 下方
    hbox:
        style_prefix "sound_setting"
        xalign 0.5 yalign 0.7
        xoffset -20
        spacing 60

        vbox:
            xoffset 40
            spacing 70
            label _("语音音量")
            label _("音乐音量")
            label _("效果音量")

        vbox:
            xoffset 40
            spacing 72
            add 'gui/settings/音量-1.png'
            add 'gui/settings/音量-1.png':
                yoffset 5
            add 'gui/settings/音量-1.png':
                yoffset 10

        vbox:
            yoffset 3
            spacing 72
            # bar value Preference("music volume")
            # bar value Preference("music volume"):
            #     yoffset 10
            bar value Preference("voice volume")
            bar value Preference("music volume")
            bar value Preference("sound volume")

        vbox:
            xoffset -40
            spacing 72
            add 'gui/settings/音量.png'
            add 'gui/settings/音量.png':
                yoffset 5
            add 'gui/settings/音量.png':
                yoffset 10


style mute_setting_label_text:
    font "SourceHanSansCN-Bold.otf"
    size 36
    color "#50350f"

style mute_setting_text is mute_setting_label_text

style sound_setting_slider:
    xsize 670
    right_bar "setting_slider_2_idle"
    left_bar "setting_slider_2r_idle"
    thumb "setting_slider_2_btn_idle"

style sound_setting_label_text is mute_setting_label_text

style sound_setting_bar:
    xysize(670, 29)
    right_bar "setting_slider_2_idle"
    left_bar "setting_slider_2r_idle"
    thumb "setting_slider_2_btn_idle"

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## 避免预缓存此屏幕，因为它可能非常大。
    predict False

    add "black_bg" alpha 0.7

    use history_menu(_("历史"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:
                bottom_margin 50

                ## 此代码可确保如果“history_height”为“None”的话仍可正常显示条
                ## 目。
                has fixed:
                    yfit True

                if h.who:

                    label h.who + "：":
                        substitute False
                        style "history_name"

                        ## 若角色颜色已设置，则从“Character”对象中读取颜色到叙述
                        ## 人文本中。
                        # if "color" in h.who_args:
                        #     text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                if h.who:
                    text "“" + what + "”":
                        substitute False
                        font "SourceHanSansCN-Bold.otf"
                        color "#ffffff"
                else:
                    text what:
                        xoffset 35
                        substitute False
                        font "SourceHanSansCN-Bold.otf"
                        color "#a9a9a9"

                if h.voice.filename != None:

                    imagebutton:
                        xalign 0.93
                        auto "history_voiceReplay_btn_%s"
                        action Play("voice", h.voice.filename)

        if not _history_list:
            label _("对话历史记录为空。")


## 此代码决定了允许在历史记录屏幕上显示哪些标签。
define gui.history_allow_tags = set()


style history_window is empty

style history_name is empty
style history_name_text is empty
style history_text is empty

style history_text is empty

style history_label is empty
style history_label_text is empty

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    size 40
    font "SourceHanSansCN-Bold.otf"
    color "#a9a9a9"
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    line_spacing 15
    size 36
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5
    size 48
    font "SourceHanSansCN-Bold.otf"
    color "#989898"


## 历史菜单屏幕 ######################################################################
##

screen history_menu(title, scroll=None, yinitial=0.0):

    frame:
        align(0.5, 0.5)
        top_padding 150
        bottom_padding 150
        left_padding 200
        right_padding 200
        background None

        hbox:

            ## 导航部分的预留空间。
            # frame:
            #     style "game_menu_navigation_frame"

            frame:

                background None

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    imagebutton:
        yalign 0.05
        auto "history_return_btn_%s"
        action Return()

# screen history():

#     tag menu

#     ## Avoid predicting this screen, as it can be very large.
#     predict False

#     use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

#         style_prefix "history"

#         for h in _history_list:

#             window:

#                 ## This lays things out properly if history_height is None.
#                 has fixed:
#                     yfit True

#                 if h.who:

#                     label h.who:
#                         style "history_name"
#                         substitute False

#                         ## Take the color of the who text from the Character, if
#                         ## set.
#                         if "color" in h.who_args:
#                             text_color h.who_args["color"]

#                 $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
#                 text what:
#                     substitute False

#         if not _history_list:
#             label _("The dialogue history is empty.")


# ## This determines what tags are allowed to be displayed on the history screen.

# define gui.history_allow_tags = { "alt", "noalt" }


# style history_window is empty

# style history_name is gui_label
# style history_name_text is gui_label_text
# style history_text is gui_text

# style history_text is gui_text

# style history_label is gui_label
# style history_label_text is gui_label_text

# style history_window:
#     xfill True
#     ysize gui.history_height

# style history_name:
#     xpos gui.history_name_xpos
#     xanchor gui.history_name_xalign
#     ypos gui.history_name_ypos
#     xsize gui.history_name_width

# style history_name_text:
#     min_width gui.history_name_width
#     text_align gui.history_name_xalign

# style history_text:
#     xpos gui.history_text_xpos
#     ypos gui.history_text_ypos
#     xanchor gui.history_text_xalign
#     xsize gui.history_text_width
#     min_width gui.history_text_width
#     text_align gui.history_text_xalign
#     layout ("subtitle" if gui.history_text_xalign else "tex")

# style history_label:
#     xfill True

# style history_label_text:
#     xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    # add "gui/overlay/confirm.png"
    add "gui/sl/黑色弹窗.png" align(.5 ,.5)


    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 90

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                # textbutton _("Yes") action yes_action
                # textbutton _("No") action no_action
                button:
                    xysize(206, 68)
                    text "取消":
                        align(.5, .5)
                        size 36 color "#545454"
                    idle_background "confirm_no_idle"
                    hover_background "confirm_no_hover"
                    action no_action
                button:
                    xysize(206, 68)
                    idle_background "confirm_yes_idle"
                    hover_background "confirm_yes_hover"
                    text "确定":
                        align(.5, .5)
                        size 36 color "#50350f"
                    action yes_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    # background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    background None
    # padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"
    color "#ffffff"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "SourceHanSansCN-Bold.otf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

# style pref_vbox:
#     variant "medium"
#     xsize 675

# ## Since a mouse may not be present, we replace the quick menu with a version
# ## that uses fewer and bigger buttons that are easier to touch.
# screen quick_menu():
#     variant "touch"

#     zorder 100

#     if quick_menu and renpy.get_screen("say"):

#         window:
#             xsize 520 ysize 81
#             align(1.0, 0.98)
#             background "quick_bg"

#             imagebutton:
#                 yalign 0.5 xalign 0.125
#                 auto "quick_skip_%s"
#                 action Skip() alternate Skip(fast=False, confirm=True)

#             imagebutton:
#                 yalign 0.5 xalign 0.32
#                 auto "quick_hist_%s"
#                 action ShowMenu("history")

#             imagebutton:
#                 yalign 0.5 xalign 0.55
#                 auto "quick_quicksave_%s"
#                 # action QuickSave(message=u'已快速保存', newest=True)
#                 action ShowMenu("save")

#             imagebutton:
#                 yalign 0.5 xalign 0.88
#                 auto "quick_system_%s"
#                 action Show("r_menu", dissolve)

#     if not renpy.get_screen("save") or not renpy.get_screen("load"):
#         key "right_click_menu" action Show("r_menu")

#     # if quick_menu and renpy.get_screen("say"):

#     #     hbox:
#     #         style_prefix "quick"

#     #         xalign 0.5
#     #         yalign 1.0

#     #         textbutton _("Back") action Rollback()
#     #         textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
#     #         textbutton _("Auto") action Preference("auto-forward", "toggle")
#     #         textbutton _("Menu") action ShowMenu()

#     # if not renpy.get_screen("save") or not renpy.get_screen("load"):
#     #     key "right_click_menu" action Show("r_menu")

# style window:
#     variant "small"
#     background "gui/phone/textbox.png"

# style radio_button:
#     variant "small"
#     foreground "gui/phone/button/radio_[prefix_]foreground.png"

# style check_button:
#     variant "small"
#     foreground "gui/phone/button/check_[prefix_]foreground.png"

# style nvl_window:
#     variant "small"
#     background "gui/phone/nvl.png"

# style main_menu_frame:
#     variant "small"
#     background "gui/phone/overlay/main_menu_test.png"

# style game_menu_outer_frame:
#     variant "small"
#     background "gui/phone/overlay/game_menu_test.png"

# style game_menu_navigation_frame:
#     variant "small"
#     xsize 510

# style game_menu_content_frame:
#     variant "small"
#     top_margin 0

# style pref_vbox:
#     variant "small"
#     xsize 600

# style bar:
#     variant "small"
#     ysize gui.bar_size
#     left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
#     right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

# style vbar:
#     variant "small"
#     xsize gui.bar_size
#     top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
#     bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

# style scrollbar:
#     variant "small"
#     ysize gui.scrollbar_size
#     base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
#     thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

# style vscrollbar:
#     variant "small"
#     xsize gui.scrollbar_size
#     base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
#     thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

# style slider:
#     variant "small"
#     ysize gui.slider_size
#     base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
#     thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

# style vslider:
#     variant "small"
#     xsize gui.slider_size
#     base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
#     thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

# style slider_vbox:
#     variant "small"
#     xsize None

# style slider_slider:
#     variant "small"
#     xsize 900
