import constanst as const
import img
import func
import time
import utils


def start():
    utils.wait_for_image(img.profile)
    utils.wait_and_tap(img.menu_bag)
    utils.scroll_down_util_found(img.treasure_map_icon, img.item_drag, 300, timeout=30)
    utils.tap_image(img.treasure_map_icon)
    utils.wait_and_tap_any(const.button_uses)
    wait_until_lucky_wheel()


def wait_until_lucky_wheel():
    utils.wait_for_image(img.profile)
    utils.wait_and_tap(img.treasure_map_lucky_wheel_start, timeout=120)
    while True:
        func.ang_pao()
        utils.tap_if_found(img.treasure_map_lucky_wheel_start)
        time.sleep(1)
