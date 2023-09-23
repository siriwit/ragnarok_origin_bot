import img
import func
import time
import sys
import utils

def alfheim_collect_item():
    utils.wait_for_image(img.profile)
    if func.go_to_event(img.event_alfheim):
        utils.wait_for_image(img.alfheim_page)
        if not utils.is_found(img.alfheim_claimed):
            utils.wait_and_tap(img.alfheim_claim_button)
            func.use_items()
        utils.tap_image(img.button_back)


def alfheim_fight():
    utils.wait_for_image(img.profile)
    if func.go_to_event(img.event_alfheim):
        while True:
            utils.wait_and_tap(img.button_start_blue_medium)
            attack()

            while True:
                if utils.is_found(img.alfheim_victory):
                    utils.wait_and_tap(img.button_next_floor)
                    attack()
                elif utils.is_found(img.alfheim_defeat):
                    utils.wait_and_tap(img.button_exit_trial_orange)
                    sys.exit(0)
                time.sleep(1)
            

def attack():
    utils.wait_for_image(img.profile)
    utils.key_press('k')
    utils.hold_press('w', timeout=4)