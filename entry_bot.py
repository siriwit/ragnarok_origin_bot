import alfheim
import anthem
import boss
import catpaw
import constanst as const
import dbbb
import extreme_challenge
import guild_collect
import guild_league
from datetime import datetime
import demon_treasure
import hazy
import hellheim
import hordor
import farm
import feast
import func
import img
import life_skill
import oracle
import preset
import sys
import woe
import guild_expedition
import time_anomaly
import ro_schedule
import monster_research
import treasure_map
import event_boss
import utils
import ygg
import phantom
import doram_quest


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def get_input(position, options=[], msg="Choose Number: "):
    if len(arguments) <= position:
        input_value = input(msg)
        return int(input_value) if is_number(input_value) else input_value
    
    input_number = 0
    value = arguments[position]
    if is_number(value):
        input_number = int(value)
    else:
        if len(options) > 0:
            for index, option in enumerate(options):
                if value.lower() in option.lower():
                    input_number = index
                    break
        else:
            return value

    return input_number

def print_menu(menu_name, menu_options):
    print(f"{menu_name}: ")
    subarrays = [menu_options[i:i+4] for i in range(0, len(menu_options), 4)]
    for subarray in subarrays:
        for menu in subarray:
            print(f"{menu}", end=generate_space(menu))
        print()


def generate_space(item):
    item_space = 30
    length = len(item)
    spaces = ""
    for _ in range(0, item_space-length):
        spaces += " "
    return spaces


def alfheim_mode():
    sub_menu = [
        '0. Back', 
        '1. Fight', 
        '2. Collect Item']
    print_menu('Alfheim', sub_menu)
    input_number = get_input(2, sub_menu)
    if input_number == 0:
        return
    elif input_number == 1:
        preset.boss(is_event=True)
        alfheim.alfheim_fight()
    elif input_number == 2:
        alfheim.alfheim_collect_item()


def life_skill_mode():
    sub_menu = [
        '0. Back',
        '1. Foraging',
        '2. Fishing',
        '3. Cooking',
        '4. Eat'
    ]
    print_menu('Life Skill', sub_menu)
    input_number = get_input(2, sub_menu)
    if input_number == 0:
        return
    elif input_number == 1:
        life_skill.start()
    elif input_number == 2:
        life_skill.start(mode='fishing')
    elif input_number == 3:
        cooking_mode()
    elif input_number == 4:
        preset.eat_food()

def cooking_mode():
    sub_menu = [
        '0. Back',
        '1. Seafood Fried Noodles',
        '2. Scallop And Crab Congee'
    ]
    print_menu('Food', sub_menu)
    input_number = get_input(3, sub_menu)
    if input_number == 0:
        return
    elif input_number == 1:
        life_skill.start(mode='cooking', expected_food=img.life_skill_cooking_seafood_fried_noodles)
    elif input_number == 2:
        life_skill.start(mode='cooking', expected_food=img.life_skill_cooking_scallop_and_crab_congee)


def daily_mode():
    sub_menu = [
            '0. Back',
            '1. Demon Treasure',
            '2. Cat Paw Caravan',
            '3. Anthem',
            '4. Hazy'
        ]
    print_menu('Daily', sub_menu)
    input_number = get_input(2, sub_menu)
    if input_number == 0:
        return
    elif input_number == 1:
        demon_treasure.daily_demon_treasure()
    elif input_number == 2:
        catpaw.daily_cat_paw()
    elif input_number == 3:
        sub_menu = [
            '0. Back',
            '1. Skip',
            '2. Not Skip'
        ]
        print_menu('Skip?', sub_menu)
        input_number = get_input(3, sub_menu)
        if input_number == 0:
            return
        elif input_number == 1:
            anthem.daily_anthem(True)
        elif input_number == 2:
            anthem.daily_anthem(False)
    elif input_number == 4:
        hazy.start()

