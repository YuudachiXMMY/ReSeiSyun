screen HiraKataKANA(kana1=None, kana2=None, learning=True):

    style_prefix "HiraKataKANA"
    if learning:
        modal True

        textbutton _("结 束 学 习"):
            align(.5,.8)
            action Hide("HiraKataKANA",dissolve), Return()

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
                        action NullAction()
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
                        action NullAction()

style HiraKataKANA_button_text:
    idle_color "#ffffff"
    hover_color "#ff0000"