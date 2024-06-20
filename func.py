import constanst as const
import configparser
import cv2 as cv
import datetime
import img
import func
import time
import utils

config = configparser.ConfigParser()
config_file_path = 'bot.ini'
config.read(config_file_path)
settings = config['SETTINGS']

shield_reflection_timeout=(0.5*60)
shield_reflection_time = time.time() - shield_reflection_timeout - 10
cooldowns = {}

def check_cooldown(key, timeout):
    if key in cooldowns:
        remaining_time = (cooldowns[key] + timeout) - time.time()
        print(f"Remaining of {key} cooldown: {remaining_time}")
        if remaining_time < 0:
            return True
    else:
        cooldowns[key] = time.time() - 10
        return True
    return False


def reset_cooldown(key):
    if key in cooldowns:
        cooldowns[key] = time.time()


def set_cooldown(key, new_timeout):
    if key in cooldowns:
        cooldowns[key] = time.time() + new_timeout


def reset_shield_reflection_time():
    global shield_reflection_time
    shield_reflection_time = time.time()


def use_manual_skill(preset=const.boss, monster_element=const.neutral):
    if settings["preset"] == 'jj_royal_guard':
        return use_royal_guard_skill(preset, monster_element)
    elif settings["preset"] == 'jj_rune_knight':
        return use_rune_knight_skill(preset)


def use_royal_guard_skill(preset, monster_element=const.neutral):
    if preset == const.boss:
        return royal_guard_fight()
    elif preset == const.farm:
        return royal_guard_farm(monster_element)


def royal_guard_farm(monster_element=const.neutral):
    count = 0
    while True:
        if count > 20:
            break

        if utils.is_found(img.royal_guard_skill_battle_rage_100):
            count += 1
            continue

        if utils.is_found(img.converter_page):
            element_recharge(monster_element)

        if utils.is_found(img.royal_guard_skill_battle_chant):
            enable_battle_chant()
        
        break
    return 0


def enable_battle_chant():
    utils.tap_offset_until_found(img.royal_guard_skill_battle_chant, img.royal_guard_skill_sacrifice, offset_x=230, offset_y=-40)
    utils.tap_until_found(img.royal_guard_skill_battle_chant, img.royal_guard_skill_battle_chant_activated)
    func.wait(2)
    utils.tap_if_found(img.royal_guard_skill_battle_chant_activated)
    utils.tap_offset_until_found(img.royal_guard_skill_battle_chant_activated, img.royal_guard_skill_over_band, offset_x=230, offset_y=-40)
    utils.tap_until_found(img.royal_guard_skill_battle_chant, img.royal_guard_skill_battle_chant_activated)


def royal_guard_fight():
    fight_state_count = 0
    count_battle_rage = 0
    while True:
        if count_battle_rage > 20:
            break

        if utils.is_found(img.royal_guard_skill_over_band):
            fight_state_count += 1

        for _ in range(0, 3):
            if utils.count_image_on_screen(img.royal_guard_skill_roar) > 1:
                utils.tap_if_found(img.royal_guard_skill_roar)
                continue

        if not utils.is_found(img.royal_guard_skill_battle_rage_100):
            if func.check_cooldown("shield_reflection", 30):
                utils.tap_if_found(img.royal_guard_skill_shield_reflection)
                func.reset_cooldown("shield_reflection")
            # utils.tap_if_found(img.swordman_skill_endure)
            # utils.tap_if_found(img.swordman_skill_provoke)
            # utils.tap_if_found(img.paladin_skill_providence)
        # utils.tap_if_found(img.sigil_skill_descending_swords)

        if utils.is_found(img.royal_guard_skill_battle_chant):
            enable_battle_chant()
        break
    return fight_state_count


def use_rune_knight_skill(preset=const.boss):
    if preset == const.boss:
        return rune_knight_preset_fight()
    elif preset == const.farm:
        return rune_knight_preset_farm()


def rune_knight_preset_farm():
    count = 0
    while True:
        if count > 20:
            break

        if utils.is_found(img.rune_knight_skill_dragon_scion_ready):
            utils.tap_image(img.rune_knight_skill_dragon_scion)
            count += 1
            continue
        break
    return 0


