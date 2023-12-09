import boss
import constanst as const
import img
import func
import utils


def start(name):
    func.create_party_and_invite()
    utils.exit_at_specific_time(4, 30, mr_farm, name)

def mr_farm(name):
    message = f'MR {name} {func.find_remaining_party_number()}'
    if not utils.is_found(img.party_number_5):
        func.send_message(message, send_to='world')
    utils.execute_until_invalid_state(240, 1, mr_wait)
    if boss.boss_wing(boss_type='mini', timeout=10):
        func.wait(5)
    func.auto_attack(const.att_all)


def mr_wait():
    func.ang_pao()
    func.use_items()
    func.close_any_panel()
    return True

