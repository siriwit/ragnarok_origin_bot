import constanst as const
import func
import img
import time
import utils

def maintain_woe():
    while True:
        utils.wait_for_image(img.woe_icon)
        utils.tap_any(const.pets)
        utils.tap_if_found(img.button_revive)
        if utils.is_found(img.guild_league_enemy):
            func.use_manual_skill()

        if utils.is_found(img.woe_meowmaru_ended):
            utils.tap_offset_until_notfound(img.woe_meowmaru_ended, img.woe_meowmaru_ended, offset_y=-300)
            utils.tap_until_found(img.woe_star, img.woe_treasure)
            utils.tap_until_notfound(img.woe_treasure, img.woe_treasure)
