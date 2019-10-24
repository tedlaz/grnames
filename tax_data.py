"""Φορολογικά δεδομένα ανά χρήση"""

TAX_DATA = {
    2002: {
        'klimaka-foroy': (7_400, 1_000, 5_000, 10_000),
        'pososta-foroy': (0, 5, 15, 30, 40),
        'klimaka-ekptosis-foroy-paidion': ((90, 210, 615, 960), 30),
        'syntelestis-ekptosis': 0.015,
        'comment': (
            'Υπόλογίζεται έκπτωση λόγω παιδιών κατευθείαν στο φόρο.'
        ),
    },
    2003: {
        'klimaka-foroy': (10_000, 3_400, 10_000),
        'pososta-foroy': (0, 15, 30, 40),
        'pros-klimakas-foroy': ((1_000, 2_000, 10_000), 1_000),
        'syntelestis-ekptosis': 0.015,
        'comment': (
            'Προσαυξάνεται το αφορολόγητο όριο με βάση τον αριθμό παιδιών.'
        ),
    },
    2004: {
        'klimaka-foroy': (10_000, 3_400, 10_000),
        'pososta-foroy': (0, 15, 30, 40),
        'pros-klimakas-foroy': ((1_000, 2_000, 10_000), 1_000),
        'syntelestis-ekptosis': 0.015,
        'comment': (
            'Ίδια κλίμακα με του 2003. '
        ),
    },
    2005: {
        'klimaka-foroy': (11_000, 2_000, 10_000),
        'pososta-foroy': (0, 15, 30, 40),
        'pros-klimakas-foroy': ((1_000, 2_000, 10_000), 1_000),
        'syntelestis-ekptosis': 0.015,
        'comment': (
            'Αλλαγή κλίμακας.'
        ),
    },
    2006: {
        'klimaka-foroy': (11_000, 2_000, 10_000),
        'pososta-foroy': (0, 15, 30, 40),
        'pros-klimakas-foroy': ((1_000, 2_000, 10_000), 1_000),
        'syntelestis-ekptosis': 0.015,
        'comment': (
            'Ίδια κλίμακα με του 2005. '
        ),
    },
    2007: {
        'klimaka-foroy': (12_000, 18_000, 45_000),
        'pososta-foroy': (0, 29, 39, 40),
        'pros-klimakas-foroy': ((1_000, 2_000, 10_000), 1_000),
        'syntelestis-ekptosis': 0.015,
        'comment': (
            'Αλλαγή κλίμακας και ποσοστών.'
        ),
    },
    2008: {
        'klimaka-foroy': (12_000, 18_000, 45_000),
        'pososta-foroy': (0, 27, 37, 40),
        'pros-klimakas-foroy': ((1_000, 2_000, 10_000), 1_000),
        'syntelestis-ekptosis': 0.015,
        'comment': (
            'Αλλαγή ποσοστών φόρου (Μείωση).'
        ),
    },
    2009: {
        'klimaka-foroy': (12_000, 18_000, 45_000),
        'pososta-foroy': (0, 25, 35, 40),
        'pros-klimakas-foroy': ((1_000, 2_000, 10_000), 1_000),
        'syntelestis-ekptosis': 0.015,
        'comment': (
            'Αλλαγή ποσοστών φόρου (Μείωση).'
        ),
    },
    2010: {
        'klimaka-foroy': (12_000, 4_000, 6_000, 4_000, 6_000, 8_000, 20_000, 40_000),
        'pososta-foroy': (0, 18, 24, 26, 32, 36, 38, 40, 45),
        'pros-klimakas-foroy': ((1_500, 3_000, 11_500), 2_000),
        'syntelestis-ekptosis': 0.015,
        'comment': (
            'Αλλαγή κλίμακας και ποσοστών φόρου.'
        ),
    },
    2011: {
        'klimaka-foroy': (5_000, 7_000, 4_000, 10_000, 14_000, 20_000, 40_000),
        'pososta-foroy': (0, 10, 18, 25, 35, 38, 40, 45),
        'pros-klimakas-foroy': ((2_000, 4_000), 3_000),
        'syntelestis-ekptosis': 0.015,
        'comment': (
            'Αλλαγή κλίμακας και ποσοστών φόρου.'
        ),
    },
    2012: {
        'klimaka-foroy': (5_000, 7_000, 4_000, 10_000, 14_000, 20_000, 40_000),
        'pososta-foroy': (0, 10, 18, 25, 35, 38, 40, 45),
        'pros-klimakas-foroy': ((2_000, 4_000), 3_000),
        'syntelestis-ekptosis': 0.015,
        'comment': (
            'Ίδια δεδομένα με του 2011.'
        ),
    },
    2013: {
        'klimaka-foroy': (25_000, 17_000),
        'pososta-foroy': (22, 32, 42),
        # 'pros-klimakas-foroy': ((2_000, 4_000), 3_000),
        'syntelestis-ekptosis': 0.015,
        'meiosi-foroy-p': {
            'max-meiosi-foroy': [2_100],
            'income-limit': 21_000,
            'bima-income': 1_000,
            'bima-meiosis-foroy': 100,
            'comment': (
                'Μέχρι εισόδημα 21.000 μείωση φόρου 2.100. '
                'Απο 21.000 και πάνω η μείωση φόρου μειώνεται κατά '
                '100 ευρώ για κάθε 1.000 ευρώ εισηδήματος μέχρι να μηδενιστεί.'
            )
        },
        'comment': (
            'Καταργήση αφορολόγητου. '
            'Κατάργηση έκπτωσης παιδιών. '
            'Μείωση φόρου για μισθωτούς/συνταξιούχους (max 2.100 ευρώ).'
        ),
    },
    2014: {
        'klimaka-foroy': (25_000, 17_000),
        'pososta-foroy': (22, 32, 42),
        'syntelestis-ekptosis': 0.015,
        'meiosi-foroy-p': {
            'max-meiosi-foroy': [2_100],
            'income-limit': 21_000,
            'bima-income': 1_000,
            'bima-meiosis-foroy': 100,
            'comment': (
                'Το ίδιο με το 2013. '
            )
        },
        'comment': (
            'Ίδιο με το 2013. '
        ),
    },
    2015: {
        'klimaka-foroy': (25_000, 17_000),
        'pososta-foroy': (22, 32, 42),
        'syntelestis-ekptosis': 0.015,
        'meiosi-foroy-p': {
            'max-meiosi-foroy': [2_100],
            'income-limit': 21_000,
            'bima-income': 1_000,
            'bima-meiosis-foroy': 100,
            'comment': (
                'Το ίδιο με το 2014. '
            )
        },
        'comment': (
            'Ίδιο με το 2014. '
        ),
    },
    2016: {
        'klimaka-foroy': (20_000, 10_000, 10_000),
        'pososta-foroy': (22, 29, 37, 45),
        'syntelestis-ekptosis': 0.015,
        'meiosi-foroy-p': {
            'max-meiosi-foroy': [1_900, 1_950, 2_000, 2_100],
            'income-limit': 20_000,
            'bima-income': 1_000,
            'bima-meiosis-foroy': 10,
            'comment': (
                'Αυξάνεται η μείωση του φόρου ανάλογα με τα παιδιά. '
                'Μέχρι εισόδημα 20.000 μείωση φόρου 1.900. '
                'Απο 21.000 και πάνω η μείωση φόρου μειώνεται κατά '
                '100 ευρώ για κάθε 1.000 ευρώ εισηδήματος μέχρι να μηδενιστεί.'
            )
        },
        'comment': (
            'Επανέρχεται η έκπτωση παιδιών στη μείωση του φόρου'
        ),
    },
    2017: {
        'klimaka-foroy': (20_000, 10_000, 10_000),
        'pososta-foroy': (22, 29, 37, 45),
        'syntelestis-ekptosis': 0.015,
        'meiosi-foroy-p': {
            'max-meiosi-foroy': [1_900, 1_950, 2_000, 2_100],
            'income-limit': 20_000,
            'bima-income': 1_000,
            'bima-meiosis-foroy': 10,
            'comment': (
                'Ίδιο με το 2016'
            )
        },
        'klimaka-eea': (12_000, 8_000, 10_000, 10_000, 25_000, 155_000),
        'pososta-eea': (0, 2.2, 5, 6.5, 7.5, 9, 10),
        'comment': (
            'Ίδιο με το 2016'
        ),
    },
    2018: {
        'klimaka-foroy': (20_000, 10_000, 10_000),
        'pososta-foroy': (22, 29, 37, 45),
        # 'syntelestis-ekptosis': 0.015, # Καταργήθηκε
        'meiosi-foroy-p': {
            'max-meiosi-foroy': [1_900, 1_950, 2_000, 2_100],
            'income-limit': 20_000,
            'bima-income': 1_000,
            'bima-meiosis-foroy': 10,
            'comment': (
                'Ιδιο με το 2017'
            )
        },
        'klimaka-eea': (12_000, 8_000, 10_000, 10_000, 25_000, 155_000),
        'pososta-eea': (0, 2.2, 5, 6.5, 7.5, 9, 10),
        'comment': (
            'Ίδιο με το 2017. '
            'Καταργήθηκε η έκπτωση 1,5% της παρακράτησης φόρου.'
        ),
    },
    2019: {
        'klimaka-foroy': (20_000, 10_000, 10_000),
        'pososta-foroy': (22, 29, 37, 45),
        # 'syntelestis-ekptosis': 0.015,   # Καταργήθηκε
        'meiosi-foroy-p': {
            'max-meiosi-foroy': [1_900, 1_950, 2_000, 2_100],
            'income-limit': 20_000,
            'bima-income': 1_000,
            'bima-meiosis-foroy': 10,
            'comment': (
                'Το ίδιο με το 2018'
            )
        },
        'klimaka-eea': (12_000, 8_000, 10_000, 10_000, 25_000, 155_000),
        'pososta-eea': (0, 2.2, 5, 6.5, 7.5, 9, 10),
        'comment': (
            'Ίδιο με το 2018'
        ),
    }
}
