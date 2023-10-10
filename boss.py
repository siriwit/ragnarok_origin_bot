import constanst as const
import img
import func
import preset
import re
import sys
import time
import utils

boss_remaining_time_dict = {}

def boss_hunt_loop(is_active=True, min_level=0, max_level=999, ignore_spawn=True):
    if func.go_to_event(img.event_boss):
        utils.wait_and_tap(img.boss_title_mvp)
        if is_active:
            count5x5 = utils.count_image_on_screen(img.event_boss_5x5)
            print('found 5x5: ' + str(count5x5))
            if min_level == 0 and count5x5 >= 2:
                close_boss_page()
                # func.wait_profile()
                # func.send_message('Finished 5/5 TR [z1][z1]')
                sys.exit(0)
            elif min_level > 0 and count5x5 >= 1:
                close_boss_page()
                sys.exit(0)

        else:
            utils.scroll_down_util_found(img.event_drag_icon_inactive, img.event_drag_icon, offset_y=300)
            utils.scroll_down_util_found(img.event_boss_inactive, img.event_drag_icon_inactive, offset_y=300)
            utils.tap_image(img.event_boss_inactive)

        while True:
            print('start boss mode - min: ' + str(min_level) + ' max: ' + str(max_level) + ' ignore_spawn: ' + str(ignore_spawn))
            if boss_monitoring(min_level, max_level, ignore_spawn):
                break
    else:
        utils.tap_if_found(img.button_back)
        sys.exit(0)


def close_boss_page():
    func.close_any_panel()


def boss_hunt_specific():
    boss_image = img.boss_chimera
    threshold = 3*60 
    send_message_to = 'party'

    func.wait_profile()
    if func.go_to_event():
        utils.scroll_down_util_found(img.event_boss, img.event_drag_icon, offset_y=300)
        utils.tap_image(img.event_boss)

        boss_configs = get_boss_config_list()
        filtered_boss_config = filter(lambda config: config['boss_remaining_time_icon'] == boss_image, boss_configs)
        boss_config = list(filtered_boss_config)

        while True:
            utils.tap_if_found(img.boss_event_battery_saving)
            boss_remaining_time = boss_monitoring_with_config(boss_config[0], threshold, False, send_message_to)
            if boss_remaining_time == 0:
                return True
            
            if boss_remaining_time > threshold:
                boss_remaining_time = boss_remaining_time - threshold
            time.sleep(boss_remaining_time)


def boss_config_obj(
        boss_region_icon, boss_remaining_time_icon, 
        boss_map_icon, boss_coming_icon, 
        boss_name, boss_wing_timeout, 
        tribe, element,
        size, level,
        boss_fight_icon=None
        ):
    config = {}
    config['boss_region_icon'] = boss_region_icon
    config['boss_remaining_time_icon'] = boss_remaining_time_icon
    config['boss_map_icon'] = boss_map_icon
    config['boss_coming_icon'] = boss_coming_icon
    config['boss_name'] = boss_name
    config['boss_wing_timeout'] = boss_wing_timeout
    config['tribe'] = tribe
    config['element'] = element
    config['size'] = size
    config['level'] = level
    config['boss_fight_icon'] = boss_fight_icon
    return config


