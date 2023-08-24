import constanst as const
import img
import sys
import time
import utils


def daily():
    farm()


def farm():
    change_skill_preset('farm')
    change_skill_auto('farm')
    change_item_preset('farm')
    pet_selector()
    attack_preset()
    sys.exit(0)


def boss():
    change_skill_preset('farm')
    change_skill_auto('boss')
    change_item_preset('farm')
    pet_selector()
    attack_preset()
    sys.exit(0)


def tank():
    change_skill_preset('tank')
    change_skill_auto('tank')
    change_item_preset('tank')
    pet_selector()
    attack_preset()
    sys.exit(0)


def pvp():
    change_skill_preset('tank')
    change_skill_auto('tank')
    change_item_preset('tank')
    pet_selector()
    attack_preset()
    againt_monster_card(tribe=const.human, element=const.neutral, size=const.medium)


def change_preset(preset):
    change_skill_preset(preset)
    change_skill_auto(preset)
    change_item_preset(preset)
    pet_selector()
    attack_preset()
    change_card()
    sys.exit(0)


def change_skill_preset(preset='farm'):
    utils.wait_for_image(img.profile)
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
        utils.wait_for_image(img.profile)
        utils.tap_image(img.preset_peco)


def change_item_preset(preset='farm'):
    utils.wait_for_image(img.profile)
    utils.key_press('b')
    utils.wait_for_image(img.preset_backpack, timeout=1)
    if utils.is_found(img.preset_backpack):
        utils.tap_image(img.preset_item_dropdown)
        if preset == 'farm':
            utils.wait_and_tap(img.preset_farm)
        elif preset == 'tank':
            utils.wait_and_tap(img.preset_tank)
        utils.tap_image(img.button_close)


def pet_selector():
    utils.wait_for_image(img.profile)
    utils.tap_any(const.preset_pet_expands)
    utils.tap_image(img.pet_icon_earthlord)


def change_skill_auto(preset='farm'):
    utils.wait_for_image(img.profile)
    utils.tap_image(img.menu_skill)
    utils.wait_and_tap_any(const.preset_settings)
    utils.wait_and_tap(img.preset_auto_settings)
    utils.scroll_down_util_found(img.preset_skill_touse_shield_reflect, img.preset_skill_drag_icon, offset_y=100)
    if preset == 'boss':
        if not utils.is_found(img.preset_skill_rapid_shield):
            if utils.is_found(img.preset_skill_shield_boomerang):
                utils.drag_and_drop_image(img.preset_skill_touse_rapid_shield, img.preset_skill_shield_boomerang)
            else:
                utils.drag_and_drop_image(img.preset_skill_touse_rapid_shield, img.preset_skill_empty_slot)
        if not utils.is_found(img.preset_skill_shield_reflect):
            utils.drag_and_drop_image(img.preset_skill_touse_shield_reflect, img.preset_skill_empty_slot)
        if not utils.is_found(img.preset_skill_provoke):
            utils.drag_and_drop_image(img.preset_skill_touse_provoke, img.preset_skill_empty_slot)
    if preset == const.time_anomaly:
        if not utils.is_found(img.preset_skill_rapid_shield):
            if utils.is_found(img.preset_skill_shield_boomerang):
                utils.drag_and_drop_image(img.preset_skill_touse_rapid_shield, img.preset_skill_shield_boomerang)
            else:
                utils.drag_and_drop_image(img.preset_skill_touse_rapid_shield, img.preset_skill_empty_slot)
        if utils.is_found(img.preset_skill_shield_reflect):
            utils.drag_and_drop_image(img.preset_skill_shield_reflect, img.preset_skill_manual)
        if utils.is_found(img.preset_skill_provoke):
            utils.drag_and_drop_image(img.preset_skill_provoke, img.preset_skill_manual)
    elif preset == 'farm':
        if not utils.is_found(img.preset_skill_shield_boomerang):
            if utils.is_found(img.preset_skill_rapid_shield):
                utils.drag_and_drop_image(img.preset_skill_touse_shield_boomerang, img.preset_skill_rapid_shield)
            else:
                utils.drag_and_drop_image(img.preset_skill_touse_shield_boomerang, img.preset_skill_empty_slot)
        if utils.is_found(img.preset_skill_shield_reflect):
            utils.drag_and_drop_image(img.preset_skill_shield_reflect, img.preset_skill_manual)
        if utils.is_found(img.preset_skill_provoke):
            utils.drag_and_drop_image(img.preset_skill_provoke, img.preset_skill_manual)
    elif preset == 'tank':
        if not utils.is_found(img.preset_skill_shield_boomerang):
            utils.drag_and_drop_image(img.preset_skill_touse_shield_boomerang, img.preset_skill_empty_slot)
        if not utils.is_found(img.preset_skill_auto_guard):
            utils.drag_and_drop_image(img.preset_skill_touse_auto_guard, img.preset_skill_empty_slot)
        if not utils.is_found(img.preset_skill_endure):
            utils.drag_and_drop_image(img.preset_skill_touse_endure, img.preset_skill_empty_slot)
        if not utils.is_found(img.preset_skill_providence):
            utils.drag_and_drop_image(img.preset_skill_touse_providence, img.preset_skill_empty_slot)
        if not utils.is_found(img.preset_skill_provoke):
            utils.drag_and_drop_image(img.preset_skill_touse_provoke, img.preset_skill_empty_slot)
        if not utils.is_found(img.preset_skill_shield_reflect):
            utils.drag_and_drop_image(img.preset_skill_touse_shield_reflect, img.preset_skill_empty_slot)
    utils.tap_image(img.button_close_skill)
    utils.wait_for_image(img.profile)


