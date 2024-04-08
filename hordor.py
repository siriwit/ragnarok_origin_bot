import constanst as const
import img
import func
import time
import sys
import utils

def hordor_dreamland(mode=img.hordor_poring_dream):
    func.wait_profile()
    if func.go_to_event(img.event_hordor):
        utils.wait_for_image(img.hordor_page)

        utils.scroll_down_util_found(mode, img.hordor_magic_ocean, offset_y=300)
        utils.wait_and_tap(mode)
        utils.tap_if_found(img.hordor_use_advance_ticket)
        utils.wait_and_tap(img.hordor_start_button)
        check_ticket_run_out()
        fight()


def fight():
    func.wait_profile()
    func.auto_attack(const.att_all)

    while True:
        if utils.is_found(img.button_challenge_again):
            utils.wait_and_tap(img.button_challenge_again)
            check_ticket_run_out()
            fight()
        time.sleep(1)


def check_ticket_run_out():
    time.sleep(0.5)
    if utils.is_found(img.hordork_not_enough_ticket):
        utils.tap_any(const.button_confirms)
        utils.wait_for_image(img.hordor_page)
        func.close_any_panel()
        sys.exit()