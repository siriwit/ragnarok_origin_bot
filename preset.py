import constanst as const
import configparser
import img
import func
import jj_royal_guard_preset
import jj_rune_knight_preset
import shared_preset
import sys
import time
import utils


config = configparser.ConfigParser()
config_file_path = 'bot.ini'
config.read(config_file_path)
settings = config['SETTINGS']

def daily():
    if settings["preset"] == 'jj_royal_guard':
        farm()
    elif settings["preset"] == 'jj_rune_knight':
        farm()


def farm():
    func.close_hidden_menu()
    if settings["preset"] == 'jj_royal_guard':
        card_deck_preset(img.card_album_decks_preset_rgpve)
        nexus_preset(img.nexus_engine_preset_pve)
        card_preset(img.preset_card_cripve)
        character_preset(1)
        change_skill_auto(const.farm)
        pet_selector()
        attack_preset()
    elif settings["preset"] == 'jj_rune_knight':
        change_skill_auto(const.sword)
        pet_selector()
        attack_preset()


def boss(is_event=False):
    func.close_hidden_menu()
    if settings["preset"] == 'jj_royal_guard':
        card_deck_preset(img.card_album_decks_preset_rgpve)
        card_preset(img.preset_card_cripve)
        nexus_preset(img.nexus_engine_preset_pve)
        character_preset(1)
        if is_event:
            change_skill_auto(const.boss_event)
        else:
            change_skill_auto(const.boss)
        pet_selector(img.pet_icon_genesis)
        attack_preset()
    elif settings["preset"] == 'jj_rune_knight':
        if is_event:
            change_skill_auto(const.boss_event)
        else:
            change_skill_auto(const.boss)
        pet_selector(img.pet_icon_genesis)
        attack_preset()


def tank():
    func.close_hidden_menu()
    if settings["preset"] == 'jj_royal_guard':
        card_deck_preset(img.card_album_decks_preset_rgtank)
        card_preset(img.preset_card_tankpvp)
        nexus_preset(img.nexus_engine_preset_tank)
        character_preset(0)
        pet_selector()
        attack_preset()
    elif settings["preset"] == 'jj_rune_knight':
        pet_selector()
        attack_preset()


def pvp():
    if settings["preset"] == 'jj_royal_guard':
        card_deck_preset(img.card_album_decks_preset_rgtank)
        card_preset(img.preset_card_tankpvp)
        nexus_preset(img.nexus_engine_preset_tank)
        character_preset(0)
        pet_selector(img.pet_icon_genesis)
        attack_preset()
    elif settings["preset"] == 'jj_rune_knight':
        change_skill_auto(const.pvp)
        pet_selector(img.pet_icon_sohee)
        attack_preset()


def eat_food():
    if settings["preset"] == 'jj_royal_guard':
        func.open_bag()
        utils.tap_image_offset(img.button_close, offset_x=100, offset_y=220)
        utils.tap_until_found(img.backpack_seafood_fried_noodles, img.button_use_small_blue)
        utils.tap_image(img.button_use_small_blue)
        func.close_any_panel()
    elif settings["preset"] == 'jj_rune_knight':
        func.open_bag()
        utils.tap_image_offset(img.button_close, offset_x=100, offset_y=220)
        utils.tap_until_found(img.backpack_seafood_fried_noodles, img.button_use_small_blue)
        utils.tap_image(img.button_use_small_blue)
        func.close_any_panel()


def character_preset(char_preset_index=1):
    if utils.tap_until_found(img.jj_profile, img.character_page):
        utils.tap_offset_until_found(img.button_close_trading, img.royalguard_mighty_defender, offset_x=150, offset_y=470)
        edit_buttons = utils.find_all_image_with_similarity(img.character_edit_button)
        if len(edit_buttons) > char_preset_index:
            location = edit_buttons[char_preset_index]
            for _ in range(0, 3):
                utils.tap_location(location, offset_y=70)
                time.sleep(1)
    func.close_any_panel()


