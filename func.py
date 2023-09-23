import constanst as const
import img
import time
import utils


def enable_aura():
    if utils.is_found(img.aura_defending_neutral):
            utils.key_press("num1")
            utils.key_press("num1")

def disable_aura():
    if utils.is_found(img.aura_defending_activated):
            utils.key_press("num1")
            utils.key_press("num1")

def butterfly_wing_morroc():
    utils.tap_until_found(img.butterfly_wing, img.city_morroc)
    utils.wait_and_tap(img.city_morroc)
    utils.wait_for_image(img.profile)


def send_message(message, send_to='party'):
    open_chat(send_to)
    if utils.is_found(img.chat_tap_to_type):
        utils.tap_image(img.chat_tap_to_type)
    time.sleep(0.3)
    utils.type(message)
    utils.tap_image(img.send_message_ok)
    utils.tap_image(img.button_send)
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
            utils.key_press("esc")
        else:
            break
        time.sleep(1)


def send_location(send_to='party'):
    open_chat(send_to)
    utils.tap_image(img.chat_button_plus)
    utils.wait_and_tap(img.chat_button_map)
    utils.tap_image(img.chat_button_send_background)
    utils.tap_image(img.chat_button_send)
    close_chat()


def party_finder(message, expected_number=img.party_number_5):
    last_sent_time = time.time() - 20
    while True:
        utils.wait_for_image(img.profile)
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
    message = boss_name + ' ' + find_remaining_party_number() + ' auto join'
    if not utils.is_found(img.party_number_5):
        send_message(message, send_message_to)


def wait_and_find_party(boss_coming_icon, boss_name, send_to, timeout=180, is_icon_apprear=True):
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

        
def auto_attack(mode=const.boss):
    while True:
        if not utils.is_found(img.auto_attack_title):
            utils.tap_offset_until_found(img.menu_bag, img.auto_attack_title, offset_x=85)
            continue
        if mode == const.boss:
            utils.wait_for_image(img.icon_auto_attack_boss, timeout=1)
            if utils.is_found(img.icon_auto_attack_boss):
                utils.wait_and_tap(img.icon_auto_attack_boss)
            else:
                utils.wait_and_tap(img.auto_attack_allmonster)
        else:
            utils.wait_and_tap(img.auto_attack_allmonster)
        utils.tap_image(img.button_auto_attack_close)
        break

def use_items():
    while True:
        if utils.is_found(img.button_confirm):
            utils.tap_image(img.button_confirm)
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
    utils.wait_for_image(img.profile)
    utils.tap_any(const.batterry_savings)
        
    if utils.tap_any_until_found_offset(const.menu_guides, img.event_side_menu, offset_x=-100):
        if event_image != None:
            if not utils.scroll_down_util_found(event_image, img.event_drag_icon, offset_y=200, timeout=10):
                utils.scroll_down_util_found(event_image, img.event_drag_icon_inactive, offset_y=200)
            utils.tap_image(event_image)
            # if event_image != img.event_boss and event_image != img.event_guild_expedition:
            if event_image not in [img.event_boss, img.event_guild_expedition]:
                utils.wait_and_tap(img.button_go_orange_small)
        return True
    else:
        return False
    

def ang_pao():
    while True:
        if utils.is_found(img.ang_pao_red):
            utils.tap_image(img.ang_pao_red, screenshot=True, result_filename=img.angpao_header)
            utils.tap_any(const.pets)
            continue
        elif utils.is_found(img.ang_pao_yellow):
            utils.tap_image(img.ang_pao_yellow, screenshot=True, result_filename=img.angpao_header)
            utils.tap_any(const.pets)
            continue
        break


def leave_party():
    utils.wait_for_image(img.profile)
    utils.tap_any_until_found(const.party_members, img.party_leave_button)
    utils.wait_and_tap(img.party_leave_button)


def close_any_panel():
    while True:
        if utils.is_found(img.profile):
            break
        
        utils.tap_if_found(img.button_back)
        utils.tap_any(const.button_closes)
        time.sleep(1)


def move_left(hold=0.5):
    utils.hold_press('a', timeout=hold)


def move_right(hold=0.5):
    utils.hold_press('d', timeout=hold)


def move_down(hold=0.5):
    utils.hold_press('s', timeout=hold)


def move_up(hold=0.5):
    utils.hold_press('w', timeout=hold)


def get_move_area():
    offset_x = -220
    offset_y = -120
    image_obj = utils.find_image_with_similarity(img.guild)
    center_x, center_y = utils.find_image_center(image_obj)
    return (center_x + offset_x), (center_y + offset_y)


def create_and_invite(friend=img.party_ppinwza, auto_accept=True):
    utils.wait_for_image(img.profile)
    utils.wait_and_tap(img.create_party)
    if auto_accept:
        utils.wait_for_image(img.party_member)
        utils.tap_image_offset(img.party_member, offset_y=120)
        utils.wait_and_tap(img.party_auto_accept)
        utils.tap_image_offset(img.party_request, offset_y=-120)
    utils.wait_and_tap(img.party_tap_to_invite)
    utils.wait_for_image(img.party_friend_tap)
    utils.tap_until_found(img.party_friend_tap, img.party_friend_tap_active)
    utils.wait_for_image(img.party_ppinwza)
    utils.tap_image_offset(friend, offset_x=380, offset_y=50)
    close_any_panel()


def leave_event():
    utils.wait_and_tap(img.button_escape, timeout=5)
    utils.wait_and_tap(img.button_confirm, timeout=5)