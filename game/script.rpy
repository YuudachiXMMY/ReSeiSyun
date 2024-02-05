label start:
    $debug = True

    if debug:
        "这是内部测试版本"
        menu start_debug_chapter_selection_0:
            "0.0 序章":
                jump prologue_scene_1_1
            "1.0 第一章":
                jump chpt1_1
            "1.5 第一课":
                jump lesson1_1
            "下一页":
                jump start_debug_chapter_selection_1

        menu start_debug_chapter_selection_1:
            "上一页":
                jump start_debug_chapter_selection_0
            "2.0 第二章":
                jump chpt2_1
            "2.5 第二课":
                jump lesson2_1
            "下一页":
                jump start_debug_chapter_selection_2

        menu start_debug_chapter_selection_2:
            "上一页":
                jump start_debug_chapter_selection_1
            "3.0 第三章":
                jump chpt3_1
            "3.5 第三课":
                jump lesson3_1

    else:
        jump prologue_scene_1_1