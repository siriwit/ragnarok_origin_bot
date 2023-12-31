import constanst as const
import img
import func
import utils
import time
import sys


def start(mode='forging', expected_food=img.life_skill_cooking_seafood_fried_noodles):
    utils.tap_offset_until_found(img.menu_bag, img.menu_life_skill, offset_x=180)
    utils.tap_image(img.menu_life_skill)
    utils.wait_for_image(img.life_skill_path_of_arts, timeout=2)
    if mode == 'forging' or mode == 'fishing':
        if not utils.is_found(img.life_skill_path_of_arts):
            utils.tap_until_found(img.life_skill_path_of_nature, img.life_skill_path_of_arts)
    elif mode == 'cooking':
        if not utils.is_found(img.life_skill_path_of_nature):
            utils.tap_until_found(img.life_skill_path_of_arts, img.life_skill_path_of_nature)

    if mode == 'forging':
        utils.wait_and_tap(img.life_skill_forging, timeout=3, similarity=0.7)
    elif mode == 'fishing':
        utils.wait_and_tap(img.life_skill_fishing)
    elif mode == 'cooking':
        utils.wait_and_tap(img.life_skill_cooking)

    if mode == 'forging' or mode == 'fishing':
        utils.wait_for_image(img.life_skill_magnifying_glass)
        utils.tap_until_found(img.life_skill_magnifying_glass, img.life_skill_nature_go)
        utils.wait_and_tap(img.life_skill_nature_go)
        utils.tap_offset_until_found(img.menu_bag, img.butterfly_wing, offset_x=180)
    elif mode == 'cooking':
        utils.wait_and_tap(img.life_skill_arts_go)
        utils.tap_offset_until_found(img.menu_bag, img.butterfly_wing, offset_x=180)

    if mode == 'forging':
        utils.wait_for_image(img.forging, timeout=120)
        forging()
    elif mode == 'fishing':
        utils.wait_for_image(img.life_skill_fishing_bait, timeout=120)
        fishing()
    elif mode == 'cooking':
        while True:
            if utils.is_found(img.life_skill_cooking_page):
                break
            if utils.is_found(img.life_skill_cooking_pot):
                utils.tap_until_found(img.life_skill_cooking_pot, img.life_skill_cooking_page)
        cooking(expected_food)


def forging():
    while True:
        if utils.is_found(img.life_skill_forging_run_out):
            sys.exit(0)

        func.wait_profile()
        func.ang_pao()
        utils.tap_image(img.forging)


def fishing():
    utils.tap_if_found(img.party_inactive)
    baiting()

    while True:
        if utils.is_found(img.life_skill_fishing_done):
            utils.wait_and_tap(img.button_confirm_medium)
            sys.exit(0)
        if utils.is_found(img.life_skill_fishing_bait):
            sys.exit(0)
        func.ang_pao()
        utils.tap_any_offset(const.guilds, offset_x=-100, offset_y=-200)
        found_image = utils.wait_and_tap(img.fishing_alert, timeout=5)
        if found_image is not None:
            utils.wait_for_image(img.life_skill_tap_anywhere, timeout=1)
            utils.tap_image_offset(img.life_skill_tap_anywhere, offset_x=-400, offset_y=-400)
        

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
    utils.scroll_down_util_found(food_image, img.life_skill_cooking_drag_icon, timeout=30, offset_y=200)
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
    utils.wait_and_tap(img.backpack_menu_consumable)
    utils.wait_for_image(food_item)
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