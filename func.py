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
    utils.wait_and_tap('images/butterfly_wing.png')
    utils.wait_and_tap('images/city_morroc.png')

def send_message(message, send_to='party'):
    open_chat(send_to)
    utils.type(message)
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
    
    if utils.is_found(img.chat_tap_to_type):
        utils.tap_image(img.chat_tap_to_type)
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


def find_boss_party(boss_name, send_message_to):
    message = boss_name + ' ' + find_remaining_party_number() + ' auto join'
    if not utils.is_found(img.party_number_5):
        send_message(message, send_message_to)


def wait_and_find_party(boss_coming_icon, boss_name, send_to, timeout=180, is_icon_apprear=True):
    print("wait_and_find_party with is_icon_apprear=" + str(is_icon_apprear) + ", timeout=" + str(timeout))
    marked_time = time.time()
    diff_time = time.time() - marked_time
    last_sent_time = time.time()
    while diff_time < timeout:
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
    if utils.is_found(img.party_number_2):
        return '-3'
    elif utils.is_found(img.party_number_3):
        return '-2'
    elif utils.is_found(img.party_number_4):
        return '-1'
    return ''

        
def auto_attack():
    while True:
        if not utils.is_found(img.auto_attack_title):
            utils.wait_and_tap(img.icon_auto_attack)
            continue
        utils.wait_for_image(img.icon_auto_attack_boss, timeout=1)
        if utils.is_found(img.icon_auto_attack_boss):
            utils.wait_and_tap(img.icon_auto_attack_boss)
        else:
            utils.wait_and_tap(img.auto_attack_allmonster)
        utils.tap_image(img.button_auto_attack_close)
        break

def use_items():
    while True:
        if utils.is_found(img.item_button_use):
            utils.tap_image(img.item_button_use)
            continue
        elif utils.is_found(img.button_back):
            utils.tap_image(img.button_back)
            continue
        elif utils.is_found(img.button_receive):
            utils.tap_image(img.button_receive)
            continue
        elif utils.is_found(img.button_submit):
            utils.tap_image(img.button_submit)
            continue
        break

def go_to_event():
    utils.tap_any(const.event_menus)
    utils.wait_for_image(img.event_side_menu, timeout=2)
    if utils.is_found(img.event_side_menu):
        return True
    else:
        return False