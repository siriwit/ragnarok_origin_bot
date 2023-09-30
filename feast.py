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
            go_to_guild_hall()


def go_to_guild_hall():
    utils.wait_for_image(img.feast_option_weekend, timeout=20)
    utils.tap_image_offset(img.feast_option_weekend, offset_x=350, offset_y=-200)
    func.wait_profile()
    utils.hold_press('s', timeout=1)
    utils.hold_press('d', timeout=0.3)

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
        utils.wait_and_tap(img.food_taste, timeout=2)
        time.sleep(2)