import constanst as const
import img
import func
import time
import utils


def start():
    func.wait_profile()
    while True:
        utils.wait_and_tap(img.menu_bag)
        utils.scroll_down_util_found(img.treasure_map_icon, img.item_drag, 300, timeout=30)

        if not utils.is_found(img.treasure_map_icon):
            break

        utils.tap_image(img.treasure_map_icon)
        utils.wait_and_tap_any(const.button_uses)
        wait_until_lucky_wheel()


def wait_until_lucky_wheel():
    func.wait_profile()
    while True:
        if utils.is_found(img.treasure_map_lucky_wheel_start):
            utils.wait_and_tap(img.treasure_map_lucky_wheel_start)
            utils.wait_until_disappear(img.treasure_map_lucky_wheel_start)
            utils.wait_and_tap(img.treasure_map_lucky_wheel_start, timeout=5)
            func.wait(5)
            utils.tap_if_found(img.treasure_map_lucky_wheel_start)
            break
        utils.tap_if_found(img.treasure_map_tool_icon)
    
    func.ang_pao()
    func.move_down(hold=1)
    func.move_down(hold=2)
