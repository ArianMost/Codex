from alchemy import grimoire


def ft_kaboom_0() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    record = grimoire.light_spell_record("Fantasy", "Earth, wind and fire")
    print(f"Testing record light spell: {record}")
    print()


if __name__ == "__main__":
    ft_kaboom_0()
