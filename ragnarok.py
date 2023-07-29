import pyautogui
import time
import sys
import utils
import constanst as const


def fishing():
    utils.wait_for_image(const.profile)
    ang_pao()
    utils.tap(1000, 300)
    utils.wait_for_image('images/fishing_alert.png')
    utils.tap_image('images/fishing_alert.png')


def ang_pao(pet_image='images/pet_icon_earthlord.png', fast=False):
    utils.wait_for_image(const.profile)
    if fast:
        utils.tap_image('images/ang_pao_red.png', screenshot=True, result_filename='images/angpao_header.png')
        utils.tap_image('images/ang_pao_yellow.png', screenshot=True, result_filename='images/angpao_header.png')
    else:
        utils.tap_image('images/ang_pao_red.png')
        utils.tap_image('images/ang_pao_yellow.png')
    utils.tap_image(pet_image)


def farm():
    utils.wait_for_image(const.profile)
    ang_pao(pet_image=const.pet_earthlord)
    utils.tap_image('images/item_alert.png', screenshot=True, before=True)
    utils.tap_image('images/button_receive.png', screenshot=True, before=True)
    utils.tap_image('images/sig_ancient_power.png')
    enable_aura()
    convert_weapon(element='water')

    fatique = utils.find_image_with_similarity('images/fatique_icon.png')
    if fatique is not None:
        utils.wait_and_tap('images/fatique_close.png')
        butterfly_wing_morroc()
        sys.exit()


def butterfly_wing_morroc():
    utils.wait_and_tap('images/butterfly_wing.png')
    utils.wait_and_tap('images/city_morroc.png')


def forging():
    utils.wait_for_image(const.profile)
    ang_pao()
    utils.tap_image('images/forging.png')


def farm_mr():
    utils.wait_for_image(const.profile)
    ang_pao(const.pet_barfo)
    utils.tap_image('images/normal_attack.png')
    utils.tap_image('images/item_alert.png', screenshot=True, before=True)


def feast():
    utils.wait_for_image(const.profile)
    ang_pao('images/pet_icon_barfo.png', fast=True)
    utils.tap_image('images/food_grab.png')
    utils.wait_for_image('images/food_taste.png', timeout=2)
    utils.tap_image('images/food_taste.png')


def daily_demon_treasure():
    utils.wait_for_image(const.profile)
    utils.tap_image('images/menu_daily.png')
    utils.wait_and_tap('images/daily_demon_treasure.png', timeout=2)
    utils.tap_image('images/button_go.png')
    utils.wait_and_tap('images/daily_demon_treasure_prontera_west.png')
    demon_treasure()


def demon_treasure(firstime=True):
    while True:
        utils.tap_image('images/rescue.png')
        utils.tap_image('images/button_use.png')
        if utils.is_found('images/button_close_purple.png'):
            time.sleep(5)
            utils.tap_image('images/button_close_purple.png')

        if utils.is_found('images/daily_demon_treasure_reach_limit.png'):
            time.sleep(5)
            if firstime:
                demon_treasure(firstime=False)
            else:
                sys.exit()


def daily_cat_paw():
    utils.wait_for_image(const.profile)

    if utils.is_found('images/cat_paw_caravan_icon.png'):
        utils.tap_image('images/cat_paw_caravan_icon.png')
    else:
        utils.tap_image('images/menu_daily.png')
        utils.tap_image('images/daily_catpaw.png')
        utils.tap_image('images/button_go.png')
        utils.wait_and_tap('images/icon_message.png', timeout=60)

    utils.wait_for_image('images/cat_paw_caravan_topbar.png', timeout=2)
    load_cargo()


