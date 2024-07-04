from collections import Counter

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
    'K': 80,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 30,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 90,
    'Y': 10,
    'Z': 50,
}


_VALUE_OFFERS = {
    'A': {3: 130, 5: 200},
    'B': {2: 45},
    'H': {5: 45, 10: 80},
    'K': {2: 150},
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
    skus: string, eg unicode (ABCDCBAABCABBAAA)

    Returns
    -------
    int, anything above -1 inclusive
    """
    basket = Counter(skus)
    basket_value = 0

    for sku in list(basket.keys()):
        if sku not in _SKU_PRICE:
            return -1
        # Kept this separate as it needs to execute before second block
        _handle_free_items(basket, sku)

    for sku in list(basket.keys()):
        basket_value = _handle_value_offers(basket, basket_value, sku)

        basket_value += _SKU_PRICE[sku] * basket[sku]

    return basket_value


def _handle_value_offers(basket, basket_value, sku):
    if sku in _VALUE_OFFERS:
        offers = _VALUE_OFFERS[sku]
        for vol in sorted(offers, reverse=True):
            full_deals = basket[sku] // vol
            if full_deals > 0:
                basket_value += offers[vol] * full_deals
                basket[sku] -= vol * full_deals
    return basket_value


def _handle_free_items(basket, sku):
    if sku in _FREE_ITEM_OFFERS:
        offers = _FREE_ITEM_OFFERS[sku]
        for vol in sorted(offers, reverse=True):
            if offers[vol] in basket:
                full_deals = basket[sku] // vol
                basket[offers[vol]] -= full_deals




