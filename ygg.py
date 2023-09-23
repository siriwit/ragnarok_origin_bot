import constanst as const
import func
import utils
import img
import preset as pre
import sys
import time

def ygg_fight():
    utils.wait_for_image(img.profile)
    if func.go_to_event(img.event_ygg):
        utils.wait_and_tap(img.button_start_blue_medium)
        utils.wait_and_tap(img.ygg_skip)
        yggdasill()


def yggdasill():
    utils.wait_for_image(img.profile)
    func.auto_attack()
    while True:
        if utils.is_found_any(const.ygg_next_wave):
            if not utils.is_found(img.ygg_map_name):
                utils.key_press(const.map)
            utils.wait_and_tap_any(const.ygg_map_root_trees, timeout=1)
            utils.tap_any(const.ygg_next_wave)

        if utils.is_found(img.victory):
            utils.tap_any(const.tap_anywheres)
            sys.exit()
        time.sleep(1)


def preset():
    pre.change_skill_auto(const.ygg)
    pre.pet_selector(img.pet_icon_sohee)
    pre.attack_preset()