def load_cargo():
    while True:
        # utils.tap_image('images/cat_paw_caravan_item_box.png')
        # utils.tap_image('images/cat_paw_caravan_load_cargo.png')

        # utils.wait_for_image('images/trading_menu_material.png', timeout=2)
        # if utils.is_found('images/trading_menu_material.png'):
        #     utils.wait_and_tap('images/cat_paw_caravan_item_requirement.png', timeout=2)
        #     utils.wait_and_tap('images/button_buy_trading.png', timeout=2)
        #     utils.wait_and_tap('images/button_buy.png', timeout=2)
        #     utils.tap_image('images/button_close_trading.png')

        # utils.wait_for_image('images/equipment_shop_topbar.png', timeout=2)
        # if utils.is_found('images/equipment_shop_topbar.png'):
        #     utils.wait_and_tap('images/button_buy.png', timeout=2)
        #     utils.tap_image('images/button_close.png')

        # utils.wait_for_image('images/trading_menu_medicine.png', timeout=2)
        # if utils.is_found('images/trading_menu_medicine.png'):
        #     utils.wait_and_tap('images/cat_paw_caravan_item_requirement.png', timeout=2)
        #     utils.wait_and_tap('images/button_buy_trading.png', timeout=2)
        #     utils.wait_and_tap('images/button_buy.png', timeout=2)
        #     utils.tap_image('images/button_close_trading.png')
        
        # utils.wait_and_tap('images/cat_paw_caravan_load_cargo.png', timeout=2)

        utils.tap_image(const.button_quick_departure)
        utils.wait_and_tap(const.button_confirm, timeout=2)
        utils.tap_image('images/cat_paw_caravan_claim_finished.png')

        if utils.is_found('images/button_claimed.png'):
            pyautogui.press('esc')
            sys.exit()
        
        time.sleep(1)


def convert_weapon(element='fire'):
    diff_time = time.time() - convert_weapon_time
    utils.log(diff_time)
    if diff_time > converter_timeout:
        perform_convert_weapon(element)

def perform_convert_weapon(element='water'):
    utils.wait_for_image(const.profile)
    pyautogui.typewrite('b')
    utils.wait_for_image('images/weapon3.png')
    utils.tap_image('images/weapon3.png')
    utils.wait_for_image('images/button_more.png')
    utils.tap_image('images/button_more.png')
    utils.wait_for_image('images/button_element.png')
    utils.tap_image('images/button_element.png')
    utils.wait_for_image('images/button_plus.png')
    utils.tap_image('images/button_plus.png')
        
    if element == 'fire':
        utils.wait_for_image('images/region_fire_slayer_converter.png')
        utils.tap_image_in_region('images/button_select.png', 'images/region_fire_slayer_converter.png')
    elif element == 'wind':
        utils.wait_for_image('images/region_wind_slayer_converter.png')
        utils.tap_image_in_region('images/button_select.png', 'images/region_wind_slayer_converter.png')
    elif element == 'water':
        utils.wait_for_image('images/region_water_1hsword_converter.png')
        utils.tap_image_in_region('images/button_select.png', 'images/region_water_1hsword_converter.png')
    else:
        utils.wait_for_image('images/region_earth_1hsword_converter.png')
        utils.tap_image_in_region('images/button_select.png', 'images/region_earth_1hsword_converter.png')
    utils.wait_for_image('images/button_use.png')
    utils.tap_image('images/button_use.png')
    pyautogui.press('esc')
    pyautogui.press('esc')
    reset_convert_weapon_time()
        

def reset_convert_weapon_time():
    global convert_weapon_time
    convert_weapon_time = time.time()


def dismantle_cogwheel():
    utils.wait_for_image('images/cogwheel_topbar.png')
    utils.tap_image('images/button_quick_select.png')
    utils.wait_for_image('images/cofwheel_dismantle_option.png', timeout=1)
    utils.tap_image('images/button_confirm.png')
    utils.tap_image('images/button_dismantle.png')


def pet_enhance():
    utils.tap_image('images/button_enhance.png')
    utils.tap_image('images/button_confirm.png')
    if utils.find_image_with_similarity('images/max_level_reached.png') is not None:
        sys.exit(0)


def yggdasill():
    utils.wait_for_image(const.profile)
    utils.tap_image('images/next_monster_wave.png')
    ang_pao()

    if utils.is_found(const.victory):
        sys.exit()


