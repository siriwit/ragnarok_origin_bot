import constanst as const
import img
import func
import preset as pre
import time
import utils

def start(mode='main'):
    func.wait_profile()
    if func.go_to_event(img.event_guild_expedition):
        go_to_expedition()
        fight()


def fight():
    duration_minutes = 20
    end_time = time.time() + duration_minutes * 60
    while time.time() < end_time:
        if utils.is_found(img.button_quick_respawn):
            utils.tap_image(img.button_quick_respawn)
            time.sleep(2)
            if utils.is_found_any(const.menu_bags):
                utils.wait_any_image(const.menu_bags)
                func.auto_attack(const.att_all, timeout=2)
            
        if utils.is_found(img.loading):
            func.wait_loading_screen()
            utils.wait_and_tap(img.menu_hourglass)
            go_to_expedition()

        if utils.is_found_any(const.menu_guides):
            go_to_expedition()

def go_to_expedition():
    # utils.wait_for_image(img.guild_expedition_page)
    utils.wait_and_tap(img.guild_expedition_boss_angeling)
    utils.wait_and_tap(img.button_go_blue_medium)
    func.wait_profile()
    func.auto_attack()


def preset():
    pre.pvp()