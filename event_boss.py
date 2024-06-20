import boss
import constanst as const
import func
import utils
import img
import sys
import time


def wing_boss(boss_name, boss_fight_icon, boss_coord_img, wait_time=60):
    func.wait_and_find_party(img.picky_mvp, f'{boss_name}', 'world', wait_time, True)
    boss.boss(fight_timeout=120, timeout=600, boss_fight_icon=boss_fight_icon, boss_coord_img=boss_coord_img, ignore_chat_wing_count=0)


def awakening(boss_name):
    similarity = 0.97
    while True:
        func.close_any_panel()
        func.wait_profile()
        func.create_party_and_invite()
        utils.tap_any_offset(const.menu_guides, offset_x=-420)
        utils.tap_until_found(img.awakening_clash_of_chaos, img.awakening_boss_crash_of_chaos_page)

        func.wait(1)
        count3x3 = utils.count_image_on_screen(img.awakening_boss_3x3)
        if count3x3 == 2:
            print(f'finished 3/3')
            func.close_any_panel()
            break

        while True:
            wait_time = 0
            utils.tap_if_found(img.awakening_boss_hero_challenge)

            if utils.is_found_any([img.awakening_boss_spawned, img.awakening_boss_spawned2], similarity=similarity):
                wait_time = 30
            elif utils.is_found_any([img.awakening_boss_1m_left, img.awakening_boss_1m_left2], similarity=similarity):
                wait_time = 60
            elif utils.is_found_any([img.awakening_boss_2m_left, img.awakening_boss_2m_left2], similarity=similarity):
                wait_time = 120
            elif utils.is_found_any([img.awakening_boss_3m_left, img.awakening_boss_3m_left2], similarity=similarity):
                wait_time = 180

            if wait_time > 0:
                boss_map_coords = None
                go_buttons = utils.find_all_image_with_similarity(img.awakening_boss_go, similarity)
                if boss_name == 'Hellhound' or boss_name == 'Twilight Bringer' or boss_name == 'Fallen Genesis':
                    utils.tap_location(go_buttons[0])
                    boss_map_coords = [img.chat_party_coord_ant_hell1, img.chat_party_coord_ant_hell2, img.chat_party_coord_ant_hell3]
                else:
                    utils.tap_location(go_buttons[1])
                    boss_map_coords = [img.chat_party_coord_payon_cave_1f1, img.chat_party_coord_payon_cave_1f2, img.chat_party_coord_payon_cave_1f3]
                wing_boss(boss_name, boss_map_coords, wait_time)
                break


def christmas():
    similarity = 0.95
    func.close_any_panel()
    func.wait_profile()
    func.create_party_and_invite()
    utils.tap_any_until_found_offset(const.menu_guides, img.christmas_page, offset_x=-430)
    utils.wait_for_image(img.christmas_page)
    utils.wait_for_image(img.christmas_sparkling_tree)
    utils.tap_until_found(img.christmas_sparkling_tree, img.christmas_sparkling_tree_page)

    # check rewards
    utils.tap_until_found(img.christmas_sparkling_tree_rewards, img.christmas_sparkling_tree_rewards_title)
    func.wait(1)
    count_3x3 = utils.count_image_on_screen(img.christmas_sparkling_tree_rewards_3x3)
    if count_3x3 >= 2:
        print(f'count 3/3: {count_3x3}')
        print(f'finished 3/3')
        func.close_any_panel()
        func.send_message("done 3/3 [z1]")
        func.leave_party()
        return False
    utils.tap_until_notfound(img.button_close, img.christmas_sparkling_tree_rewards_title)

    while True:
        wait_time = 0
        utils.tap_if_found(img.christmas_sparkling_tree_personal_point)

        if utils.is_found_any([img.boss_antonio, img.boss_antonio2]):
            wait_time = 1
        elif utils.is_found_any([img.christmas_sparkling_tree_1min], similarity=similarity):
            wait_time = 100
        elif utils.is_found_any([img.christmas_sparkling_tree_2min], similarity=similarity):
            wait_time = 160

        if wait_time > 0:
            if utils.is_found_any([img.boss_antonio, img.boss_antonio2]):
                go_buttons = utils.find_all_image_with_similarity(img.christmas_sparkling_tree_go_button)
                if len(go_buttons) == 2:
                    utils.tap_location(go_buttons[0])
            else:
                utils.tap_until_found(img.christmas_sparkling_tree_go_button, img.christmas_sparkling_tree_go_southeast_payon)
                utils.tap_until_notfound(img.christmas_sparkling_tree_go_southeast_payon, img.christmas_sparkling_tree_go_southeast_payon)

            while True:
                utils.wait_for_image(img.loading, timeout=60)
                utils.wait_until_disappear(img.loading)
                func.open_map()
                if utils.is_found(img.map_southeast_payon):
                    func.close_map()
                    break
                func.close_map()
                
            func.close_any_panel()
            func.create_party_and_invite()
            func.kick_party_member()
            func.request_people_join_message('Antonio')
            coords = [img.chat_party_coord_southeast_payon1, img.chat_party_coord_southeast_payon2, img.chat_party_coord_southeast_payon3]
            wing_boss('Antonio', img.boss_antonio_fight, coords, wait_time)
            func.use_items()
            return True
        else:
            func.wait(1)
    

def christmas_evil_reindeer():
    func.close_any_panel()
    func.close_hidden_menu()
    if boss.boss_wing(boss_type='mini', timeout=10):
        func.wait(5)
    return False

def picky_boss(boss_name):

    ultimate_clash_boss_icon = ''
    coords = []
    boss_fight_icon = ''
    if boss_name == 'Angelic Picky':
        ultimate_clash_boss_icon = img.picky_boss_angelic_picky
        boss_fight_icon = img.boss_angelic_picky_fight
        coords = [img.chat_party_coord_prontera_south1, img.chat_party_coord_prontera_south2]
    elif boss_name == 'Demonic Eggy':
        ultimate_clash_boss_icon = img.picky_boss_demonic_eggy
        boss_fight_icon = img.boss_demonic_eggy_fight
        coords = [img.chat_party_coord_prontera_north1, img.chat_party_coord_prontera_north2, img.chat_party_coord_prontera_north3]

    func.close_any_panel()
    utils.key_press('u')
    utils.wait_for_image(img.picky_boss_ultimate_clash)
    utils.tap_until_found(img.picky_boss_ultimate_clash, img.picky_boss_ultimate_clash_page)
    if utils.is_found(img.picky_boss_ultimate_clash_page):

        if utils.is_found(img.picky_boss_3_3, similarity=0.99):
            func.close_any_panel()
            return False
        
        while True:
            found_image = utils.is_found_any(const.picky_boss_times, similarity=0.99)

            if found_image is not None:
                utils.tap_until_notfound(ultimate_clash_boss_icon, ultimate_clash_boss_icon)
                utils.wait_for_image(img.picky_boss_map)
                if not utils.execute_until_valid_state_with_timeout(150, 1, boss.running_to_boss_map_state, img.picky_boss_map):
                    func.butterfly_wing_morroc()
                    return True

                boss_wait_time = 0
                if found_image == img.picky_boss_1m:
                    boss_wait_time = 60
                elif found_image == img.picky_boss_2m:
                    boss_wait_time = 120
                elif found_image == img.picky_boss_3m:
                    boss_wait_time = 180
                elif found_image == img.picky_boss_19m or found_image == img.picky_boss_20m:
                    boss_wait_time = 0

                boss_wait_time = boss_wait_time - 10
                wing_boss(boss_name, boss_fight_icon, coords, boss_wait_time)
                
                return True
            
            time.sleep(1)
            
            