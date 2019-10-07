"""Greek VAT validation functions"""


def is_afm(afm):
    """Algorithmic check for greek vat numbers (afm

    :param afm: Greek Vat Number (9 digits)
    :return: True / False
    """
    afm = str(afm)
    if len(afm) != 9 or not afm.isdigit():
        return False
    tot = sum([(int(afm[i]) * (2 ** (8 - i))) for i in range(8)])
    check = (tot % 11) % 10
    return check == int(afm[8])
