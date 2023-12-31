import constanst as const
import cv2 as cv
import datetime
import img
import func
import time
import utils


def use_rune_knight_skill():
    while True:
        
        utils.tap_if_found(img.quests_inactive)

        for _ in range(0, 5):
            if utils.is_found(img.rune_knight_skill_berserk_disabled, similarity=0.99):
                utils.tap_if_found(img.rune_knight_skill_rune_of_faith)
                continue

            if utils.is_found(img.rune_knight_skill_dragon_state, similarity=0.85) and utils.is_found(img.hp_sp_80_percent):
                utils.tap_if_found(img.rune_knight_skill_berserk)

            utils.tap_if_found(img.rune_knight_skill_ignition_break)
            utils.tap_if_found(img.rune_knight_skill_ignition_break2)
            utils.tap_if_found(img.rune_knight_skill_rune_of_courage)
            utils.tap_if_found(img.rune_knight_skill_dragon_breath_fire)

        if not utils.is_found(img.rune_knight_skill_dragon_state):
            utils.tap_if_found(img.rune_knight_skill_provoke)
        break


def butterfly_wing_morroc():
    utils.tap_until_found(img.butterfly_wing, img.city_morroc)
    utils.wait_and_tap(img.city_morroc)
    wait_loading_screen()
    close_any_panel()
    func.wait_profile()
    time.sleep(3)


def wait_loading_screen():
    utils.wait_for_image(img.loading)
    utils.wait_until_disappear(img.loading)


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
    while True:
        if utils.is_found(img.chat_tab_party_active) or utils.is_found(img.chat_tab_party_inactive):
            break
        utils.key_press("enter")
        time.sleep(1)
    if send_to == 'party' and utils.is_found(img.chat_tab_party_inactive):
        utils.tap_image(img.chat_tab_party_inactive)
    elif send_to == 'world' and utils.is_found(img.chat_tab_world_inactive):
        utils.tap_image(img.chat_tab_world_inactive)
    
    time.sleep(1)


def close_chat():
    while True:
        if utils.is_found(img.chat_button_plus):
            utils.tap_until_notfound(img.chat_collapse, img.chat_collapse)
        else:
            break
        time.sleep(1)


def open_map():
    utils.execute_until_invalid_state(5, 1, open_map_state)


def open_map_state():
    utils.key_press('m')
    if utils.wait_for_image(img.wing, timeout=1) is not None:
        return False
    return True


def close_map():
    utils.execute_until_invalid_state(5, 1, close_map_state)


def close_map_state():
    utils.key_press('m')
    if utils.wait_for_image(img.butterfly_wing, timeout=1) is not None:
        return False
    return True


def send_location(send_to='party'):
    open_chat(send_to)
    utils.tap_image(img.chat_button_plus)
    utils.wait_and_tap(img.chat_button_map)
    utils.tap_until_notfound(img.chat_button_send_background, img.chat_button_map)
    utils.wait_and_tap(img.chat_button_send)
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
    while True:
        if not utils.is_found(img.auto_attack_title):
            if utils.tap_any_until_found_offset(const.menu_bags, img.auto_attack_title, offset_x=85, timeout=timeout):
                continue
        if mode == const.boss:
            utils.wait_for_image(img.icon_auto_attack_boss, timeout=1)
            if utils.is_found(img.icon_auto_attack_boss):
                utils.wait_and_tap(img.icon_auto_attack_boss)
            else:
                utils.wait_and_tap(img.auto_attack_allmonster)
        else:
            utils.wait_and_tap(img.auto_attack_allmonster)
        if all_radius:
            utils.tap_if_found(img.auto_attack_all)
        utils.tap_image(img.button_auto_attack_close)
        break

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
        break

def go_to_event(event_image=None):
    func.wait_profile()
    utils.tap_any(const.batterry_savings)
        
    if utils.tap_any_until_found_offset(const.menu_guides, img.event_page, offset_x=-100):
        if event_image != None:
            if utils.is_found(img.event_moonlit_arena):
                utils.scroll_down_util_found(event_image, img.event_moonlit_arena, offset_y=100, timeout=1)
            if not utils.scroll_down_util_found(event_image, img.event_drag_icon, offset_y=200, timeout=10, similarity=0.85):
                utils.scroll_down_util_found(event_image, img.event_drag_icon_inactive, offset_y=200, similarity=0.85)
            # utils.wait_and_tap(event_image, similarity=0.85)
            # if event_image != img.event_boss and event_image != img.event_guild_expedition:
            if event_image not in [img.event_boss, img.event_guild_expedition]:
                utils.tap_until_found(event_image, img.button_go_orange_small)
                utils.wait_and_tap(img.button_go_orange_small)
            else:
                utils.tap_until_notfound(event_image, event_image)
        return True
    else:
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


def close_any_panel(depth=99, timeout=10):
    depth_count = 1
    marked_time_main = time.time()
    while time.time() - marked_time_main < timeout:
        if utils.is_found(img.power_up_icon) or depth_count >= depth:
            break
        
        utils.tap_if_found(img.button_back)
        utils.tap_any(const.button_closes)
        utils.tap_if_found(img.chat_collapse)
        utils.tap_any(const.tap_anywheres)
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


def leave_event():
    utils.wait_and_tap(img.button_escape, timeout=30)
    utils.wait_and_tap(img.button_confirm, timeout=5)
    utils.wait_for_image(img.loading, timeout=5)
    utils.wait_until_disappear(img.loading, timeout=5)


def wait_profile(timeout=10):
    utils.wait_for_image(img.power_up_icon, timeout)


def wait(timeout=10):
    marked_time = time.time()
    while time.time() - marked_time < timeout:
        utils.wait_for_image(img.power_up_icon, timeout=0.5)

def close_hidden_menu():
    func.close_any_panel()
    func.wait_profile()
    if utils.is_found_any(const.menu_guilds):
        utils.tap_offset_until_found(img.menu_bag, img.butterfly_wing, offset_x=180)

def open_bag():
    utils.tap_until_found(img.menu_bag, img.backpack_title)


def open_hidden_menu():
    if not utils.is_found_any(const.menu_guilds):
        utils.tap_offset_until_found(img.menu_bag, img.menu_album, offset_x=180)


def close_debug_window():
    cv.destroyAllWindows()


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
