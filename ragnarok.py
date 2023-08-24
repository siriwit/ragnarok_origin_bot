import pyautogui
import boss
import func
import time
import sys
import utils
import img
import picky_boss
import preset
import time_anomaly
import ygg
import alfheim
import hordor


def fishing():
    utils.wait_for_image(img.profile)
    ang_pao()
    utils.tap(1000, 300)
    utils.wait_for_image('images/fishing_alert.png')
    utils.tap_image('images/fishing_alert.png')


def ang_pao(pet_image=img.pet_icon_earthlord):
    utils.wait_for_image(img.profile)
    while True:
        if utils.is_found(img.ang_pao_red):
            utils.tap_image(img.ang_pao_red, screenshot=True, result_filename=img.angpao_header)
            utils.tap_image(pet_image)
            continue
        elif utils.is_found(img.ang_pao_yellow):
            utils.tap_image(img.ang_pao_yellow, screenshot=True, result_filename=img.angpao_header)
            utils.tap_image(pet_image)
            continue
        break
        

def farm():
    utils.wait_for_image(img.profile)
    ang_pao(pet_image=img.pet_icon_earthlord)
    utils.tap_image('images/item_alert.png', screenshot=True, before=True)
    utils.tap_image('images/button_receive.png', screenshot=True, before=True)
    utils.tap_image('images/sig_ancient_power.png')
    func.enable_aura()
    convert_weapon(element='wind')

    fatique = utils.find_image_with_similarity('images/fatique_icon.png')
    if fatique is not None:
        utils.wait_and_tap('images/fatique_close.png')
        butterfly_wing_morroc()
        utils.wait_for_image(img.profile)
        func.disable_aura()
        sys.exit()


def butterfly_wing_morroc():
    utils.wait_and_tap('images/butterfly_wing.png')
    utils.wait_and_tap('images/city_morroc.png')


def forging():
    utils.wait_for_image(img.profile)
    ang_pao()
    utils.tap_image('images/forging.png')


def farm_mr():
    utils.wait_for_image(img.profile)
    ang_pao(img.pet_icon_barfo)
    utils.tap_image('images/normal_attack.png')
    utils.tap_image('images/item_alert.png', screenshot=True, before=True)


def feast():
    utils.wait_for_image(img.profile)
    ang_pao(img.pet_icon_earthlord)
    func.use_items()
    if utils.is_found(img.food_grab):
        utils.tap_image(img.food_grab)
        utils.wait_and_tap(img.food_taste, timeout=2)
        time.sleep(2)


def daily_demon_treasure():
    utils.wait_for_image(img.profile)
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
    utils.wait_for_image(img.profile)

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

        utils.tap_image(img.button_quick_departure)
        utils.wait_and_tap(img.button_confirm, timeout=2)
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
    utils.wait_for_image(img.profile)
    pyautogui.typewrite('b')
    utils.wait_and_tap(img.weapon4)
    utils.wait_and_tap(img.button_more)
    utils.wait_and_tap(img.button_element)
    utils.wait_and_tap(img.button_plus)
        
    if element == 'fire':
        utils.wait_for_image('images/region_fire_slayer_converter.png')
        utils.tap_image_in_region('images/button_select.png', 'images/region_fire_slayer_converter.png')
    elif element == 'wind':
        utils.wait_for_image(img.region_wind_1hsword_converter)
        utils.tap_image_in_region(img.button_select, img.region_wind_1hsword_converter)
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


def daily_anthem():
    utils.wait_for_image(img.profile)
    utils.wait_for_image(img.menu_daily)
    utils.tap_image(img.menu_daily)
    utils.wait_and_tap('images/daily_anthem.png', timeout=2)
    utils.tap_image(img.button_go)
    utils.wait_and_tap('images/daily_anthem_anthem_trial_option.png', timeout=120)
    utils.tap_image('images/button_use.png')
    utils.wait_and_tap('images/button_submit.png', timeout=1)
    utils.tap_image('images/button_start.png')
    utils.wait_for_image(img.team_confirm, timeout=1)
    if utils.is_found(img.team_confirm):
        utils.wait_until_disappear(img.team_confirm)
    anthem()


def anthem():
    utils.wait_for_image(img.profile)
    utils.tap_image('images/anthem_activate.png')
    utils.wait_for_image('images/anthem_lucky_wheel.png')
    utils.wait_for_image('images/anthem_activate.png')
    anthem_fight()


