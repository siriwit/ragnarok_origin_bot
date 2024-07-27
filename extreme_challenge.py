import img
import constanst as const
import func
import utils


def start(is_assist=False):
    func.close_any_panel()
    should_exit_assist = False
    if func.go_to_event(img.event_extreme_challenge) and utils.wait_for_image(img.extreme_challenge_page, timeout=120) is not None:
        while select_boss(is_assist):
            while True:
                if utils.is_found(img.button_cross_server) and utils.is_found(img.extreme_challenge_difficult_normal):
                    if utils.is_found(img.extreme_challenge_difficult_normal):
                        utils.tap_until_found(img.extreme_challenge_difficult_normal, img.extreme_challenge_difficult_hell_item)
                        utils.tap_until_found(img.extreme_challenge_difficult_hell_item, img.extreme_challenge_difficult_hell)
                    else:
                        continue
                
                if utils.is_found(img.extreme_challenge_difficult_hell):
                    utils.tap_if_found(img.button_cross_server)
                    utils.wait_and_tap(img.button_agree, timeout=1)

                    if utils.is_found(img.extreme_challenge_max_assist_reached):
                        should_exit_assist = True
                    utils.tap_until_notfound(img.button_agree, img.button_agree)
                
                if utils.is_found(img.loading) or utils.is_found(img.button_escape):
                    break

                utils.tap_if_found(img.button_cancel_white)
                    
            fight()

            if is_assist and should_exit_assist:
                break

    func.close_any_panel()


def in_queue_state():
    
    if utils.is_found(img.loading) or utils.is_found(img.button_escape):
        return True

    return False


def fight():
    func.wait_loading_screen()
    func.open_map()
    utils.tap_image_offset(img.extreme_challenge_map, offset_y=-100)
    utils.tap_image_offset(img.extreme_challenge_map, offset_y=-100)
    func.close_map()
    func.auto_attack(const.att_all)

    if utils.wait_for_image(img.victory, timeout=60) is not None:
        func.close_any_panel(img.button_escape)
        func.leave_event(5)


def select_boss(is_assist=False):
    utils.wait_for_image(img.extreme_challenge_page)
    boss_count = 0
    while not is_assist:
        if boss_count >= 4:
            return False
        
        if utils.wait_for_image(img.extreme_challenge_reward_claimed, timeout=2) is not None:
            utils.tap_image_offset(img.extreme_challenge_reward_claimed, offset_x=-300, offset_y=-120)
            boss_count += 1
            func.wait(2)
            continue
        break
    return True

