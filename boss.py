import constanst as const
import configparser
import img
import func
import preset
import re
import time
import utils

config = configparser.ConfigParser()
config_file_path = 'bot.ini'
config.read(config_file_path)
settings = config['SETTINGS']

boss_remaining_time_dict = {}

def boss_hunt_loop(is_active=True, min_level=0, max_level=999, ignore_spawn=True, party_mode=True):
    if func.go_to_event(img.event_boss):
        utils.wait_and_tap(img.boss_title_mvp)
        if is_active:
            count5x5 = utils.count_image_on_screen(img.event_boss_5x5)
            print('found 5x5: ' + str(count5x5))
            if not party_mode and count5x5 >= 1:
                close_boss_page()
                return True
            elif min_level == 0 and count5x5 >= 2:
                close_boss_page()
                func.wait_profile()
                func.send_message('Finished 5/5 TR [z1][z1]')
                return True
            elif min_level > 0 and count5x5 >= 1:
                close_boss_page()
                return True

        else:
            utils.scroll_down_util_found(img.event_drag_icon_inactive, img.event_drag_icon, offset_y=300)
            utils.scroll_down_util_found(img.event_boss_inactive, img.event_drag_icon_inactive, offset_y=300)
            utils.tap_image(img.event_boss_inactive)

        while True:
            print('start boss mode - min: ' + str(min_level) + ' max: ' + str(max_level) + ' ignore_spawn: ' + str(ignore_spawn))
            if boss_monitoring(min_level, max_level, ignore_spawn, party_mode):
                break
    else:
        utils.tap_if_found(img.button_back)
        utils.tap_any(const.button_closes)
    
    return False


def boss_follower():
    boss_configs = get_boss_config_list(0, 999)
    boss_status_path = settings['boss_status_path']
    while True:
        if utils.is_found(img.die_upgrade_title):
            handle_die_loop()

        utils.tap_if_found(img.boss_fightend_battery_saving)
        func.ang_pao()
        func.use_items()
        func.handle_battle_log()
        
        utils.tap_if_found(img.button_join)
        utils.tap_if_found(img.button_agree_small_blue)
        utils.tap_if_found(img.button_clear)

        if utils.is_found(img.chat_party_icon):
            boss_status = utils.read_file(boss_status_path, 'boss_status')
            print(boss_status)
            filtered_boss_config = filter(lambda config: config['boss_name'] == boss_status, boss_configs)
            boss_config = list(filtered_boss_config)
            print(boss_config)
            if len(boss_config) > 0:
                boss_fight_icon = boss_config[0]['boss_fight_icon']
                if boss_fight_icon is not None and utils.is_found(boss_fight_icon):
                    continue

                coord_imgs = boss_config[0]['coord_imgs']
                if coord_imgs is not None:
                    follow_coord(boss_config[0]['coord_imgs'], 30, 0.85, leader_mode=False)

        time.sleep(1)


def close_boss_page():
    func.close_any_panel(is_boss_mode=True)


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
        boss_fight_icon=None,
        coord_imgs=None,
        map_distant_offset=0
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
    config['coord_imgs'] = coord_imgs
    config['map_distant_offset'] = map_distant_offset
    return config


