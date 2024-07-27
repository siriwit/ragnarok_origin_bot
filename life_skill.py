import constanst as const
import img
import func
import utils
import time
import sys


def start(mode='foraging', expected_food=img.life_skill_cooking_seafood_fried_noodles):
    utils.execute_until_valid_state_with_timeout(600, 1, life_skill_state, mode, expected_food)


def life_skill_state(mode, expected_food):
    func.use_items()
    func.close_any_panel(img.butterfly_wing)
    func.open_hidden_menu()
    func.wait(1)
    utils.tap_any_until_found_any([img.menu_life_skill], img.life_skill_path_of_arts)
    if mode == 'foraging' or mode == 'fishing':
        if not utils.is_found(img.life_skill_path_of_arts):
            utils.tap_until_found(img.life_skill_path_of_nature, img.life_skill_path_of_arts)
    elif mode == 'cooking':
        if not utils.is_found(img.life_skill_path_of_nature):
            utils.tap_until_found(img.life_skill_path_of_arts, img.life_skill_path_of_nature)

    if mode == 'foraging':
        utils.wait_and_tap(img.life_skill_foraging, timeout=3, similarity=0.7)
    elif mode == 'fishing':
        utils.wait_and_tap(img.life_skill_fishing)
    elif mode == 'cooking':
        utils.wait_and_tap(img.life_skill_cooking)

    if mode == 'foraging' or mode == 'fishing':
        utils.wait_for_image(img.life_skill_magnifying_glass)
        utils.tap_until_found(img.life_skill_magnifying_glass, img.life_skill_nature_go)
        utils.tap_until_notfound(img.life_skill_nature_go, img.life_skill_nature_go)
        func.close_hidden_menu()
    elif mode == 'cooking':
        utils.wait_and_tap(img.life_skill_arts_go)
        func.close_hidden_menu()

    if mode == 'foraging':
        if utils.wait_for_image(img.foraging, timeout=120) is not None:
            foraging()
        else:
            life_skill_state('foraging', None)
        return True
    elif mode == 'fishing':
        if utils.wait_for_image(img.life_skill_fishing_bait, timeout=120) is not None:
            fishing()
        else:
            life_skill_state('fishing', None)
        return True
    elif mode == 'cooking':
        utils.execute_until_valid_state_with_timeout(60, 1, wait_cooking_page_state, expected_food)
        return True
    
    return False


def wait_cooking_page_state(expected_food):
    utils.wait_and_tap(img.life_skill_cooking_pot, timeout=2)
    if utils.is_found(img.life_skill_cooking_page):
        cooking(expected_food)
        return True
    return False


def foraging():
    utils.execute_until_valid_state_with_timeout(600, 1, foraging_state)


def foraging_state():
    if utils.wait_for_image(img.life_skill_foraging_run_out, timeout=2) is not None:
        return True

    func.close_any_panel()
    func.ang_pao()
    utils.tap_image(img.foraging)
    return False


def fishing():
    utils.tap_if_found(img.party_inactive)
    baiting()
    utils.execute_until_valid_state_with_timeout(2000, 1, fishing_state)   


def fishing_state():
    if utils.is_found(img.life_skill_fishing_done):
        utils.wait_and_tap(img.button_confirm_medium)
        return True
    if utils.is_found(img.life_skill_fishing_bait):
        return True
    func.ang_pao()
    func.close_any_panel()
    utils.tap_any_offset(const.guilds, offset_x=-200, offset_y=-200)
    found_image = utils.wait_and_tap(img.fishing_alert, timeout=5)
    if found_image is not None:
        utils.wait_for_image(img.life_skill_tap_anywhere, timeout=1)
        utils.tap_image_offset(img.life_skill_tap_anywhere, offset_x=-400, offset_y=-400)
    return False
        

def baiting():
    utils.wait_for_image(img.life_skill_fishing_bait)
    while True:
        utils.tap_image(img.life_skill_fishing_bait)
        if utils.is_found(img.life_skill_fishing_mount):
            utils.tap_image(img.mount, similarity=0.7)
        if utils.is_found(img.life_skill_fishing_leave):
            break

