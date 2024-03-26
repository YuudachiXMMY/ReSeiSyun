label start:
    $debug = True

    if debug:
        "这是内部测试版本"
        menu start_debug_chapter_selection_1:
            "0.0 序章":
                jump prologue_scene_1_1
            "1.0 第一章":
                jump chpt1_1
            "1.5 第一课":
                jump lesson1_1
            "下一页":
                jump start_debug_chapter_selection_2

        menu start_debug_chapter_selection_2:
            "上一页":
                jump start_debug_chapter_selection_1
            "2.0 第二章":
                jump chpt2_1
            "2.5 第二课":
                jump lesson2_1
            "下一页":
                jump start_debug_chapter_selection_3

        menu start_debug_chapter_selection_3:
            "上一页":
                jump start_debug_chapter_selection_2
            "3.0 第三章":
                jump chpt3_1
            "3.5 第三课":
                jump lesson3_1
            "下一页":
                jump start_debug_chapter_selection_4

        menu start_debug_chapter_selection_4:
            "上一页":
                jump start_debug_chapter_selection_3
            "4.0 第四章":
                jump chpt4_1
            "4.5 第四课":
                jump lesson4_1
            "下一页":
                jump start_debug_chapter_selection_5

        menu start_debug_chapter_selection_5:
            "上一页":
                jump start_debug_chapter_selection_4
            "5.0 第五课":
                jump lesson5_1
            "5.5 第五章":
                jump chpt5_1

    else:
        jump prologue_scene_1_1