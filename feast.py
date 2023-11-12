import constanst as const
import datetime
import img
import func
import time
import utils


def start():
    func.wait_profile()
    utils.tap_any(const.batterry_savings)

    today = datetime.date.today()
    day_of_week = today.weekday()
    if day_of_week < 5:
        if func.go_to_event(img.event_feast):
            go_to_guild_hall()
    else:
        if func.go_to_event(img.event_feast_weekend):
            go_to_guild_hall(is_weekend=True)


def go_to_guild_hall(is_weekend=False):
    if is_weekend:
        utils.wait_for_image(img.feast_option_weekend, timeout=20)
        utils.tap_image_offset(img.feast_option_weekend, offset_x=350, offset_y=-200)
    else:
        utils.wait_and_tap(img.feast_skip_button, timeout=20)
    func.wait_profile()
    func.move_down(hold=1)
    func.move_right(hold=0.5)

    duration_minutes = 20
    end_time = time.time() + duration_minutes * 60
    while time.time() < end_time:
        feast()
        time.sleep(1)


def feast():
    func.wait_profile()
    func.ang_pao()
    func.use_items()
    if utils.is_found(img.food_grab):
        utils.tap_image(img.food_grab)
        if utils.wait_for_image(img.food_taste, timeout=1) is not None:
            utils.wait_and_tap(img.food_taste, timeout=2)
        elif utils.wait_for_image(img.feast_action_block_while_mounted, timeout=1, similarity=0.85) is not None:
            utils.wait_and_tap(const.mounts)
        time.sleep(2)

    