def daily_anthem():
    utils.wait_for_image(const.profile)
    utils.wait_for_image(const.menu_daily)
    utils.tap_image(const.menu_daily)
    utils.wait_and_tap('images/daily_anthem.png', timeout=2)
    utils.tap_image(const.button_go)
    utils.wait_and_tap('images/daily_anthem_anthem_trial_option.png', timeout=120)
    utils.tap_image('images/button_use.png')
    utils.wait_and_tap('images/button_submit.png', timeout=1)
    utils.tap_image('images/button_start.png')
    utils.wait_for_image(const.team_confirm, timeout=1)
    if utils.is_found(const.team_confirm):
        utils.wait_until_disappear(const.team_confirm)
    anthem()


def anthem():
    utils.wait_for_image(const.profile)
    utils.tap_image('images/anthem_activate.png')
    utils.wait_for_image('images/anthem_lucky_wheel.png')
    utils.wait_for_image('images/anthem_activate.png')
    anthem_fight()


def anthem_fight():
    utils.wait_for_image(const.profile)
    utils.hold_press('a', timeout=0.5)
    utils.hold_press('w', timeout=3)
    utils.key_press('k')
    utils.tap_image(const.pet_earthlord)
    utils.wait_for_image(const.victory, timeout=150)
    utils.tap_image('images/button_use.png')
    utils.wait_and_tap('images/button_submit.png', timeout=1)
    utils.wait_and_tap('images/daily_anthem_tap_anywhere1.png', timeout=20)
    utils.wait_and_tap('images/daily_selectable_card.png', timeout=20)
    utils.wait_and_tap('images/daily_anthem_tap_anywhere2.png', timeout=20)
    utils.wait_and_tap('images/button_escape.png', timeout=20)
    utils.wait_and_tap('images/button_confirm.png', timeout=20)
    time.sleep(20)
    sys.exit(0)


def boss():
    utils.wait_for_image(const.profile)
    boss_attack()
    boss_fight()


def map_wing():
    while True:
        if utils.is_found(const.icon_boss) or utils.is_found(const.icon_boss_left) or utils.is_found(const.icon_boss_right) or utils.is_found(const.icon_boss_top) or utils.is_found(const.icon_boss_bottom):
            utils.tap_image(const.icon_boss)
            utils.tap_image(const.icon_boss_left)
            utils.tap_image(const.icon_boss_right)
            utils.tap_image(const.icon_boss_top)
            utils.tap_image(const.icon_boss_bottom)
            time.sleep(2)
            utils.tap_image(const.button_map_close)
            auto_attack()
            break
        utils.tap_image(const.wing)
        time.sleep(0.5)


def boss_fight():
    while True:
        if utils.is_found(const.die_upgrade_title):
            utils.wait_until_disappear(const.die_upgrade_title)
            auto_attack()

        enable_aura()

        if utils.is_found(const.button_battle_log):
            utils.tap_image(const.tap_anywhere)
            butterfly_wing_morroc()
            return
        time.sleep(1)


def enable_aura():
    if utils.is_found(const.aura_denfending_neutral):
            utils.key_press("num1")
            utils.key_press("num1")


def boss_attack():
    utils.tap_image(const.icon_auto_attack)

    while True:
        if utils.is_found(const.icon_auto_attack_boss):
            utils.wait_and_tap(const.icon_auto_attack_boss)
            utils.tap_image(const.button_auto_attack_close)
            break
        utils.key_press('F3')
        time.sleep(1)

def auto_attack():
    utils.tap_image(const.icon_auto_attack)
    utils.wait_for_image(const.icon_auto_attack_boss, timeout=1)
    if utils.is_found(const.icon_auto_attack_boss):
        utils.wait_and_tap(const.icon_auto_attack_boss)
    else:
        utils.wait_and_tap(const.auto_attack_allmonster)
    utils.tap_image(const.button_auto_attack_close)


def oracle():
    utils.wait_for_image(const.profile)
    utils.tap_image(const.pet_earthlord)

    if utils.is_found(const.button_agree):
        utils.tap_image(const.button_agree)
        utils.wait_for_image(const.oracle_present, timeout=60)
        send_message('[z1]')
        utils.wait_and_tap(const.button_escape, timeout=20)
        utils.wait_and_tap(const.button_confirm, timeout=20)

