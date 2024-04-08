import constanst as const
import func
import img
import time
import utils
import sys

def request_oracle():
    func.leave_party()
    while True:
        func.open_hidden_menu()
        utils.wait_and_tap_any(const.menu_guilds, timeout=2)
        check_oracle_request()
        utils.wait_for_image(img.guild_menu_info, timeout=2)
        check_oracle_request()
        utils.tap_image_offset(img.guild_menu_info, offset_y=100)
        check_oracle_request()
        is_anyone_accept = request_all_member()
        if not is_anyone_accept:
            oracle()


def request_all_member():
    is_found_teasing = False
    utils.wait_for_image(img.oracle_guild_page)
    check_oracle_request()
    utils.wait_for_image(img.guild_request_oracle_icon, timeout=3)
    check_oracle_request()
    while True:

        utils.tap_image(img.guild_request_oracle_icon)
        if utils.is_found(img.guild_request_oracle_icon):
            is_found_teasing = True
            utils.drag_up(img.guild_request_oracle_icon, offset_y=80)

        if check_oracle_request():
            return True

        if is_found_teasing and not utils.is_found(img.guild_request_oracle_icon):
            func.close_hidden_menu()
            return False
        
        if not is_found_teasing:
            func.close_hidden_menu()
            sys.exit(0)
        
        time.sleep(1)


def oracle(in_main_page=True):
    while True:
        if in_main_page:
            func.wait_profile()
            utils.tap_any(const.pets)

        if utils.is_found(img.button_agree):
            utils.tap_image(img.button_agree)
            utils.wait_for_image(img.oracle_present, timeout=60)
            func.send_message('[z1]')
            func.leave_event()
            func.wait_profile()
            check_oracle_request()
            time.sleep(3)
            check_oracle_request()
            func.leave_party()
            check_oracle_request()
            func.wait_profile()
            break

        time.sleep(1)

def check_oracle_request():
    if utils.is_found(img.button_agree):
        oracle(in_main_page=False)
        return True
