import constanst as const
import func
import img
import utils

def start():
    utils.execute_until_valid_state_with_timeout(600, 1, hazy_state)


def hazy_state():
    func.close_any_panel()
    func.wait_profile()
    utils.tap_any_until_found_offset(const.menu_guides, img.daily_hazy, offset_x=-210)
    if utils.wait_and_tap(img.daily_hazy) is not None:
        utils.wait_and_tap(img.quick_pass_ticket)
        utils.wait_and_tap_any(const.button_confirms)
        func.use_items()
        func.close_any_panel()
        return True
    
    return False
