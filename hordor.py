import img
import func
import time
import utils

def hordor_dreamland(mode=img.hordor_poring_dream):
    utils.wait_for_image(img.profile)
    if func.go_to_event():
        utils.scroll_down_util_found(img.event_hordor, img.event_drag_icon, offset_y=300)
        utils.wait_and_tap(img.event_hordor)
        utils.wait_and_tap(img.button_go_orange_small)
        utils.wait_for_image(img.hordor_page)

        utils.scroll_down_util_found(mode, img.hordor_magic_ocean, offset_y=300)
        utils.wait_and_tap(mode)
        utils.tap_if_found(img.hordor_use_advance_ticket)
        utils.wait_and_tap(img.hordor_start_button)
        fight()


def fight():
    utils.wait_for_image(img.profile)
    utils.key_press('k')

    while True:
        if utils.is_found(img.hordork_not_enough_ticket):
            break

        if utils.is_found(img.button_challenge_again):
            utils.wait_and_tap(img.button_challenge_again)
            fight()
        time.sleep(1)