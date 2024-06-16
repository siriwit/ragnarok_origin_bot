import boss
import constanst as const
import img
import func
import preset
import utils


def start(name, wing_boss, invite_people, should_att, warp_detect):
    func.create_party_and_invite()
    func.element_convert(const.neutral)
    utils.exit_at_specific_time_or_invalid_state(4, 40, mr_farm, name, 'world', wing_boss, invite_people, should_att, warp_detect)
    func.butterfly_wing_morroc()


def monster(monster, name, invite_people):
    func.create_party_and_invite()
    utils.exit_at_specific_time_or_invalid_state(4, 40, specific_monster_state, monster, name, invite_people, 'party')


def mr_farm(name, send_msg_to, wing_boss, invite_people, should_att, warp_detect):

    if invite_people:
        message = f'MR {name} {func.find_remaining_party_number()}'
        if not utils.is_found(img.party_number_5):
            func.send_message(message, send_to=send_msg_to)
    
    preset.pet_selector(img.pet_icon_dunell)

    if wing_boss and \
    func.check_cooldown(const.mini_boss, 15*60) and \
    boss.boss_wing(boss_type=const.mini_boss, timeout=30):
        func.wait(5)
        func.close_any_panel()
        func.reset_cooldown(const.mini_boss)

    if should_att:
        func.auto_attack(const.att_all, all_radius=False)

    utils.execute_until_invalid_state(240, 1, mr_wait, warp_detect)

    return True


def mr_wait(warp_detect):
    func.ang_pao()
    func.use_items()
    func.close_any_panel()
    func.handle_battle_log(False)
    func.kick_party_member()

    func.guild_quest_aid()

    if warp_detect and utils.is_found_any([img.map_warp1, img.map_warp2]):
        func.wing()
        return False
    return True


def specific_monster_state(monster, name, invite_people, send_msg_to):
    if invite_people:
        message = f'MR {name} {func.find_remaining_party_number()}'
        if not utils.is_found(img.party_number_5):
            func.send_message(message, send_to=send_msg_to)
    
    preset.pet_selector(img.pet_icon_dunell)

    utils.execute_until_invalid_state(240, 1, wing_until_found_monster, monster)

    return True

    
def wing_until_found_monster(monster):
    func.wait(2)

    if utils.is_found(monster):
        count = 5
        while True:
            if utils.is_found(monster):
                count += 5
                func.wait(1)
            
            if count < 0:
                return False

            print(f"count: {count}")
            count -= 1
    return True