def get_boss_config_list(min_level=0, max_level=999):
    boss_wing_base_timeout = int(settings['boss_wing_base_timeout'])
    boss_configs = [
        boss_config_obj(
            img.boss_region_angeling, img.boss_angeling, 
            img.boss_map_poring_island, img.boss_coming_angeling, 
            'Angeling', boss_wing_base_timeout, const.angel, const.holy, const.medium,
            35, img.boss_angeling_fight,
            [img.chat_party_coord_poring_island1, img.chat_party_coord_poring_island2]),
        boss_config_obj(
            img.boss_region_golden_thief_bug, img.boss_golden_thief_bug, 
            img.boss_map_culvert_2f, img.boss_coming_golden_thief_bug, 
            'Golden Thief Bug', boss_wing_base_timeout, const.insect, const.fire, const.large,
            45, img.boss_golden_thief_bug_fight,
            [img.chat_party_coord_culvert_2f1, img.chat_party_coord_culvert_2f2, img.chat_party_coord_culvert_2f3],
            map_distant_offset=40),
        boss_config_obj(
            img.boss_region_deviling, img.boss_deviling, 
            img.boss_map_poring_island, img.boss_coming_deviling, 
            'Deviling', boss_wing_base_timeout, const.demon, const.shadow, const.medium,
            48, img.boss_deviling_fight,
            [img.chat_party_coord_poring_island1, img.chat_party_coord_poring_island2]),
        boss_config_obj(
            img.boss_region_orc_hero, img.boss_orc_hero, 
            img.boss_map_orc_village, img.boss_coming_orc_hero, 
            'Orc Hero', boss_wing_base_timeout+5, const.demi_human, const.earth, const.large,
            55, img.boss_orc_hero_fight, 
            [img.chat_party_coord_orc_village1, img.chat_party_coord_orc_village2, img.chat_party_coord_orc_village3]),
        boss_config_obj(
            img.boss_region_maya, img.boss_maya, 
            img.boss_map_ant_hell, img.boss_coming_maya, 
            'Maya', boss_wing_base_timeout+5, const.insect, const.earth, const.large,
            58, img.boss_maya_fight,
            [img.chat_party_coord_ant_hell1, img.chat_party_coord_ant_hell2, img.chat_party_coord_ant_hell3],
            map_distant_offset=40),
        boss_config_obj(
            img.boss_region_orc_lord, img.boss_orc_lord, 
            img.boss_map_orc_village, img.boss_coming_orc_lord, 
            'Orc Lord', boss_wing_base_timeout+10, const.demi_human, const.earth, const.large,
            60, img.boss_orc_lord_fight,
            [img.chat_party_coord_orc_village1, img.chat_party_coord_orc_village2, img.chat_party_coord_orc_village3]),
        boss_config_obj(
            img.boss_region_goblin_chief, img.boss_goblin_chief, 
            img.boss_map_goblin_forest, img.boss_coming_goblin_chief,
            'Goblin Chief', boss_wing_base_timeout+20, const.demi_human, const.wind, const.medium,
            62, img.boss_goblin_fight,
            [img.chat_party_coord_goblin_forest1, img.chat_party_coord_goblin_forest2, img.chat_party_coord_goblin_forest3]),
        boss_config_obj(
            img.boss_region_drake, img.boss_drake, 
            img.boss_map_shipwreck_labyrinth, img.boss_coming_drake, 
            'Drake', boss_wing_base_timeout+20, const.undead, const.undead, const.medium,
            65, img.boss_drake_fight,
            [img.chat_party_coord_shipwreck_labyrinth1, img.chat_party_coord_shipwreck_labyrinth2, img.chat_party_coord_shipwreck_labyrinth3],
            map_distant_offset=40),
        boss_config_obj(
            img.boss_region_eddga, img.boss_eddga, 
            img.boss_map_deep_payon_forest, img.boss_coming_eddga, 
            'Eddga', boss_wing_base_timeout+20, const.brute, const.fire, const.large,
            68, img.boss_eddga_fight,
            [img.chat_party_coord_deep_payon_forest1, img.chat_party_coord_deep_payon_forest2, img.chat_party_coord_deep_payon_forest3]),
        boss_config_obj(
            img.boss_region_mistress, img.boss_mistress, 
            img.boss_map_garden, img.boss_coming_mistress, 
            'Mistress', boss_wing_base_timeout+20, const.insect, const.wind, const.small,
            70, img.boss_mistress_fight,
            [img.chat_party_coord_garden1, img.chat_party_coord_garden2, img.chat_party_coord_garden3]),
        boss_config_obj(
            img.boss_region_osiris, img.boss_osiris, 
            img.boss_map_pyramid_3f, img.boss_coming_osiris, 
            'Osiris', boss_wing_base_timeout+20, const.undead, const.undead, const.medium,
            72, img.boss_osiris_fight,
            [img.chat_party_coord_pyramid_3f1, img.chat_party_coord_pyramid_3f2, img.chat_party_coord_pyramid_3f3],
            map_distant_offset=80),
        boss_config_obj(
            img.boss_region_phreeoni, img.boss_phreeoni, 
            img.boss_map_southern_sograt, img.boss_coming_phreeoni, 
            'Phreeoni', boss_wing_base_timeout+20, const.brute, const.neutral, const.large,
            76, img.boss_phreeoni_fight,
            [img.chat_party_coord_southern_sograt1, img.chat_party_coord_southern_sograt2, img.chat_party_coord_southern_sograt3]),
        boss_config_obj(
            img.boss_region_moonlight, img.boss_moonlight, 
            img.boss_map_payon_cave_3f, img.boss_coming_moonlight, 
            'Moonlight', boss_wing_base_timeout+20, const.demon, const.fire, const.medium,
            79, img.boss_moonlight_fight,
            [img.chat_party_coord_payon_cave_3f1, img.chat_party_coord_payon_cave_3f2, img.chat_party_coord_payon_cave_3f3],
            map_distant_offset=120),
        boss_config_obj(
            img.boss_region_dracula, img.boss_dracula, 
            img.boss_map_geffen_underground_2f, img.boss_coming_dracula, 
            'Dracula', boss_wing_base_timeout+60, const.demon, const.shadow, const.large,
            80, None,
            [img.chat_party_coord_geffen_underground1, img.chat_party_coord_geffen_underground2, img.chat_party_coord_geffen_underground3],
            map_distant_offset=60),
        boss_config_obj(
            img.boss_region_doppelganger, img.boss_doppelganger, 
            img.boss_map_geffen_underground_3f, img.boss_coming_doppel, 
            'Doppel', boss_wing_base_timeout+60, const.demon, const.shadow, const.medium,
            83, img.boss_doppelganger_fight,
            [img.chat_party_coord_geffen_underground1, img.chat_party_coord_geffen_underground2, img.chat_party_coord_geffen_underground3],
            map_distant_offset=80),
        boss_config_obj(
            img.boss_region_pharaoh, img.boss_pharaoh, 
            img.boss_map_sphinx_crypt_level_2, img.boss_coming_pharaoh, 
            'Pharaoh', boss_wing_base_timeout+90, const.demi_human, const.shadow, const.large,
            86, img.boss_pharaoh_fight,
            [img.chat_party_coord_sphinx_crypt_level_2_1, img.chat_party_coord_sphinx_crypt_level_2_2, img.chat_party_coord_sphinx_crypt_level_2_3],
            map_distant_offset=80),
        boss_config_obj(
            img.boss_region_chimera, img.boss_chimera, 
            img.boss_map_glast_heim, img.boss_coming_chimera, 
            'Chimera', boss_wing_base_timeout+150, const.brute, const.fire, const.large,
            109, img.boss_chimera_fight,
            [img.chat_party_coord_glast_heim1, img.chat_party_coord_glast_heim2, img.chat_party_coord_glast_heim3]),
        boss_config_obj(
            img.boss_region_owl_baron, img.boss_owl_baron, 
            img.boss_map_glast_heim_2f, img.boss_coming_owl_baron, 
            'Owl Baron', boss_wing_base_timeout+180, const.demon, const.neutral, const.large,
            110, img.boss_owl_baron_fight,
            [img.chat_party_coord_glast_heim_castle_2f_1, img.chat_party_coord_glast_heim_castle_2f_2],
            map_distant_offset=60),
        boss_config_obj(
            img.boss_region_bloody_knight, img.boss_bloody_knight, 
            img.boss_map_glast_heim_order_2f, img.boss_coming_bloody_knight, 
            'Bloody Knight', boss_wing_base_timeout+240, const.formless, const.shadow, const.large,
            112, img.boss_bloody_knight_fight,
            [img.chat_party_coord_glast_heim_order_2f_1, img.chat_party_coord_glast_heim_order_2f_2],
            map_distant_offset=80),
        boss_config_obj(
            img.boss_region_dark_lord, img.boss_dark_lord, 
            img.boss_map_catacomb, img.boss_coming_dark_lord, 
            'Dark Lord', boss_wing_base_timeout+240, const.demon, const.undead, const.large,
            113, img.boss_dark_lord_fight,
            [img.chat_party_coord_catacomb1, img.chat_party_coord_catacomb2],
            map_distant_offset=100),
        boss_config_obj(
            img.boss_region_garm, img.boss_garm, 
            img.boss_map_lutie_field, img.boss_coming_garm, 
            'Garm', boss_wing_base_timeout+240, const.brute, const.water, const.large,
            114, img.boss_garm_fight,
            [img.chat_party_coord_lutie_field1, img.chat_party_coord_lutie_field2, img.chat_party_coord_lutie_field3]),
        boss_config_obj(
            img.boss_region_windstorm_knight, img.boss_windstorm_knight, 
            img.boss_map_toy_factory_2f, img.boss_coming_stormy_knight, 
            'Windstorm Knight', boss_wing_base_timeout+240, const.formless, const.wind, const.large,
            116, img.boss_windstorm_knight_fight,
            [img.chat_party_coord_toy_factory_2f_1, img.chat_party_coord_toy_factory_2f_2]),
        boss_config_obj(
            img.boss_region_time_manager, img.boss_time_manager, 
            img.boss_map_clock_tower_basement_2f, img.boss_coming_time_manager, 
            'Time Manager', boss_wing_base_timeout+240, const.demon, const.neutral, const.large,
            116, img.boss_time_manager_fight,
            [img.chat_party_coord_tower_basement_2f_1, img.chat_party_coord_tower_basement_2f_2, img.chat_party_coord_clock_tower_basement_2f_3]),
        boss_config_obj(
            img.boss_region_tao_gunka, img.boss_tao_gunka, 
            img.boss_map_northern_cave_ruande, img.boss_coming_tao_gunka, 
            'Tao Gunka', boss_wing_base_timeout+270, const.demon, const.earth, const.large,
            120, img.boss_tao_gunka_fight,
            [img.chat_party_coord_northern_cave_ruande1, img.chat_party_coord_northern_cave_ruande2, img.chat_party_coord_northern_cave_ruande3]),
        boss_config_obj(
            img.boss_region_mutant_dragon, img.boss_mutant_dragon, 
            img.boss_map_papuchicha_forest, img.boss_coming_mutant_dragon, 
            'Mutant Dragon', boss_wing_base_timeout+270, const.dragon, const.fire, const.large,
            122, img.boss_mutant_dragon_fight,
            [img.chat_party_coord_papuchicha_forest1, img.chat_party_coord_papuchicha_forest2])
    ]
    filtered_boss_config = filter(lambda config: config['level'] >= min_level and config['level'] <= max_level, boss_configs)
    return list(filtered_boss_config)


