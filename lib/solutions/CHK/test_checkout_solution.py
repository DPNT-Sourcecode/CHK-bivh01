import pytest
from lib.solutions.CHK.checkout_solution import checkout


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