def rune_knight_preset_fight():
    fight_state_count = 0
    count_dragon_scion = 0
    while True:
        if count_dragon_scion > 20:
            break

        if utils.is_found(img.rune_knight_skill_dragon_scion_ready):
            utils.tap_image(img.rune_knight_skill_dragon_scion)
            count_dragon_scion += 1
            continue

        utils.tap_if_found(img.quests_inactive)

        if utils.is_found(img.rune_knight_skill_berserk):
            fight_state_count += 1

        for _ in range(0, 5):
            if utils.count_image_on_screen(img.rune_knight_skill_rune_of_faith) > 1:
                utils.tap_if_found(img.rune_knight_skill_rune_of_faith)
                continue

            if utils.is_found(img.rune_knight_skill_dragon_state, similarity=0.85) and utils.is_found(img.hp_sp_80_percent):
                utils.tap_if_found(img.rune_knight_skill_berserk)
            utils.tap_if_found(img.rune_knight_skill_charge_attack)
            utils.tap_if_found(img.rune_knight_skill_ignition_break)
            utils.tap_if_found(img.rune_knight_skill_ignition_break2)
            utils.tap_if_found(img.rune_knight_skill_rune_of_courage)
            utils.tap_if_found(img.rune_knight_skill_rune_of_mercy)
            # utils.tap_if_found(img.rune_knight_skill_dragon_breath_fire)

        if not utils.is_found(img.rune_knight_skill_dragon_state):
            utils.tap_if_found(img.swordman_skill_provoke)
        utils.tap_if_found(img.sigil_skill_descending_swords)
        break
    return fight_state_count

def butterfly_wing_morroc():
    if utils.is_found(img.map_morroc):
        return
    func.close_hidden_menu()
    utils.execute_until_valid_state_with_timeout(30, 1, try_butterfly_wing)
    wait_loading_screen()
    close_any_panel()
    func.wait_profile()
    time.sleep(3)


def try_butterfly_wing():
    if utils.is_found(img.map_morroc):
        return True
    if utils.is_found(img.loading):
        return True
    utils.tap_until_found(img.butterfly_wing, img.city_morroc, timeout=2)
    utils.tap_until_notfound(img.city_morroc, img.city_morroc, timeout=2)
    return False


def wait_loading_screen():
    wait_screen = utils.wait_for_image(img.loading)
    utils.wait_until_disappear(img.loading)
    return wait_screen


def send_message(message, send_to='party'):
    open_chat(send_to)
    if utils.is_found(img.chat_tap_to_type):
        utils.tap_image(img.chat_tap_to_type)
    time.sleep(0.3)
    utils.type(message)
    utils.key_press("enter")
    utils.wait_and_tap(img.button_send)
    close_chat()

def open_chat(send_to='party'):
    utils.execute_until_valid_state_with_timeout(15, 1, open_chat_state)

    if send_to == 'party' and utils.is_found(img.chat_tab_party_inactive):
        utils.tap_image(img.chat_tab_party_inactive)
    elif send_to == 'world' and utils.is_found(img.chat_tab_world_inactive):
        utils.tap_image(img.chat_tab_world_inactive)
    elif send_to == 'guild' and utils.is_found(img.chat_tab_guild_inactive):
        utils.tap_image(img.chat_tab_guild_inactive)
    
    time.sleep(1)


def open_chat_state():
    if utils.is_found(img.chat_tab_party_active) or utils.is_found(img.chat_tab_party_inactive):
        return True
    if utils.is_found(img.chat_tab_guild_active) or utils.is_found(img.chat_tab_guild_inactive):
        return True
    else:
        func.close_any_panel()
    utils.key_press("enter")
    time.sleep(1)
    return False


def close_chat():
    if not utils.execute_until_valid_state_with_timeout(15, 1, close_chat_state):
        close_any_panel()


def close_chat_state():
    if not utils.is_found(img.chat_button_plus):
        return True
    utils.tap_until_notfound(img.chat_collapse, img.chat_collapse)
    time.sleep(1)
    return False