def boss_monitoring(min_level=0, max_level=999, ignore_spawn=True, party_mode=True):
    utils.write_to_file('boss_status', 'finding boss')
    utils.wait_and_tap(img.boss_title_mvp)
    threshold = int(settings['boss_run_threshold'])
    
    boss_configs = get_boss_config_list(min_level, max_level)
    print('boss count: ' + str(len(boss_configs)))
    for boss_config in boss_configs:
        if boss_monitoring_with_config(boss_config, threshold, ignore_spawn, send_message_to='world', party_mode=party_mode) == 0:
            return True
    
    utils.scroll_up_util_found(boss_configs[0]['boss_region_icon'], img.boss_drag_icon, offset_y=200, timeout=120)
    return False


def boss_monitoring_with_config(boss_config, threshold, ignore_spawn, send_message_to='world', party_mode=True):
    utils.scroll_down_util_found(boss_config['boss_region_icon'], img.boss_drag_icon, timeout=120)
    time_left = find_boss_time(
        boss_config['boss_remaining_time_icon'], boss_config['boss_region_icon'], 
        boss_config['boss_map_icon'], threshold, 
        boss_config['map_distant_offset'], ignore_spawn)
    
    if time_left < (threshold + boss_config['map_distant_offset']):
        print('under_threshold')
        wait_boss_coming_icon_disapear(
            boss_config['boss_coming_icon'], boss_config['boss_name'], 
            time_left, boss_config['tribe'], 
            boss_config['element'], boss_config['size'],
            boss_config['level'],
            send_message_to, party_mode)
        boss(boss_type='mvp', timeout=boss_config['boss_wing_timeout'], boss_fight_icon=boss_config['boss_fight_icon'], boss_coord_img=boss_config['coord_imgs'])
        return 0
    return time_left


