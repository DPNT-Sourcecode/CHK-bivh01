import pytest

from lib.solutions.CHK.checkout_solution import checkout, _handle_free_items, \
    _calculate_basket_value, _handle_bundle_offer, _STXYZ_BUNDLE


class TestCheckout:
    @pytest.mark.parametrize(
        "skus, value",
        [
            ("", 0),
            ("A", 50),
            ("B", 30),
            ("C", 20),
            ("D", 15),
            ("-", -1),
            ("AAA", 130),
            ("BB", 45),
            ("BBB", 75),
            ('E', 40),
            ('EE', 80),
            ('EEB', 80),
            ("AAAAA", 200),
            ("AAAAAAAA", 330),
            ("BEBEEE", 160),
            ("ABCDEABCDE", 280),
            ("ABCDCBAABCABBAAA", 495),
            ("F", 10),
            ("FF", 20),
            ("FFF", 20),
            ("FFFF", 30),
            ("ABCDCBAAFBCABFBAAFA", 515),
            ("STXYZ", 82),
            ("STXYZZZ", 107),
            ("STXYZSTXYZ", 152),
        ]
    )
    def test_expected_output(self, skus, value):
        assert value == checkout(skus)

    @pytest.mark.parametrize(
        "basket, f_sku, expected",
        [
            ({'E': 4, 'B': 2}, 'B', 0),
            ({'E': 2, 'B': 2}, 'B', 1),
            ({'F': 3}, 'F', 2),
        ]
    )
    def test_handle_free_items(self, basket, f_sku, expected):
        _handle_free_items(basket=basket)

        assert basket[f_sku] == expected

    @pytest.mark.parametrize(
        'basket, expected',
        [
            ({'A': 2, 'B': 1}, 130),
            ({'A': 3}, 130),
            ({'O': 10}, 100),
        ]
    )
    def test_handle_value_offers(self, basket, expected):
        assert expected == _calculate_basket_value(basket=basket,
                                                   basket_value=0)

    @pytest.mark.parametrize(
        'basket, bundle, expected',
        [
            ({'S': 3}, _STXYZ_BUNDLE, 45),
            ({'S': 4}, _STXYZ_BUNDLE, 45),
            ({'S': 3, 'O': 4}, _STXYZ_BUNDLE, 45),
            ({'S': 3, 'T': 3, 'X': 2}, _STXYZ_BUNDLE, 90),
            ({'S': 3, 'T': 1, 'X': 1, 'Y': 1, 'Z': 3}, _STXYZ_BUNDLE, 135),
        ]
    )
    def test_handle_bundle_offers(self, basket, bundle, expected):
        assert expected == _handle_bundle_offer(basket=basket,
                                                basket_value=0,
                                                bundle=bundle)