def boss_hunt_mode():

    sub_menu = [
            '0. Back',
            '1. Leader',
            '2. Follower'
        ]
    input_number = get_input(2, sub_menu, "MVP Mode: ")
    if input_number == 1:
        sub_menu = [
            '0. Back',
            '1. Active',
            '2. Inactive'
        ]
        is_active = True if get_input(3, sub_menu, "Is Active Mode: ") == 1 else False
        min_level = get_input(4, [], "Min Level: ")
        max_level = get_input(5, [], "Max Level: ")

        sub_menu = [
                '0. Back',
                '1. Ignore',
                '2. Not Ignore'
            ]
        ignore_spawn = True if get_input(6, sub_menu, "Should ignore spawn: ") == 1 else False

        sub_menu = [
                '0. Back',
                '1. Party',
                '2. Solo'
            ]
        party_mode = True if get_input(7, sub_menu, "Party?: ") == 1 else False

        sub_menu = [
            '0. Back',
            '1. TR',
            '2. PR'
        ]
        tr_mode = True if get_input(8, sub_menu, "PR/TR Mode?: ") == 1 else False

        print(f"\n")
        print(f"Start boss hunt:")
        print(f" is_active= {is_active}")
        print(f" min_level= {min_level}")
        print(f" max_level= {max_level}")
        print(f" ignore_spawn= {ignore_spawn}")
        print(f" party= {party_mode}\n")
        print(f" tr_mode= {tr_mode}\n")
        utils.exit_at_specific_time_or_invalid_state(4, 50, boss_loop_state, is_active, min_level, max_level, ignore_spawn, party_mode, tr_mode)
    elif input_number == 2:
        boss.boss_follower()


def boss_loop_state(is_active, min_level, max_level, ignore_spawn, party_mode, tr_mode):
    if boss.boss_hunt_loop(is_active, min_level, max_level, ignore_spawn, party_mode, tr_mode):
        return False
    return True


def hordor_mode():
    sub_menu = [
            '0. Back',
            '1. Poring Dream',
            '2. Magic Ocean',
            '3. Waste Land',
            '4. Paradise Courage'
        ]
    print_menu('Hordor', sub_menu)
    input_number = get_input(2, sub_menu)
    if input_number == 0:
        return
    elif input_number == 1:
        hordor.hordor_dreamland(mode=img.hordor_poring_dream)
    elif input_number == 2:
        hordor.hordor_dreamland(mode=img.hordor_magic_ocean)
    elif input_number == 3:
        hordor.hordor_dreamland(mode=img.hordor_wasteland)
    elif input_number == 4:
        hordor.hordor_dreamland(mode=img.hordor_paradise_courage)


def preset_mode():
    sub_menu = [
            '0. Back',
            '1. Daily',
            '2. Farm',
            '3. Boss',
            '4. Party',
            '5. PVP',
            '6. Card',
            '7. Element'
        ]
    print_menu('Preset', sub_menu)
    input_number = get_input(2, sub_menu)
    if input_number == 0:
        return
    elif input_number == 1:
        preset.daily()
    elif input_number == 2:
        preset.farm()
    elif input_number == 3:
        sub_menu = [
                '0. Back',
                '1. Event',
                '2. Not Event'
            ]
        print_menu('Mode', sub_menu)
        is_event = True if get_input(3, sub_menu, "Is event?: ") == 1 else False
        print(f"is event: {is_event}")
        preset.boss(is_event)
    elif input_number == 4:
        preset.party()
    elif input_number == 5:
        preset.pvp()
    elif input_number == 6:
        sub_menu = [
            '0. Back',
            '1. None',
            '2. angel',
            '3. brute',
            '4. demon',
            '5. dragon',
            '6. formless',
            '7. insect',
            '8. demi-human',
            '9. human',
            '10. poison'
        ]
        print_menu('Tribe', sub_menu)
        tribe = get_input(3, sub_menu, 'Choose Tribe: ')
        
        element = choose_element(4)

        sub_menu = [
            '0. Back',
            '1. None',
            '2. small',
            '3. medium',
            '4. large'
        ]
        print_menu('Size', sub_menu)
        size = get_input(5, sub_menu, 'Choose Size: ')
        if tribe > 0:
            if tribe == 1:
                tribe = None
            elif tribe == 2:
                tribe = const.angel
            elif tribe == 3:
                tribe = const.brute
            elif tribe == 4:
                tribe = const.demon
            elif tribe == 5:
                tribe = const.dragon
            elif tribe == 6:
                tribe = const.formless
            elif tribe == 7:
                tribe = const.insect
            elif tribe == 8:
                tribe = const.demi_human
            elif tribe == 9:
                tribe = const.human
            elif tribe == 10:
                tribe = const.poison
        else:
            return
        
        if element > 0:
            element = get_element_text(element)
        else:
            return
        
        if size > 0:
            if size == 1:
                size = None
            elif size == 2:
                size = const.small
            elif size == 3:
                size = const.medium
            elif size == 4:
                size = const.large
        else:
            return
        print(f"tribe: {tribe} element: {element} size: {size}")
        preset.againt_monster_card(tribe, element, size)
    elif input_number == 7:
        element = choose_element(3)
        if element > 0:
            element = get_element_text(element)
        else:
            return
        func.element_convert(element)
    func.close_any_panel()


