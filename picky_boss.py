import boss
import constanst as const
import func
import utils
import img
import sys
import time


def picky_boss_hunt():
    func.wait_profile()
    utils.tap_all(const.picky_boss_menu_icon)
    utils.wait_and_tap(img.picky_boss_ultimate_clash)
    utils.wait_for_image(img.picky_boss_ultimate_clash_page, timeout=2)
    if utils.is_found(img.picky_boss_ultimate_clash_page):

        if utils.is_found(img.picky_boss_3_3, threshold=0.99):
            utils.tap_image(img.button_back)
            utils.tap_image(img.button_back)
            sys.exit(0)
        
        while True:
            found_image = utils.is_found_any(const.picky_boss_times, threshold=0.99)
            if found_image == img.picky_boss_1m:
                wing_boss(60)
                break
            elif found_image == img.picky_boss_2m:
                wing_boss(120)
                break
            elif found_image == img.picky_boss_3m:
                wing_boss(180)
                break
            elif found_image == img.picky_boss_19m or found_image == img.picky_boss_20m:
                utils.wait_for_image(img.picky_boss_map)
                wing_boss(0)
                break
            time.sleep(1)
            utils.tap_image(img.picky_boss_turn_in)


def wing_boss(wait_time=60):
    utils.tap_image(img.picky_mvp)
    func.wait_and_find_party(img.picky_mvp, 'MVP Picky', 'world', wait_time, True)
    boss.boss()