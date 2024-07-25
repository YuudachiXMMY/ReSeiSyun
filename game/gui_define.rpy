init offset = -2

image blank_idle:
    "gui/blank.png"

image blank_hover:
    "gui/blank.png"

image bg_cover:
    "blank_hover"

image black_bg:
    "gui/black.png"

image white_bg:
    "gui/white.png"

image past_cover:
    "gui/past.png"

image main_bg:
    "gui/main/bg.png"

image ending_script:
    "gui/ending_script.png"

## Reviw ######################################################################
##
image review_button_bg:
    "gui/review/question_bg.png"

## 确认 ######################################################################
##
image confirm_yes_idle:
    "gui/sl/confirm.png"

image confirm_yes_hover:
    "confirm_yes_idle"

image confirm_no_idle:
    "gui/sl/cancel.png"

image confirm_no_hover:
    "confirm_no_idle"

## Save & Load ######################################################################
##
image sl_bg:
    "gui/sl/sl_bg.png"

image sl_sl_btn_idle:
    "gui/sl/tag_unselected.png"

image sl_sl_btn_hover:
    "gui/sl/tag_selected.png"

image sl_page_previous_idle:
    "gui/sl/arrow.png"

image sl_page_previous_hover:
    "sl_page_previous_idle"

image sl_page_next_idle:
    xzoom -1.0
    "gui/sl/arrow.png"

image sl_page_next_hover:
    xzoom -1.0
    "gui/sl/arrow.png"

image sl_close_idle:
    "gui/sl/close.png"

image sl_close_hover:
    "sl_close_idle"

image sl_slot_bg:
    Composite(
        (418, 256),
        (14, 13), "gui/sl/unsave_bg.png"
    )

image sl_slot_bg_hover:
    Composite(
        (418, 256),
        (0, 0), "gui/sl/box_selected.png",
        (14, 13), "gui/sl/unsave_bg.png"
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
    "gui/settings/underline.png"

image setting_slider_2r_idle:
    "gui/settings/blue_underline.png"

image setting_slider_2_btn_idle:
    "gui/settings/white_dot.png"


#* 打勾按钮
image setting_click_idle:
    Composite(
        (26, 26),
        (0, 0), "gui/settings/check_box.png")

image setting_toggled_btn_idle:
    "setting_click_selected_idle"

image setting_click_selected_idle:
    Composite(
        (26, 26),
        (0, 0), "gui/settings/check_box.png",
        (0, -10), "gui/settings/check_icon.png")

image setting_click_selected_hover:
    "setting_click_selected_idle"

## 快速条 ######################################################################
##
image quick_bg:
    "gui/dialogue/quick_menu.png"

image quick_system_idle:
    "gui/dialogue/setting.png"

image quick_system_hover:
    "gui/dialogue/setting2.png"

image quick_skip_idle:
    "gui/dialogue/skipping_unselected.png"

image quick_skip_hover:
    "gui/dialogue/skipping_selected.png"

image quick_quicksave_idle:
    "gui/dialogue/save_button.png"

image quick_quicksave_hover:
    "gui/dialogue/save_button2.png"

image quick_quickload_idle:
    "gui/dialogue/load_button.png"

image quick_quickload_hover:
    "gui/dialogue/load_button2.png"

image quick_hist_idle:
    "gui/dialogue/replay.png"

image quick_hist_hover:
    "gui/dialogue/replay2.png"


## Right Menu ######################################################################
##
image r_menu_background:
    "gui/dialogue/r_menu.png"

image r_menu_save_idle:
    "gui/dialogue/save_button.png"

image r_menu_save_hover:
    "gui/dialogue/save_button2.png"

image r_menu_load_idle:
    "gui/dialogue/load_button.png"

image r_menu_load_hover:
    "gui/dialogue/load_button2.png"

image r_menu_history_idle:
    "gui/dialogue/replay.png"

image r_menu_history_hover:
    "gui/dialogue/replay2.png"

image r_menu_review_idle:
    "gui/dialogue/review_button.png"

image r_menu_review_hover:
    "gui/dialogue/review_button2.png"

image r_menu_setting_idle:
    "gui/dialogue/setting.png"

image r_menu_setting_hover:
    "gui/dialogue/setting2.png"

image r_menu_mainmenu_idle:
    xoffset -3
    "gui/dialogue/return_button.png"

image r_menu_mainmenu_hover:
    xoffset -3
    "gui/dialogue/return_button2.png"

image r_menu_exit_idle:
    xoffset 5
    "gui/dialogue/exit.png"

image r_menu_exit_hover:
    xoffset 5
    "gui/dialogue/exit2.png"