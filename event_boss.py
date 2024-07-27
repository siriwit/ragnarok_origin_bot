import boss
import constanst as const
import func
import utils
import img
import sys
import time
import preset


def wing_boss(boss_name, boss_fight_icon, boss_coord_img, wait_time=60, butterflywing=True):
    func.wait_and_find_party(img.picky_mvp, f'{boss_name}', 'world', wait_time, True)
    boss.boss(fight_timeout=120, timeout=600, boss_fight_icon=boss_fight_icon, boss_coord_img=boss_coord_img, ignore_chat_wing_count=0, butterflywing=butterflywing)


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

def picky_boss(boss_name, tr=True, butterflywing=True):
    print(f"boss name: {boss_name}, TR?: {tr}, Butterfly Wing: {butterflywing}")
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

        count3x3 = utils.count_image_on_screen(img.picky_boss_3x3)
        tr_mode_3x3_count = 4 if tr else 2
        print(f"3x3 check: {tr_mode_3x3_count} and actual found:{count3x3}")
        if count3x3 >= tr_mode_3x3_count:
            print(f'finished 3/3')
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

                boss_wait_time = boss_wait_time - 15
                wing_boss(boss_name, boss_fight_icon, coords, boss_wait_time, butterflywing)
                
                return True
            
            time.sleep(1)


def sakura(tr=True, butterflywing=True):
    func.close_any_panel()
    func.create_party_and_invite()
    utils.key_press('u')
    utils.wait_for_image(img.sakura_wedding_page)

    if utils.is_found(img.sakura_wedding_spirit_anomaly):
        utils.tap_until_found(img.sakura_wedding_spirit_anomaly, img.sakura_spirit_anomaly_page)

        count3x3 = utils.count_image_on_screen(img.sakura_spirit_anomaly_3x3, similarity=0.95)
        tr_mode_3x3_count = 2 if tr else 1
        print(f"3x3 check: {tr_mode_3x3_count} and actual found:{count3x3}")
        if count3x3 >= tr_mode_3x3_count:
            func.close_any_panel()
            func.send_message("done 3/3 [z1]")
            func.leave_party()
            return False

        utils.wait_for_image(img.sakura_spirit_anomaly_go_button)
        go_button = utils.find_most_top_coordinate([img.sakura_spirit_anomaly_go_button])
        utils.tap_location_until_found(go_button, img.sakura_spirit_anomaly_southern_payon)
        
        utils.execute_until_valid_state_with_timeout(300, 1, sakura_boss_state, butterflywing)

    return True


def sakura_boss_state(butterflywing):
    func.close_any_panel(img.sakura_spirit_anomaly_southern_payon)
    time_pattern = r"([\d]{2})[:-]([\d]{2})"
    remaining_time = utils.get_text_from_image_with_expect_pattern(img.sakura_spirit_anomaly_southern_payon, offset_x=250, offset_y=0, text_pattern=time_pattern)
    if remaining_time is None:
        return False

    try:
        minutes, seconds = map(int, remaining_time.split(":"))
        boss_wait_time = (minutes * 60 + seconds)
        print(f"waiting time: minutes: {minutes}, seconds: {seconds} = {boss_wait_time}")
    except ValueError as e:
        print(f"Error: {e}")
        return False
    
    if remaining_time is not None and boss_wait_time <= 180:
        utils.tap_until_notfound(img.sakura_spirit_anomaly_southern_payon, img.sakura_spirit_anomaly_southern_payon)
        start_time = time.time()
        if not utils.execute_until_valid_state_with_timeout(150, 1, boss.running_to_boss_map_state, img.sakura_boss_map):
            func.butterfly_wing_morroc()
            return True
        elapsed_running_time = time.time() - start_time

        boss_wait_time = boss_wait_time - elapsed_running_time -5
        wing_boss('Event Boss', 
                    img.boss_incarnation_of_love_fight, 
                    [img.chat_party_coord_southern_payon1, img.chat_party_coord_southern_payon2], 
                    boss_wait_time, 
                    butterflywing)
        
        func.send_message("[z1]")
        func.leave_party()
        preset.attack_preset()
        return True
    
    return False
            
            