def card_preset(preset_name):
    open_change_card_page()
    if preset_name == img.preset_card_cripve and not utils.is_found(img.preset_card_cripve_active):
        utils.tap_until_found(img.preset_card_album_belt, img.preset_card_album_belt_page)
        utils.tap_until_notfound(img.preset_card_cripve, img.preset_card_cripve)
    elif preset_name == img.preset_card_tankpvp and not utils.is_found(img.preset_card_tankpvp_active):
        utils.tap_until_found(img.preset_card_album_belt, img.preset_card_album_belt_page)
        utils.tap_until_notfound(img.preset_card_tankpvp, img.preset_card_tankpvp)
    func.close_any_panel()


def card_deck_preset(preset):
    func.open_menu_guide()
    if utils.tap_until_found(img.guide_card_album, img.card_album_decks):
        utils.tap_until_found(img.card_album_decks, img.card_album_decks_active)
        utils.wait_for_image(img.card_album_decks_preset)
        utils.tap_until_found(img.card_album_decks_preset, preset)
        utils.tap_until_notfound(preset, preset, similarity=0.95)
    func.close_any_panel()


def nexus_preset(preset):
    func.open_hidden_menu()
    if utils.tap_offset_until_found(img.menu_album, img.nexus_engine_page, offset_x=-450, offset_y=-420):
        utils.wait_for_image(img.nexus_engine_preset)
        utils.tap_until_found(img.nexus_engine_preset, preset)
        utils.tap_until_notfound(preset, preset)
    func.close_hidden_menu()


def party():
    if settings["preset"] == 'jj_royal_guard':
        func.create_party_and_invite()
    elif settings["preset"] == 'jj_rune_knight':
        func.create_party_and_invite()


def sigil(preset=const.tank):
    if settings["preset"] == 'jj_royal_guard':
        func.open_hidden_menu()
        open_sigil_page(img.sigil_paladin)
        if preset == const.tank:
            utils.wait_and_tap(img.sigil_preset_tank)
        elif preset == const.farm:
            utils.wait_and_tap(img.sigil_preset_farm)
        elif preset == const.pvp:
            utils.wait_and_tap(img.sigil_preset_pvp)
        func.close_hidden_menu()
    elif settings["preset"] == 'jj_rune_knight':
        func.open_hidden_menu()
        open_sigil_page(img.sigil_rune_knight)
        if preset == const.tank:
            utils.wait_and_tap(img.sigil_preset_tank)
        elif preset == const.farm:
            utils.wait_and_tap(img.sigil_preset_farm)
        elif preset == const.pvp:
            utils.wait_and_tap(img.sigil_preset_pvp)
        func.close_hidden_menu()


def open_sigil_page(waiting_rune):
    utils.wait_for_image(img.menu_album, timeout=2)
    utils.tap_image_offset(img.menu_album, offset_x=-320)
    utils.wait_for_image(waiting_rune)
    utils.wait_and_tap(img.sigil_preset_dropdown)


def change_preset(preset):
    if settings["preset"] == 'jj_royal_guard':
        # change_skill_preset(preset)
        # change_skill_auto(preset)
        # change_item_preset(preset)
        pet_selector()
        attack_preset()
        change_card()
        sys.exit(0)
    elif settings["preset"] == 'jj_rune_knight':
        pet_selector()
        attack_preset()
        change_card()


def change_skill_preset(preset='farm'):
    func.wait_profile()
    utils.tap_image(img.menu_skill)
    utils.wait_for_image(img.preset_skill, timeout=1)
    if utils.is_found(img.preset_skill):
        if preset == 'farm':
            if utils.is_found(img.preset_farm):
                print('farm')
                utils.tap_image(img.button_close_skill)
                return
            utils.tap_image(img.preset_tank)
            utils.wait_and_tap(img.preset_farm)
        elif preset == 'tank':
            if utils.is_found(img.preset_tank):
                print('tank')
                utils.tap_image(img.button_close_skill)
                return
            utils.tap_image(img.preset_farm)
            utils.wait_and_tap(img.preset_tank)
        utils.tap_image(img.button_close_skill)
        func.wait_profile()
        utils.tap_image(img.preset_peco)


