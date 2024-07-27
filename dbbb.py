import constanst as const
import img
import func
import sys
import time
import utils


def party_finder():
    while True:
        func.wait_profile()
        message = 'dbbb ' + func.find_remaining_party_number()
        if utils.is_found(img.party_number_5):
            if utils.is_found(img.dbbb_player_away):
                continue
            break
        else:
            func.send_message(message, 'world')
        func.wait(20)

    use_branch()


def use_branch():
    func.open_bag()
    utils.scroll_down_until_found(img.dbbb_dead_branch, img.item_drag, 300)
    tap_until_used(img.dbbb_dead_branch)
    tap_until_used(img.dbbb_bloody_branch)
    func.close_any_panel()
    func.wait_profile()
    func.auto_attack(const.att_all)
    sys.exit(0)



def tap_until_used(branch):
    utils.tap_until_found(branch, img.button_use_small_blue)

    while True:
        utils.tap_image(img.button_use_small_blue)
        func.wait(1)
        if utils.is_found(img.dbbb_party_too_far):
            func.wait(3)
            continue
        elif utils.is_found_any(const.tap_anywheres):
            utils.tap_any(const.tap_anywheres)
            continue
        break

