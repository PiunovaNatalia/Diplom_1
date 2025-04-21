class Data:
    buns_data = [
        ['Флюоресцентная булка R2-D3', 25.5],
        ['Краторная булка N-200i', 100.0],
    ]

    ingredients_data = [
        ['FILLING', 'Мясо бессмертных моллюсков Protostomia', 1337.0],
        ['SAUCE', 'Соус фирменный Space Sauce', 80.0],
    ]

    burger_data = [
        {
            'bun': ['Флюоресцентная булка R2-D3', 25.5],
            'ingredients': ingredients_data,
            'expected_price': 1468.0,
            'expected_receipt': (
                "(==== Флюоресцентная булка R2-D3 ====)\n"
                "= filling Мясо бессмертных моллюсков Protostomia =\n"
                "= sauce Соус фирменный Space Sauce =\n"
                "(==== Флюоресцентная булка R2-D3 ====)\n"
                "\n"
                "Price: 1468.0"
            ),
        },
        {
            'bun': ['Краторная булка N-200i', 100.0],
            'ingredients': ingredients_data,
            'expected_price': 1617.0,
            'expected_receipt': (
                "(==== Краторная булка N-200i ====)\n"
                "= filling Мясо бессмертных моллюсков Protostomia =\n"
                "= sauce Соус фирменный Space Sauce =\n"
                "(==== Краторная булка N-200i ====)\n"
                "\n"
                "Price: 1617.0"
            ),
        },
    ]

    EXPECTED_AVAILABLE_BUNS = 3
    EXPECTED_AVAILABLE_INGREDIENTS = 6
