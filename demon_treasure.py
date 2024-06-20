import constanst as const
import func
import img
import time
import utils

def daily_demon_treasure():
    func.wait_profile()
    utils.execute_until_valid_state_with_timeout(30, 1, func.open_daily_page_state)
    if utils.wait_and_tap(img.daily_demon_treasure, timeout=2) is not None:
        utils.tap_until_found(img.button_go, img.daily_demon_treasure_prontera_west)
        utils.wait_and_tap(img.daily_demon_treasure_prontera_west)
        demon_treasure()
    else:
        func.close_any_panel()


def demon_treasure(firstime=True):
    count = 0
    while True:
        func.close_any_panel()
        if utils.is_found(img.daily_demon_treasure_rescue):
            utils.tap_image(img.daily_demon_treasure_rescue)
            count = 0

        func.use_items()
        if utils.is_found(img.button_close_purple):
            time.sleep(5)
            utils.tap_image(img.button_close_purple)

        utils.wait_any_image([img.daily_demon_treasure_reach_limit1, img.daily_demon_treasure_reach_limit2], timeout=1)
        if utils.is_found_any([img.daily_demon_treasure_reach_limit1, img.daily_demon_treasure_reach_limit2]):
            time.sleep(5)
            if firstime:
                demon_treasure(firstime=False)
            break

        count += 1
        print(f"count: {count}")

        if count > 10:
            daily_demon_treasure()
        func.wait(1)