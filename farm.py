import constanst as const
import func
import img
import utils

def farm(minutes, monster_name, monster_element):
    func.create_party_and_invite()
    func.element_convert(monster_element)
    utils.execute_until_valid_state_with_timeout((minutes*60), 1, farm_state, monster_name, monster_element)


def farm_disable():
    utils.tap_offset_until_found(img.power_up_icon, img.farm_page, offset_y=80)
    utils.wait_for_image(img.farm_unlock_button, timeout=2)
    unlocks = utils.find_all_image_with_similarity(img.farm_unlock_button)
    if len(unlocks) < 2:
        utils.tap_until_found(img.farm_close_button, img.farm_unlock_button)
    func.close_any_panel()


def farm_enable():
    utils.tap_offset_until_found(img.power_up_icon, img.farm_page, offset_y=80)
    unlocks = utils.find_all_image_with_similarity(img.farm_unlock_button)
    if len(unlocks) >= 2:
        utils.tap_location_until_found(unlocks[1], img.farm_close_button)
    func.close_any_panel()


def monster_annihilation(minutes):
    utils.execute_until_valid_state_with_timeout((minutes*60), 1, monster_annihilation_state)


def farm_state(monster_name, monster_element):

    message = f'{monster_name} {func.find_remaining_party_number()} auto join'
    if not utils.is_found(img.party_number_5):
        func.send_message(message, send_to='world')

    utils.execute_until_valid_state_with_timeout(300, 1, check_item_loop, True, monster_element)

    handle_material()

    if utils.is_found(img.fatique_icon, similarity=0.95):
        utils.tap_any_until_found_offset(const.menu_bags, img.butterfly_wing, offset_x=210, offset_y=50)
        func.butterfly_wing_morroc()
        func.send_message(f"done [z1]")
        func.leave_party()
        return True

    return False


def monster_annihilation_state():
    utils.execute_until_valid_state_with_timeout(300, 1, check_item_loop, False)
    handle_material()

    if utils.is_found(img.map_morroc):
        return True
    return False


def handle_material():
    similarity = 0.95
    stalling_item_list = [img.item_dust_999, img.item_insect_leg_999]
    # selling_list = [img.item_pine_apple_999, img.item_melon_999, img.item_red_candle_999]
    func.open_bag()
    utils.tap_image_offset(img.button_close, offset_x=100, offset_y=270)

    stalling_item(stalling_item_list, similarity)
    # sell_item(selling_list, similarity)

    func.close_any_panel()


def stalling_item(stalling_item_list, similarity):
    if utils.wait_any_image(stalling_item_list, timeout=5, similarity=similarity) is not None:
        utils.tap_any_until_found(stalling_item_list, img.button_more, similarity=similarity)
        utils.tap_until_found(img.button_more, img.button_stall)
        utils.tap_until_found(img.button_stall, img.button_list_item)
        utils.execute_until_invalid_state(60, 1, stalling_item_loop, stalling_item_list, similarity)


def stalling_item_loop(stalling_item_list, similarity):
    utils.tap_if_found(img.button_list_item)
    coords = utils.find_image_more_than_offset_coordinate(stalling_item_list, offset_x=700, offset_y=0, similarity=similarity)
    if len(coords) > 0:
        utils.tap_location_until_found(coords[0], img.button_list_item, timeout=3)
        if utils.wait_for_image(img.button_list_item) is not None:
            utils.tap_until_notfound(img.button_list_item, img.button_list_item)
            func.wait(1)
        return True
    return False


def sell_item(selling_list, similarity):
    if utils.wait_any_image(selling_list, timeout=1, similarity=similarity) is not None:
        utils.wait_and_tap_any(selling_list, similarity=similarity)
        utils.tap_until_found(img.button_sell_small_blue, img.selling_list_page)
        utils.execute_until_invalid_state(60, 1, sell_item_loop, selling_list, similarity)


def sell_item_loop(selling_list, similarity):
    if utils.is_found_any(selling_list, similarity=similarity):
        utils.wait_and_tap_any(selling_list, similarity=similarity)
        if utils.wait_for_image(img.button_sell_small_blue) is not None:
            utils.tap_until_found(img.button_sell_small_blue, img.button_sell_large_blue)
            utils.tap_until_notfound(img.button_sell_large_blue, img.button_sell_large_blue)
            utils.wait_for_image(img.selling_list_you_sold, timeout=2)
            utils.wait_until_disappear(img.selling_list_you_sold, timeout=5)
        return True
    return False


def check_item_loop(should_check_fatique_icon=True, monster_element=const.neutral):
    func.wait_profile()

    if should_check_fatique_icon and utils.is_found(img.fatique_icon):
        return True
    
    func.kick_party_member()
    func.ang_pao()
    func.use_items()
    func.use_manual_skill(const.farm, monster_element)
    func.guild_quest_aid()

    return False