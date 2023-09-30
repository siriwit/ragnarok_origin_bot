import boss
import constanst as const
import func
import img
import utils

def start():
    func.wait_profile()
    if func.go_to_event(img.event_juperos):
        utils.wait_for_image(img.juperos_page)
        utils.wait_and_tap(img.button_start_blue_medium)
        fight()


def fight():
    utils.wait_any_image(const.profiles, timeout=150)
    utils.key_press('k')
    boss.boss_fight(butterflywing=False)