def wait_boss_coming_icon_disapear(boss_coming_icon, boss_name, 
                                   time_left, boss_tribe, boss_element, 
                                   boss_size, boss_level, send_message_to='world', 
                                   party_mode=True):
    utils.write_to_file('boss_status', boss_name)
    start_time = time.time()
    func.wait_profile()
    time.sleep(2)
    if party_mode:
        func.send_message(boss_name)
        func.find_boss_party(boss_name, send_message_to)

    if time_left > 60:
        if settings["preset"] == 'jj_royal_guard':
            preset.againt_monster_card(boss_tribe, boss_element, boss_size, boss_level)
            preset.pet_selector(img.pet_icon_genesis)
            func.element_convert(boss_element)
        elif settings["preset"] == 'jj_rune_knight':
            preset.againt_monster_card(boss_tribe, boss_element, boss_size, boss_level)
            preset.pet_selector(img.pet_icon_sohee)

    diff_time = time.time() - start_time
    time_left = int(time_left-diff_time)

    print('wait boss coming icon appear for ' + str(time_left) + ' sec')
    func.wait_and_find_party(boss_coming_icon, boss_name, send_to=send_message_to, timeout=time_left, is_icon_apprear=True, party_mode=party_mode)
    print('wait boss coming icon disappear for ' + str(time_left) + ' sec')
    utils.wait_for_image(boss_coming_icon, timeout=2)
    func.wait_and_find_party(boss_coming_icon, boss_name, send_to=send_message_to, timeout=time_left, is_icon_apprear=False, party_mode=party_mode)

