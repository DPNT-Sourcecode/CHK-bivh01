from collections import defaultdict, Counter

_SKU_PRICE_TABLE = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15
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
    int
    """
    basket = Counter(skus)
    basket_value = 0

    if set(basket.keys()) == set(skus.split('')):
        return -1



        # TODO add condition for special offers



