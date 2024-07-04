from collections import Counter, OrderedDict
from dataclasses import dataclass

_SKU_PRICE_TABLE = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40
}


@dataclass
class _Offer:
    offers: dict


@dataclass
class ValueOffer(_Offer):
    def get_offer(self, count):
        """
        Returns the best value deal with the given count

        Params
        ------
        count: int

        Returns
        -------
        int
        """
        for vol in sorted(self.offers, reverse=True):
            if count > vol:
                return
        return 0




@dataclass
class FreeItemOffer(ValueOffer):
        pass

_OFFERS_TABLE = {
    'A': OrderedDict({5: 200, 3: 130}),
    'B': OrderedDict({2: 45}),
    'E': OrderedDict({2: 'B'})
}
# _OFFERS_TABLE = {
#     'A': ValueOffer(offers={3: 130, 5: 200}),
#     'B': ValueOffer(offers={2: 45}),
#     'E': FreeItemOffer(offers={2: 'B'})
# }
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
            for



            # offer = _OFFERS_TABLE[sku].get_offer(basket[sku])

            # remainder = basket[sku] % offer.volume
            # full_deals = basket[sku] // _OFFERS_TABLE[sku].volume

            # basket_value += (full_deals * _OFFERS_TABLE[sku].value +
            #                  remainder * _SKU_PRICE_TABLE[sku])
        else:
            basket_value += _SKU_PRICE_TABLE[sku] * basket[sku]

    return basket_value

def