def open_map():
    utils.execute_until_invalid_state(10, 1, open_map_state)


def open_map_state():
    utils.key_press('m')
    if utils.wait_for_image(img.wing, timeout=1) is not None:
        return False
    return True


def close_map():
    utils.execute_until_invalid_state(10, 1, close_map_state)


def close_map_state():
    if utils.is_found(img.wing):
        utils.key_press('m')

    if utils.wait_for_image(img.butterfly_wing, timeout=1) is not None:
        return False
    return True


def send_location(send_to='party'):
    open_chat(send_to)
    utils.tap_image(img.chat_button_plus)
    utils.wait_and_tap(img.chat_button_map, timeout=7)
    utils.tap_until_notfound(img.chat_button_send_background, img.chat_button_map, timeout=3)
    utils.wait_and_tap(img.chat_button_send, timeout=3)
    close_chat()


def party_finder(message, expected_number=img.party_number_5):
    last_sent_time = time.time() - 20
    while True:
        func.wait_profile()
        chat_message = message + ' ' + find_remaining_party_number()
        if utils.is_found(expected_number):
            break
        else:
            diff_last_sent = time.time() - last_sent_time
            if diff_last_sent > 20:
                send_message(chat_message, 'world')
                last_sent_time = time.time()
        time.sleep(1)


def find_boss_party(boss_name, send_message_to):
    utils.tap_if_found(img.party_inactive)
    message = boss_name + ' ' + find_remaining_party_number() + ' auto join'
    if not utils.is_found(img.party_number_5):
        send_message(message, send_message_to)


def wait_and_find_party(boss_coming_icon, boss_name, send_to, timeout=180, is_icon_apprear=True, party_mode=True):
    print("wait_and_find_party with is_icon_apprear=" + str(is_icon_apprear) + ", timeout=" + str(timeout))
    marked_time = time.time()
    last_sent_time = time.time()
    while time.time() - marked_time < timeout:
        if is_icon_apprear:
            if utils.is_found(boss_coming_icon):
                return
        else:
            if not utils.is_found(boss_coming_icon):
                return
            
        diff_last_sent = time.time() - last_sent_time
        message = boss_name + ' ' + find_remaining_party_number() + ' auto join'
        kick_party_member()
        if not utils.is_found(img.party_number_5) and diff_last_sent > 30:
            print("not found number 5 icon")
            if party_mode:
                send_message(message, send_to)
            last_sent_time = time.time()

        diff_time = time.time() - marked_time
        print("remaining wait: " + str(timeout-diff_time))
        time.sleep(1)
    

def find_remaining_party_number():
    if utils.is_found(img.party_number_1):
        return '-4'
    elif utils.is_found(img.party_number_2):
        return '-3'
    elif utils.is_found(img.party_number_3):
        return '-2'
    elif utils.is_found(img.party_number_4):
        return '-1'
    return ''

        
def auto_attack(mode=const.boss, all_radius=True, timeout=10):
    result = False
    while True:
        if not utils.is_found(img.auto_attack_title):
            if utils.tap_any_until_found_offset(const.menu_bags, img.auto_attack_title, offset_x=85, timeout=timeout):
                continue
        if mode == const.boss:
            utils.wait_for_image(img.icon_auto_attack_boss, timeout=1)
            if utils.is_found(img.icon_auto_attack_boss):
                utils.wait_and_tap(img.icon_auto_attack_boss)
                result = True
            else:
                utils.wait_and_tap(img.auto_attack_allmonster)
        else:
            utils.wait_and_tap(img.auto_attack_allmonster)
        if all_radius:
            utils.tap_if_found(img.auto_attack_all)
        utils.tap_image(img.button_auto_attack_close)
        break
    return result

def use_items():
    while True:
        if utils.is_found(img.button_confirm):
            utils.tap_image(img.button_confirm)
            time.sleep(0.5)
            continue
        elif utils.is_found(img.button_receive):
            utils.tap_image(img.button_receive)
            continue
        elif utils.is_found(img.item_button_use):
            utils.tap_image(img.item_button_use)
            continue
        elif utils.is_found(img.button_submit):
            utils.tap_image(img.button_submit)
            continue
        utils.tap_if_found(img.button_back)
        break


