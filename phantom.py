import boss
import constanst as const
import img
import func
import utils


def start():
    if (func.go_to_event(img.event_phantom_hunt)):
        utils.wait_for_image(img.phantom_page)
        utils.exit_at_specific_time_or_invalid_state(20, 50, entering)


def entering():

    if utils.is_found(img.phantom_begin):
        return True
    
    maps = [img.phantom_northern, img.phantom_easthern, img.phantom_southern, img.phantom_western]
    for map in maps:
        utils.tap_until_found(map, img.button_confirm, timeout=3)
        utils.tap_until_notfound(img.button_confirm, img.button_confirm, timeout=3)
        if func.wait_loading_screen() is not None:
            fight()
            return False
    return True


def fight():
    should_restart = False
    while True:
        if utils.is_found(img.button_revive):
            utils.tap_image(img.button_revive)
            func.wait(2)

        func.auto_attack(const.att_all, timeout=3)

        func.open_map()
        if utils.is_found(img.phantom_map_inner_zone):
            func.close_map()
            func.leave_event()
            should_restart = True
            break
        else:
            utils.tap_any([img.phantom_map_boss, img.phantom_map_boss2, img.phantom_map_boss3, img.phantom_map_boss4])
            func.close_map()

        if utils.is_found(img.phantom_boss_fight_icon) or utils.is_found(img.phantom_player_enemy):
            utils.execute_until_valid_state_with_timeout(30, 1, wait_until_found_boss_state)
            continue

        if utils.is_found(img.phantom_diamond_box):
            func.use_items()
        
    if should_restart:
        func.wait_loading_screen()
        start()

        


def wait_until_found_boss_state():
    if utils.is_found(img.loading):
        return True
    if utils.is_found(img.phantom_player_enemy) or utils.is_found(img.phantom_boss_fight_icon):
        func.use_manual_skill()
    return False