def send_message(message, send_to='party'):
    utils.key_press("enter")
    time.sleep(1)
    if send_to == 'party' and utils.is_found(const.chat_tab_party_inactive):
        utils.tap_image(const.chat_tab_party_inactive)
    elif send_to == 'world' and utils.is_found(const.chat_tab_world_inactive):
        utils.tap_image(const.chat_tab_world_inactive)
    time.sleep(1)
    utils.type(message)
    utils.tap_image(const.button_send)
    time.sleep(1)
    utils.key_press("esc")

def boss_config_obj(boss_region_icon, boss_remaining_time_icon, boss_map_icon, boss_coming_icon, boss_name):
    config = {}
    config['boss_region_icon'] = boss_region_icon
    config['boss_remaining_time_icon'] = boss_remaining_time_icon
    config['boss_map_icon'] = boss_map_icon
    config['boss_coming_icon'] = boss_coming_icon
    config['boss_name'] = boss_name
    # config['boss_threshold'] = boss_threshold
    return config

def boss_monitoring():
    utils.wait_for_image(const.boss_title_mvp)
    should_ignore_spawn = True
    threshold = 3*60
    # map [region, boss, map, boss_coming_icon, boss_name]
    boss_configs = [
        boss_config_obj(const.boss_region_angeling, const.boss_angeling, const.boss_map_poring_island, const.boss_coming_angeling, 'Angeling'),
        boss_config_obj(const.boss_region_golden_thief_bug, const.boss_golden_thief_bug, const.boss_map_culvert_2f, const.boss_coming_golden_thief_bug, 'Golden Thief Bug'),
        boss_config_obj(const.boss_region_deviling, const.boss_deviling, const.boss_map_poring_island, const.boss_coming_deviling, 'Deviling'),
        boss_config_obj(const.boss_region_orc_hero, const.boss_orc_hero, const.boss_map_orc_village, const.boss_coming_orc_hero, 'Orc Hero'),
        boss_config_obj(const.boss_region_maya, const.boss_maya, const.boss_map_ant_hell, const.boss_coming_maya, 'Maya'),
        boss_config_obj(const.boss_region_orc_lord, const.boss_orc_lord, const.boss_map_orc_village, const.boss_coming_orc_lord, 'Orc Lord'),
        boss_config_obj(const.boss_region_goblin_chief, const.boss_goblin_chief, const.boss_map_goblin_forest, const.boss_coming_goblin_chief, 'Goblin Chief'),
        boss_config_obj(const.boss_region_drake, const.boss_drake, const.boss_map_shipwreck_labyrinth, const.boss_coming_drake, 'Drake'),
        boss_config_obj(const.boss_region_eddga, const.boss_eddga, const.boss_map_deep_payon_forest, const.boss_coming_eddga, 'Eddga'),
        boss_config_obj(const.boss_region_mistress, const.boss_mistress, const.boss_map_garden, const.boss_coming_mistress, 'Mistress'),
        boss_config_obj(const.boss_region_osiris, const.boss_osiris, const.boss_map_pyramid_3f, const.boss_coming_osiris, 'Osiris'),
        boss_config_obj(const.boss_region_phreeoni, const.boss_phreeoni, const.boss_map_southern_sograt, const.boss_coming_phreeoni, 'Phreeoni'),
        boss_config_obj(const.boss_region_moonlight, const.boss_moonlight, const.boss_map_payon_cave_3f, const.boss_coming_moonlight, 'Moonlight'),
        boss_config_obj(const.boss_region_dracula, const.boss_dracula, const.boss_map_geffen_underground_2f, const.boss_coming_dracula, 'Dracula'),
        boss_config_obj(const.boss_region_doppelganger, const.boss_doppelganger, const.boss_map_geffen_underground_3f, const.boss_coming_doppel, 'Doppel'),
        boss_config_obj(const.boss_region_pharaoh, const.boss_pharaoh, const.boss_map_sphinx_crypt_level_2, const.boss_coming_pharaoh, 'Pharaoh')
    ]

    for boss_config in boss_configs:
        utils.scroll_down_util_found(boss_config['boss_region_icon'], const.boss_drag_icon)
        time_left = find_boss_time(boss_config['boss_remaining_time_icon'], boss_config['boss_map_icon'], threshold, should_ignore_spawn)
        print(time_left)
        if time_left < threshold:
            print('under_threshold')
            wait_boss_coming_icon_disapear(boss_config['boss_coming_icon'], boss_config['boss_name'], time_left)
            boss()
            return True
    utils.scroll_up_util_found(const.boss_angeling, const.boss_drag_icon, 300)
    return False


