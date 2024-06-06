screen HiraKataKANA(kana1=None, kana2=None, learning=True):

    style_prefix "HiraKataKANA"
    if learning:
        modal True

        textbutton _("结 束 学 习"):
            align(.5,.8)
            action Hide("HiraKataKANA",dissolve), Return()


    # 音量
    if learning:
        hbox:
            style_prefix "learn_sound_setting"
            xalign 0.0 yalign 0.9
            xoffset -20
            spacing 60

            vbox:
                xoffset 40
                spacing 40
                # label _("音乐音量")
                label _("语音音量")

            vbox:
                xoffset 40
                spacing 42
                # add 'gui/settings/音量-1.png'
                add 'gui/settings/音量-1.png':
                    yoffset 5

            vbox:
                yoffset 3
                spacing 42
                # bar value Preference("music volume")
                # bar value Preference("music volume"):
                #     yoffset 10
                # bar value Preference("music volume")
                bar value Preference("sound volume")

            vbox:
                xoffset -40
                spacing 42
                # add 'gui/settings/音量.png'
                add 'gui/settings/音量.png':
                    yoffset 5

    # Learn
    vbox:
        if learning:
            align(.5,.45)
            spacing 20
        else:
            align(.95,.25)
            spacing 10
        hbox:
            if learning:
                spacing 40
            else:
                spacing 20
            if kana1 is not None and kana1 in HiraKataKANA:
                for kana in HiraKataKANA[kana1]:
                    imagebutton:
                        idle ("images/HiraKataKANA/"+str(kana)+".png")
                        hover ("images/HiraKataKANA/"+str(kana)+"2.png")
                        action Play("sound", "audio/se/sushiyin/"+str(kana)+".mp3")
        hbox:
            if learning:
                spacing 40
            else:
                spacing 20
            if kana2 is not None and kana2 in HiraKataKANA:
                for kana in HiraKataKANA[kana2]:
                    imagebutton:
                        idle ("images/HiraKataKANA/"+str(kana)+".png")
                        hover ("images/HiraKataKANA/"+str(kana)+"2.png")
                        action Play("sound", "audio/se/sushiyin/"+str(kana)+".mp3")

style HiraKataKANA_button_text:
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