def choose_element(input_index):
    sub_menu = [
        '0. Back',
        '1. None',
        '2. holy',
        '3. fire',
        '4. earth',
        '5. neutral',
        '6. shadow',
        '7. wind',
        '8. water',
        '9. undead'
    ]
    print_menu('Element', sub_menu)
    element = get_input(input_index, sub_menu, 'Choose Element: ')
    return element


def get_element_text(number):
    element = None
    if number == 2:
        element = const.holy
    elif number == 3:
        element = const.fire
    elif number == 4:
        element = const.earth
    elif number == 5:
        element = const.neutral
    elif number == 6:
        element = const.shadow
    elif number == 7:
        element = const.wind
    elif number == 8:
        element = const.water
    elif number == 9:
        element = const.undead
    return element

def monster_research_mode():
    mr_name = get_input(2, [], 'Map Name: ')

    sub_menu = [
                '0. Back',
                '1. Wing',
                '2. Not Wing'
            ]
    print_menu('Wing Mode', sub_menu)
    wing_mini_mode = True if get_input(3, sub_menu, "Wing Mini?: ") == 1 else False

    sub_menu = [
                '0. Back',
                '1. Invite',
                '2. Not Invite'
            ]
    print_menu('Invite People Mode', sub_menu)
    invite_people = True if get_input(4, sub_menu, "Invite People?: ") == 1 else False

    sub_menu = [
                '0. Back',
                '1. All Monsters',
                '2. No Attack'
            ]
    print_menu('Attack Mode', sub_menu)
    attack_monster = True if get_input(5, sub_menu, "Attack Monster?: ") == 1 else False

    sub_menu = [
                '0. Back',
                '1. Detect',
                '2. Not Detect'
            ]
    warp_detect = True if get_input(6, sub_menu, "Warp Detect?: ") == 1 else False
    
    print(f"Map Name: {mr_name}, Wing Mini?: {wing_mini_mode}, Invite People?: {invite_people}, Attack All Mons?: {attack_monster}, Warp Detect?: {warp_detect}")
    preset.change_skill_auto(const.mr)
    monster_research.start(mr_name, wing_mini_mode, invite_people, attack_monster, warp_detect)


def guild_expedetion_mode():

    sub_menu = [
        '0. Back',
        '1. Drake',
        '2. Phreeoni',
        '3. Moonlight',
        '4. Doppel',
        '5. Bapho',
        '6. Angeling',
        '7. Golden Theif Bug',
        '8. Deviling',
        '9. Goblin',
        '10. Eddga'
    ]

    print_menu('Boss', sub_menu)
    input_number = get_input(2, sub_menu, 'Choose Boss: ')

    sub_menu = [
        '0. Back',
        '1. Level 1',
        '2. Level 2'
    ]
    print_menu('Level', sub_menu)
    level = get_input(3, sub_menu, 'Choose Level: ')

    if input_number == 0:
        return
    elif input_number == 1:
        guild_expedition.start(img.guild_expedition_boss_drake, level)
    elif input_number == 2:
        guild_expedition.start(img.guild_expedition_boss_phreeoni, level)
    elif input_number == 3:
        guild_expedition.start(img.guild_expedition_boss_moonlight, level)
    elif input_number == 4:
        guild_expedition.start(img.guild_expedition_boss_doppel, level)
    elif input_number == 5:
        guild_expedition.start(img.guild_expedition_boss_bapho, level)
    elif input_number == 6:
        guild_expedition.start(img.guild_expedition_boss_angeling, level)
    elif input_number == 7:
        guild_expedition.start(img.guild_expedition_boss_golden_thief_bug, level)
    elif input_number == 8:
        guild_expedition.start(img.guild_expedition_boss_deviling, level)
    elif input_number == 9:
        guild_expedition.start(img.guild_expedition_boss_goblin, level)
    elif input_number == 10:
        guild_expedition.start(img.guild_expedition_boss_eddga, level)