def find_boss_time(boss_image, boss_region_icon, boss_map, threshold, map_distant_offset, ignore_spawn=False):
    print("Find " + boss_image)

    previous_boss_time = get_boss_cache_remain_time(boss_image)

    result = get_confirm_boss_remain_time(boss_image, boss_region_icon)
    print('remain: ' + str(result))

    if previous_boss_time > 0 and previous_boss_time != 9999 and (previous_boss_time - result > 240):
        find_remaining_time_util_realistic(previous_boss_time, result, boss_image, ignore_spawn)

    boss_remaining_time_dict[boss_image] = result

    print(f"time left: {result}")
    print(f"ignore spawn: {ignore_spawn}")
    print(f"map_distant_offset: {map_distant_offset}")
    condition1 = not ignore_spawn and result == 0
    condition2 = (result < (threshold + map_distant_offset) and result > map_distant_offset)
    print(f"con1: {condition1}")
    print(f"con2: {condition2}")
    if (condition1) or (condition2):
    # if (not ignore_spawn and result == 0) or (result > 0 and result < threshold):
    # if True:
        utils.tap_image(boss_image)
        utils.tap_until_notfound(img.boss_button_go, img.boss_button_go)
        marked_time = time.time()
        if not utils.execute_until_valid_state_with_timeout(150, 1, running_to_boss_map_state, boss_map):
            func.butterfly_wing_morroc()
            func.go_to_event(img.event_boss)
            utils.wait_and_tap(img.boss_title_mvp)
            return 9999
        diff_time = time.time() - marked_time
        boss_remaining_time_dict.clear()
        return result - diff_time
    print("")

    return 9999


