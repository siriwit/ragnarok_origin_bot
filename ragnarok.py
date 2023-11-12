import pyautogui
import anthem
import boss
import constanst as const
import feast
import func
import dbbb
import juperos
import time
import sys
import utils
import img
import oracle
import picky_boss
import preset
import time_anomaly
import ygg
import alfheim
import hordor
import guild_expedition
import treasure_map
import life_skill
import demon_treasure
import catpaw
import hazy
import nightmare
import hellheim
import halfyear
import cv2 as cv
import guild_collect
        

def farm():
    func.wait_profile()
    func.ang_pao()
    func.use_items()
    # convert_weapon(element='wind')

    if utils.is_found(img.fatique_icon, similarity=0.95):
        utils.wait_and_tap(img.fatique_close)
        func.butterfly_wing_morroc()
        sys.exit()


def farm_mr():
    func.wait_profile()
    func.ang_pao()
    func.use_items()


def convert_weapon(element='fire'):
    diff_time = time.time() - convert_weapon_time
    utils.log(diff_time)
    if diff_time > converter_timeout:
        perform_convert_weapon(element)

def perform_convert_weapon(element='water'):
    func.wait_profile()
    pyautogui.typewrite('b')
    utils.wait_and_tap(img.weapon5)
    utils.wait_and_tap(img.button_more)
    utils.wait_and_tap(img.button_element)
    utils.wait_and_tap(img.button_plus)
        
    if element == 'fire':
        utils.wait_for_image('images/region_fire_slayer_converter.png')
        utils.tap_image_in_region('images/button_select.png', 'images/region_fire_slayer_converter.png')
    elif element == 'wind':
        utils.wait_for_image(img.region)
        utils.tap_image_in_region(img.button_select, img.region_wind_spear_converter)
    elif element == 'water':
        utils.wait_for_image('images/region_water_1hsword_converter.png')
        utils.tap_image_in_region('images/button_select.png', 'images/region_water_1hsword_converter.png')
    else:
        utils.wait_for_image('images/region_earth_1hsword_converter.png')
        utils.tap_image_in_region('images/button_select.png', 'images/region_earth_1hsword_converter.png')
    utils.wait_for_image('images/button_use.png')
    utils.tap_image('images/button_use.png')
    func.close_any_panel()
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
    utils.tap_image(img.button_enhance)
    utils.tap_image(img.button_confirm)
    utils.tap_image(img.pet_enhance_tap_to_close)
    if utils.is_found(img.max_level_reached) or utils.is_found(img.pet_enhance_out_of_amber):
        func.close_any_panel()
        sys.exit(0)


def maintain_woe():
    func.wait_profile()
    utils.tap_any(const.pets)
    utils.tap_if_found(img.button_respawn)


def dev():
    utils.wait_for_image(img.power_up_icon, timeout=2)
    preset.ensure_use_support_skill(img.preset_skill_shield_reflect, img.preset_skill_touse_shield_reflect)
    sys.exit(0)