def attack_preset():
    utils.wait_for_image(img.profile)
    utils.tap_image(img.icon_auto_attack)
    utils.tap_if_found(img.auto_attack_all)
    utils.tap_image(img.button_auto_attack_close)


def open_change_card_page():
    utils.wait_for_image(img.profile)
    utils.key_press('b')
    utils.wait_and_tap(img.weapon4)
    utils.wait_and_tap(img.button_more)
    utils.wait_and_tap(img.button_card)


def close_card_page(expected_depth=2):
    current_depth = 0
    while current_depth < expected_depth:
        if utils.is_found(img.card_page) or utils.is_found(img.card_select_a_card_title):
            utils.key_press('esc')
            current_depth += 1
            time.sleep(1)
            continue
        break

def change_card(preset=None):
    open_change_card_page()
    card_weapon_preset(preset)
    card_shield_preset(preset)
    card_armor(preset)
    card_cloak_preset(preset)
    close_card_page()


def againt_monster_card(tribe='', element='', size=''):
    open_change_card_page()
    card_weapon_preset(tribe, element, size)
    card_shield_preset(tribe)
    card_armor(tribe, element)
    card_cloak_preset(element)
    close_card_page()


def card_cloak_preset(element=None):
    utils.wait_and_tap(img.card_cloak)

    if element == const.earth or element == const.fire:
        card_objects = [card_change_object(img.card_hode_current, img.card_hode_touse),
                        card_change_object(img.card_jakk_current, img.card_jakk_touse)]
    elif element == const.water or element == const.wind:
        card_objects = [card_change_object(img.card_marse_current, img.card_marse_touse),
                        card_change_object(img.card_dustiness_current, img.card_dustiness_touse)]
    elif element == const.shadow or element == const.undead:
        card_objects = [card_change_object(img.card_isis_current, img.card_isis_touse),
                        card_change_object(img.card_orc_zombie_current, img.card_orc_zombie_touse)]
    elif element == const.neutral:
        card_objects = [card_change_object(img.card_orc_baby_current, img.card_orc_baby_touse),
                        card_change_object(img.card_jakk_current, img.card_jakk_touse)]
    else:
        card_objects = [card_change_object(img.card_isis_current, img.card_isis_touse),
                        card_change_object(img.card_orc_zombie_current, img.card_orc_zombie_touse)]
    
    if len(card_objects) > 0:
        card_edges = [img.card_edge_cloak1, img.card_edge_cloak2]
        card_change(card_edges, card_objects)


