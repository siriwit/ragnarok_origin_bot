import constanst as const
import img
import func
import utils


def start():
    if func.go_to_event(img.event_hellheim):
        if utils.wait_for_image(img.helheim_page, timeout=60) is None:
            start()
            return
        
        utils.wait_and_tap(img.button_got_it, timeout=3)
        utils.wait_and_tap(img.helheim_level_hard)

        utils.execute_until_valid_state_with_timeout(30, 1, skip_state)

        func.close_any_panel()

def skip_state():
    if utils.is_found(img.helheim_insufficient_attempt):
        return True

    utils.wait_and_tap(img.helheim_skip_inactive)
    utils.wait_and_tap(img.helheim_skip)
    
    func.use_items()
    return False