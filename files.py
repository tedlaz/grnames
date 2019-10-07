"""File functions"""


import hashlib
import os
import zipfile
import urllib.request as ur
from collections import namedtuple
from functools import lru_cache
BUF_SIZE = 65536


def fsha1(filepath):
    """Check sha1 of the file

    :param filepath: file path
    :return: sha1 string
    """
    sha1 = hashlib.sha1()
    with open(filepath, 'rb') as fil:
        while True:
            data = fil.read(BUF_SIZE)
            if not data:
                break
            sha1.update(data)
    return sha1.hexdigest()


def download_file(url, directory, lazy=True):
    """Download file url from internet

    :param url:
    :param directory:
    :param lazy: If file exists and lazy=True do nothing
    :return:
    """
    from tedutil.logger import logger
    filename = url.split('/')[-1]
    *front, last = filename.split('.')
    oldfront = '.'.join(front) + '.' + 'old'
    oldfilename = '.'.join([oldfront, last])
    olddirfile = os.path.join(directory, oldfilename)
    dirfile = os.path.join(directory, filename)
    if os.path.exists(dirfile):
        if not lazy:
            os.rename(dirfile, olddirfile)
            logger.info(fsha1(olddirfile))
            ur.urlretrieve(url, dirfile)
            logger.info("%s exists but you asked to download again." % dirfile)
            logger.info(fsha1(dirfile))
        else:
            logger.info("%s already exists. I am lazy ;-)" % dirfile)
        return dirfile
    ur.urlretrieve(url, dirfile)
    logger.info(fsha1(dirfile))
    logger.info("%s downloaded!!!" % dirfile)
    return dirfile


@lru_cache()
def zipfile_data(zip_file, filename, encoding='CP1253'):
    """

    :param zip_file: zip file name
    :param filename: file name inside zip file
    :param encoding: encoding
    :return: text lines
    """
    with zipfile.ZipFile(zip_file) as zfile:
        with zfile.open(filename) as fname:
            fdata = fname.read().decode(encoding)
    return fdata.split('\n')


def create_zip(txt_data, zip_filename, filename='JL10', encoding='CP1253'):
    with zipfile.ZipFile(zip_filename, 'w') as file:
        file.writestr(filename, txt_data.encode(encoding))


def read_csv_file(filename, stripper='|', encoding="utf8"):
    with open(filename, encoding=encoding) as file:
        file_data = file.read()
    data = list()
    for line in file_data.split('\n'):
        if line.startswith(' ') or len(line) < 3:
            continue
        data.append(tuple(i.strip() for i in line.split(stripper)))
    return data


def read_named_csv_file(filename, splitter='|', encoding="utf8"):
    """

    :param filename: csv filename with first row containing field names
    :param splitter: split character
    :param encoding: file encoding
    :return: list of named tuples
    """
    with open(filename, encoding=encoding) as file:
        file_data = file.read()
    data = list()
    data_iter = iter(file_data.split('\n'))
    field_names = [i.strip() for i in next(data_iter).split(splitter)]
    Row = namedtuple('Row', field_names)
    for line in data_iter:
        if line.startswith(' ') or len(line) < 3:
            continue
        data.append(Row(*[i.strip() for i in line.split(splitter)]))
    return data


def file2data(file_name, encoding='utf8'):
    with open(file_name, encoding=encoding) as fil:
        data = fil.read()
    return data


def write2file(data, file_name, encoding='utf8'):
    with open(file_name, 'w', encoding=encoding) as fil:
        fil.write(data)