def event_boss_mode():
    sub_menu = [
        '0. Back',
        '1. Twilight Bringer',
        '2. Bijou',
        '3. Hellhound',
        '4. Abyss Demon',
        '5. Fallen Genesis',
        '6. Fallen Nemesis',
        '7. Antonio',
        '8. Evil Reindeer',
        '9. Angelic Picky',
        '10. Demonic Eggy',
        '11. Mournful Sakura Spirit'
    ]

    print_menu('Event Boss', sub_menu)
    input_number = get_input(2, sub_menu, 'Choose Boss: ')

    sub_menu = [
        '0. Back',
        '1. TR',
        '2. PR'
    ]
    tr_mode = True if get_input(3, sub_menu, "PR/TR Mode?: ") == 1 else False

    sub_menu = [
        '0. Back',
        '1. Wing to Morroc',
        '2. Not Wing'
    ]
    butterflywing = True if get_input(4, sub_menu, "Butterfly Wing Mode?: ") == 1 else False

    # preset.boss()
    if input_number == 0:
        return
    elif input_number == 1:
        event_boss.awakening('Twilight Bringer')
    elif input_number == 2:
        event_boss.awakening('Bijou')
    elif input_number == 3:
        event_boss.awakening('Hellhound')
    elif input_number == 4:
        event_boss.awakening('Abyss Demon')
    elif input_number == 5:
        event_boss.awakening('Fallen Genesis')
    elif input_number == 6:
        event_boss.awakening('Fallen Nemesis')
    elif input_number == 7:
        utils.exit_at_specific_time_or_invalid_state(4, 50, event_boss.christmas)
    elif input_number == 8:
        utils.execute_until_valid_state_with_timeout(180, 1, event_boss.christmas_evil_reindeer)
    elif input_number == 9:
        boss_name = 'Angelic Picky'
        utils.exit_at_specific_time_or_invalid_state(4, 50, event_boss.picky_boss, boss_name, tr_mode, butterflywing)
    elif input_number == 10:
        boss_name = 'Demonic Eggy'
        utils.exit_at_specific_time_or_invalid_state(4, 50, event_boss.picky_boss, boss_name, tr_mode, butterflywing)
    elif input_number == 11:
        utils.exit_at_specific_time_or_invalid_state(4, 50, event_boss.sakura, tr_mode, butterflywing)


def farm_mode():
    sub_menu = [
        '0. Back',
        '1. Normal Farm',
        '2. Monster Annihilation',
        '3. Disable',
        '4. Enable'
    ]

    print_menu('Farm', sub_menu)
    input_number = get_input(2, sub_menu, 'Choose Mode: ')
    if input_number == 0:
        return
    elif input_number == 1:
        minutes = get_input(3, [], 'How long? (miute): ')
        monster_name = get_input(4, [], 'Put monster name: ')
        element = choose_element(5)
        element = get_element_text(element)
        print(f"Farm end in {minutes} mins, Monster Name: {monster_name}, element: {element}")
        farm.farm_enable()
        farm.farm(minutes, monster_name, element)
    elif input_number == 2:
        minutes = get_input(3, [], 'How long? (miute): ')
        farm.monster_annihilation(minutes)
    elif input_number == 3:
        farm.farm_disable()
    elif input_number == 4:
        farm.farm_enable()


def ygg_mode():
    sub_menu = [
        '0. Back',
        '1. Fight',
        '2. Skip'
    ]
    print_menu('YGG', sub_menu)
    input_number = get_input(2, sub_menu, 'Choose Mode: ')
    if input_number == 0:
        return
    elif input_number == 1:
        ygg.ygg_fight()
    elif input_number == 2:
        ygg.ygg_fight(True)