def open_event_page_state():
    utils.key_press('f')
    if utils.wait_for_image(img.event_page) is not None:
        return True
    return False


def go_to_event(event_image=None):
    func.close_any_panel(img.power_up_icon)
    utils.tap_any(const.batterry_savings)
    utils.tap_if_found(img.button_confirm)
    handle_if_need_to_go_to_checkpoint()
    handle_battle_log(True)

    if utils.execute_until_valid_state_with_timeout(10, 1, open_event_page_state):
        if event_image != None:
            if utils.is_found(img.event_moonlit_arena):
                utils.scroll_down_util_found(event_image, img.event_moonlit_arena, offset_y=100, timeout=1)
            if utils.is_found(img.event_theme_party):
                utils.scroll_down_util_found(event_image, img.event_theme_party, offset_y=100, timeout=1)
            if utils.is_found(img.event_initial_trial_of_nerdiness):
                utils.scroll_down_util_found(event_image, img.event_initial_trial_of_nerdiness, offset_y=100, timeout=1)
            if utils.is_found(img.event_initial_trial_of_nerdiness):
                utils.scroll_down_util_found(event_image, img.event_initial_trial_of_nerdiness, offset_y=100, timeout=1)
            if not utils.scroll_down_util_found(event_image, img.event_drag_icon, offset_y=200, timeout=10, similarity=0.85):
                utils.scroll_down_util_found(event_image, img.event_drag_icon_inactive, offset_y=200, similarity=0.85)

            if event_image not in [img.event_boss, img.event_guild_expedition]:
                utils.tap_until_found(event_image, img.button_go_orange_small)
                if utils.wait_and_tap(img.button_go_orange_small) is not None:
                    return True
            elif event_image == img.event_boss:
                if utils.tap_until_found(event_image, img.boss_title_mvp, delay=2):
                    return True
            else:
                if utils.tap_until_notfound(event_image, event_image):
                    return True
    func.close_any_panel()
    return False
    

def ang_pao():
    while True:
        if utils.is_found(img.ang_pao_red):
            utils.tap_image(img.ang_pao_red, screenshot=True, result_filename=img.angpao_header)
            utils.tap_offset_until_notfound(img.angpao_header, img.angpao_header, offset_x=400)
            continue
        elif utils.is_found(img.ang_pao_yellow):
            utils.tap_image(img.ang_pao_yellow, screenshot=True, result_filename=img.angpao_header)
            utils.tap_any(const.pets)
            continue
        utils.tap_offset_until_notfound(img.angpao_header, img.angpao_header, offset_x=400)
        utils.tap_image(img.ang_pao_yellow, screenshot=True, result_filename=img.angpao_header)
        break


def leave_party():
    func.wait_profile()
    func.wait(2)
    if utils.is_found_any(const.party_members):
        utils.tap_any_until_found(const.party_members, img.party_leave_button)
        utils.wait_and_tap(img.party_leave_button)


def close_any_panel(expected_found_image=img.power_up_icon, depth=99, timeout=10, is_boss_mode=False):
    depth_count = 1
    marked_time_main = time.time()
    while time.time() - marked_time_main < timeout:
        utils.tap_if_found(img.button_back)
        if utils.is_found(expected_found_image) or depth_count >= depth:
            break
        
        utils.tap_any(const.button_closes)
        utils.tap_if_found(img.chat_collapse)
        utils.tap_if_found(img.divination_house_daily_fortune_skip)
        utils.tap_any(const.tap_anywheres)
        # utils.tap_offset_if_found(img.rune_knight_skill_popup_rune_of_faith, offset_y=-50)
        
        if not is_boss_mode and utils.is_found(img.button_battle_log):
            utils.tap_offset_until_notfound(img.button_battle_log, img.button_battle_log, offset_y=100)

        depth_count += 1


def move_left(hold=0.5):
    if not can_move():
        return
    offset = -100
    start_x, start_y = get_move_area()
    utils.drag_and_drop(start_x, start_y, start_x + offset, start_y, duration=hold)


