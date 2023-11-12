import constanst as const
import func
import img
import time
import utils

def maintain_woe():
    while True:
        utils.wait_for_image(img.woe_icon)
        utils.tap_any(const.pets)
        utils.tap_if_found(img.button_respawn)
        time.sleep(1)