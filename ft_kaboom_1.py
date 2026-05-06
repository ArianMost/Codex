print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")


def ft_kaboom_1() -> None:
    from alchemy.grimoire.dark_spellbook import dark_spell_record

    print(dark_spell_record("Chaos", "frogs, bats and eyeball"))
    print()


if __name__ == "__main__":
    ft_kaboom_1()
