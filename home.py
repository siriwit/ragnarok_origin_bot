import img
import constanst as const
import func
import json
import random
import utils

plant_cache = {img.home_farm_plant_wheat: 0, 
               img.home_farm_plant_corn: 0, 
               img.home_farm_plant_flax: 0, 
               img.home_farm_plant_carrot: 0,
               img.home_farm_plant_mushroom: 0}

plant_point = {img.home_farm_plant_wheat: 10, 
               img.home_farm_plant_corn: 10, 
               img.home_farm_plant_flax: 30, 
               img.home_farm_plant_carrot: 60,
               img.home_farm_plant_mushroom: 120}

def farm(mode='onetime'):
    plants = [img.home_farm_plant_wheat, img.home_farm_plant_corn, img.home_farm_plant_flax, img.home_farm_plant_carrot, img.home_farm_plant_mushroom]
    restore_plant_point()
    print(f"restore plant: {plant_cache}")
    func.create_party_and_invite()
    if go_to_home():
        if mode == 'loop':
            utils.exit_at_specific_time_or_invalid_state(4, 50, farm_state, plants, True, True)
        elif mode == 'onetime':
            farm_state(plants, True, False)
    func.close_hidden_menu()
    func.leave_event()


def restore_plant_point():
    global plant_cache
    try:
        with open("plant.json", "r") as file:
            plant_cache = json.load(file)
            print(f"inside plant: {plant_cache}")
    except FileNotFoundError:
        print(f"not found plant: {plant_cache}")
        plant_cache = {img.home_farm_plant_wheat: 0, 
               img.home_farm_plant_corn: 0, 
               img.home_farm_plant_flax: 0, 
               img.home_farm_plant_carrot: 0,
               img.home_farm_plant_mushroom: 0}


def farm_state(seeds, random_plant=False, is_loop_mode=True):
    plant_mode_state(seeds, random_plant)
    animal_farm_state()
    midtown()
    if is_loop_mode:
        utils.execute_until_invalid_state(120, 1, func.waiting_loop_state)
    return True


def midtown():
    home_management_selection(img.home_management_center_workshop)
    ensure_party_ui()
    utils.execute_until_valid_state_with_timeout(20, 1, movedown_midtown_state)


def plant_mode_state(seeds, random_plant):
    if random_plant:
        seeds = pick_plant(plant_cache)
        print(f"seeds: {seeds}")

    home_management_selection(img.home_management_center_farm)
    if utils.wait_for_image(img.home_guide_quest, timeout=5) is not None:
        ensure_party_ui()
        utils.execute_until_valid_state_with_timeout(10, 1, move_farm_state)
        if utils.is_found_any([img.home_farm_harvest, img.home_farm_plant, img.home_farm_plant_fertilize]) is not None:
            utils.execute_until_invalid_state(15, 1, plant_harvest_state, seeds[0])
            utils.execute_until_valid_state_with_timeout(10, 1, moveup_farm_state, [img.home_farm_harvest, img.home_farm_plant])
            utils.execute_until_invalid_state(15, 1, plant_harvest_state, seeds[1])


def pick_plant(items):
    if all(value == 0 for value in items.values()):
        selected_items = random.sample(list(items.keys()), 2)
    else:
        sorted_items = sorted(items, key=items.get)
        selected_items = sorted_items[:2]
    return selected_items


def animal_farm_state():
    home_management_selection(img.home_management_center_corral)
    if utils.wait_for_image(img.home_guide_quest, timeout=5) is not None:
        if utils.wait_for_image(img.home_corral_chicken_active, timeout=2) is not None:
            # collect egg
            utils.execute_until_invalid_state(20, 1, collect_feed_animal_template, img.home_corral_egg, img.home_corral_harvest)
            utils.scroll_down_until_found(img.home_corral_lock_icon, img.home_corral_chicken_icon, timeout=3, offset_y=50)
            utils.execute_until_invalid_state(20, 1, collect_feed_animal_template, img.home_corral_egg, img.home_corral_harvest)
            # feed chicken
            scroll_up(img.home_corral_chicken_icon)
            utils.execute_until_invalid_state(20, 1, collect_feed_animal_template, img.home_corral_feed_corral, img.home_corral_feed_button)
            utils.scroll_down_until_found(img.home_corral_lock_icon, img.home_corral_chicken_icon, timeout=3, offset_y=50)
            utils.execute_until_invalid_state(20, 1, collect_feed_animal_template, img.home_corral_feed_corral, img.home_corral_feed_button)
            scroll_up(img.home_corral_chicken_icon)
        
        utils.tap_offset_until_found(img.home_corral_chicken_active, img.home_corral_cow_active, offset_y=150)
        if utils.wait_for_image(img.home_corral_cow_active, timeout=2) is not None:
            # collect cow milk
            utils.execute_until_invalid_state(10, 1, collect_feed_animal_template, img.home_corral_milk_bottle, img.home_corral_harvest)
            # feed cow
            utils.execute_until_invalid_state(10, 1, collect_feed_animal_template, img.home_corral_feed_corral, img.home_corral_feed_button)

        utils.tap_offset_until_found(img.home_corral_cow_active, img.home_corral_sheep_active, offset_y=150)
        if utils.wait_for_image(img.home_corral_sheep_active, timeout=2) is not None:
            # collect sheep
            utils.execute_until_invalid_state(10, 1, collect_feed_animal_template, img.home_corral_wool, img.home_corral_harvest)
            # feed cow
            utils.execute_until_invalid_state(10, 1, collect_feed_animal_template, img.home_corral_feed_corral, img.home_corral_feed_button)


def scroll_up(drag_icon):
    for _ in range(0, 3):
        utils.drag_down(drag_icon)


def home_management_selection(home_management_center_mode_icon):
    utils.tap_offset_until_found(img.home_guide_quest, img.home_management_center_page, offset_x=-100, offset_y=0)
    utils.tap_until_found(home_management_center_mode_icon, img.button_go_blue_small2)
    utils.tap_until_notfound(img.button_go_blue_small2, img.button_go_blue_small2)


def collect_feed_animal_template(closed_to_animal_icon, action_icon):
    if utils.is_found(img.home_corral_collapsed_menu):
        utils.tap_until_notfound(img.home_corral_collapsed_menu, img.home_corral_collapsed_menu)
    if utils.wait_for_image(closed_to_animal_icon, timeout=2) is None:
        return False

    utils.tap_image_offset(closed_to_animal_icon, offset_x=-80)
    utils.tap_if_found(action_icon)
    return True


def movedown_midtown_state():
    if utils.wait_any_image(const.guilds, timeout=2) is not None:
        return True
    func.move_down()
    return False


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
        plant_cache[seed] += plant_point[seed]
        with open("plant.json", "w") as file:
            json.dump(plant_cache, file)
        print(f"plant point: {plant_cache}")

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
        if utils.wait_for_image(img.home_guide_quest, timeout=60) is not None:
            return True
    return False


def ensure_party_ui():
    if not utils.is_found(img.icon_speaker):
        utils.tap_offset_until_found(img.home_farm_plant_home_icon, img.icon_speaker, offset_x=0, offset_y=200)