def change_item_preset(preset='farm'):
    func.wait_profile()
    utils.key_press('b')
    utils.wait_for_image(img.preset_backpack, timeout=1)
    if utils.is_found(img.preset_backpack):
        utils.tap_image(img.preset_item_dropdown)
        if preset == 'farm':
            utils.wait_and_tap(img.preset_farm)
        elif preset == 'tank':
            utils.wait_and_tap(img.preset_tank)
        utils.tap_image(img.button_close)


def pet_selector(pet=img.pet_icon_earthlord):
    func.wait_profile()
    func.close_hidden_menu()
    if settings["preset"] == 'jj_royal_guard':
        if not utils.is_found(pet):
            utils.tap_any_offset(const.pets, offset_x=-75)
            most_left_coordinate = utils.find_most_left_coordinate(const.pets)
            utils.tap_image(pet)
            time.sleep(0.5)
            utils.tap_location(most_left_coordinate, offset_x=-75)
    elif settings["preset"] == 'jj_rune_knight':
        if not utils.is_found(pet):
            utils.execute_until_valid_state_with_timeout(5, 0.5, expand_pet_state)
            utils.tap_image(pet)
            utils.execute_until_valid_state_with_timeout(5, 0.5, hide_pet_state)


def hide_pet_state():
    try_expand_collepse_pet()
    if utils.count_all_image_on_screen(const.pets) <= 1:
        return True
    return False
        

def expand_pet_state():
    try_expand_collepse_pet()
    if utils.count_all_image_on_screen(const.pets) > 1:
        return True
    return False


def try_expand_collepse_pet():
    most_left_coordinate = utils.find_most_left_coordinate(const.pets)
    utils.tap_location(most_left_coordinate, offset_x=-80)
    time.sleep(0.5)


def change_skill_auto(preset=None):
    if settings["preset"] == 'jj_royal_guard':
        func.wait_profile()
        open_preset_skill()
        jj_royal_guard_preset.change_skill_manual(preset)
        utils.wait_and_tap(img.preset_auto_settings)
        jj_royal_guard_preset.change_skill_auto(preset)
        func.close_any_panel()

    elif settings["preset"] == 'jj_rune_knight':
        func.wait_profile()
        open_preset_skill()
        jj_rune_knight_preset.change_skill_manual(preset)
        utils.wait_and_tap(img.preset_auto_settings)
        jj_rune_knight_preset.change_skill_auto(preset)
        func.close_any_panel()
        func.close_hidden_menu()

def open_preset_skill():
    # sometime the offset need to be 80
    utils.tap_any_until_found_offset(const.menu_guides, img.preset_skill, offset_x=80, offset_y=-80)
    # utils.tap_any_until_found_offset(const.menu_guides, img.preset_skill, offset_x=220, offset_y=-80)
    utils.wait_and_tap(img.preset_skill)
    utils.tap_image_offset(img.preset_tab_skill, offset_y=120)
    utils.wait_for_image(img.preset_settings_drag_your_skill_text)


def dismiss_skill(tobe_dismiss):
    if utils.is_found(tobe_dismiss):
        utils.drag_and_drop_image(tobe_dismiss, img.preset_skill_manual)


def attack_preset():
    func.wait_profile()
    utils.tap_offset_until_found(img.menu_bag, img.auto_attack_title, offset_x=85)
    utils.tap_if_found(img.auto_attack_all)
    utils.tap_image(img.button_auto_attack_close)


def open_change_card_page():
    func.close_any_panel(img.menu_bag)
    func.open_bag()
    if utils.wait_and_tap(img.weapon7) is not None and \
        utils.wait_for_image(img.button_more) is not None:
        utils.tap_until_found(img.button_more, img.button_card, delay=1)
        utils.tap_until_found(img.button_card, img.card_page, delay=1)
        return True
    return False


def change_card(preset=None):
    if open_change_card_page():
        card_weapon_preset(preset)
        card_shield_preset(preset)
        card_armor(preset)
        card_cloak_preset(preset)
    func.close_any_panel()


def againt_monster_card(tribe='', element='', size='', boss_level=0):
    if open_change_card_page():
        card_weapon_preset(tribe, element, size)
        card_shield_preset(tribe, boss_level)
        card_armor(tribe, element, boss_level)
        card_cloak_preset(tribe, element, boss_level)
    func.close_any_panel()


