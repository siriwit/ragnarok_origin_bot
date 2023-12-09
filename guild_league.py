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
    func.wait_profile()
    func.auto_attack(const.att_all)

    func.open_map()
    utils.wait_and_tap(img.guild_league_map_center)
    func.close_map()

    while True:
        func.use_rune_knight_skill()

        if utils.is_found(img.button_revive):
            utils.tap_image(img.button_revive)
            func.wait(2)
            fight()

        if utils.is_found(img.guild_league_battle_report_page):
            break
