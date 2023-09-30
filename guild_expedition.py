import img
import func
import preset as pre
import time
import utils

def start():
    func.wait_profile()
    if func.go_to_event(img.event_guild_expedition):
        go_to_expedition()

        duration_minutes = 20
        end_time = time.time() + duration_minutes * 60
        while time.time() < end_time:
            if utils.is_found(img.button_quick_respawn):
                utils.tap_image(img.button_quick_respawn)
                time.sleep(2)
                if utils.wait_for_image(img.guild_expedition_map_fun_arena, timeout=2) != None:
                    func.auto_attack()
                else:
                    utils.wait_and_tap(img.menu_hourglass)
                    utils.wait_and_tap(img.guild_expedition_icon)
                    go_to_expedition()


def go_to_expedition():
    # utils.wait_for_image(img.guild_expedition_page)
    utils.wait_and_tap(img.guild_expedition_boss_drake)
    utils.wait_and_tap(img.button_go_blue_medium)
    func.wait_profile()
    func.auto_attack()


def preset():
    pre.pvp()