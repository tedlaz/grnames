"""Various functions for tax purposes"""
from dec import dec
from dec import klimaka
from dec import relu
from dec import slide_add
from dec import dec2float_dic
from tax_data import TAX_DATA


def children_reduction(children, ekptosi_foroy_paidion):
    """first=[1000, 2000, 10000], after=1000
        children_reduction(2, first, after) = 2000
        children_reduction(4, first, after) = 11000
        first: Λίστα με ποσό ανά παιδί (Το 1ο ποσό για το 1ο παιδί,
               το 2ο ποσό για το 2ο παιδί κλπ)
        after: Ποσό που αντιστοιχεί σε κάθε εξτρα παιδί αφού τελειώσει η first
    """
    children = int(children)
    if ekptosi_foroy_paidion is None:
        return 0
    first, after = ekptosi_foroy_paidion
    if children <= 0:
        return 0
    lfirst = len(first)
    if lfirst == 0:
        return children * after
    if lfirst >= children:
        return first[children-1]
    return first[-1] + (children - lfirst) * after

# Πριν το 2002 το νόμισμα ήταν η δραχμή


def meiosi_foroy(income, meiosi, paidia):
    """Meiosi foroy"""
    len_mf = len(meiosi['max-meiosi-foroy'])
    if len_mf >= (paidia + 1):
        max_meiosi_foroy = meiosi['max-meiosi-foroy'][paidia]
    else:
        max_meiosi_foroy = meiosi['max-meiosi-foroy'][-1]
    if income <= meiosi['income-limit']:
        return max_meiosi_foroy
    yperbainon = relu(income - meiosi['income-limit'])
    aa1 = yperbainon // meiosi['bima-income']
    aa2 = 1 if yperbainon % meiosi['bima-income'] else 0
    meiosi_meiosis = (aa1 + aa2) * meiosi['bima-meiosis-foroy']
    return relu(max_meiosi_foroy - meiosi_meiosis)


def calc_period_tax(year, income, children=0, barytis=14, extra=0):
    """Calculates tax for period

    :param year: year
    :param apodoxes: period income
    :param children: number of children
    :param barytis: period slice
    :param extra: extra income (current period only)
    :return: period tax payable
    """
    income = dec(income)
    extra = dec(extra)
    yearly = income * barytis
    tyearly = (income * barytis) + extra
    tforos = calc_tax(year, tyearly, children)
    foros = calc_tax(year, yearly, children)
    tax_delta = tforos['tax'] - foros['tax']
    wtax_delta = tforos['wtax'] - foros['wtax']
    tforos['period_normal_income'] = income
    tforos['period_extra'] = extra
    tforos['period_total_income'] = income + extra
    tforos['barytis'] = barytis
    tforos['period_tax_normal'] = dec(foros['tax'] / dec(barytis))
    tforos['period_tax_extra'] = tax_delta
    tforos['period_tax'] = tforos['period_tax_normal'] + tax_delta
    tforos['period_wtax_normal'] = dec(foros['wtax'] / dec(barytis))
    tforos['period_wtax_extra'] = wtax_delta
    tforos['period_wtax'] = tforos['period_wtax_normal'] + wtax_delta
    return tforos


def calc_tax(year, income, children=0):
    """
    Παίρνουμε από το TAX_DATA τα δεδομένα της χρήσης και το γεμίζουμε
    με τα αποτελέσματα των υπολογισμών
    """
    # Καθαρισμός μεταβλητών εισόδου
    year = int(year)
    income = dec(income)
    children = int(children)
    data = TAX_DATA.get(year, None)
    if not data:
        return {'error': f'Δεν υπάρχουν δεδομένα για το έτος {year}'}
    data['etos'] = year
    data['forologiteo'] = income
    data['paidia'] = children
    data['klimaka-foroy-f'] = data['klimaka-foroy']
    # Αύξηση του αφορολόγητου ορίου
    if 'pros-klimakas-foroy' in data:
        data['klimaka-foroy-f'] = slide_add(
            data['klimaka-foroy'],
            children_reduction(children, data['pros-klimakas-foroy'])
        )
    # Υπολογισμός φόρου με βάση την τελική κλίμακα φόρου
    data['foros-klimakas'] = klimaka(
        data['forologiteo'], data['klimaka-foroy-f'], data['pososta-foroy'])
    data['foros-poy-analogei'] = data['foros-klimakas']
    # Μείωση φόρου μισθωτών/συνταξιούχων(Μετά την κατάργηση του αφορολόγητου)
    if 'meiosi-foroy-p' in data:
        data['meiosi-foroy'] = meiosi_foroy(data['forologiteo'],
                                            data['meiosi-foroy-p'], children)
        data['foros-poy-analogei'] = relu(
            data['foros-poy-analogei'] - data['meiosi-foroy'])
    # Μείωση φόρου λόγω παιδιών (πριν από το 2003)
    if 'klimaka-ekptosis-foroy-paidion' in data:
        data['ekptosi-foroy-paidion'] = children_reduction(
            children,
            data.get('klimaka-ekptosis-foroy-paidion', None),
        )
        data['foros-poy-analogei'] = relu(data['foros-klimakas'] -
                                          data['ekptosi-foroy-paidion'])
    # Παρακράτηση φόρου
    data['ekptosi-parakratithentos-foroy'] = dec(
        dec(data.get('syntelestis-ekptosis', 0), 3) * data['foros-poy-analogei'])
    data['foros-poy-parakratithike'] = data['foros-poy-analogei'] - \
        data['ekptosi-parakratithentos-foroy']
    # Εισφορά Αληλλεγγύης
    data['eea'] = dec(0)
    if 'klimaka-eea' in data:
        data['eea'] = klimaka(
            data['forologiteo'], data['klimaka-eea'], data['pososta-eea']
        )
    # Συνολικό φορολογικό κόστος
    data['total-tax'] = data['foros-poy-parakratithike'] + data['eea']
    return dec2float_dic(data)


if __name__ == '__main__':
    for i in range(2002, 2020):
        print(calc_tax(i, 12000, 1))