def get_boss_config_list(min_level=0, max_level=999):
    boss_configs = [
        boss_config_obj(
            img.boss_region_angeling, img.boss_angeling, 
            img.boss_map_poring_island, img.boss_coming_angeling, 
            'Angeling', 60, const.angel, const.holy, const.medium,
            35, img.boss_angeling_fight),
        boss_config_obj(
            img.boss_region_golden_thief_bug, img.boss_golden_thief_bug, 
            img.boss_map_culvert_2f, img.boss_coming_golden_thief_bug, 
            'Golden Thief Bug', 60, const.insect, const.fire, const.large,
            45),
        boss_config_obj(
            img.boss_region_deviling, img.boss_deviling, 
            img.boss_map_poring_island, img.boss_coming_deviling, 
            'Deviling', 60, const.demon, const.shadow, const.medium,
            48, img.boss_deviling_fight),
        boss_config_obj(
            img.boss_region_orc_hero, img.boss_orc_hero, 
            img.boss_map_orc_village, img.boss_coming_orc_hero, 
            'Orc Hero', 120, const.demi_human, const.earth, const.large,
            55, img.boss_orc_hero_fight),
        boss_config_obj(
            img.boss_region_maya, img.boss_maya, 
            img.boss_map_ant_hell, img.boss_coming_maya, 
            'Maya', 120, const.insect, const.earth, const.large,
            58, img.boss_maya_fight),
        boss_config_obj(
            img.boss_region_orc_lord, img.boss_orc_lord, 
            img.boss_map_orc_village, img.boss_coming_orc_lord, 
            'Orc Lord', 120, const.demi_human, const.earth, const.large,
            60, img.boss_orc_lord_fight),
        boss_config_obj(
            img.boss_region_goblin_chief, img.boss_goblin_chief, 
            img.boss_map_goblin_forest, img.boss_coming_goblin_chief,
            'Goblin Chief', 150, const.demi_human, const.wind, const.medium,
            62, img.boss_goblin_fight),
        boss_config_obj(
            img.boss_region_drake, img.boss_drake, 
            img.boss_map_shipwreck_labyrinth, img.boss_coming_drake, 
            'Drake', 150, const.undead, const.undead, const.medium,
            65, img.boss_drake_fight),
        boss_config_obj(
            img.boss_region_eddga, img.boss_eddga, 
            img.boss_map_deep_payon_forest, img.boss_coming_eddga, 
            'Eddga', 150, const.brute, const.fire, const.large,
            68, img.boss_eddga_fight),
        boss_config_obj(
            img.boss_region_mistress, img.boss_mistress, 
            img.boss_map_garden, img.boss_coming_mistress, 
            'Mistress', 180, const.insect, const.wind, const.small,
            70, img.boss_mistress_fight),
        boss_config_obj(
            img.boss_region_osiris, img.boss_osiris, 
            img.boss_map_pyramid_3f, img.boss_coming_osiris, 
            'Osiris', 150, const.undead, const.undead, const.medium,
            72, img.boss_osiris_fight),
        boss_config_obj(
            img.boss_region_phreeoni, img.boss_phreeoni, 
            img.boss_map_southern_sograt, img.boss_coming_phreeoni, 
            'Phreeoni', 150, const.brute, const.neutral, const.large,
            76, img.boss_phreeoni_fight),
        boss_config_obj(
            img.boss_region_moonlight, img.boss_moonlight, 
            img.boss_map_payon_cave_3f, img.boss_coming_moonlight, 
            'Moonlight', 180, const.demon, const.fire, const.medium,
            79, img.boss_moonlight_fight),
        boss_config_obj(
            img.boss_region_dracula, img.boss_dracula, 
            img.boss_map_geffen_underground_2f, img.boss_coming_dracula, 
            'Dracula', 180, const.demon, const.shadow, const.large,
            80),
        boss_config_obj(
            img.boss_region_doppelganger, img.boss_doppelganger, 
            img.boss_map_geffen_underground_3f, img.boss_coming_doppel, 
            'Doppel', 180, const.demon, const.shadow, const.medium,
            83, img.boss_doppelganger_fight),
        boss_config_obj(
            img.boss_region_pharaoh, img.boss_pharaoh, 
            img.boss_map_sphinx_crypt_level_2, img.boss_coming_pharaoh, 
            'Pharaoh', 180, const.demi_human, const.shadow, const.large,
            86, img.boss_pharaoh_fight),
        boss_config_obj(
            img.boss_region_chimera, img.boss_chimera, 
            img.boss_map_glast_heim, img.boss_coming_pharaoh, 
            'Chimera', 210, const.brute, const.fire, const.large,
            109),
        boss_config_obj(
            img.boss_region_owl_baron, img.boss_owl_baron, 
            img.boss_map_glast_heim_2f, img.boss_coming_pharaoh, 
            'Owl Baron', 210, const.demon, const.neutral, const.large,
            110, img.boss_owl_baron_fight),
        boss_config_obj(
            img.boss_region_bloody_knight, img.boss_bloody_knight, 
            img.boss_map_glast_heim_order_2f, img.boss_coming_pharaoh, 
            'Bloody Knight', 210, const.formless, const.shadow, const.large,
            112),
        boss_config_obj(
            img.boss_region_dark_lord, img.boss_dark_lord, 
            img.boss_map_catacomb, img.boss_coming_pharaoh, 
            'Dark Lord', 210, const.demon, const.undead, const.large,
            113)
    ]
    filtered_boss_config = filter(lambda config: config['level'] >= min_level and config['level'] <= max_level, boss_configs)
    return list(filtered_boss_config)


