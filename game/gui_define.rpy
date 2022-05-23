init offset = -2

image blank_idle:
    "gui/blank.png"

image blank_hover:
    "gui/blank.png"

image bg_cover:
    "blank_hover"

image black_bg:
    "gui/black.png"

image past_cover:
    "gui/past.png"

image main_bg:
    "gui/main/bg.png"


## 确认 ######################################################################
##
image confirm_yes_idle:
    "gui/sl/确定.png"

image confirm_yes_hover:
    "confirm_yes_idle"

image confirm_no_idle:
    "gui/sl/取消.png"

image confirm_no_hover:
    "confirm_no_idle"

## Save & Load ######################################################################
##
image bg_cover:
image sl_bg:
    "gui/sl/界面.png"

image sl_sl_btn_idle:
    "gui/sl/标签-未选.png"

image sl_sl_btn_hover:
    "gui/sl/标签-选中.png"

image sl_page_previous_idle:
    "gui/sl/箭头.png"

image sl_page_previous_hover:
    "sl_page_previous_idle"

image sl_page_next_idle:
    xzoom -1.0
    "gui/sl/箭头.png"

image sl_page_next_hover:
    xzoom -1.0
    "gui/sl/箭头.png"

image sl_close_idle:
    "gui/sl/关闭.png"

image sl_close_hover:
    "sl_close_idle"

image sl_slot_bg:
    Composite(
        (418, 256),
        (14, 13), "gui/sl/未存档.png"
    )

image sl_slot_bg_hover:
    Composite(
        (418, 256),
        (0, 0), "gui/sl/选中框.png",
        (14, 13), "gui/sl/未存档.png"
    )

## 历史回放 ######################################################################
##
image history_voiceReplay_btn_idle:
    'gui/history/history_voiceReplay_btn_idle.png'

image history_voiceReplay_btn_hover:
    'gui/history/history_voiceReplay_btn_hover.png'

image history_return_btn_idle:
    'gui/history/history_return_btn_idle.png'

image history_return_btn_hover:
    'gui/history/history_return_btn_hover.png'


## 设置 ######################################################################
##
image bg_up:
    'gui/settings/up.png'

image bg_down:
    'gui/settings/down.png'

image setting_slider_2_idle:
    "gui/settings/底层线.png"

image setting_slider_2r_idle:
    "gui/settings/蓝色线.png"

image setting_slider_2_btn_idle:
    "gui/settings/白色点.png"


#* 打勾按钮
image setting_click_idle:
    Composite(
        (26, 26),
        (0, 0), "gui/settings/方框.png")

image setting_toggled_btn_idle:
    "setting_click_selected_idle"

image setting_click_selected_idle:
    Composite(
        (26, 26),
        (0, 0), "gui/settings/方框.png",
        (0, -10), "gui/settings/勾.png")

image setting_click_selected_hover:
    "setting_click_selected_idle"

## 快速条 ######################################################################
##
image quick_bg:
    "gui/dialogue/设置长条.png"

image quick_system_idle:
    "gui/dialogue/设置.png"

image quick_system_hover:
    "gui/dialogue/设置2.png"

image quick_skip_idle:
    "gui/dialogue/快进-未选.png"

image quick_skip_hover:
    "gui/dialogue/快进-选中.png"

image quick_quicksave_idle:
    "gui/dialogue/存档.png"

image quick_quicksave_hover:
    "gui/dialogue/存档2.png"

image quick_quickload_idle:
    "gui/dialogue/读档.png"

image quick_quickload_hover:
    "gui/dialogue/读档2.png"

image quick_hist_idle:
    "gui/dialogue/文本回放.png"

image quick_hist_hover:
    "gui/dialogue/文本回放2.png"


## Right Menu ######################################################################
##
image r_menu_background:
    "gui/dialogue/目录.png"

image r_menu_save_idle:
    "gui/dialogue/存档.png"

image r_menu_save_hover:
    "gui/dialogue/存档2.png"

image r_menu_load_idle:
    "gui/dialogue/读档.png"

image r_menu_load_hover:
    "gui/dialogue/读档2.png"

image r_menu_history_idle:
    "gui/dialogue/文本回放.png"

image r_menu_history_hover:
    "gui/dialogue/文本回放2.png"

image r_menu_review_idle:
    "gui/dialogue/复习回顾.png"

image r_menu_review_hover:
    "gui/dialogue/复习回顾2.png"

image r_menu_setting_idle:
    "gui/dialogue/设置.png"

image r_menu_setting_hover:
    "gui/dialogue/设置2.png"

image r_menu_mainmenu_idle:
    xoffset -3
    "gui/dialogue/返回标题.png"

image r_menu_mainmenu_hover:
    xoffset -3
    "gui/dialogue/返回标题2.png"

image r_menu_exit_idle:
    xoffset 5
    "gui/dialogue/退出游戏.png"

image r_menu_exit_hover:
    xoffset 5
    "gui/dialogue/退出游戏2.png"