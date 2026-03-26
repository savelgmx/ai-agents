def approve_changes(changes):

    print("\n=== PROPOSED CHANGES ===")

    for c in changes:
        print(f"\nFILE: {c['file']}")
        print(c["code"][:300])

    choice = input("\nApply changes? (y/n): ")

    return choice.lower() == "y"
