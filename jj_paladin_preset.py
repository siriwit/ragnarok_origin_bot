import constanst as const
import img
import func
import utils


def change_skill_auto(preset):
    if preset == const.boss or preset == const.ygg:
        # ensure_use_support_skill(img.preset_skill_normal_attack, img.preset_skill_touse_normal_attack)
        utils.scroll_down_util_found(img.preset_skill_touse_provoke, img.preset_skill_drag_icon, offset_y=200)
        func.ensure_replace_skill(img.preset_skill_provoke, img.preset_skill_touse_provoke, [img.preset_skill_providence, img.preset_skill_endure])
        func.ensure_use_support_skill(img.preset_skill_shield_reflect, img.preset_skill_touse_shield_reflect)
        func.ensure_use_support_skill(img.preset_skill_spear_quicken, img.preset_skill_touse_spear_quicken)
        func.ensure_use_support_skill(img.preset_skill_auto_guard, img.preset_skill_touse_auto_guard)
        func.ensure_use_support_skill(img.preset_skill_martyr, img.preset_skill_touse_martyr)
    else:
        # ensure_use_support_skill(img.preset_skill_normal_attack, img.preset_skill_touse_normal_attack)
        utils.scroll_down_util_found(img.preset_skill_touse_provoke, img.preset_skill_drag_icon, offset_y=200)
        func.ensure_replace_skill(img.preset_skill_providence, img.preset_skill_touse_providence, [img.preset_skill_provoke])
        func.ensure_use_support_skill(img.preset_skill_shield_reflect, img.preset_skill_touse_shield_reflect)
        func.ensure_use_support_skill(img.preset_skill_spear_quicken, img.preset_skill_touse_spear_quicken)
        func.ensure_use_support_skill(img.preset_skill_auto_guard, img.preset_skill_touse_auto_guard)
        func.ensure_use_support_skill(img.preset_skill_martyr, img.preset_skill_touse_martyr)
