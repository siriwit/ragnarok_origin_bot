import constanst as const
import img
import func
import preset
import sys
import utils


def start(element=const.earth, level=const.normal):
    func.wait_profile()
    if not utils.is_found_any(const.party_members):
        func.create_and_invite()
        utils.wait_for_image(img.party_number_2, timeout=60)
    preset.againt_monster_card(element=element)
    func.party_finder('NT ' + element + ' normal')
    if func.go_to_event(img.event_nightmare_temple):
        utils.wait_for_image(img.nightmare_temple_page)

        if element == const.earth:
            utils.tap_until_found(img.nightmare_temple_grief_of_hell, img.nightmare_temple_grief_of_hell_active)
        elif element == const.water:
            utils.tap_until_found(img.nightmare_temple_pity_of_sea, img.nightmare_temple_pity_of_sea_active)
        elif element == const.fire:
            utils.tap_until_found(img.nightmare_temple_wrath_of_lava, img.nightmare_temple_wrath_of_lava_active)
            
        if level == const.normal:
            utils.tap_until_found(img.nightmare_temple_level_normal, img.nightmare_temple_level_normal_active)

        utils.wait_and_tap(img.nightmare_temple_enter_fairyland)
        utils.wait_and_tap_any(const.button_starts)
        fight(element)

    sys.exit(0)


def fight(element=None):
    utils.wait_for_image(img.profile, timeout=150)
    func.auto_attack(mode=const.att_all)

    if element == const.fire:
        func.move_right(hold=2)

    while True:
        func.use_items()
        if utils.is_found_any(const.tap_anywheres):
            utils.wait_and_tap_any(const.tap_anywheres, timeout=5)
            func.close_any_panel()
            func.leave_event()
            break
    utils.wait_any_image(const.profiles, timeout=60)
    func.send_message('[z1][z1]')
    func.leave_party()

