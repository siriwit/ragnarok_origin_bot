
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
                if fight():
                    fight_1x += 1
            time.sleep(1)


def fight():
    if utils.is_found(img.button_go_challenge):
        utils.wait_and_tap(img.button_go_challenge)
        utils.wait_and_tap(img.button_start_blue_medium)
        
        func.wait_profile()
        func.auto_attack()

        utils.wait_for_image(img.time_anomaly_page, timeout=60)
        return True

    return False


def preset():
    ps.change_skill_preset()
    ps.change_skill_auto(preset=const.time_anomaly)
    ps.againt_monster_card(tribe=const.dragon, element=const.water, size=const.large)
    ps.attack_preset()