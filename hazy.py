import constanst as const
import func
import img
import utils

def start():
    func.wait_profile()
    utils.tap_any_until_found_offset(const.menu_guides, img.daily_hazy, offset_x=-210)
    utils.wait_and_tap(img.daily_hazy)
    utils.wait_and_tap(img.quick_pass_ticket)
    utils.wait_and_tap_any(const.button_confirms)
    func.use_items()
    func.close_any_panel()
