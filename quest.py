import img
import func
import utils

def start(selected_quest=img.quests_event):
    func.close_any_panel()
    func.wait_profile()
    quest_start(selected_quest)

    while True:
        if utils.is_found(img.icon_message):
            utils.tap_image(img.icon_message)
            utils.tap_if_found(img.icon_next_dialog)
            func.wait(1)
            continue

        if utils.is_found(img.icon_next_dialog):
            utils.tap_image(img.icon_next_dialog)
            continue

        if utils.is_found(img.icon_collect):
            utils.tap_if_found(img.icon_collect)
            func.wait(3)
            continue
        
        utils.tap_if_found(img.button_drink)
        utils.tap_if_found(img.quests_inactive)

        if utils.is_found(img.quests):
            quest_start(selected_quest)


def quest_start(selected_quest):
    utils.tap_if_found(img.quests_inactive)
    utils.wait_and_tap(img.quests, timeout=1)
    utils.wait_and_tap(selected_quest, timeout=1)
    utils.wait_and_tap_any([img.button_go_blue_small, img.button_submit], timeout=2)