def move_right(hold=0.5):
    if not can_move():
        return
    offset = 100
    start_x, start_y = get_move_area()
    utils.drag_and_drop(start_x, start_y, start_x + offset, start_y, duration=hold)


def move_down(hold=0.5):
    if not can_move():
        return
    offset = 100
    start_x, start_y = get_move_area()
    utils.drag_and_drop(start_x, start_y, start_x , start_y + offset, hold=hold)


def move_up(hold=0.5):
    if not can_move():
        return
    offset = -100
    start_x, start_y = get_move_area()
    utils.drag_and_drop(start_x, start_y, start_x , start_y + offset, hold=hold)


def can_move():
    return utils.is_found(img.ride_peco) or utils.is_found_any(const.guilds) is not None


def get_move_area():
    if utils.is_found(img.ride_peco):
        offset_x = 238
        offset_y = 22
        return get_move_area_location([img.ride_peco], offset_x, offset_y)
    elif utils.is_found_any(const.guilds):
        offset_x = -223
        offset_y = -118
        return get_move_area_location(const.guilds, offset_x, offset_y)

def get_move_area_location(image_paths, offset_x, offset_y):
    image_objs = utils.find_all_images(image_paths, similarity=0.8)
    if len(image_objs) > 0:
        center_x, center_y = utils.find_image_center(image_objs[0])
        return (center_x + offset_x), (center_y + offset_y)
    return None

def create_party_and_invite(auto_accept=True):
    func.wait_profile()
    
    if utils.is_found(img.party_inactive):
        utils.tap_until_found(img.party_inactive, img.create_party, timeout=5)

    if utils.is_found(img.create_party):
        utils.wait_and_tap(img.create_party)
        if auto_accept:
            utils.wait_for_image(img.party_member)
            utils.tap_image_offset(img.party_member, offset_y=120)
            utils.wait_and_tap(img.party_auto_accept)
            utils.tap_image_offset(img.party_request, offset_y=-120)
        # utils.wait_and_tap(img.party_tap_to_invite)
        # utils.wait_for_image(img.party_friend_tap)
        # utils.tap_until_found(img.party_friend_tap, img.party_friend_tap_active)
        # wait(1)
        # utils.scroll_down_util_found(friend, img.button_invite, timeout=5)
        # utils.wait_for_image(friend)
        # utils.tap_image_offset(friend, offset_x=380, offset_y=50)
        close_any_panel()
        # utils.wait_and_tap(img.party_one_tap_rally)
        # one_tap_rally()


def one_tap_rally():
    utils.wait_and_tap(img.party_one_tap_rally)


def accept_rally():
    utils.tap_if_found(img.button_join)


def leave_event(timeout=30):
    utils.tap_until_found(img.button_escape, img.button_confirm, timeout=timeout)
    utils.tap_until_notfound(img.button_confirm, img.button_confirm)
    utils.wait_for_image(img.loading, timeout=5)
    utils.wait_until_disappear(img.loading, timeout=5)


def wait_profile(timeout=10):
    utils.wait_for_image(img.power_up_icon, timeout)


def wait(timeout=10):
    marked_time = time.time()
    while time.time() - marked_time < timeout:
        utils.wait_for_image(img.power_up_icon, timeout=0.5)

def close_hidden_menu():
    func.close_any_panel(img.butterfly_wing)
    func.wait_profile()
    if utils.is_found_any(const.menu_guilds):
        utils.tap_offset_until_found(img.menu_bag, img.butterfly_wing, offset_x=180)

def open_bag():
    utils.tap_any_until_found(const.menu_bags, img.backpack_title)


def open_hidden_menu():
    if not utils.is_found_any(const.menu_guilds):
        utils.tap_offset_until_found(img.menu_bag, img.menu_album, offset_x=180)


def close_debug_window():
    cv.destroyAllWindows()


def open_menu_guide():
    utils.key_press('g')
    if utils.wait_for_image(img.guide_page, timeout=3) is not None:
        return True
    return False


