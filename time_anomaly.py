
import boss
import func
import utils
import img
import preset as ps
import constanst as const

def time_anomaly():
    utils.wait_for_image(img.profile)
    if func.go_to_event():
        utils.wait_and_tap(img.event_time_anomaly)
        utils.wait_and_tap(img.button_go_orange_small)
        utils.wait_and_tap(img.button_go_challenge)
        utils.wait_and_tap(img.button_start_blue_medium)
        
        utils.wait_for_image(img.profile)
        utils.key_press('k')
        func.enable_aura()

        utils.wait_for_image(img.time_anomaly_page, timeout=60)


def preset():
    ps.change_skill_preset()
    ps.change_skill_auto(preset=const.time_anomaly)
    ps.againt_monster_card(tribe=const.dragon, element=const.water, size=const.large)
    ps.attack_preset()