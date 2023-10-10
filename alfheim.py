import constanst as const
import img
import func
import preset as pre
import time
import sys
import utils

def alfheim_collect_item():
    func.wait_profile()
    if func.go_to_event(img.event_alfheim):
        utils.wait_for_image(img.alfheim_page)
        if not utils.is_found(img.alfheim_claimed):
            utils.wait_and_tap(img.alfheim_claim_button)
            func.use_items()
        utils.tap_image(img.button_back)


def alfheim_fight():
    func.wait_profile()
    if func.go_to_event(img.event_alfheim):
        while True:
            utils.wait_and_tap(img.button_start_blue_medium)
            utils.wait_for_image(img.loading)
            utils.wait_until_disappear(img.loading)
            attack()

            while True:
                if utils.is_found(img.alfheim_victory):
                    utils.wait_and_tap(img.button_next_floor)
                    attack()
                elif utils.is_found(img.alfheim_defeat):
                    utils.wait_and_tap(img.button_exit_trial_orange)
                    func.close_any_panel()
                    sys.exit(0)
                time.sleep(1)
            

def attack():
    func.wait_profile()
    func.move_up(hold=2)
    func.auto_attack(const.att_all)


def preset():
    pre.change_skill_auto(const.farm)
    pre.pet_selector(img.pet_icon_sohee)
    pre.attack_preset()