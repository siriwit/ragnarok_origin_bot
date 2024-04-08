import constanst as const
import img
import func
import utils


def start():
    if func.go_to_event(img.event_guild_league):
        utils.wait_for_image(img.guild_league_page)

        while True:
            if utils.is_found(img.button_start_blue_medium):
                utils.tap_until_found(img.button_start_blue_medium, img.button_sub_field)
                utils.tap_until_notfound(img.button_sub_field, img.button_sub_field)
                break
            func.wait(2)

        fight()


def fight():
    utils.tap_if_found(img.button_revive)
    func.wait_profile()

    utils.exit_at_specific_time_or_invalid_state(21, 20, fight_state)


def fight_state():
    func.auto_attack(const.att_all, timeout=3)
    
    if utils.wait_for_image(img.guild_league_enemy, timeout=3) is None:
        func.open_map()
        utils.wait_and_tap_any([img.guild_league_map_east, img.guild_league_map_west])
        func.close_map()
    else:
        func.use_manual_skill()

    if utils.is_found(img.button_revive):
        utils.tap_until_notfound(img.button_revive, img.button_revive)
        func.wait(2)

    if utils.is_found(img.guild_league_battle_report_page) or utils.is_found_any(const.menu_guides):
        return False
    
    return True