def card_armor(tribe=None, element=None):
    utils.wait_and_tap(img.card_armor)
    if tribe == const.human:
        card_objects = [card_change_object(img.card_sasquatch_current, img.card_sasquatch_touse)]
    elif element == const.earth:
        card_objects = [card_change_object(img.card_sandman_current, img.card_sandman_touse)]
    elif element == const.fire:
        card_objects = [card_change_object(img.card_pasana_current, img.card_pasana_touse)]
    elif element == const.water:
        card_objects = [card_change_object(img.card_swordfish_current, img.card_swordfish_touse)]
    elif element == const.wind:
        card_objects = [card_change_object(img.card_dokebi_current, img.card_dokebi_touse)]
    else:
        card_objects = [card_change_object(img.card_argiope_current, img.card_argiope_touse)]
        
    if len(card_objects) > 0:
        card_edges = [img.card_edge_armor1, img.card_edge_armor2]
        card_change(card_edges, card_objects)


def card_shield_preset(tribe=None):
    utils.wait_and_tap(img.card_shield)

    if tribe == const.human:
        card_objects = [card_change_object(img.card_tirfing_current, img.card_tirfing_touse)]
    else:
        card_objects = [card_change_object(img.card_alice_current, img.card_alice_touse)]
        
    if len(card_objects) > 0:
        card_edges = [img.card_edge_shield1, img.card_edge_shield2]
        card_change(card_edges, card_objects)


def card_weapon_preset(tribe='', element='', size=''):
    utils.wait_and_tap(img.card_weapon)
    card_objects = []
    if size == const.medium:
        card_objects = [card_change_object(img.card_skeleton_worker_current, img.card_skeleton_worker_touse),
                     card_change_object(img.card_skeleton_worker_current, img.card_skeleton_worker_touse)]
    elif element == const.fire:
        card_objects = [card_change_object(img.card_vadon_current, img.card_vadon_touse),
                     card_change_object(img.card_vadon_current, img.card_vadon_touse)]
    elif element == const.wind:
        card_objects = [card_change_object(img.card_mandragora_current, img.card_mandragora_touse),
                     card_change_object(img.card_mandragora_current, img.card_mandragora_touse)]
    elif element == const.water:
        card_objects = [card_change_object(img.card_drainliar_current, img.card_drainliar_touse),
                     card_change_object(img.card_drainliar_current, img.card_drainliar_touse)]
    elif tribe == const.demon:
        card_objects = [card_change_object(img.card_strouf_current, img.card_strouf_touse),
                     card_change_object(img.card_strouf_current, img.card_strouf_touse)]
    elif tribe == const.brute:
        card_objects = [card_change_object(img.card_goblin_current, img.card_goblin_touse),
                     card_change_object(img.card_goblin_current, img.card_goblin_touse)]
    elif tribe == const.formless:
        card_objects = [card_change_object(img.card_peco_egg_current, img.card_peco_egg_touse),
                     card_change_object(img.card_peco_egg_current, img.card_peco_egg_touse)]
    else:
        card_objects = [card_change_object(img.card_skeleton_worker_current, img.card_skeleton_worker_touse),
                     card_change_object(img.card_skeleton_worker_current, img.card_skeleton_worker_touse)]
    
    if len(card_objects) > 0:
        card_edges = [img.card_edge_weapon1, img.card_edge_weapon2]
        card_change(card_edges, card_objects)


def card_change_object(selected_current_card, to_be_selected_card):
    card_object = {}
    card_object['selected_current_card'] = selected_current_card
    card_object['to_be_selected_card'] = to_be_selected_card
    return card_object


def card_change(card_edges, card_objects):
    utils.wait_until_found_all_images(card_edges, len(card_objects), timeout=30)
    card_edges = utils.find_all_images(card_edges)
    similarity = 0.98
    index = 0
    for card_edge in card_edges:
        card_object = card_objects[index]
        utils.tap_location(card_edge)
        utils.wait_for_image(img.card_select_a_card_title, timeout=1)
        time.sleep(0.5)
        if not utils.is_found(card_object['selected_current_card']):
            utils.scroll_down_util_found(card_object['to_be_selected_card'], img.card_drag_icon, offset_y=200, similarity=similarity)
            utils.wait_and_tap(card_object['to_be_selected_card'], similarity=similarity)
            utils.wait_and_tap(img.button_change)
            utils.wait_and_tap(img.button_receive)
            utils.wait_for_image(img.card_select_a_card_title, timeout=1)
        else:
            close_card_page(expected_depth=1)
        time.sleep(0.5)
        index += 1