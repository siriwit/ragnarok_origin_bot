import constanst as const
import img
import func
import time
import utils


def daily_cat_paw():
    func.wait_profile()

    if utils.is_found(img.cat_paw_caravan_icon):
        utils.tap_image(img.cat_paw_caravan_icon)
    else:
        utils.tap_any_until_found_offset(const.menu_guides, img.daily_quest_page, offset_x=-200)
        utils.tap_image(img.daily_catpaw)
        utils.tap_until_notfound(img.button_go, img.button_go)
        utils.wait_and_tap(img.icon_message, timeout=60)

    utils.wait_for_image(img.cat_paw_caravan_topbar, timeout=2)
    load_cargo()


def load_cargo():
    while True:
        utils.tap_image(img.button_quick_departure)
        utils.wait_and_tap(img.button_confirm, timeout=2)
        utils.tap_image(img.cat_paw_caravan_claim_finished)

        if utils.is_found(img.button_claimed):
            func.close_any_panel()
            break
        
        time.sleep(1)