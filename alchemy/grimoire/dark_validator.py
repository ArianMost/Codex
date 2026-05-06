from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ing = dark_spell_allowed_ingredients()
    is_valid = any(ing in ingredients.lower() for ing in allowed_ing)
    status = "VALID" if is_valid else "INVALID"

    return f"{ingredients} - {status}"
