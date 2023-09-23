import constanst as const
import func
import img
import sys
import utils

def daily_anthem():
    utils.wait_for_image(img.profile)
    utils.tap_any_until_found_offset(const.menu_guides, img.daily_anthem, offset_x=-210)
    utils.wait_and_tap(img.daily_anthem, timeout=2)
    utils.wait_and_tap(img.button_go)
    utils.wait_and_tap(img.daily_anthem_anthem_trial_option, timeout=120)
    utils.wait_and_tap(img.button_start)
    utils.wait_for_image(img.team_confirm, timeout=1)
    if utils.is_found(img.team_confirm):
        utils.wait_until_disappear(img.team_confirm)
    anthem()


def anthem():
    utils.wait_for_image(img.profile)
    utils.wait_and_tap(img.anthem_activate)
    utils.wait_for_image(img.anthem_lucky_wheel)
    utils.wait_for_image(img.anthem_activate)
    anthem_fight()


def anthem_fight():
    utils.wait_for_image(img.profile)
    func.move_left(hold_move=0.5)
    func.move_up(hold_move=3)
    func.auto_attack()
    utils.wait_for_image(img.victory, timeout=150)
    func.use_items()
    utils.wait_and_tap_any(const.tap_anywheres, timeout=5)
    utils.wait_and_tap(img.daily_selectable_card, timeout=5)
    utils.wait_and_tap_any(const.tap_anywheres, timeout=5)
    utils.wait_and_tap(img.button_escape, timeout=5)
    utils.wait_and_tap(img.button_confirm, timeout=5)
    utils.wait_for_image(img.profile)
    sys.exit(0)