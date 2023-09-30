import constanst as const
import img
import func
import utils


def start():
    if func.go_to_event(img.event_hellheim):
        utils.wait_for_image(img.helheim_page, timeout=60)
        utils.wait_and_tap(img.button_got_it, timeout=3)
        utils.wait_and_tap(img.helheim_level_hard)

        while True:
            if utils.is_found(img.helheim_insufficient_attempt):
                break

            utils.wait_and_tap(img.helheim_skip)
            utils.wait_and_tap(img.helheim_skip_inactive)
            func.use_items()

        func.close_any_panel()