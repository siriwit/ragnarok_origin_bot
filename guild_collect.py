import constanst as const
import func
import img
import utils


def start():
    func.open_hidden_menu()
    utils.wait_and_tap_any(const.menu_guilds, timeout=2)
    utils.wait_for_image(img.guild_menu_info, timeout=2)
    utils.tap_image_offset(img.guild_menu_info, offset_y=300)

    collect_sign_in()
    collect_city_lord()



def collect_sign_in():
    utils.wait_and_tap(img.guild_collect_guild_sign_in)


def collect_city_lord():
    utils.scroll_down_util_found(img.guild_collect_city_lord_room, img.guild_collect_guild_sign_in, offset_y=200)
    utils.wait_and_tap(img.guild_collect_city_lord_room)
    utils.wait_and_tap(img.guild_collect_option_enter_the_master_chamber, timeout=30)
    utils.wait_and_tap_any(const.city_lord_room_treasures, similarity=0.25, timeout=20)
    utils.wait_for_image(img.guild_collect_city_lord_room_treasure_obtained)
    func.butterfly_wing_morroc()
    