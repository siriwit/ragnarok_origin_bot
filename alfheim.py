import img
import func
import time
import utils

def alfheim_collect_item():
    utils.wait_for_image(img.profile)
    if func.go_to_event():
        utils.scroll_down_util_found(img.event_alfheim, img.event_drag_icon, 300)
        utils.wait_and_tap(img.event_alfheim)
        utils.wait_and_tap(img.button_go_orange_small)
        utils.wait_and_tap(img.alfheim_claim_button)
        func.use_items()
        utils.tap_image(img.button_back)


def alfheim_fight():
    utils.wait_for_image(img.profile)
    if func.go_to_event():
        utils.scroll_down_util_found(img.event_alfheim, img.event_drag_icon, 300)
        utils.wait_and_tap(img.event_alfheim)
        utils.wait_and_tap(img.button_go_orange_small)
        utils.wait_and_tap(img.button_start_blue_medium)
        utils.wait_for_image(img.profile)
        utils.key_press('k')
        utils.hold_press('w', timeout=2)

        while True:
            if utils.is_found(img.button_exit_trial_orange):
                utils.tap_image(img.button_exit_trial_orange)
                break
            time.sleep(1)
            