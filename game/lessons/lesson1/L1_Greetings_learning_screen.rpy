screen L1_Greetings(learning=True):

    style_prefix "HiraKataKANA"
    if learning:
        modal True

        textbutton _("结 束 学 习"):
            align(.9,.8)
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
            imagebutton:
                idle "l1 picture1"
                action NullAction()
            imagebutton:
                idle "l1 picture2"
                action NullAction()

        hbox:
            if learning:
                spacing 40
            else:
                spacing 20
            imagebutton:
                idle "l1 picture3"
                action NullAction()
            imagebutton:
                idle "l1 picture4"
                action NullAction()

style HiraKataKANA_button_text:
    idle_color "#ffffff"
    hover_color "#ff0000"