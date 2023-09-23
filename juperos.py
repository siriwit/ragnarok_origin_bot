import boss
import func
import img
import utils

def start():
    utils.wait_for_image(img.profile)
    if func.go_to_event(img.event_juperos):
        utils.wait_for_image(img.juperos_page)
        utils.wait_and_tap(img.button_start_blue_medium)
        fight()


def fight():
    utils.wait_for_image(img.profile, timeout=150)
    utils.key_press('k')
    boss.boss_fight(butterflywing=False)

