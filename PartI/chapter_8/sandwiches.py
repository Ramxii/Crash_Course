def sandwich_maker(*ingredients):
    """Accepts ingredients of a sandwich_make"""
    print(f"Sandwich Ingredients: ")
    for ingredient in ingredients:
        print(f"\t- {ingredient}")

sandwich_maker('lettuce')
sandwich_maker('cheese', 'eggs', 'bacon')
sandwich_maker('ham', 'ketchup')
