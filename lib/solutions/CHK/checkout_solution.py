from collections import Counter
from dataclasses import dataclass

_SKU_PRICE_TABLE = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40
}


@dataclass
class Offer:
    volume: int


@dataclass
class ValueOffer(Offer):
    value: int


@dataclass
class FreeItemOffer(Offer):
    free_item: str


_OFFERS_TABLE = {
    'A': [ValueOffer(volume=3, value=130),
          ValueOffer(volume=5, value=200)],
    'B': [ValueOffer(volume=2, value=45)],
    'E': FreeItemOffer(volume=2, free_item='B')
}
# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus):
    """
    Accepts a string of all SKUs for a basket and returns the basket value.
    Returns -1 if any invalid SKUs are passed in.

    Params
    ------
    skus: string, eg (ABCDCBAABCABBAAA)

    Returns
    -------
    int, anything above -1 inclusive
    """
    basket = Counter(skus)
    basket_value = 0

    for sku in basket:
        if sku not in _SKU_PRICE_TABLE:
            return -1

        if sku in _OFFERS_TABLE:
            remainder = basket[sku] % _OFFERS_TABLE[sku].volume
            full_deals = basket[sku] // _OFFERS_TABLE[sku].volume

            basket_value += (full_deals * _OFFERS_TABLE[sku].value +
                             remainder * _SKU_PRICE_TABLE[sku])
        else:
            basket_value += _SKU_PRICE_TABLE[sku] * basket[sku]

    return basket_value

def

