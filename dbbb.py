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
            break
        else:
            func.send_message(message, 'world')
        time.sleep(20)

    use_branch()


def use_branch():
    utils.key_press('b')
    utils.scroll_down_util_found(img.dbbb_dead_branch, img.item_drag, 300)
    tap_until_used(img.dbbb_dead_branch)
    tap_until_used(img.dbbb_bloody_branch)
    func.close_any_panel()
    func.wait_profile()
    utils.key_press('k')
    sys.exit(0)



def tap_until_used(branch):
    utils.tap_until_found(branch, img.button_use_small_blue)

    while True:
        utils.tap_image(img.button_use_small_blue)
        time.sleep(0.5)
        if utils.is_found(img.dbbb_party_too_far):
            time.sleep(3)
            continue
        break

