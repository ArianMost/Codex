from .elements import create_air
from .potions import healing_potion, strength_potion
from .transmutation import lead_to_gold
from .grimoire import light_spell_record


heal = healing_potion

__all__ = [
    "create_air",
    "strength_potion",
    "heal",
    "lead_to_gold",
    "light_spell_record"]