def boss_monitoring(min_level=0, max_level=999, ignore_spawn=True):
    utils.wait_for_image(img.boss_title_mvp)
    threshold = 3*60
    
    boss_configs = get_boss_config_list(min_level, max_level)
    print('boss count: ' + str(len(boss_configs)))
    for boss_config in boss_configs:
        if boss_monitoring_with_config(boss_config, threshold, ignore_spawn, send_message_to='world') == 0:
            return True
    
    utils.scroll_up_util_found(boss_configs[0]['boss_region_icon'], img.boss_drag_icon, offset_y=300, timeout=120)
    return False


def boss_monitoring_with_config(boss_config, threshold, ignore_spawn, send_message_to='world'):
    utils.scroll_down_util_found(boss_config['boss_region_icon'], img.boss_drag_icon, timeout=120)
    time_left = find_boss_time(boss_config['boss_remaining_time_icon'], boss_config['boss_map_icon'], threshold, ignore_spawn)
    print(time_left)
    if time_left < threshold:
        print('under_threshold')
        wait_boss_coming_icon_disapear(
            boss_config['boss_coming_icon'], boss_config['boss_name'], 
            time_left, boss_config['tribe'], 
            boss_config['element'], boss_config['size'],
            send_message_to)
        boss(boss_config['boss_wing_timeout'], boss_config['boss_fight_icon'])
        return 0
    return time_left


def wait_boss_coming_icon_disapear(boss_coming_icon, boss_name, time_left, boss_tribe, boss_element, boss_size, send_message_to='world'):

    start_time = time.time()
    func.wait_profile()
    time.sleep(2)
    func.send_message(boss_name)

    func.find_boss_party(boss_name, send_message_to)

    if time_left > 30:
        preset.againt_monster_card(boss_tribe, boss_element, boss_size)
        preset.pet_selector(img.pet_icon_sohee)

    diff_time = time.time() - start_time
    time_left = int(time_left-diff_time)

    print('wait boss coming icon appear for ' + str(time_left) + ' sec')
    func.wait_and_find_party(boss_coming_icon, boss_name, send_to=send_message_to, timeout=time_left, is_icon_apprear=True)
    print('wait boss coming icon disappear for ' + str(time_left) + ' sec')
    utils.wait_for_image(boss_coming_icon, timeout=2)
    func.wait_and_find_party(boss_coming_icon, boss_name, send_to=send_message_to, timeout=time_left, is_icon_apprear=False)

def find_boss_time(boss_image, boss_map, threshold, ignore_spawn=False):
    print("Find " + boss_image)

    previous_boss_time = get_boss_cache_remain_time(boss_image)

    result = get_confirm_boss_remain_time(boss_image)
    print('remain: ' + str(result))

    if previous_boss_time > 0 and previous_boss_time != 9999 and (previous_boss_time - result > 240):
        find_remaining_time_util_realistic(previous_boss_time, result, boss_image, ignore_spawn)

    boss_remaining_time_dict[boss_image] = result
    if (not ignore_spawn and result == 0) or (result > 0 and result < threshold):
    # if True:
        utils.tap_image(boss_image)
        utils.tap_until_notfound(img.boss_button_go, img.boss_button_go)
        marked_time = time.time()
        while True:
            utils.wait_for_image(img.loading, timeout=120)
            utils.wait_until_disappear(img.loading)
            if utils.is_found(boss_map):
                break
        diff_time = time.time() - marked_time
        boss_remaining_time_dict.clear()
        return result - diff_time
    print("")

    if ignore_spawn and result == 0:
        result = 9999

    return result


def get_confirm_boss_remain_time(boss_image):
    result1 = boss_remaining_time(boss_image)
    result2 = boss_remaining_time(boss_image)
    diff = result2 - result1
    if diff > 5:
        get_confirm_boss_remain_time(boss_image)
    return result2