def card_change_object(used_card, selected_current_card, to_be_selected_card):
    card_object = {}
    card_object['used_card'] = used_card
    card_object['selected_current_card'] = selected_current_card
    card_object['to_be_selected_card'] = to_be_selected_card
    return card_object


def ensure_replace_skill(ensure_skill, ensure_touse_skill, tobe_replaced_skills):
    for tobe_replaced_skill in tobe_replaced_skills:
        if not utils.is_found(ensure_skill):
            if utils.is_found(tobe_replaced_skill, similarity=0.95):
                utils.drag_and_drop_image(ensure_touse_skill, tobe_replaced_skill)
                break
            elif utils.is_found(img.preset_skill_empty_slot, similarity=0.95):
                utils.drag_and_drop_image(ensure_touse_skill, img.preset_skill_empty_slot)
                break

def ensure_use_support_skill(ensure_skill, ensure_touse_skill):
    if utils.wait_for_image(ensure_skill, timeout=1) is None:
        utils.drag_and_drop_image(ensure_touse_skill, img.preset_skill_empty_slot)


def remove_skill_if_needed(ensure_skill):
    if utils.wait_for_image(ensure_skill, timeout=1) is not None:
        utils.drag_and_drop_image(ensure_skill, img.preset_skill_manual)


def handle_if_need_to_go_to_checkpoint():
    if utils.wait_for_image(img.button_return_to_checkpoint, timeout=2) is not None:
        utils.tap_until_notfound(img.button_return_to_checkpoint, img.button_return_to_checkpoint)
        func.wait_loading_screen()
        func.wait_profile()


def handle_battle_log(butterflywing):
    utils.tap_if_found(img.battery_saving1)
    if utils.is_found(img.button_battle_log):
        func.use_items()
        func.close_any_panel(timeout=3)
        func.handle_if_need_to_go_to_checkpoint()
        if butterflywing:
            func.butterfly_wing_morroc()
        return True
    return False


def request_people_join_message(prefix, suffix='auto join', send_to='world'):
    message = f'{prefix} {func.find_remaining_party_number()} {suffix}'
    if not utils.is_found(img.party_number_5):
        func.send_message(message, send_to=send_to)


def kick_party_member():
    similarity = 0.9
    if utils.is_found_any(const.party_kicks):
        if utils.is_found(img.party_offline):
            print("Tap img.party_offline")
            utils.tap_offset_until_found(img.party_offline, img.button_kick_out, offset_x=85, offset_y=-38, similarity=similarity)
        elif utils.is_found(img.party_offline2):
            print("Tap img.party_offline2")
            utils.tap_offset_until_found(img.party_offline2, img.button_kick_out, offset_x=85, offset_y=-38, similarity=similarity)
        elif utils.is_found(img.party_offline3):
            print("Tap img.party_offline3")
            utils.tap_offset_until_found(img.party_offline3, img.button_kick_out, offset_x=85, offset_y=-38, similarity=similarity)
        elif utils.is_found(img.party_die_afk):
            print("Tap img.party_die_afk")
            utils.tap_offset_until_found(img.party_die_afk, img.button_kick_out, offset_x=85, offset_y=-38, similarity=similarity)
        # elif utils.is_found(img.party_die_afk2):
        #     print("Tap img.party_die_afk2")
        #     utils.tap_offset_until_found(img.party_die_afk2, img.button_kick_out, offset_x=85, offset_y=-38, similarity=similarity)
        utils.wait_and_tap(img.button_kick_out)
        utils.wait_and_tap(img.button_confirm)


def party_checking():
    if utils.is_found(img.party_number_5):
        utils.tap_until_found(img.party_number_5, img.party_title)
        if utils.is_found(img.party_away):
            utils.tap_until_found(img.party_away, img.button_kick_out)
            utils.tap_until_found(img.button_kick_out, img.button_confirm)
        close_any_panel()


def element_convert(element=None):
    open_bag()
    utils.tap_until_found(img.weapon7, img.button_more, delay=3)
    utils.tap_until_found(img.button_more, img.button_element, delay=2)
    utils.tap_until_found(img.button_element, img.converter_page, delay=2)

    element_select(element)
    close_any_panel()


