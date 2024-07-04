import pytest
from lib.solutions.CHK.checkout_solution import checkout, _handle_free_items


class TestCheckout:
    @pytest.mark.parametrize(
        "skus, value",
        [
            # ("", 0),
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


    def test_handle_value_offers(self):
        pass


    def test_handle_bundle_offers(self):
        pass
        pass