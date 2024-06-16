
import boss
import func
import utils
import img
import preset as ps
import constanst as const
import time

def start():
    func.wait_profile()
    if func.go_to_event(img.event_time_anomaly):
        utils.wait_for_image(img.time_anomaly_page)

        fight_1x = 0
        fight_2x = 0
        fight_3x = 0

        while True:
            if fight_3x == 2 or utils.is_found(img.time_anomaly_event_settling):
                utils.tap_image(img.button_back)
                func.wait_profile()
                break

            if fight_1x == 0 and utils.is_found(img.time_anomaly_1x):
                if fight():
                    fight_1x += 1
            elif fight_2x == 0 and utils.is_found(img.time_anomaly_2x):
                if fight():
                    fight_2x += 1
            elif fight_3x < 1 and utils.is_found(img.time_anomaly_3x):
                horn_mode = fight_3x == 0
                if fight(horn_mode):
                    fight_1x += 1
            time.sleep(1)


def fight(horn_mode=False):
    if utils.is_found(img.button_go_challenge):
        utils.wait_and_tap(img.button_go_challenge)
        if horn_mode:
            utils.tap_offset_until_notfound(img.button_go_challenge, img.time_anomaly_page, offset_y=20)
        else:
            utils.tap_until_notfound(img.button_go_challenge, img.time_anomaly_page)
        utils.wait_and_tap(img.button_start_blue_medium)
        func.wait_profile()
        func.auto_attack(mode=const.boss)

        while True:
            func.use_manual_skill()
            if utils.is_found(img.time_anomaly_page):
                break

        return True

    return False


def preset():
    ps.change_skill_preset()
    ps.change_skill_auto(preset=const.time_anomaly)
    ps.againt_monster_card(tribe=const.dragon, element=const.earth, size=const.large, boss_level=95)
    ps.attack_preset()