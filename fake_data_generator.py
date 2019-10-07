"""Generators for Greek amka/afm for testing purposes"""
from random import randint
from random import choice
from random import choices
from datetime import datetime
from datetime import date
from datetime import timedelta
from collections import namedtuple
from amka import is_amka
from afm import is_afm
from files import zipfile_data


def load_names(zip_file, csv_file):
    """

    :param zip_file:
    :param csv_file:
    :return:
    """
    names = []
    frequency = []
    for lin in zipfile_data(zip_file, csv_file, "utf8"):
        if len(lin) < 3:
            continue
        name, freq, *_ = lin.strip().split(';')
        names.append(name)
        frequency.append(int(freq))
    return names, frequency


def load_surnames(zip_file, csv_file):
    """

    :param zip_file:
    :param csv_file:
    :return:
    """
    smnames = []
    sfnames = []
    for lin in zipfile_data(zip_file, csv_file, "utf8"):
        if len(lin) < 3:
            continue
        sna = lin.split()
        if len(sna) == 1:
            smnames.append(sna[0])
            sfnames.append(sna[0])
        else:
            smnames.append(sna[0])
            sfnames.append(sna[1])
    return smnames, sfnames


def distribution(alist, center, density=1):
    """

    :param alist:
    :param center:
    :param density:
    :return:
    """
    try:
        index_center = alist.index(center)
    except ValueError:
        index_center = len(alist) // 2
    left = alist[:index_center]
    right = alist[index_center+1:]
    len_left = len(left)
    len_right = len(right)
    mxl = max(len_left, len_right)
    stleft = [i+1 for i in range(mxl)][mxl-len_left:]
    rmxl = list(range(mxl))
    rmxl.reverse()
    stright = [i+1 for i in rmxl][:len_right]
    stleft.append(mxl+1)
    final = stleft + stright
    return [i**density for i in final]


def distribution_range(apo, eos, center=None, density=3):
    """

    :param apo:
    :param eos:
    :param center:
    :param density:
    :return:
    """
    points = list(range(apo, eos + 1))
    return points, distribution(points, center, density)


def generate_amka(year=None):
    """Greek social security number (amka) generator

    :return: algorithmically valid amka
    """
    mon = str(randint(101, 112))[1:]
    day = str(randint(101, 128))[1:]
    if year:
        yea = year
    else:
        yea = str(randint(100, 199))[1:]
    res = str(randint(10000, 10999))[1:]
    for i in range(10):
        num = '%s%s%s%s%s' % (day, mon, yea, res, i)
        if is_amka(num):
            return num


def generate_afm():
    """Greek tax number (afm) generator

    :return: algorithmically valid afm
    """
    no1 = str(randint(100000000, 999999999))[1:]
    for i in range(10):
        num = '%s%s' % (no1, i)
        if is_afm(num):
            return num


def generate_afms(number_of_afms):
    """Generate greek afms

    :param number_of_afms:
    :return:
    """
    afms = []
    for _ in range(number_of_afms):
        afms.append(generate_afm())
    return afms


def generate_dates(date_from, date_to, number_of_dates):
    fyear, fmonth, fday = [int(i) for i in date_from.split('-')]
    tyear, tmonth, tday = [int(i) for i in date_to.split('-')]
    dfrom = date(fyear, fmonth, fday)
    dto = date(tyear, tmonth, tday)
    delta = dto - dfrom
    dates = []
    for _ in range(number_of_dates):
        num = randint(0, delta.days)
        dat = dfrom + timedelta(days=num)
        dates.append(dat.isoformat())
    dates.sort()
    return dates


def generate_values(number_of_values, min_val, maxval):
    vals = []
    for _ in range(number_of_values):
        vals.append(randint(min_val, maxval) / 100)
    return vals


def generate_all(zip_file, number, age_from=18, age_to=65,
                 center=None, density=3):
    """Generate fake Greek persons with name, surname, father and mother name
        vat number, social sequrity number

    :param zip_file: zip file containing names, male/female
    :param number: Number of persons
    :param age_from: Minimum age
    :param age_to: Maximum age
    :param center: Mean age
    :param density: Variance
    :return:
    """
    year_now = datetime.now().year
    points, dist = distribution_range(age_from, age_to, center, density)
    # print(dist)
    years = [str(abs(i - year_now))[2:] for i in points]
    males, freq_males = load_names(zip_file, "smale.csv")
    females, freq_females = load_names(zip_file, "sfemale.csv")
    sur_males, sur_females = load_surnames(zip_file, "eponyma.csv")
    final_list = []
    for _ in range(number):
        mf = randint(0, 1)
        if mf == 0:
            nam = choices(males, freq_males)[0].capitalize()
            snam = choice(sur_males).capitalize()
        else:
            nam = choices(females, freq_females)[0].capitalize()
            snam = choice(sur_females).capitalize()
        father = choices(males, freq_males)[0].capitalize()
        mother = choices(females, freq_females)[0].capitalize()
        amka = generate_amka(choices(years, dist)[0])
        afm = generate_afm()
        while mother == nam:  # όχι ιδιο μητρώνυμο και όνομα
            mother = choices(females, freq_females)[0].capitalize()
        while father == nam:  # όχι ίδιο πατρώνυμο και όνομα
            father = choices(males, freq_males)[0].capitalize()
        epon = "%s %s" % (snam, nam)
        final_list.append({
            'name': nam,
            'surname': snam,
            'father': father,
            'mother': mother,
            'afm': afm,
            'amka': amka
        })
    return final_list


def generate_financial(date_from, date_to, number, afm_num,
                       min_value=1, max_value=100):
    """

    :param date_from:
    :param date_to:
    :param number:
    :param afm_num:
    :param min_value:
    :param max_value:
    :return:
    """
    afms = generate_afms(afm_num)
    dates = generate_dates(date_from, date_to, number)
    amounts = generate_values(number, min_value*100, max_value*100)
    vals = []
    Vals = namedtuple('Vals', "date par val afm")
    for i in range(number):
        afm = choice(afms)
        vals.append(Vals(dates[i], i + 1, amounts[i], afm))
    return vals
