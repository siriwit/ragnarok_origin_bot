import constanst as const
import img
import func
import preset
import re
import sys
import time
import utils

boss_remaining_time_dict = {}

def boss_hunt_loop(is_active=True):
    utils.wait_for_image(img.profile)
    if func.go_to_event():
        if is_active:
            if utils.is_found(img.boss_team_rewards_done):
                sys.exit(0)
            utils.scroll_down_util_found(img.event_boss, img.event_drag_icon, offset_y=300)
            utils.tap_image(img.event_boss)
        else:
            utils.scroll_down_util_found(img.event_drag_icon_inactive, img.event_drag_icon, offset_y=300)
            utils.scroll_down_util_found(img.event_boss_inactive, img.event_drag_icon_inactive, offset_y=300)
            utils.tap_image(img.event_boss_inactive)

        while True:
            if boss_monitoring():
                break
        
def boss_config_obj(
        boss_region_icon, boss_remaining_time_icon, 
        boss_map_icon, boss_coming_icon, 
        boss_name, boss_wing_timeout, 
        tribe, element,
        size
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
    return config


def boss_monitoring():
    utils.wait_for_image(img.boss_title_mvp)
    should_ignore_spawn = True
    threshold = 3*60
    boss_configs = [
        boss_config_obj(
            img.boss_region_angeling, img.boss_angeling, 
            img.boss_map_poring_island, img.boss_coming_angeling, 
            'Angeling', 45, const.angel, const.holy, const.medium),
        boss_config_obj(
            img.boss_region_golden_thief_bug, img.boss_golden_thief_bug, 
            img.boss_map_culvert_2f, img.boss_coming_golden_thief_bug, 
            'Golden Thief Bug', 45, const.insect, const.fire, const.large),
        boss_config_obj(
            img.boss_region_deviling, img.boss_deviling, 
            img.boss_map_poring_island, img.boss_coming_deviling, 
            'Deviling', 45, const.demon, const.shadow, const.medium),
        boss_config_obj(
            img.boss_region_orc_hero, img.boss_orc_hero, 
            img.boss_map_orc_village, img.boss_coming_orc_hero, 
            'Orc Hero', 90, const.demi_human, const.earth, const.large),
        boss_config_obj(
            img.boss_region_maya, img.boss_maya, 
            img.boss_map_ant_hell, img.boss_coming_maya, 
            'Maya', 90, const.insect, const.earth, const.large),
        boss_config_obj(
            img.boss_region_orc_lord, img.boss_orc_lord, 
            img.boss_map_orc_village, img.boss_coming_orc_lord, 
            'Orc Lord', 90, const.demi_human, const.earth, const.large),
        boss_config_obj(
            img.boss_region_goblin_chief, img.boss_goblin_chief, 
            img.boss_map_goblin_forest, img.boss_coming_goblin_chief,
            'Goblin Chief', 120, const.demi_human, const.wind, const.medium),
        boss_config_obj(
            img.boss_region_drake, img.boss_drake, 
            img.boss_map_shipwreck_labyrinth, img.boss_coming_drake, 
            'Drake', 120, const.undead, const.undead, const.medium),
        boss_config_obj(
            img.boss_region_eddga, img.boss_eddga, 
            img.boss_map_deep_payon_forest, img.boss_coming_eddga, 
            'Eddga', 120, const.brute, const.fire, const.large),
        boss_config_obj(
            img.boss_region_mistress, img.boss_mistress, 
            img.boss_map_garden, img.boss_coming_mistress, 
            'Mistress', 120, const.insect, const.wind, const.small),
        boss_config_obj(
            img.boss_region_osiris, img.boss_osiris, 
            img.boss_map_pyramid_3f, img.boss_coming_osiris, 
            'Osiris', 120, const.undead, const.undead, const.medium),
        boss_config_obj(
            img.boss_region_phreeoni, img.boss_phreeoni, 
            img.boss_map_southern_sograt, img.boss_coming_phreeoni, 
            'Phreeoni', 120, const.brute, const.neutral, const.large),
        boss_config_obj(
            img.boss_region_moonlight, img.boss_moonlight, 
            img.boss_map_payon_cave_3f, img.boss_coming_moonlight, 
            'Moonlight', 150, const.demon, const.fire, const.medium),
        boss_config_obj(
            img.boss_region_dracula, img.boss_dracula, 
            img.boss_map_geffen_underground_2f, img.boss_coming_dracula, 
            'Dracula', 150, const.demon, const.shadow, const.large),
        boss_config_obj(
            img.boss_region_doppelganger, img.boss_doppelganger, 
            img.boss_map_geffen_underground_3f, img.boss_coming_doppel, 
            'Doppel', 150, const.demon, const.shadow, const.medium),
        boss_config_obj(
            img.boss_region_pharaoh, img.boss_pharaoh, 
            img.boss_map_sphinx_crypt_level_2, img.boss_coming_pharaoh, 
            'Pharaoh', 150, const.demi_human, const.shadow, const.large)
    ]

    for boss_config in boss_configs:
        utils.scroll_down_util_found(boss_config['boss_region_icon'], img.boss_drag_icon)
        time_left = find_boss_time(boss_config['boss_remaining_time_icon'], boss_config['boss_map_icon'], threshold, should_ignore_spawn)
        print(time_left)
        if time_left < threshold:
            print('under_threshold')
            wait_boss_coming_icon_disapear(
                boss_config['boss_coming_icon'], boss_config['boss_name'], 
                time_left, boss_config['tribe'], 
                boss_config['element'], boss_config['size'])
            boss(boss_config['boss_wing_timeout'])
            return True
    utils.scroll_up_util_found(img.boss_angeling, img.boss_drag_icon, 300)
    return False


def wait_boss_coming_icon_disapear(boss_coming_icon, boss_name, time_left, boss_tribe, boss_element, boss_size):
    send_message_to = 'world'
    offset = 5
    change_card_offset = 15

    utils.wait_for_image(img.profile)
    time.sleep(2)
    func.send_message(boss_name)

    time_left = int(time_left-offset)

    func.find_boss_party(boss_name, send_message_to)

    if time_left > 15:
        preset.againt_monster_card(boss_tribe, boss_element, boss_size)
        time_left = int(time_left-change_card_offset)

    if time_left > 100:
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
        utils.tap_image(img.boss_button_go)
        marked_time = time.time()
        utils.wait_for_image(boss_map, timeout=150)
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
        current_boss_time = utils.boss_remaining_time(boss_image, ignore_spawn)
        print("re-evaluate boss remaining time:" + str(current_boss_time))
        time.sleep(1)


def boss_attack(timeout=120):
    utils.tap_image(img.icon_auto_attack)

    marked_time = time.time()
    diff_time = 0
    while True:
        if diff_time > timeout:
            return False

        if utils.is_found(img.icon_auto_attack_boss):
            utils.wait_and_tap(img.icon_auto_attack_boss)
            utils.tap_image(img.button_auto_attack_close)
            func.send_location()
            return True
        utils.key_press('F3')
        time.sleep(1)
        diff_time = time.time() - marked_time

def boss(timeout=120):
    utils.wait_for_image(img.profile)
    if boss_attack(timeout):
        boss_fight()
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


def boss_fight():
    while True:
        if utils.is_found(img.die_upgrade_title):
            utils.wait_until_disappear(img.die_upgrade_title)
            func.auto_attack()

        func.enable_aura()

        utils.tap_if_found(img.boss_battery_saving)

        if utils.is_found(img.button_battle_log):
            utils.tap_image(img.tap_anywhere)
            func.use_items()
            func.butterfly_wing_morroc()
            return
        time.sleep(1)