def running_to_boss_map_state(boss_map):
    utils.wait_for_image(img.loading, timeout=5)
    utils.wait_until_disappear(img.loading)
    if utils.is_found(boss_map):
        return True
    func.open_map()
    if utils.is_found(boss_map):
        func.close_map()
        return True
    func.close_map()
    return False

def get_confirm_boss_remain_time(boss_image, boss_region_icon):
    result1 = boss_remaining_time(boss_image, boss_region_icon)
    result2 = boss_remaining_time(boss_image, boss_region_icon)
    diff = result2 - result1
    if diff > 5:
        get_confirm_boss_remain_time(boss_image, boss_region_icon)
    return result2


def get_boss_cache_remain_time(boss_image):
    if not boss_remaining_time_dict and boss_image in boss_remaining_time_dict:
        previous_boss_time = boss_remaining_time_dict[boss_image]
        print('previous_boss_time: ' + str(previous_boss_time))
        return previous_boss_time
    return 0


def boss_remaining_time(image_filename, boss_region_icon, count=0):
    text = utils.get_text_from_image(image_filename)

    if count > 10 and utils.is_found(img.boss_drag_icon):
        utils.drag_up(img.boss_drag_icon)
        count = 0
            
    try:
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
            count += 1
            return boss_remaining_time(image_filename, boss_region_icon, count)
    except Exception as e:
        print("An error occurred:", e)
        print(text)
        utils.tap_if_found(img.button_mvp_team_close)
        utils.tap_if_found(img.button_mvp_victory_close)
        utils.tap_if_found(img.button_clear)
        if utils.is_found(img.boss_drag_icon):
            if boss_region_icon == img.boss_region_angeling:
                utils.scroll_up_util_found(boss_region_icon, img.boss_drag_icon, timeout=2)
            else:
                utils.scroll_down_util_found(boss_region_icon, img.boss_drag_icon, timeout=2)
        count += 1
        return boss_remaining_time(image_filename, boss_region_icon, count)


def find_remaining_time_util_realistic(previous_boss_time, current_boss_time, boss_image, ignore_spawn):
    while previous_boss_time > 0 and (previous_boss_time - current_boss_time > 120):
        current_boss_time = boss_remaining_time(boss_image, ignore_spawn)
        print("re-evaluate boss remaining time:" + str(current_boss_time))
        time.sleep(1)


def boss_wing(boss_type='mvp', timeout=120, coord_imgs=None):
    marked_time = time.time()
    diff_time = 0
    similarity = 0.90
    wing_count = 0
    while True:
        print(f"Wing boss: {int(diff_time)}/{timeout}")
        if diff_time > timeout:
            return False

        if check_boss_icon(boss_type):
            return True

        # map boss icon
        if utils.is_found_any(const.small_map_boss_icons):
            func.open_map()
            utils.tap_any(const.boss_icons)
            func.close_map()
            if utils.execute_until_valid_state_with_timeout(30, 1, check_boss_icon, boss_type, 5):
                return True

        # someone ping coordinate
        if wing_count >= 5 and coord_imgs is not None and utils.is_found(img.chat_party_icon):
            if follow_coord(coord_imgs, (timeout-diff_time), similarity):
                return True
            
        # wing
        utils.tap_any_offset(const.menu_bags, offset_y=100, similarity=similarity)
        utils.tap_any_offset(const.menu_bags, offset_y=100, similarity=similarity)
        diff_time = time.time() - marked_time
        wing_count += 1


