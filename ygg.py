import constanst as const
import func
import utils
import img
import sys
import time

def ygg_fight():
    utils.wait_for_image(img.profile)
    if func.go_to_event():
        utils.scroll_down_util_found(img.event_ygg, img.event_drag_icon, offset_y=300)
        utils.tap_image(img.event_ygg)
        utils.wait_and_tap(img.button_go_orange_small)
        utils.wait_and_tap(img.button_start_blue_medium)
        utils.wait_and_tap(img.ygg_skip)
        yggdasill()


def yggdasill():
    utils.wait_for_image(img.profile)
    func.auto_attack()
    while True:
        if utils.is_found_any(const.ygg_next_wave):
            if not utils.is_found(img.ygg_map_name):
                utils.key_press('m')
            utils.wait_and_tap(img.ygg_map_tree_root, timeout=1)
            utils.tap_any(const.ygg_next_wave)

        if utils.is_found(img.victory):
            utils.tap_image(img.tap_anywhere)
            sys.exit()
        time.sleep(1)