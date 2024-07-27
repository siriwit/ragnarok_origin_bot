import constanst as const
import img
import func
import utils


def change_skill_auto(preset):

    if preset == const.mr:
        func.remove_skill_if_needed(img.preset_skill_warrior_zeal)
        func.remove_skill_if_needed(img.preset_skill_auto_guard)
        func.remove_skill_if_needed(img.preset_skill_divine_majesty)
        func.remove_skill_if_needed(img.preset_skill_shield_of_god)
    else:
        # ensure_use_support_skill(img.preset_skill_normal_attack, img.preset_skill_touse_normal_attack)
        scroll_to_damage_skill()
        func.ensure_use_support_skill(img.preset_skill_divine_majesty, img.preset_skill_touse_divine_majesty)

        scroll_to_support_skill()
        func.ensure_use_support_skill(img.preset_skill_auto_guard, img.preset_skill_touse_auto_guard)
        func.ensure_use_support_skill(img.preset_skill_shield_of_god, img.preset_skill_touse_shield_of_god)
        func.ensure_use_support_skill(img.preset_skill_spear_quicken, img.preset_skill_touse_spear_quicken)
        func.ensure_use_support_skill(img.preset_skill_warrior_zeal, img.preset_skill_touse_warrior_zeal)
        

def change_skill_manual(preset=const.boss):
    print(preset)
    if preset == const.boss:
        scroll_to_support_skill()
        func.ensure_replace_skill(img.preset_skill_provoke, img.preset_skill_touse_provoke, [img.preset_skill_crescent_slasher])
    elif preset == const.pvp or preset == const.boss_event:
        scroll_to_damage_skill()
        func.ensure_replace_skill(img.preset_skill_providence, img.preset_skill_touse_providence, [img.preset_skill_over_brand])


def scroll_to_support_skill():
    scroll_to_damage_skill()
    if not utils.is_found(img.preset_skill_drag_icon_support_skill) and utils.is_found(img.preset_skill_drag_icon_damage_skills):
        utils.scroll_down_until_found(img.preset_skill_touse_provoke, img.preset_skill_drag_icon_damage_skills)
    utils.scroll_down_until_found(img.preset_skill_touse_shield_of_god, img.preset_skill_drag_icon_support_skill)


def scroll_to_damage_skill():
    if utils.is_found(img.preset_skill_drag_icon_statue_skill):
        utils.scroll_up_util_found(img.preset_skill_drag_icon_support_skill, img.preset_skill_drag_icon_statue_skill)
    if utils.is_found(img.preset_skill_drag_icon_support_skill):
        utils.scroll_up_util_found(img.preset_skill_drag_icon_damage_skills, img.preset_skill_drag_icon_support_skill)
    
