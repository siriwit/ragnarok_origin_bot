import constanst as const
import func
import img
import time
import utils
import sys

def request_oracle():
    while True:
        if not utils.is_found(img.menu_guild):
            utils.tap_offset_until_found(img.menu_bag, img.menu_guild, offset_x=180)

        utils.wait_and_tap(img.menu_guild, timeout=2)
        utils.wait_for_image(img.guild_menu_info, timeout=2)
        utils.tap_image_offset(img.guild_menu_info, offset_y=100)
        is_anyone_accept = request_all_member()
        if not is_anyone_accept:
            oracle()


def request_all_member():
    is_found_teasing = False
    utils.wait_for_image(img.oracle_guild_page)
    utils.wait_for_image(img.guild_request_oracle_icon, timeout=3)
    while True:
        if not utils.is_found(img.guild_request_oracle_icon):
            # utils.scroll_down_util_found(img.guild_request_oracle_icon, img.guild_online_status, 300)
            close_hidden_menu()
            sys.exit(0)

        utils.tap_image(img.guild_request_oracle_icon)
        if utils.is_found(img.guild_request_oracle_icon):
            is_found_teasing = True
            utils.drag_up(img.guild_request_oracle_icon, offset_y=80)

        if utils.is_found(img.button_agree):
            oracle(in_main_page=False)
            return True

        if is_found_teasing and not utils.is_found(img.guild_request_oracle_icon):
            close_hidden_menu()
            return False
        
        time.sleep(1)


def oracle(in_main_page=True):
    while True:
        if in_main_page:
            utils.wait_for_image(img.profile)
            utils.tap_any(const.pets)

        if utils.is_found(img.button_agree):
            utils.tap_image(img.button_agree)
            utils.wait_for_image(img.oracle_present, timeout=60)
            func.send_message('[z1]')
            utils.wait_and_tap_any(const.escape_buttons, timeout=20)
            utils.wait_and_tap(img.button_confirm, timeout=20)
            utils.wait_for_image(img.profile)
            func.leave_party()
            utils.wait_for_image(img.profile)
            break

        time.sleep(1)


def close_hidden_menu():
    func.close_any_panel()
    utils.wait_for_image(img.profile)
    if utils.is_found(img.menu_guild):
        utils.tap_offset_until_found(img.menu_bag, img.butterfly_wing, offset_x=180)