def cooking(expected_food):
    cooking_normal_food(expected_food)
    combine_food(expected_food)
    cooking_3star(expected_food)


def cooking_normal_food(expected_food):
    while True:
        if utils.is_found(img.life_skill_cooking_page):
            break
        elif utils.is_found(img.life_skill_cooking_pot):
            utils.tap_image(img.life_skill_cooking_pot)
            break
        func.wait(1)

    if expected_food == img.life_skill_cooking_seafood_fried_noodles:
        cook(img.life_skill_cooking_chewy_noodles, 5, main_food=expected_food)
        func.wait()
        utils.wait_and_tap(img.life_skill_cooking_pot)
        cook(img.life_skill_cooking_tuna_kebab, 5, main_food=expected_food)
        func.wait()
    elif expected_food == img.life_skill_cooking_scallop_and_crab_congee:
        cook(img.life_skill_cooking_crab_stick, 5, main_food=expected_food)
        func.wait()
        utils.wait_and_tap(img.life_skill_cooking_pot)
        cook(img.life_skill_cooking_scallop_congee, 5, main_food=expected_food)
        func.wait()
    func.close_any_panel()


def cooking_3star(expected_food):
    while True:
        if utils.is_found(img.wing):
            break
        utils.key_press('m')
        utils.wait_for_image(img.wing)
    utils.tap_image_offset(img.wing, offset_x=-70, offset_y=-115)
    utils.key_press('m')
    func.wait(10)
    utils.wait_for_image(img.life_skill_cooking_pot, timeout=30)
    utils.tap_until_found(img.life_skill_cooking_pot, img.life_skill_cooking_meal_prep)
    cook(expected_food, 1, is_star_food=True)
    func.wait(5)
    func.close_any_panel()


def cook(food_image, number, is_star_food=False, main_food=img.life_skill_cooking_seafood_fried_noodles):
    utils.scroll_down_until_found(food_image, img.life_skill_cooking_drag_icon, timeout=30, offset_y=200)
    utils.wait_and_tap(food_image)

    if is_star_food:
        utils.tap_until_found(img.life_skill_cooking_3star_inactive, img.life_skill_cooking_3star_active)
        
    for _ in range(number-1):
        utils.tap_image(img.life_skill_cooking_plus_button)
    utils.wait_and_tap(img.life_skill_cooking_produce_button)

    if utils.wait_for_image(img.life_skill_cooking_mounted, 3) is not None:
        func.close_any_panel()
        func.wait(2)
        utils.wait_and_tap_any(const.mounts)
        cooking_normal_food(main_food)


def combine_food(expected_food):

    if expected_food == img.life_skill_cooking_seafood_fried_noodles:
        combine(img.backpack_chewy_noodles_1x)
        combine(img.backpack_tuna_kebab_1x)
        combine(img.backpack_chewy_noodles_2x)
        combine(img.backpack_tuna_kebab_2x)
    elif expected_food == img.life_skill_cooking_scallop_and_crab_congee:
        combine(img.backpack_crab_stick_1x)
        combine(img.backpack_scallop_congee_1x)
        combine(img.backpack_crab_stick_2x)
        combine(img.backpack_scallop_congee_2x)


def combine(food_item):
    func.open_bag()
    utils.tap_image_offset(img.backpack_eden_coin, offset_x=30, offset_y=280)
    utils.tap_offset_until_found(img.backpack_star, food_item, offset_y=280)
    foods = utils.find_all_image_with_similarity(food_item, similarity=0.95)
    for food in foods:
        utils.tap_location(food)
        if utils.wait_and_tap(img.button_more, timeout=1) is not None:
            utils.wait_and_tap(img.button_combine,timeout=1)
            utils.wait_for_image(img.life_skill_cooking_plus_button)
            for _ in range(5):
                utils.tap_image(img.life_skill_cooking_plus_button)
            func.wait(1)
            utils.wait_and_tap(img.button_combine_large)
            utils.wait_and_tap(img.button_confirm, timeout=1)
            utils.wait_for_image(img.combine_obtained)
            func.close_any_panel()
            break
    func.close_any_panel()