import constanst as const
import img
import func
import sys
import time
import utils


def daily():
    farm()


def farm():
    func.close_hidden_menu()
    # change_skill_preset(const.farm)
    change_skill_auto(const.farm)
    # change_item_preset(const.farm)
    pet_selector()
    attack_preset()


def boss():
    func.close_hidden_menu()
    # change_skill_preset(const.farm)
    change_skill_auto(const.boss)
    # change_item_preset(const.farm)
    pet_selector(img.pet_icon_sohee)
    attack_preset()


def tank():
    func.close_hidden_menu()
    # change_skill_preset(const.tank)
    # change_skill_auto(const.tank)
    # change_item_preset(const.tank)
    pet_selector()
    attack_preset()


def pvp():
    # change_skill_preset(const.tank)
    change_skill_auto(const.farm)
    # change_item_preset(const.tank)
    pet_selector(img.pet_icon_sohee)
    attack_preset()
    againt_monster_card(tribe=const.human, element=const.neutral, size=const.medium)


def change_preset(preset):
    # change_skill_preset(preset)
    # change_skill_auto(preset)
    # change_item_preset(preset)
    pet_selector()
    attack_preset()
    change_card()
    sys.exit(0)


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
    if not utils.is_found(pet):
        utils.tap_any_offset(const.pets, offset_x=-75)
        most_left_coordinate = utils.find_most_left_coordinate(const.pets)
        utils.tap_image(pet)
        time.sleep(0.5)
        utils.tap_location(most_left_coordinate, offset_x=-75)


def change_skill_auto(preset=None):
    func.wait_profile()
    utils.tap_any_until_found_offset(const.menu_guides, img.preset_skill, offset_x=100, offset_y=-50)
    utils.wait_and_tap(img.preset_skill)
    utils.tap_image_offset(img.preset_tab_skill, offset_y=120)

    utils.wait_and_tap(img.preset_auto_settings)
    
    # if preset == const.boss:
    #     ensure_use_attack_skill(img.preset_skill_rapid_shield, img.preset_skill_touse_rapid_shield, img.preset_skill_shield_boomerang)
    #     ensure_use_support_skill(img.preset_skill_shield_reflect, img.preset_skill_touse_shield_reflect)
    #     ensure_use_support_skill(img.preset_skill_provoke, img.preset_skill_touse_provoke)
    # if preset == const.time_anomaly:
    #     ensure_use_attack_skill(img.preset_skill_rapid_shield, img.preset_skill_touse_rapid_shield, img.preset_skill_shield_boomerang)
    #     dismiss_skill(img.preset_skill_shield_reflect)
    #     dismiss_skill(img.preset_skill_provoke)
    # if preset == const.ygg:
    #     ensure_use_attack_skill(img.preset_skill_shield_boomerang, img.preset_skill_touse_shield_boomerang, img.preset_skill_rapid_shield)
    #     ensure_use_support_skill(img.preset_skill_shield_reflect, img.preset_skill_touse_shield_reflect)
    #     ensure_use_support_skill(img.preset_skill_provoke, img.preset_skill_touse_provoke)
    if preset == const.boss or preset == const.ygg:
        # ensure_use_support_skill(img.preset_skill_normal_attack, img.preset_skill_touse_normal_attack)
        utils.scroll_down_util_found(img.preset_skill_touse_provoke, img.preset_skill_drag_icon, offset_y=200)
        ensure_replace_skill(img.preset_skill_provoke, img.preset_skill_touse_provoke, img.preset_skill_providence)
        ensure_use_support_skill(img.preset_skill_shield_reflect, img.preset_skill_touse_shield_reflect)
        ensure_use_support_skill(img.preset_skill_spear_quicken, img.preset_skill_touse_spear_quicken)
        ensure_use_support_skill(img.preset_skill_auto_guard, img.preset_skill_touse_auto_guard)
        ensure_use_support_skill(img.preset_skill_martyr, img.preset_skill_touse_martyr)
    else:
        # ensure_use_support_skill(img.preset_skill_normal_attack, img.preset_skill_touse_normal_attack)
        utils.scroll_down_util_found(img.preset_skill_touse_provoke, img.preset_skill_drag_icon, offset_y=200)
        ensure_replace_skill(img.preset_skill_providence, img.preset_skill_touse_providence, img.preset_skill_provoke)
        ensure_use_support_skill(img.preset_skill_shield_reflect, img.preset_skill_touse_shield_reflect)
        ensure_use_support_skill(img.preset_skill_spear_quicken, img.preset_skill_touse_spear_quicken)
        ensure_use_support_skill(img.preset_skill_auto_guard, img.preset_skill_touse_auto_guard)
        ensure_use_support_skill(img.preset_skill_martyr, img.preset_skill_touse_martyr)
        
    utils.tap_image(img.button_close_skill)
    func.wait_profile()