def element_select(element):
    utils.tap_until_found(img.converter_dropdown_button, img.converter_dropdown_disable, delay=1)
    if element == const.fire:
        utils.wait_for_image(img.converter_dropdown_water_icon)
        utils.tap_until_notfound(img.converter_dropdown_water_icon, img.converter_water_active)
    elif element == const.wind:
        utils.wait_for_image(img.converter_dropdown_earth_icon)
        utils.tap_until_notfound(img.converter_dropdown_earth_icon, img.converter_earth_active)
    elif element == const.water:
        utils.wait_for_image(img.converter_dropdown_wind_icon)
        utils.tap_until_notfound(img.converter_dropdown_wind_icon, img.converter_wind_active)
    elif element == const.earth or element == const.shadow or element == const.undead:
        utils.wait_for_image(img.converter_dropdown_fire_icon)
        utils.tap_until_notfound(img.converter_dropdown_fire_icon, img.converter_fire_active)
    else:
        utils.tap_until_found(img.converter_dropdown_disable, img.converter_neutral_active)


def element_recharge(element=None):
    if utils.is_found(img.converter_page):
        if element == const.fire:
            utils.execute_until_valid_state_with_timeout(10, 1, recharge_loop, img.converter_recharge_water)
        elif element == const.wind:
            utils.execute_until_valid_state_with_timeout(10, 1, recharge_loop, img.converter_recharge_earth)
        elif element == const.water:
            utils.execute_until_valid_state_with_timeout(10, 1, recharge_loop, img.converter_recharge_wind)
        elif element == const.earth:
            utils.execute_until_valid_state_with_timeout(10, 1, recharge_loop, img.converter_recharge_fire)
            

def recharge_loop(element):
    utils.tap_if_found(element)
    utils.tap_until_found(img.button_recharge, img.converter_recharge_select_button, timeout=2)
    if utils.is_found(img.converter_recharge_select_button):
        for _ in range(0, 5):
            utils.tap_if_found(img.converter_recharge_select_button)
            func.wait(0.5)
        utils.tap_until_notfound(img.button_recharge_inactive, img.converter_recharge_select_button)
        element_select(element)
        return True
    return False


def wing():
    utils.tap_any_offset(const.menu_bags, offset_y=100)
    utils.tap_any_offset(const.menu_bags, offset_y=100)


def guild_quest_aid():
    if utils.is_found(img.chat_guild_icon):
        func.open_chat(const.chat_guild)

        if utils.is_found(img.button_aid):
            utils.tap_until_found(img.button_aid, img.button_aid_eden)
            utils.tap_until_notfound(img.button_aid_eden, img.button_aid_eden)

        engrave_gemstone()
        func.close_chat()


def engrave_gemstone():
    if utils.is_found_any(const.gemstone_help_graves):
        location = utils.find_most_bottom_coordinate(const.gemstone_help_graves)
        utils.tap_location_until_found(location, img.gemstone_page)
        tap_all_stone()
        if check_cooldown('mygem', 3600):
            utils.tap_until_found(img.gemstone_my_rough_stone, img.gemstone_guild_assist)
            my_rough_stone_engrave()
        close_any_panel()


def my_rough_stone_engrave():
    utils.tap_if_found(img.gemstone_guild_assist)
    utils.wait_until_disappear(img.gemstone_guild_assist, timeout=1)
    if utils.is_found(img.gemstone_guild_assist) and \
        utils.is_found_within_timeout(img.gemstone_my_rough_stone_engraved, timeout=3):
        tap_all_stone()
        set_cooldown('mygem', 999999)


def tap_all_stone():
    locations = utils.find_all_images([img.gemstone_empty, img.gemstone_empty2, img.gemstone_not_empty, img.gemstone_big_empty, img.gemstone_big_not_empty])
    for location in locations:
        utils.tap_location(location)
        func.wait(1)


def open_daily_page_state():
    utils.key_press('h')
    if utils.wait_for_image(img.daily_quest_page, timeout=2) is not None:
        return True
    return False