def card_cloak_preset(tribe=None, element=None, boss_level=0):
    card_edges = [img.card_edge_cloak1, img.card_edge_cloak2]
    if settings["preset"] == 'jj_royal_guard' or settings["preset"] == 'jj_rune_knight':
        utils.tap_any_until_found_any([img.card_cloak, img.card_cloak2, img.card_cloak3], card_edges)
        card_objects = shared_preset.card_cloak(tribe, element, boss_level)
        
    if len(card_objects) > 0:
        card_change(card_edges, card_objects)


def card_armor(tribe=None, element=None, boss_level=0):
    card_edges = [img.card_edge_armor1, img.card_edge_armor2]
    if settings["preset"] == 'jj_royal_guard' or settings["preset"] == 'jj_rune_knight':
        utils.tap_any_until_found_any([img.card_armor], card_edges)
        card_objects = shared_preset.card_armor(tribe, boss_level, element)
            
    if len(card_objects) > 0:
        card_change(card_edges, card_objects)


def card_shield_preset(tribe=None, boss_level=0):
    card_edges = [img.card_edge_shield1, img.card_edge_shield2]
    if settings["preset"] == 'jj_royal_guard' or settings["preset"] == 'jj_rune_knight':
        utils.tap_any_until_found_any([img.card_shield], card_edges)
        card_objects = shared_preset.card_shield(tribe, boss_level)
        
    if len(card_objects) > 0:
        card_change(card_edges, card_objects)


def card_weapon_preset(tribe='', element='', size=''):
    card_edges = [img.card_edge_weapon1, img.card_edge_weapon2]
    if settings["preset"] == 'jj_royal_guard' or settings["preset"] == 'jj_rune_knight':
        utils.tap_any_until_found_any([img.card_weapon], card_edges)
        card_objects = shared_preset.card_weapon(size, element, tribe)
        
    if len(card_objects) > 0:
        card_change(card_edges, card_objects)


def card_change(card_edges, card_objects):
    print(card_objects)

    similarity = 0.97
    index = 0

    utils.wait_until_found_all_images(card_edges, len(card_objects), similarity=similarity, timeout=30)
    if should_skip_change_card(card_objects):
        return

    card_edges = utils.find_all_images(card_edges, similarity)
    print(f"found card_edges: {len(card_edges)} {card_edges}")
    for card_edge in card_edges:
        card_object = card_objects[index]
        utils.tap_location_until_found(card_edge, img.card_select_a_card_title)
        if not utils.is_found(card_object['selected_current_card'], similarity=similarity):
            utils.wait_for_image(card_object['to_be_selected_card'], timeout=3)
            if utils.scroll_down_util_found(card_object['to_be_selected_card'], img.card_drag_icon, offset_y=200, similarity=similarity, timeout=3):
                select_card(card_object, similarity)
                utils.wait_for_image(img.card_page, timeout=1)
            else:
                utils.tap_any_until_found(const.button_closes, img.card_page)
        else:
            utils.tap_any_until_found(const.button_closes, img.card_page)
        index += 1


def select_card(card_object, similarity):
    utils.wait_for_image(card_object['to_be_selected_card'])
    to_be_selected_cards = utils.find_all_images([card_object['to_be_selected_card']], similarity)
    for to_be_selected_card in to_be_selected_cards:
        utils.tap_location(to_be_selected_card)
        if utils.tap_until_notfound(img.button_replace, img.button_replace):
            break


def should_skip_change_card(card_objects):
    cards = extract_property_as_array(card_objects, 'used_card')
    print(cards)
    expected_card_number = len(card_objects)
    actual_card_number = 0
    for card in cards:
        found_number = utils.count_image_on_screen(card)
        print('find ' + card + ' on screen, found: ' + str(found_number))
        actual_card_number += found_number
    print('expected_card_number:' + str(expected_card_number) + ' actual_card_number: ' + str(actual_card_number))
    return expected_card_number == actual_card_number


def extract_property_as_array(objects, property_name):
    result = [str(obj[property_name]) for obj in objects]
    return list(set(result))