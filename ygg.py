import constanst as const
from datetime import datetime
import func
import utils
import img
import preset as pre
import sys
import time

def ygg_fight(skip=False):
    func.close_any_panel()
    if func.go_to_event(img.event_ygg):

        if skip:
            utils.wait_for_image(img.ygg_page)

            if datetime.now().weekday() == 5 or datetime.now().weekday() == 6:
                utils.tap_if_found(img.ygg_duo_defense)
            else: 
                utils.tap_if_found(img.ygg_solo_defense)
                
            utils.tap_until_found(img.button_skip, img.button_confirm)
            utils.tap_until_notfound(img.button_confirm, img.button_confirm)
            utils.tap_until_found(img.ygg_weekly_reward, img.button_claim)
            utils.tap_until_notfound(img.button_claim, img.button_claim)
            func.close_any_panel()
        else:
            utils.wait_and_tap(img.button_start_blue_medium)
            func.wait_loading_screen()
            utils.wait_and_tap(img.ygg_skip)
            yggdasill()


def yggdasill():
    func.wait_profile()
    func.auto_attack()
    while True:
        if utils.is_found_any(const.ygg_next_wave):
            if not utils.is_found(img.ygg_map_name):
                utils.key_press(const.map)
            utils.wait_and_tap_any(const.ygg_map_root_trees, timeout=1)
            utils.tap_any(const.ygg_next_wave)

        if utils.is_found(img.victory):
            utils.wait_and_tap_any(const.tap_anywheres)
            sys.exit()
        time.sleep(1)


def preset():
    pre.change_skill_auto(const.ygg)
    pre.pet_selector(img.pet_icon_sohee)
    pre.attack_preset()