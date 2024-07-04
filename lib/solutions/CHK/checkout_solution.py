from collections import Counter, OrderedDict
from dataclasses import dataclass

_SKU_PRICE = {
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
    pass


@dataclass
class FreeItemOffer(ValueOffer):
    pass


_VALUE_OFFERS = {
    'A': ValueOffer(offers={3: 130, 5: 200}),
    'B': ValueOffer(offers={2: 45}),
}

_FREE_ITEM_OFFERS = {
    'E': FreeItemOffer(offers={2: 'B'}),
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
        if sku not in _SKU_PRICE:
            return -1
        # Kept this seperate as it needs to execture before second block
        _handle_free_items(basket, sku)

        basket_value = _handle_value_offers(basket, basket_value, sku)

        basket_value += _SKU_PRICE[sku] * basket[sku]

    return basket_value


def _handle_value_offers(basket, basket_value, sku):
    if sku in _VALUE_OFFERS:
        offers = _VALUE_OFFERS[sku].offers
        for vol in sorted(offers, reverse=True):
            full_deals = basket[sku] // vol
            if full_deals > 0:
                basket_value += offers[vol] * full_deals
                basket[sku] -= vol * full_deals
    return basket_value


def _handle_free_items(basket, sku):
    if sku in _FREE_ITEM_OFFERS:
        offers = _FREE_ITEM_OFFERS[sku].offers
        for vol in sorted(offers, reverse=True):
            full_deals = basket[sku] // vol
            basket[offers[vol]] -= full_deals


