################################################################################
## Initialization
################################################################################

init offset = -1

define config.auto_voice = "audio/voice/{id}.mp3"


################################################################################
## Variables
################################################################################

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

    use review_menu(_("Review"), scroll=("vpgrid" if 1010 else "viewport"), yinitial=0.0):

        style_prefix "review"


        if renpy.get_screen("kana_review"):
            $ review_tmp_lst = chpt1_C_answer_kana
        elif renpy.get_screen("vocab_review"):
            $ review_tmp_lst = chpt1_C_answer_tango
        elif renpy.get_screen("bunka_review"):
            $ review_tmp_lst = chpt1_C_answer_bunka
        else:
            $ review_tmp_lst = ["Error"]

        if renpy.get_screen("kana_review") or renpy.get_screen("vocab_review"):
            for i in review_tmp_lst:
                window:
                    xfill True yfill True
                    if renpy.get_screen("kana_review"):
                        xysize(273, 251)
                        imagebutton:
                            xysize(246, 251)
                            idle "images/HiraKataKANA/"+str(i)+".png"
                            hover "images/HiraKataKANA/"+str(i)+"2.png"
                            action Play("sound", "audio/se/sushiyin/"+str(i)+".mp3")
                    else:
                        xysize(681, 356)
                        imagebutton:
                            xysize(601, 356)
                            idle "images/wupin/danci/"+str(i)+"s.png"
                            hover "images/wupin/danci/"+str(i)+"s.png"
                            action Play("sound", "audio/se/sushiyin/"+str(i)+".mp3")
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
            textbutton _("退出游戏") action Quit(confirm=True):
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

################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():
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
            action Start("prologue_scene_1_1")

        imagebutton:
            xalign 0.04 yalign 0.18
            idle "gui/main/load.png"
            action ShowMenu("load")

    # vbox:
    #     # style_prefix "navigation"

    #     xpos gui.navigation_xpos
    #     yalign 0.5

    #     spacing gui.navigation_spacing

        # Debug
        # textbutton _("Debug Mode: "+str(persistent.debug)) action ToggleVariable("persistent.debug")

        # if main_menu:

        #     textbutton _("序章") action Start("prologue_scene_1_1")
        #     textbutton _("第一章") action Start("chpt1_1")
        #     textbutton _("第一课") action Start("lesson1_1")

        # else:

        #     textbutton _("History") action ShowMenu("history")

        #     textbutton _("Save") action ShowMenu("save")

        # textbutton _("Load") action ShowMenu("load")

        # textbutton _("Preferences") action ShowMenu("preferences")

        # if _in_replay:

        #     textbutton _("End Replay") action EndReplay(confirm=True)

        # elif not main_menu:

        #     textbutton _("Main Menu") action MainMenu()

        # textbutton _("About") action ShowMenu("about")

        # if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

        #     ## Help isn't necessary or relevant to mobile devices.
        #     textbutton _("Help") action ShowMenu("help")

        # if renpy.variant("pc"):

        #     ## The quit button is banned on iOS and unnecessary on Android and
        #     ## Web.
        #     textbutton _("Quit") action Quit(confirm=not main_menu)


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

    background "gui/overlay/main_menu.png"

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

    background "gui/overlay/game_menu.png"

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

    # tag menu

    # use game_menu(_("Preferences"), scroll="viewport"):

    #     vbox:

    #         hbox:
    #             box_wrap True

    #             if renpy.variant("pc") or renpy.variant("web"):

    #                 vbox:
    #                     style_prefix "radio"
    #                     label _("Display")
    #                     textbutton _("Window") action Preference("display", "window")
    #                     textbutton _("Fullscreen") action Preference("display", "fullscreen")

    #             vbox:
    #                 style_prefix "radio"
    #                 label _("Rollback Side")
    #                 textbutton _("Disable") action Preference("rollback side", "disable")
    #                 textbutton _("Left") action Preference("rollback side", "left")
    #                 textbutton _("Right") action Preference("rollback side", "right")

    #             vbox:
    #                 style_prefix "check"
    #                 label _("Skip")
    #                 textbutton _("Unseen Text") action Preference("skip", "toggle")
    #                 textbutton _("After Choices") action Preference("after choices", "toggle")
    #                 textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

    #             ## Additional vboxes of type "radio_pref" or "check_pref" can be
    #             ## added here, to add additional creator-defined preferences.

    #         null height (4 * gui.pref_spacing)

    #         hbox:
    #             style_prefix "slider"
    #             box_wrap True

    #             vbox:

    #                 label _("Text Speed")

    #                 bar value Preference("text speed")

    #                 label _("Auto-Forward Time")

    #                 bar value Preference("auto-forward time")

    #             vbox:

    #                 if config.has_music:
    #                     label _("Music Volume")

    #                     hbox:
    #                         bar value Preference("music volume")

    #                 if config.has_sound:

    #                     label _("Sound Volume")

    #                     hbox:
    #                         bar value Preference("sound volume")

    #                         if config.sample_sound:
    #                             textbutton _("Test") action Play("sound", config.sample_sound)


    #                 if config.has_voice:
    #                     label _("Voice Volume")

    #                     hbox:
    #                         bar value Preference("voice volume")

    #                         if config.sample_voice:
    #                             textbutton _("Test") action Play("voice", config.sample_voice)

    #                 if config.has_music or config.has_sound or config.has_voice:
    #                     null height gui.pref_spacing

    #                     textbutton _("Mute All"):
    #                         action Preference("all mute", "toggle")
    #                         style "mute_all_button"

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

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()

    if not renpy.get_screen("save") or not renpy.get_screen("load"):
        key "right_click_menu" action Show("r_menu")

style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