def ensure_replace_skill(ensure_skill, ensure_touse_skill, possible_used_skill):
    if not utils.is_found(ensure_skill):
        if utils.is_found(possible_used_skill, similarity=0.95):
            utils.drag_and_drop_image(ensure_touse_skill, possible_used_skill)
        else:
            utils.drag_and_drop_image(ensure_touse_skill, img.preset_skill_empty_slot)


def ensure_use_support_skill(ensure_skill, ensure_touse_skill):
    if not utils.is_found(ensure_skill):
        utils.drag_and_drop_image(ensure_touse_skill, img.preset_skill_empty_slot)


def dismiss_skill(tobe_dismiss):
    if utils.is_found(tobe_dismiss):
        utils.drag_and_drop_image(tobe_dismiss, img.preset_skill_manual)


def attack_preset():
    func.wait_profile()
    utils.tap_offset_until_found(img.menu_bag, img.auto_attack_title, offset_x=85)
    utils.tap_if_found(img.auto_attack_all)
    utils.tap_image(img.button_auto_attack_close)


def open_change_card_page():
    func.wait_profile()
    func.open_bag()
    utils.wait_and_tap(img.weapon5)
    utils.wait_and_tap(img.button_more)
    utils.wait_and_tap(img.button_card)


def change_card(preset=None):
    open_change_card_page()
    # card_weapon_preset(preset)
    card_shield_preset(preset)
    card_armor(preset)
    card_cloak_preset(preset)
    func.close_any_panel()


def againt_monster_card(tribe='', element='', size=''):
    open_change_card_page()
    # card_weapon_preset(tribe, element, size)
    card_shield_preset(tribe)
    card_armor(tribe, element)
    card_cloak_preset(element)
    func.close_any_panel()


def card_cloak_preset(element=None):
    utils.wait_and_tap_any([img.card_cloak, img.card_cloak2, img.card_cloak3])

    if element == const.earth:
        card_objects = [card_change_object(img.card_hode, img.card_hode_current, img.card_hode_touse),
                        card_change_object(img.card_hode, img.card_hode_current, img.card_hode_touse)]
    elif element == const.fire:
        card_objects = [card_change_object(img.card_jakk, img.card_jakk_current, img.card_jakk_touse),
                        card_change_object(img.card_jakk, img.card_jakk_current, img.card_jakk_touse)]
    elif element == const.water:
        card_objects = [card_change_object(img.card_marse, img.card_marse_current, img.card_marse_touse),
                        card_change_object(img.card_marse, img.card_marse_current, img.card_marse_touse)]
    elif element == const.wind:
        card_objects = [card_change_object(img.card_dustiness, img.card_dustiness_current, img.card_dustiness_touse),
                        card_change_object(img.card_dustiness, img.card_dustiness_current, img.card_dustiness_touse)]
    elif element == const.shadow:
        card_objects = [card_change_object(img.card_isis, img.card_isis_current, img.card_isis_touse),
                        card_change_object(img.card_isis, img.card_isis_current, img.card_isis_touse)]
    elif element == const.undead:
        card_objects = [card_change_object(img.card_orc_zombie, img.card_orc_zombie_current, img.card_orc_zombie_touse),
                        card_change_object(img.card_orc_zombie, img.card_orc_zombie_current, img.card_orc_zombie_touse)]
    elif element == const.poison:
        card_objects = [card_change_object(img.card_myst, img.card_myst_current, img.card_myst_touse),
                        card_change_object(img.card_myst, img.card_myst_current, img.card_myst_touse)]
    elif element == const.neutral:
        card_objects = [card_change_object(img.card_orc_baby, img.card_orc_baby_current, img.card_orc_baby_touse),
                        card_change_object(img.card_jakk, img.card_jakk_current, img.card_jakk_touse)]
    else:
        card_objects = [card_change_object(img.card_isis, img.card_isis_current, img.card_isis_touse),
                        card_change_object(img.card_orc_zombie, img.card_orc_zombie_current, img.card_orc_zombie_touse)]
    
    if len(card_objects) > 0:
        card_edges = [img.card_edge_cloak1, img.card_edge_cloak2]
        card_change(card_edges, card_objects)


