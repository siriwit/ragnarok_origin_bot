import constanst as const
import img
import func
import utils
import time
import sys


def start(mode='forging'):
    utils.tap_offset_until_found(img.menu_bag, img.menu_life_skill, offset_x=180)
    utils.tap_image(img.menu_life_skill)
    utils.wait_for_image(img.life_skill_path_of_arts, timeout=2)
    if not utils.is_found(img.life_skill_path_of_arts):
        utils.tap_image(img.life_skill_path_of_nature)

    if mode == 'forging':
        utils.wait_and_tap(img.life_skill_forging)
    else:
        utils.wait_and_tap(img.life_skill_fishing)

    utils.wait_and_tap(img.life_skill_magnifying_glass)
    utils.wait_and_tap(img.life_skill_go)
    utils.tap_offset_until_found(img.menu_bag, img.butterfly_wing, offset_x=180)

    if mode == 'forging':
        utils.wait_for_image(img.forging, timeout=120)
        forging()
    else:
        utils.wait_for_image(img.life_skill_fishing_bait, timeout=120)
        fishing()


def forging():
    while True:
        if utils.is_found(img.life_skill_forging_run_out):
            sys.exit(0)

        func.wait_profile()
        func.ang_pao()
        utils.tap_image(img.forging)


def fishing():
    utils.tap_if_found(img.party_inactive)
    baiting()

    while True:
        if utils.is_found(img.life_skill_fishing_done):
            utils.wait_and_tap(img.button_confirm_medium)
            sys.exit(0)
        if utils.is_found(img.life_skill_fishing_bait):
            sys.exit(0)
        func.ang_pao()
        utils.tap_any_offset(const.guilds, offset_x=-100, offset_y=-200)
        found_image = utils.wait_and_tap(img.fishing_alert, timeout=5)
        if found_image != None:
            utils.wait_and_tap(img.life_skill_tap_anywhere, timeout=1)
        

def baiting():
    utils.wait_and_tap(img.life_skill_fishing_bait)
    if utils.wait_for_image(img.life_skill_fishing_mount, timeout=2) != None:
        utils.wait_and_tap(img.mount)
        time.sleep(1)
    utils.wait_and_tap(img.life_skill_fishing_bait)

# def fishing():
#     func.wait_profile()
#     func.ang_pao()
#     utils.tap(1000, 300)
#     utils.wait_for_image('images/fishing_alert.png')
#     utils.tap_image('images/fishing_alert.png')