def extreme_challenge_mode():
    sub_menu = [
        '0. Back',
        '1. Fight',
        '2. Assist'
    ]
    print_menu('Extreme Challenge', sub_menu)
    input_number = get_input(2, sub_menu, 'Choose Mode: ')
    print(f"Extreme Challenge: {input_number}")
    if input_number == 0:
        return
    elif input_number == 1:
        extreme_challenge.start()
    elif input_number == 2:
        extreme_challenge.start(is_assist=True)


def doram_mode():
    sub_menu = [
        '0. Back',
        '1. Divination',
        '2. Meow Tarot',
        '3. Wishing',
        '4. Beach hidden',
        '5. Onsen'
    ]

    print_menu('Doram Mode', sub_menu)
    input_number = get_input(2, sub_menu, 'Choose Mode: ')
    print(f"Doram Mode: {input_number}")
    if input_number == 0:
        return
    elif input_number == 1:
        doram_quest.divination()
    elif input_number == 2:
        doram_quest.meow_tarot()
    elif input_number == 3:
        doram_quest.transform_doram()
        doram_quest.wishing_pool()
    elif input_number == 4:
        doram_quest.transform_doram()
        doram_quest.beach_hidden_obj()
    elif input_number == 5:
        doram_quest.transform_doram()
        doram_quest.onsen_pool()


print("==================================================================")
print("=====================  Ragnarok Origin v0.1 ======================")
print("==================================================================")

arguments = sys.argv
print(arguments)

while True:
    main_menu = [
        '0. Exit', 
        '1. Alfhelm', 
        '2. Daily', 
        '3. Life Skill', 
        '4. Hellheim', 
        '5. Oracle', 
        '6. Guild Collect Item', 
        '7. Farm', 
        '8. dbbb',
        '9. MVP',
        '10. WOE',
        '11. Hordor',
        '12. Preset',
        '13. Guild Expedition',
        '14. Schedule',
        '15. Feast',
        '16. Time Anomaly',
        '17. Monster Research',
        '18. Treasure Map',
        '19. Go To Main Page',
        '20. Guild League',
        '21. Event Boss',
        '22. YGG',
        '23. Extreme Challenge',
        '24. Phantom',
        '25. Doram']
    print_menu('Main Menu', main_menu)

    input_number = get_input(1, main_menu)

    if input_number == 0:
        break
    elif input_number == 1:
        alfheim_mode()
    elif input_number == 2:
        daily_mode()
    elif input_number == 3:
        life_skill_mode()
    elif input_number == 4:
        hellheim.start()
    elif input_number == 5:
        oracle.request_oracle()
    elif input_number == 6:
        guild_collect.start()
    elif input_number == 7:
        farm_mode()
    elif input_number == 8:
        dbbb.party_finder()
    elif input_number == 9:
        boss_hunt_mode()
    elif input_number == 10:
        woe.maintain_woe()
    elif input_number == 11:
        hordor_mode()
    elif input_number == 12:
        preset_mode()
    elif input_number == 13:
        if datetime.now().weekday() == 3 or datetime.now().weekday() == 6:
            guild_expedetion_mode()
        else:
            print("Not the event date")
    elif input_number == 14:
        ro_schedule.start()
    elif input_number == 15:
        feast.start()
    elif input_number == 16:
        if datetime.now().weekday() == 1 or datetime.now().weekday() == 5:
            time_anomaly.start()
        else:
            print("Not the event date")
    elif input_number == 17:
        monster_research_mode()
    elif input_number == 18:
        treasure_map.start()
    elif input_number == 19:
        func.use_items()
        func.close_any_panel()
        func.leave_party()
    elif input_number == 20:
        guild_league.start()
    elif input_number == 21:
        event_boss_mode()
    elif input_number == 22:
        ygg_mode()
    elif input_number == 23:
        extreme_challenge_mode()
    elif input_number == 24:
        phantom.start()
    elif input_number == 25:
        doram_mode()
    
    func.close_debug_window()

    if len(arguments) > 0:
        break

