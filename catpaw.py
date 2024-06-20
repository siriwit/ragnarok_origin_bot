import constanst as const
import img
import func
import time
import utils


def daily_cat_paw():
    func.wait_profile()
    utils.execute_until_valid_state_with_timeout(600, 1, go_to_catpaw_state)


def go_to_catpaw_state():
    func.close_any_panel()
    if utils.is_found(img.cat_paw_caravan_icon):
        utils.tap_image(img.cat_paw_caravan_icon)
        if utils.wait_for_image(img.cat_paw_caravan_topbar, timeout=2) is not None:
            utils.execute_until_valid_state_with_timeout(120, 1, load_cargo_state)
            return True
    
    utils.execute_until_valid_state_with_timeout(30, 1, func.open_daily_page_state)
    utils.tap_image(img.daily_catpaw)
    utils.tap_until_notfound(img.button_go, img.button_go)
    if utils.wait_and_tap(img.icon_message, timeout=60) is not None:
        if utils.wait_for_image(img.cat_paw_caravan_topbar, timeout=2) is not None:
            utils.execute_until_valid_state_with_timeout(120, 1, load_cargo_state)
            return True
    return False


def load_cargo_state():
    utils.tap_image(img.button_quick_departure)
    utils.wait_and_tap(img.button_confirm, timeout=2)
    utils.tap_image(img.cat_paw_caravan_claim_finished)

    utils.tap_if_found(img.cat_paw_caravan_return_now)

    if utils.is_found(img.cat_paw_caravan_return_now):
        utils.tap_image(img.cat_paw_caravan_return_now)
        time.sleep(1)

    if utils.is_found(img.button_claimed):
        func.close_any_panel()
        return True
    
    return False