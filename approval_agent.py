def approve_changes(changes):

    print("\n=== CHANGES PREVIEW ===")

    for c in changes:
        print(f"\nFILE: {c['file']}")
        print(c["code"][:500])

    choice = input("\nApply changes? (y/n): ")

    return choice.lower() == "y"
