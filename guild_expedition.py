import constanst as const
import img
import func
import preset as pre
import time
import utils

def start(selected_boss, level, mode='leader'):
    boss_list = [img.guild_expedition_boss_drake, 
        img.guild_expedition_boss_phreeoni, 
        img.guild_expedition_boss_moonlight, 
        img.guild_expedition_boss_doppel, 
        img.guild_expedition_boss_bapho,
        img.guild_expedition_boss_angeling,
        img.guild_expedition_boss_golden_thief_bug,
        img.guild_expedition_boss_deviling,
        img.guild_expedition_boss_goblin,
        img.guild_expedition_boss_eddga]
    func.wait_profile()
    if func.go_to_event(img.event_guild_expedition):
        go_to_expedition(boss_list, selected_boss, level)

        if mode == 'leader':
            fight_mode(selected_boss, level)
        elif mode == 'follwer':
            follower_mode()


def fight_mode(selected_boss, level):
    duration_minutes = 20 * 60
    utils.execute_until_invalid_state(duration_minutes, 1, fight_state, 1, selected_boss, level)
        

def fight_state(selected_boss, level):
    if utils.is_found(img.button_quick_respawn):
        utils.tap_image(img.button_quick_respawn)
        time.sleep(2)
        if utils.is_found_any(const.menu_bags):
            utils.wait_any_image(const.menu_bags)
            func.auto_attack(const.att_all, timeout=2)
            # func.one_tap_rally()

    if utils.is_found_any(const.menu_guides):
        start(selected_boss, level)

    if utils.is_found(img.guild_expedition_end):
        func.close_any_panel()
        return False
    return True
        

def follower_mode():
    duration_minutes = 20 * 60
    utils.execute_until_invalid_state(duration_minutes, 1, follower_state)


def follower_state():
    func.accept_rally()

    if utils.is_found_any(const.menu_guides):
        start()

    if utils.is_found(img.guild_expedition_end):
        return False
    return True
        

def go_to_expedition(boss_list, expected_boss, level):
    while True:
        utils.scroll_down_util_found_any_drag_images(expected_boss, boss_list, offset_y=200)

        if utils.is_found(expected_boss):
            if level > 1:
                level -= 1
                utils.scroll_down_util_not_found(expected_boss, expected_boss, timeout=10)
                continue
            utils.wait_and_tap(expected_boss)
            utils.tap_image_offset(expected_boss, offset_x=100)
            break
        func.wait(1)
    
    utils.execute_until_invalid_state(600, 1, enter_dungeon_state)
    
    utils.wait_for_image(img.button_escape)
    func.auto_attack()


def enter_dungeon_state():
    if utils.is_found(img.button_escape):
        return False
    utils.wait_and_tap(img.button_go_blue_medium, timeout=1)
    return True


def preset():
    pre.pvp()