def wait_boss_coming_icon_disapear(boss_coming_icon, boss_name, time_left):
    send_message_to = 'party'
    time_left = int(time_left)
    if time_left > 120:
        wait_and_find_party(boss_coming_icon, boss_name, send_to=send_message_to, timeout=time_left, is_icon_apprear=True)
    wait_and_find_party(boss_coming_icon, boss_name, send_to=send_message_to, timeout=time_left, is_icon_apprear=False)


def wait_and_find_party(boss_coming_icon, boss_name, send_to, timeout=180, is_icon_apprear=True):
    current_time = time.time()
    diff_time = time.time() - current_time
    last_sent_time = time.time()
    while diff_time < timeout:
        if is_icon_apprear:
            if utils.is_found(boss_coming_icon):
                return
        else:
            if not utils.is_found(boss_coming_icon):
                return
            
        diff_last_sent = time.time() - last_sent_time
        message = boss_name + ' ' + find_remaining_party_number() + ' auto'
        if not utils.is_found(const.party_number_5) and diff_last_sent > 30:
            send_message(message, send_to)
            last_sent_time = time.time()
        time.sleep(1)
    

def find_remaining_party_number():
    if utils.is_found(const.party_number_2):
        return '-3'
    elif utils.is_found(const.party_number_3):
        return '-2'
    elif utils.is_found(const.party_number_4):
        return '-1'
    return ''


def find_boss_time(boss_image, boss_map, threshold, ignore_spawn=False):
    print("Find " + boss_image)
    result = utils.boss_remaining_time(boss_image, ignore_spawn)
    print('remain: ' + str(result))
    if (not ignore_spawn and result == 0) or (result > 0 and result < threshold):
    # if True:
        utils.tap_image(boss_image)
        utils.tap_image(const.boss_button_go)
        marked_time = time.time()
        utils.wait_for_image(boss_map, timeout=150)
        diff_time = time.time() - marked_time
        return result - diff_time
    print("")
    return result


def boss_hunt_loop():
    utils.wait_for_image(const.profile)
    tap_menu([const.event_menu1, const.event_menu2])
    utils.wait_for_image(const.event_side_menu, timeout=2)
    if utils.is_found(const.event_side_menu):
        # utils.scroll_down_util_found(const.event_boss, const.event_drag_icon, offset_y=300)
        # utils.tap_image(const.event_boss)

        utils.scroll_down_util_found(const.event_daily_inactive, const.event_drag_icon, offset_y=300)
        utils.scroll_down_util_found(const.event_boss_inactive, const.event_daily_inactive, offset_y=300)
        utils.tap_image(const.event_boss_inactive)

        while True:
            result = boss_monitoring()
            if result:
                break


def tap_menu(menu_images):
    for menu in menu_images:
        if utils.is_found(menu):
            utils.tap_image(menu)
            return


def dev():
    utils.wait_for_image(const.profile)
    print(find_remaining_party_number())
    sys.exit(0)


convert_weapon_time = time.time()
converter_timeout=(48*60)
utils.configure_logging()
while True:
    value = sys.argv[1]
    if value == "fishing":
        fishing()
    elif value == "angpao":
        ang_pao('images/pet_icon_barfo.png')
    elif value == "farm":
        farm()
    elif value == "farm_mr":
        farm_mr()
    elif value == "forging":
        forging()
    elif value == "feast":
        feast()
    elif value == "daily_demon_treasure":
        daily_demon_treasure()
    elif value == "daily_catcaravan":
        daily_cat_paw()
    elif value == "daily_anthem":
        daily_anthem()
    elif value == "ygg":
        yggdasill()
    elif value == "pet_enhance":
        pet_enhance()
    elif value == "dev":
        dev()
    elif value == "boss":
        boss()
    elif value == "boss_fight":
        boss_fight()
    elif value == "oracle":
        oracle()
    elif value == "boss_hunt":
        boss_hunt_loop()
    else:
        break
    time.sleep(1)


