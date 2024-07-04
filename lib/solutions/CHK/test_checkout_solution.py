import pytest
from lib.solutions.CHK.checkout_solution import checkout, _handle_free_items


class TestCheckout:
    @pytest.mark.parametrize(
        "skus, value",
        [
            # ("", 0),
            # ("A", 50),
            # ("B", 30),
            # ("C", 20),
            # ("D", 15),
            # ("-", -1),
            # ("AAA", 130),
            # ("BB", 45),
            # ("BBB", 75),
            # ('E', 40),
            # ('EEB', 80),
            # ("AAAAA", 200),
            # ("AAAAAAAA", 330),
            ("BEBEEE", 160),
            ("ABCDEABCDE", 280),
            ("ABCDCBAABCABBAAA", 495)
        ]
    )
    def test_expected_output(self, skus, value):
        assert value == checkout(skus)

    @pytest.mark.parametrize(
        "basket, t_sku, f_sku, expected",
        [
            ({'E': 4, 'B': 2}, 'E', 'B', 0),
            ({'E': 2, 'B': 2}, 'E', 'B', 1),
        ]
    )
    def test_handle_free_items(self, basket, t_sku, f_sku, expected):
        _handle_free_items(basket=basket,
                           sku=t_sku)

        assert basket[f_sku] == expected