def check_boss_icon(boss_type='mvp', delay=0, similarity=0.9):
    func.wait(delay)
    utils.tap_offset_until_found(img.menu_bag, img.auto_attack_title, interval=0.3, offset_x=85, similarity=similarity)

    if boss_type == 'mvp':
        return auto_attack()
    elif boss_type == 'mini':
        return auto_attack(img.icon_auto_attack_mini)


def auto_attack(target=img.icon_auto_attack_boss, should_send_location=True):
    if utils.is_found(target):
        utils.wait_and_tap(target)
        utils.tap_until_notfound(img.button_auto_attack_close, img.button_auto_attack_close)
        if should_send_location:
            func.send_location()
        return True
    else:
        utils.tap_image(img.button_auto_attack_close)
    return False


def follow_coord(coord_imgs, remaining_time, similarity, leader_mode=True):
    marked_time_main = time.time()
    while time.time() - marked_time_main < remaining_time:
        func.open_chat()
        img_coord = utils.find_most_bottom_coordinate(coord_imgs)
        print(img_coord)
        if len(img_coord) == 0:
            break
        utils.tap_location(img_coord)
        func.close_chat()

        if leader_mode:
            utils.tap_offset_until_found(img.menu_bag, img.auto_attack_title, interval=0.3, offset_x=85, similarity=similarity)
            marked_time = time.time()
            while time.time() - marked_time < 5:
                if auto_attack(should_send_location=False):
                    return True
        else:
            return True
    utils.tap_image(img.button_auto_attack_close)
    func.close_any_panel(is_boss_mode=True)
    return False


def boss(boss_type='mvp', fight_timeout=120, timeout=120, boss_fight_icon=None, boss_coord_img=None):
    func.wait_profile()
    if boss_wing(boss_type, timeout, boss_coord_img):
        boss_fight(boss_fight_icon=boss_fight_icon, fight_timeout=fight_timeout, timeout=timeout)
    else:
        utils.wait_and_tap(img.button_auto_attack_close, timeout=2)
        func.butterfly_wing_morroc()


def boss_fight(butterflywing=True, boss_fight_icon=None, fight_timeout=60, timeout=60):
    boss_fight_icon_count = 0
    marked_time = time.time()

    fight_timeout_increase = 20
    utils.save_screenshot()
    while time.time() - marked_time < fight_timeout:
        print(f"boss fight timeout: {int(time.time() - marked_time)}/{fight_timeout}")
        if utils.is_found(img.die_upgrade_title):
            fight_timeout += fight_timeout_increase
            utils.execute_until_valid_state_with_timeout(600, 1, handle_die_loop)
        
        func.ang_pao()
        func.use_items()
        utils.tap_if_found(img.button_back)

        if func.handle_battle_log(butterflywing):
            return
        
        if func.use_manual_skill() == 0:
            func.close_any_panel(img.royal_guard_skill_over_band, is_boss_mode=True)
        
        if boss_fight_icon != None:
            if utils.is_found(boss_fight_icon) or utils.is_found(img.button_return_to_checkpoint):
                fight_timeout += fight_timeout_increase
                boss_fight_icon_count += 1
            if boss_fight_icon_count < 2 and time.time() - marked_time > timeout:
                if butterflywing:
                    func.butterfly_wing_morroc()
                return
            print(f"boss icon count: {boss_fight_icon_count}")
        
        time.sleep(1)


def handle_die_loop():
    utils.tap_if_found(img.boss_fightend_battery_saving)
    if utils.is_found(img.button_battle_log):
        time.sleep(1)
        return True
    if not utils.is_found(img.die_upgrade_title) and not utils.is_found(img.button_return_to_checkpoint):
        func.wait(2)
        func.auto_attack(mode=const.boss)
        return True
    return False