def get_boss_cache_remain_time(boss_image):
    if not boss_remaining_time_dict and boss_image in boss_remaining_time_dict:
        previous_boss_time = boss_remaining_time_dict[boss_image]
        print('previous_boss_time: ' + str(previous_boss_time))
        return previous_boss_time
    return 0


def boss_remaining_time(image_filename):
    text = utils.get_text_from_image(image_filename)

    if not isinstance(text, str):
        boss_remaining_time(image_filename)

    pattern = r"([\d]{2})[:-]([\d]{2})"
    match_result = re.search(pattern, text)
    if 'Spawn' in text:
        print('Spawned')
        return 0
    elif match_result:
        print(match_result.group(0))
        minute_str = match_result.group(1)
        second_str = match_result.group(2)
        minute = int(minute_str)
        second = int(second_str)
        result = ((minute*60)+second)
        return result
    else:
        return boss_remaining_time(image_filename)


def find_remaining_time_util_realistic(previous_boss_time, current_boss_time, boss_image, ignore_spawn):
    while previous_boss_time > 0 and (previous_boss_time - current_boss_time > 120):
        current_boss_time = boss_remaining_time(boss_image, ignore_spawn)
        print("re-evaluate boss remaining time:" + str(current_boss_time))
        time.sleep(1)


def boss_wing(timeout=120):
    marked_time = time.time()
    diff_time = 0
    while True:
        if diff_time > timeout:
            return False

        utils.tap_offset_until_found(img.menu_bag, img.auto_attack_title, interval=0.3, offset_x=85)
        if utils.is_found(img.icon_auto_attack_boss):
            utils.wait_and_tap(img.icon_auto_attack_boss)
            utils.tap_image(img.button_auto_attack_close)
            func.send_location()
            return True
        else:
            utils.tap_image(img.button_auto_attack_close)
        utils.tap_image_offset(img.menu_bag, offset_y=100)
        utils.tap_image_offset(img.menu_bag, offset_y=100)
        diff_time = time.time() - marked_time

def boss(timeout=120, boss_fight_icon=None):
    func.wait_profile()
    if boss_wing(timeout):
        boss_fight(boss_fight_icon=boss_fight_icon)
    else:
        utils.wait_and_tap(img.button_auto_attack_close, timeout=2)
        func.butterfly_wing_morroc()

def map_wing():
    while True:
        if utils.is_found(img.icon_boss) or utils.is_found(img.icon_boss_left) or utils.is_found(img.icon_boss_right) or utils.is_found(img.icon_boss_top) or utils.is_found(img.icon_boss_bottom):
            utils.tap_image(img.icon_boss)
            utils.tap_image(img.icon_boss_left)
            utils.tap_image(img.icon_boss_right)
            utils.tap_image(img.icon_boss_top)
            utils.tap_image(img.icon_boss_bottom)
            time.sleep(2)
            utils.tap_image(img.button_map_close)
            func.auto_attack()
            break
        utils.tap_image(img.wing)
        time.sleep(0.5)


def boss_fight(butterflywing=True, boss_fight_icon=None, timeout=60):
    boss_fight_icon_count = 0
    marked_time = time.time()
    while True:
        if utils.is_found(img.die_upgrade_title):
            handle_die_loop()

        utils.tap_if_found(img.sig_ancient_power)

        utils.tap_if_found(img.boss_fightend_battery_saving)
        func.ang_pao()
        func.use_items()

        if utils.is_found(img.button_battle_log):
            utils.tap_image_offset(img.button_battle_log, offset_y=100)
            utils.tap_offset_until_notfound(img.button_battle_log, img.button_battle_log, offset_y=100)
            func.use_items()
            if butterflywing:
                func.butterfly_wing_morroc()
            return
        
        if boss_fight_icon != None:
            if utils.is_found(boss_fight_icon):
                boss_fight_icon_count += 1
            if boss_fight_icon_count < 3 and time.time() - marked_time > timeout:
                if butterflywing:
                    func.butterfly_wing_morroc()
                return
        time.sleep(1)


def handle_die_loop():
    while True:
        utils.tap_if_found(img.boss_fightend_battery_saving)
        if utils.is_found(img.button_battle_log):
            break
        if not utils.is_found(img.die_upgrade_title):
            func.auto_attack(mode=const.boss)
            break
        time.sleep(1)