convert_weapon_time = time.time()
converter_timeout=(48*60)
utils.configure_logging()
while True:
    value = sys.argv[1]
    if value == "fishing":
        life_skill.start(mode='fishing')
        sys.exit(0)
    elif value == "angpao":
        func.ang_pao()
    elif value == "farm":
        farm()
    elif value == "farm_mr":
        farm_mr()
    elif value == "forging":
        life_skill.start()
        sys.exit(0)
    elif value == "feast":
        feast.start()
        sys.exit(0)
    elif value == "cooking":
        life_skill.start(mode='cooking')
        sys.exit(0)
    elif value == "daily_demon_treasure":
        demon_treasure.daily_demon_treasure()
        sys.exit(0)
    elif value == "daily_catcaravan":
        catpaw.daily_cat_paw()
        sys.exit(0)
    elif value == "daily_anthem":
        anthem.daily_anthem()
        sys.exit(0)
    elif value == "ygg":
        ygg.preset()
        ygg.ygg_fight()
    elif value == "pet_enhance":
        pet_enhance()
    elif value == "dev":
        dev()
    elif value == "boss":
        boss.boss()
    elif value == "boss_fight":
        boss.boss_fight()
    elif value == "oracle":
        print('select mode:' + str(sys.argv[2]))
        mode = sys.argv[2]
        if mode == 'wait':
            oracle.oracle()
        else:
            oracle.request_oracle()
    elif value == "dbbb":
        dbbb.party_finder()
    elif value == "boss_hunt":
        print('argument2:' + sys.argv[2])
        is_active = False if sys.argv[2] == 'False' else bool(sys.argv[2])
        min_level = int(sys.argv[3])
        max_level = int(sys.argv[4])
        ignore_spawn = False if sys.argv[5] == 'False' else bool(sys.argv[5])
        print('boss mode:' + str(is_active))
        print('level more than: ' + str(min_level))
        print('level less than: ' + str(max_level))
        boss.boss_hunt_loop(is_active, min_level, max_level, ignore_spawn)
    elif value == "boss_specific":
        preset.tank()
        boss.boss_hunt_specific()
    elif value == "picky_boss":
        picky_boss.picky_boss_hunt()
    elif value == "preset":
        print('select preset:' + str(sys.argv[2]))
        preset.change_preset(sys.argv[2])
    elif value == "preset_daily":
        preset.daily()
        sys.exit(0)
    elif value == "preset_farm":
        preset.farm()
        sys.exit(0)
    elif value == "preset_boss":
        preset.boss()
        sys.exit(0)
    elif value == "preset_tank":
        preset.tank()
        sys.exit(0)
    elif value == "preset_ygg":
        preset.ygg()
        sys.exit(0)
    elif value == "preset_pvp":
        preset.pvp()
        sys.exit(0)
    elif value == "preset_card":
        print('select tribe:' + str(sys.argv[2]))
        print('select element:' + str(sys.argv[3]))
        print('select size:' + str(sys.argv[4]))
        tribe = None if sys.argv[2] == 'None' else sys.argv[2]
        element = None if sys.argv[3] == 'None' else sys.argv[3]
        size = None if sys.argv[4] == 'None' else sys.argv[4]
        preset.againt_monster_card(tribe, element, size)
        sys.exit(0)
    elif value == "alfheim":
        print('select mode:' + str(sys.argv[2]))
        mode = sys.argv[2]
        if mode == 'fight':
            alfheim.preset()
            alfheim.alfheim_fight()
        else:
            alfheim.alfheim_collect_item()
        sys.exit(0)
    elif value == "time_anomaly":
        # time_anomaly.preset()
        time_anomaly.start()
        sys.exit(0)
    elif value == "hordor":
        print('select mode:' + str(sys.argv[2])) 
        mode = sys.argv[2]
        if mode == 'poring':
            hordor.hordor_dreamland(mode=img.hordor_poring_dream)
        elif mode == 'ocean':
            hordor.hordor_dreamland(mode=img.hordor_magic_ocean)
        elif mode == 'waste':
            hordor.hordor_dreamland(mode=img.hordor_wasteland)
        elif mode == 'paradise':
            hordor.hordor_dreamland(mode=img.hordor_paradise_courage)
        sys.exit(0)
    elif value == 'guild_exp':
        guild_expedition.start()
        sys.exit(0)
    elif value == 'ju':
        juperos.start()
        sys.exit(0)
    elif value == 'woe':
        maintain_woe()
    elif value == 'treasure_map':
        treasure_map.start()
        sys.exit(0)
    elif value == 'hazy':
        hazy.start()
        sys.exit(0)
    elif value == 'nt':
        element = const.earth if sys.argv[2] == 'None' else sys.argv[2]
        nightmare.start(element)
        sys.exit(0)
    elif value == 'create_party':
        func.create_party_and_invite()
        sys.exit(0)
    elif value == 'helheim':
        hellheim.start()
        sys.exit(0)
    elif value == 'collect':
        guild_collect.start()
        sys.exit(0)
    else:
        break
    time.sleep(1)


