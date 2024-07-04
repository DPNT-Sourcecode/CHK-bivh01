from collections import Counter
from dataclasses import dataclass


@dataclass
class Bundle:
    items: tuple
    required_vol: int


_STXYZ_BUNDLE = Bundle(
    items=('Z', 'S', 'T', 'Y', 'X'),
    required_vol=3)

_SKU_PRICE = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10,
    'G': 20,
    'H': 10,
    'I': 35,
    'J': 60,
    'K': 70,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 20,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 17,
    'Y': 20,
    'Z': 21,
}

_VALUE_OFFERS = {
    'A': {3: 130, 5: 200},
    'B': {2: 45},
    'H': {5: 45, 10: 80},
    'K': {2: 120},
    'P': {5: 200},
    'Q': {3: 80},
    'V': {2: 90, 3: 130}
}

_FREE_ITEM_OFFERS = {
    'E': {2: 'B'},
    'F': {3: 'F'},
    'N': {3: 'M'},
    'R': {3: 'Q'},
    'U': {4: 'U'}
}


# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus):
    """
    Accepts a string of all SKUs for a basket and returns the basket value.
    Returns -1 if any invalid SKUs are passed in.

    Params
    ------
    skus: string, e.g. unicode (ABCDCBAABCABBAAA)

    Returns
    -------
    int, anything above -1 inclusive
    """
    basket = Counter(skus)
    basket_value = 0

    for sku in list(basket.keys()):
        if sku not in _SKU_PRICE:
            return -1

    _handle_free_items(basket=basket)

    basket_value += _calculate_basket_value(basket=basket,
                                            basket_value=basket_value)

    return basket_value


def _handle_free_items(basket):
    """
    This helper function handles any "free item" offers.

    Items are removed from the basket directly.
    Examples:
        If 2 Es are found, one B is removed.
        If 3 Fs are found then an F is removed.

    Params
    ------
    basket: dict
    """
    for sku in list(basket.keys()):
        if sku in _FREE_ITEM_OFFERS:
            offers = _FREE_ITEM_OFFERS[sku]
            for vol in sorted(offers, reverse=True):
                if offers[vol] in basket:
                    full_deals = basket[sku] // vol
                    basket[offers[vol]] -= full_deals


def _calculate_basket_value(basket, basket_value):
    """
    Returns the total value of the basket including all deals expect for
    free items.

    Params
    ------
    basket: dict, Keys are SKUs, these are paired to the total count for this
        sku
    basket_value: int

    Returns
    -------
    basket_value: int
    """
    basket_value += _handle_bundle_offer(basket=basket,
                                         basket_value=basket_value,
                                         bundle=_STXYZ_BUNDLE)

    for sku in list(basket.keys()):
        if sku in _VALUE_OFFERS:
            offers = _VALUE_OFFERS[sku]
            for vol in sorted(offers, reverse=True):
                full_deals = basket[sku] // vol
                if full_deals > 0:
                    basket_value += offers[vol] * full_deals
                    basket[sku] -= vol * full_deals

        basket_value += _SKU_PRICE[sku] * basket[sku]

    return basket_value


def _handle_bundle_offer(basket, basket_value, bundle):
    """
    Handles bundle offers.

    Params
    ------
    basket: dict, Keys are SKUs, these are paired to the total count for this
        sku
    basket_value: int
    bundle: Bundle object, contains the required volume for the offer to work
        and the relevant items.

    Returns
    -------
    basket_value: int
    """
    item_queue = []
    for x in bundle.items:
        if x in basket:
            item_queue.extend([x] * basket[x])

    num_of_bundle_items = len(item_queue)
    num_of_bundles = num_of_bundle_items // bundle.required_vol

    while num_of_bundles > 0:
        for i in range(bundle.required_vol):
            sku = item_queue.pop(0)
            basket[sku] -= 1
        basket_value += 45
        num_of_bundles -= 1

    return basket_value


