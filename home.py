import img
import func
import utils


def farm(mode):
    if mode == 'plant':
        utils.exit_at_specific_time_or_invalid_state(4, 50, plant_mode, [img.home_farm_plant_flax, img.home_farm_plant_carrot])


def plant_mode(seeds):
    func.create_party_and_invite()
    if go_to_home():
        utils.tap_offset_until_found(img.home_guide_quest, img.home_management_center_page, offset_x=-100, offset_y=0)
        utils.tap_until_found(img.home_management_center_farm, img.button_go_blue_small2)
        utils.tap_until_notfound(img.button_go_blue_small2, img.button_go_blue_small2)
        if utils.wait_for_image(img.home_guide_quest, timeout=5) is not None:
            utils.execute_until_valid_state_with_timeout(10, 1, move_farm_state)
            if utils.is_found_any([img.home_farm_harvest, img.home_farm_plant, img.home_farm_plant_fertilize]) is not None:
                utils.execute_until_invalid_state(60, 1, plant_harvest_state, seeds[0])
                utils.execute_until_valid_state_with_timeout(10, 1, moveup_farm_state, [img.home_farm_harvest, img.home_farm_plant])
                utils.execute_until_invalid_state(60, 1, plant_harvest_state, seeds[1])
    else:
        func.close_hidden_menu()
    func.leave_event()
    func.wait(120)
    return True


def move_farm_state():
    if utils.wait_any_image([img.home_farm_harvest, img.home_farm_plant, img.home_farm_plant_fertilize], timeout=2) is not None:
        return True
    func.move_right()
    return False


def moveout_farm_state():
    if utils.wait_any_image([img.home_farm_plant_fertilize], timeout=2) is None:
        return True
    func.move_left()
    return False


def moveup_farm_state(until_founds):
    if utils.wait_any_image(until_founds, timeout=2) is not None:
        return True
    func.move_up()
    return False


def plant_harvest_state(seed):
    if utils.is_found(img.home_farm_harvest):
        harvest()
    
    if utils.is_found(img.home_farm_plant):
        plant(seed)

    if utils.is_found(img.home_farm_plant_fertilize):
        return False
    else:
        utils.execute_until_valid_state_with_timeout(10, 1, move_farm_state)

    return True


def harvest():
    multiple_selection(img.home_farm_harvest)
    utils.tap_until_notfound(img.home_farm_harvest, img.home_farm_harvest)


def plant(seed):
    multiple_selection(img.home_farm_plant)
    utils.wait_and_tap(seed)
    utils.tap_image(img.home_farm_plant)
    if utils.wait_for_image(img.button_buy_orange1, timeout=2) is not None:
        utils.tap_until_found(img.home_farm_plant, img.button_buy_orange1)
        utils.tap_until_notfound(img.button_buy_orange1, img.button_buy_orange1)
        utils.wait_for_image(img.home_farm_plant)
    utils.tap_until_found(img.home_farm_plant, img.home_farm_plant_fertilize)


def multiple_selection(target_image):
    utils.tap_image_offset(target_image, offset_x=-130, offset_y=-320)


def go_to_home():
    func.open_hidden_menu()
    if utils.tap_offset_until_found(img.menu_album, img.home_page, offset_x=-450, offset_y=-450):
        utils.wait_for_image(img.home_page)
        utils.wait_and_tap(img.button_return_to_home)
        if utils.wait_for_image(img.home_guide_quest, timeout=30) is not None:
            return True
    return False