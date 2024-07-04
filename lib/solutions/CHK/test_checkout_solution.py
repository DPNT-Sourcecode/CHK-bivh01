import pytest
from checkout_solution import checkout

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
            ("ABCDCBAABCABBAAA", 0)
        ]
    )
    def test_expected_output(self, skus, value):
        assert value == checkout(skus)