def card_armor(tribe=None, element=None):
    utils.wait_and_tap(img.card_armor)
    if tribe == const.human:
        card_objects = [card_change_object(img.card_sasquatch, img.card_sasquatch_current, img.card_sasquatch_touse)]
    elif element == const.earth:
        card_objects = [card_change_object(img.card_sandman, img.card_sandman_current, img.card_sandman_touse)]
    elif element == const.fire:
        card_objects = [card_change_object(img.card_pasana, img.card_pasana_current, img.card_pasana_touse)]
    elif element == const.water:
        card_objects = [card_change_object(img.card_swordfish, img.card_swordfish_current, img.card_swordfish_touse)]
    elif element == const.wind:
        card_objects = [card_change_object(img.card_dokebi, img.card_dokebi_current, img.card_dokebi_touse)]
    else:
        card_objects = [card_change_object(img.card_argiope, img.card_argiope_current, img.card_argiope_touse)]
        
    if len(card_objects) > 0:
        card_edges = [img.card_edge_armor1, img.card_edge_armor2]
        card_change(card_edges, card_objects)


def card_shield_preset(tribe=None):
    utils.wait_and_tap(img.card_shield)

    if tribe == const.human:
        card_objects = [card_change_object(img.card_tirfing, img.card_tirfing_current, img.card_tirfing_touse)]
    else:
        card_objects = [card_change_object(img.card_alice, img.card_alice_current, img.card_alice_touse)]
        
    if len(card_objects) > 0:
        card_edges = [img.card_edge_shield1, img.card_edge_shield2]
        card_change(card_edges, card_objects)


def card_weapon_preset(tribe='', element='', size=''):
    utils.wait_and_tap(img.card_weapon)
    card_objects = []
    if size == const.medium:
        card_objects = [card_change_object(img.card_skeleton_worker, img.card_skeleton_worker_current, img.card_skeleton_worker_touse),
                     card_change_object(img.card_skeleton_worker, img.card_skeleton_worker_current, img.card_skeleton_worker_touse)]
    elif size == const.large:
        card_objects = [card_change_object(img.card_minorous, img.card_minorous_current, img.card_minorous_touse),
                     card_change_object(img.card_minorous, img.card_minorous_current, img.card_minorous_touse)]
    elif element == const.fire:
        card_objects = [card_change_object(img.card_vadon, img.card_vadon_current, img.card_vadon_touse),
                     card_change_object(img.card_vadon, img.card_vadon_current, img.card_vadon_touse)]
    elif element == const.wind:
        card_objects = [card_change_object(img.card_mandragora, img.card_mandragora_current, img.card_mandragora_touse),
                     card_change_object(img.card_mandragora, img.card_mandragora_current, img.card_mandragora_touse)]
    elif element == const.water:
        card_objects = [card_change_object(img.card_drainliar, img.card_drainliar_current, img.card_drainliar_touse),
                     card_change_object(img.card_drainliar, img.card_drainliar_current, img.card_drainliar_touse)]
    elif tribe == const.demon:
        card_objects = [card_change_object(img.card_strouf, img.card_strouf_current, img.card_strouf_touse),
                     card_change_object(img.card_strouf, img.card_strouf_current, img.card_strouf_touse)]
    elif tribe == const.brute:
        card_objects = [card_change_object(img.card_goblin, img.card_goblin_current, img.card_goblin_touse),
                     card_change_object(img.card_goblin, img.card_goblin_current, img.card_goblin_touse)]
    elif tribe == const.formless:
        card_objects = [card_change_object(img.card_peco_egg, img.card_peco_egg_current, img.card_peco_egg_touse),
                     card_change_object(img.card_peco_egg, img.card_peco_egg_current, img.card_peco_egg_touse)]
    else:
        card_objects = [card_change_object(img.card_skeleton_worker, img.card_skeleton_worker_current, img.card_skeleton_worker_touse),
                     card_change_object(img.card_skeleton_worker, img.card_skeleton_worker_current, img.card_skeleton_worker_touse)]
    
    if len(card_objects) > 0:
        card_edges = [img.card_edge_weapon1, img.card_edge_weapon2]
        card_change(card_edges, card_objects)


def card_change_object(used_card, selected_current_card, to_be_selected_card):
    card_object = {}
    card_object['used_card'] = used_card
    card_object['selected_current_card'] = selected_current_card
    card_object['to_be_selected_card'] = to_be_selected_card
    return card_object


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
        utils.tap_location(card_edge)
        utils.wait_for_image(img.card_select_a_card_title, timeout=1)
        if not utils.is_found(card_object['selected_current_card'], similarity=similarity):
            if utils.scroll_down_util_found(card_object['to_be_selected_card'], img.card_drag_icon, offset_y=200, similarity=similarity, timeout=3):
                utils.wait_and_tap(card_object['to_be_selected_card'], similarity=similarity)
                utils.wait_and_tap(img.button_change)
                utils.wait_and_tap(img.button_receive)
                utils.wait_for_image(img.card_select_a_card_title, timeout=1)
            else:
                utils.tap_any_until_found(const.button_closes, img.card_select_a_card_title)
        else:
            utils.tap_any_until_found(const.button_closes, img.card_select_a_card_title)
        time.sleep(0.5)
        index += 1


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