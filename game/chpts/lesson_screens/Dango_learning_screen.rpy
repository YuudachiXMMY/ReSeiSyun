screen Dango(tar=None, learning=True):

    style_prefix "Dango"
    if learning:
        modal True

        textbutton _("结 束 学 习"):
            align(.5,.8)
            action Hide("Dango",dissolve), Return()


    # 音量
    hbox:
        style_prefix "learn_sound_setting"
        xalign 0.0 yalign 0.9
        xoffset -20
        spacing 60

        vbox:
            xoffset 40
            spacing 40
            label _("音乐音量")
            label _("语音音量")

        vbox:
            xoffset 40
            spacing 42
            add 'gui/settings/音量-1.png'
            add 'gui/settings/音量-1.png':
                yoffset 5

        vbox:
            yoffset 3
            spacing 42
            # bar value Preference("music volume")
            # bar value Preference("music volume"):
            #     yoffset 10
            bar value Preference("music volume")
            bar value Preference("sound volume")

        vbox:
            xoffset -40
            spacing 42
            add 'gui/settings/音量.png'
            add 'gui/settings/音量.png':
                yoffset 5

    # Learn
    vbox:
        if learning:
            align(.5,.225)
            spacing 20
        else:
            align(.95,.025)
            spacing 10
        grid 2 2:
            if learning:
                spacing 40
            else:
                spacing 20
            if tar is not None:
                for word in tar:
                    imagebutton:
                        idle ("images/wupin/danci/"+str(word)+"s.png")
                        hover ("images/wupin/danci/"+str(word)+"s.png")
                        action Play("sound", "audio/se/sushiyin/"+str(word)+".mp3")
        # hbox:
        #     if learning:
        #         spacing 40
        #     else:
        #         spacing 20
        #     if kana2 is not None and kana2 in HiraKataKANA:
        #         for kana in HiraKataKANA[kana2]:
        #             imagebutton:
        #                 idle ("images/HiraKataKANA/"+str(kana)+".png")
        #                 hover ("images/HiraKataKANA/"+str(kana)+"2.png")
        #                 action Play("sound", "audio/se/sushiyin/"+str(kana)+".mp3")

style Dango_button_text:
    idle_color "#ffffff"
    hover_color "#ff0000"

style learn_sound_setting_slider:
    xsize 400
    right_bar "setting_slider_2_idle"
    left_bar "setting_slider_2r_idle"
    thumb "setting_slider_2_btn_idle"

style learn_sound_setting_label_text:
    font "经典中圆简.ttf"
    size 36
    color "#ffffff"

style learn_sound_setting_bar:
    xysize(400, 29)
    right_bar "setting_slider_2_idle"
    left_bar "setting_slider_2r_idle"
    thumb "setting_slider_2_btn_idle"