def anthem_fight():
    utils.wait_for_image(img.profile)
    utils.hold_press('a', timeout=0.5)
    utils.hold_press('w', timeout=3)
    utils.key_press('k')
    utils.tap_image(img.pet_icon_earthlord)
    utils.wait_for_image(img.victory, timeout=150)
    func.use_items()
    utils.wait_and_tap(img.daily_anthem_tap_anywhere1, timeout=20)
    utils.wait_and_tap(img.daily_selectable_card, timeout=20)
    utils.wait_and_tap(img.daily_anthem_tap_anywhere2, timeout=20)
    utils.wait_and_tap(img.button_escape, timeout=20)
    utils.wait_and_tap(img.button_confirm, timeout=20)
    utils.wait_for_image(img.profile)
    sys.exit(0)
        

def dbbb_party_finder():
    utils.wait_for_image(img.profile)
    message = 'dbbb ' + func.find_remaining_party_number()
    if utils.is_found(img.party_number_5):
        sys.exit()
    else:
        func.send_message(message, 'world')
    time.sleep(20)


def request_oracle():
    if utils.is_found(img.menu_hidden):
        utils.tap_image(img.menu_hidden)
        utils.wait_and_tap(img.menu_guild, timeout=2)
        utils.wait_and_tap(img.guild_menu_member, timeout=2)
        request_all_member()
        oracle()


def request_all_member():
    is_found_teasing = False
    while True:
        if not utils.is_found(img.guild_request_oracle_icon):
            utils.scroll_down_util_found(img.guild_request_oracle_icon, img.guild_online_status, 300)

        utils.tap_image(img.guild_request_oracle_icon)
        if utils.is_found(img.guild_request_oracle_icon):
            is_found_teasing = True
            utils.drag_up(img.guild_request_oracle_icon, offset_y=100)

        if utils.is_found(img.button_agree):
            oracle(in_main_page=False)
            return

        if is_found_teasing and not utils.is_found(img.guild_request_oracle_icon):
            utils.tap_image(img.guild_close_button)
            return
        
        time.sleep(1)


def oracle(in_main_page=True):
    while True:
        if in_main_page:
            utils.wait_for_image(img.profile)
            utils.tap_image(img.pet_icon_earthlord)

        if utils.is_found(img.button_agree):
            utils.tap_image(img.button_agree)
            utils.wait_for_image(img.oracle_present, timeout=60)
            func.send_message('[z1]')
            utils.wait_and_tap(img.button_escape, timeout=20)
            utils.wait_and_tap(img.button_confirm, timeout=20)
            utils.wait_for_image(img.profile)

            if in_main_page:
                utils.wait_and_tap(img.party_number_2, timeout=2)
                utils.wait_and_tap(img.party_leave_button, timeout=2)

        time.sleep(1)


def leave_party(party_number=img.party_number_2):
    utils.tap_image(party_number)
    utils.wait_and_tap(img.party_leave_button)


def dev():
    utils.wait_for_image(img.profile)
    hordor.hordor_dreamland()
    sys.exit(0)

convert_weapon_time = time.time()
converter_timeout=(48*60)
utils.configure_logging()
while True:
    value = sys.argv[1]
    if value == "fishing":
        fishing()
    elif value == "angpao":
        ang_pao(img.pet_icon_earthlord)
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
        request_oracle()
    elif value == "dbbb":
        dbbb_party_finder()
    elif value == "boss_hunt":
        print('argument2:' + sys.argv[2])
        is_active = False if sys.argv[2] == 'False' else bool(sys.argv[2])
        print('boss mode:' + str(is_active))
        boss.boss_hunt_loop(is_active)
    elif value == "picky_boss":
        picky_boss.picky_boss_hunt()
    elif value == "preset":
        print('select preset:' + str(sys.argv[2]))
        preset.change_preset(sys.argv[2])
    elif value == "preset_daily":
        preset.daily()
    elif value == "preset_farm":
        preset.farm()
    elif value == "preset_boss":
        preset.boss()
    elif value == "preset_tank":
        preset.tank()
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
            preset.farm()
            alfheim.alfheim_fight()
        else:
            alfheim.alfheim_collect_item()
        sys.exit(0)
    elif value == "time_anomaly":
        time_anomaly.preset()
        time_anomaly.time_anomaly()
        sys.exit(0)
    elif value == "hordor":
        print('select mode:' + str(sys.argv[2])) 
        mode = sys.argv[2]
        if mode == 'poring':
            hordor.hordor_dreamland(mode=img.hordor_poring_dream)
        elif mode == 'ocean':
            hordor.hordor_dreamland(mode=img.hordor_magic_ocean)
        sys.exit(0)
    else:
        break
    time.sleep(1)


