import img
import func
import utils


def divination():
    go_to_divination_main_page(divination_state)


def divination_state():
    utils.tap_until_found(img.divination_house_daily_fortune, img.icon_message)
    func.wait(2)
    icons = utils.find_all_image_with_similarity(img.icon_message)
    if len(icons) > 1:
        utils.tap_location_until_found(icons[1], img.divination_house_daily_fortune_item_orange)
        func.wait(2)
        utils.drag_and_drop_image(img.divination_house_daily_fortune_item_orange, img.divination_house_daily_fortune_item_target)
        utils.drag_and_drop_image(img.divination_house_daily_fortune_item_teeth, img.divination_house_daily_fortune_item_target)
        utils.wait_and_tap(img.divination_house_daily_fortune_tap_anywhere)
        if utils.wait_for_image(img.icon_message, timeout=5) is not None:
            topbox = utils.find_most_top_coordinate([img.icon_message])
            utils.tap_location(topbox)
            utils.wait_for_image(img.divination_house_daily_fortune_nala, timeout=3)
            utils.tap_until_notfound(img.divination_house_daily_fortune_nala, img.divination_house_daily_fortune_nala)


def meow_tarot():
    go_to_divination_main_page(meow_tarot_state)


def meow_tarot_state():
    utils.tap_until_found(img.divination_house_meow_tarot, img.icon_message)
    func.wait(1)
    icons = utils.find_all_image_with_similarity(img.icon_message)
    if len(icons) > 1:
        utils.tap_location_until_found(icons[1], img.divination_house_meow_tarot_sanity)
        utils.tap_until_found(img.divination_house_meow_tarot_sanity, img.divination_house_meow_tarot_gift_x1)
        utils.tap_until_notfound(img.divination_house_meow_tarot_gift_x1, img.divination_house_meow_tarot_gift_x1)
        if utils.wait_and_tap(img.divination_house_meow_tarot_close_button, timeout=30) is not None and \
            utils.wait_for_image(img.divination_house_meow_tarot_nala) is not None:
            utils.tap_any_until_notfound_any([img.divination_house_meow_tarot_nala, img.divination_house_meow_tarot_jjjj], 
                                             [img.divination_house_meow_tarot_nala, img.divination_house_meow_tarot_jjjj], 
                                             delay=1)


def go_to_divination_main_page(executable_function):
    if func.go_to_event(img.event_divination_house):
        utils.wait_for_image(img.icon_message, timeout=120)
        func.wait(1)
        icon = utils.find_most_top_coordinate([img.icon_message])
        if icon is not None:
            utils.tap_location_until_found(icon, img.divination_house_daily_fortune, delay=5)
            executable_function()
        func.close_any_panel()


def wishing_pool():
    func.open_map()
    utils.wait_for_image(img.map_free_port_wishing_pool)
    utils.tap_image_offset(img.map_free_port_wishing_pool, offset_x=-3, offset_y=3)
    func.close_map()
    if utils.wait_for_image(img.doram_wishing_pool_wish, timeout=180) is not None:
        utils.execute_until_invalid_state(180, 1, wishing_state)


def wishing_state():
    utils.tap_until_found(img.doram_wishing_pool_wish, img.button_confirm)
    if utils.wait_for_image(img.doram_wishing_pool_wish_no_rewards, timeout=3) is not None:
        utils.tap_until_notfound(img.button_cancel_white, img.button_cancel_white)
        return False
    else:
        utils.tap_until_notfound(img.button_confirm, img.button_confirm)
        func.wait(5)
    return True


def transform_doram():
    utils.execute_until_valid_state_with_timeout(10, 1, transform_doram_state)
        

def transform_doram_state():
    if utils.wait_for_image(img.doram_skill_eye, timeout=1) is not None:
        return True
    utils.tap_if_found(img.ride_peco)
    func.wait(2)
    utils.key_press('t')
    return False


def beach_hidden_obj():
    func.open_map()
    utils.wait_for_image(img.map_free_port_star)
    utils.tap_image_offset(img.map_free_port_star, offset_x=56, offset_y=-32)
    func.close_map()
    func.wait(60)
    if utils.wait_for_image(img.doram_hidden_obj_search, timeout=180) is not None:
        utils.execute_until_invalid_state(240, 1, hidden_obj_search_state)


def hidden_obj_search_state():
    utils.tap_until_notfound(img.doram_hidden_obj_search, img.doram_hidden_obj_search)
    if utils.wait_for_image(img.doram_hidden_obj_search_daily_limit, timeout=3) is not None:
        return False
    return True


def onsen_pool():
    func.open_map()
    utils.wait_for_image(img.map_free_port_onsen_pool)
    utils.tap_image_offset(img.map_free_port_onsen_pool, offset_x=30, offset_y=-30)
    func.close_map()
    func.wait(60)
    if utils.wait_for_image(img.doram_onsen_enter, timeout=300) is not None:
        func.wait(3)
        utils.wait_for_image(img.doram_onsen_enter, timeout=2)
        utils.tap_until_found(img.doram_onsen_enter, img.button_confirm, delay=2)
        utils.tap_until_notfound(img.button_confirm, img.button_confirm, delay=2)
        utils.wait_for_image(img.doram_onsen_enter)
        utils.execute_until_invalid_state(720, 1, onsen_state)


def onsen_state():
    utils.tap_if_found(img.doram_skill_eye)
    if utils.wait_for_image(img.doram_onsen_enter, timeout=2) is None:
        return False
    return True