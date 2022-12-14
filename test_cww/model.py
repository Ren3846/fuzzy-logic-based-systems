input_lvs = [
    {
        'X': (0, 101, 1),
        'name': 'Age',
        'terms': {
            'young': {'umf': ('trapmf', 0, 0, 0.55, 4.61), 'lmf': ('trapmf', 0, 0, 0.09, 1.15, 1)},
            'adult': {'umf': ('trapmf', 0.42, 2.25, 4.00, 5.41), 'lmf': ('trapmf', 2.79, 3.21, 3.21, 0.34, 3.71)},
            'middle age': {'umf': ('trapmf', 3.38, 5.50, 7.25, 9.02), 'lmf': ('trapmf', 5.79, 6.28, 6.28, 0.33, 6.67)},
            'old': {'umf': ('trapmf', 7.37, 9.36, 10, 10), 'lmf': ('trapmf', 8.68, 9.91, 10, 10, 1)},
        }
    },

    {
        'X': (0, 251, 1),
        'name': 'Height',
        'terms': {
            'little': {'umf': ('trapmf', 0, 0, 0.55, 4.61), 'lmf': ('trapmf', 0, 0, 0.09, 1.15, 1)},
            'short': {'umf': ('trapmf', 0.42, 2.25, 4.00, 5.41), 'lmf': ('trapmf', 2.79, 3.21, 3.21, 0.34, 3.71)},
            'average': {'umf': ('trapmf', 3.38, 5.50, 7.25, 9.02), 'lmf': ('trapmf', 5.79, 6.28, 6.28, 0.33, 6.67)},
            'tall': {'umf': ('trapmf', 7.37, 9.36, 10, 10), 'lmf': ('trapmf', 8.68, 9.91, 10, 10, 1)},
        }
    },

    {
        'X': (0, 50.01, 0.01),
        'name': 'Body type',
        'terms': {
            'thin': {'umf': ('trapmf', 0, 0, 0.55, 4.61), 'lmf': ('trapmf', 0, 0, 0.09, 1.15, 1)},
            'average': {'umf': ('trapmf', 0.42, 2.25, 4.00, 5.41), 'lmf': ('trapmf', 2.79, 3.21, 3.21, 0.34, 3.71)},
            'athletic': {'umf': ('trapmf', 3.38, 5.50, 7.25, 9.02), 'lmf': ('trapmf', 5.79, 6.28, 6.28, 0.33, 6.67)},
            'extra pound': {'umf': ('trapmf', 7.37, 9.36, 10, 10), 'lmf': ('trapmf', 8.68, 9.91, 10, 10, 1)},
        }
    },

    {
        'X': (0, 100_001, 1),
        'name': 'Income',
        'terms': {
            'low': {'umf': ('trapmf', 0, 0, 0.55, 4.61), 'lmf': ('trapmf', 0, 0, 0.09, 1.15, 1)},
            'medium': {'umf': ('trapmf', 0.42, 2.25, 4.00, 5.41), 'lmf': ('trapmf', 2.79, 3.21, 3.21, 0.34, 3.71)},
            'high': {'umf': ('trapmf', 3.38, 5.50, 7.25, 9.02), 'lmf': ('trapmf', 5.79, 6.28, 6.28, 0.33, 6.67)},
            'extremely high': {'umf': ('trapmf', 7.37, 9.36, 10, 10), 'lmf': ('trapmf', 8.68, 9.91, 10, 10, 1)},
        }
    }
]

output_lv = {
    'X': (0, 10.1, 0.1),
    'name': 'Attractive level',
    'terms': {
        'none to very little': {'umf': ('trapmf', 0, 0, 0.59, 3.95), 'lmf': ('trapmf', 0, 0, 0.09, 1.32, 1)},
        'very low': {'umf': ('trapmf', 0.28, 2.00, 3.00, 5.22), 'lmf': ('trapmf', 1.79, 2.37, 2.37, 2.71, 0.48)},
        'low': {'umf': ('trapmf', 0.98, 2.75, 4.00, 5.41), 'lmf': ('trapmf', 2.79, 3.30, 3.30, 3.71, 0.42)},
        'medium': {'umf': ('trapmf', 2.38, 4.50, 6.00, 8.18), 'lmf': ('trapmf', 4.79, 5.12, 5.12, 5.35, 0.27)},
        'above medium': {'umf': ('trapmf', 4.02, 5.65, 7.00, 8.41), 'lmf': ('trapmf', 5.89, 6.34, 6.34, 6.81, 0.40)},
        'high': {'umf': ('trapmf', 4.38, 6.50, 7.75, 9.62), 'lmf': ('trapmf', 6.79, 7.25, 7.25, 7.91, 0.47)},
        'extremely high': {'umf': ('trapmf', 5.21, 8.27, 10, 10), 'lmf': ('trapmf', 7.66, 9.82, 10, 10, 1)},
    }
}

rule_base = [
    (('young', 'short', 'thin', 'low'), 'medium'),
    (('young', 'short', 'thin', 'medium'), 'above medium'),
    (('young', 'short', 'thin', 'high'), 'very low'),
    (('young', 'short', 'thin', 'extremely high'), 'very low'),
    (('young', 'short', 'average', 'low'), 'above medium'),
    (('young', 'short', 'average', 'medium'), 'high'),
    (('young', 'short', 'average', 'high'), 'medium'),
    (('young', 'short', 'average', 'extremely high'), 'extremely high'),
    (('young', 'short', 'athletic', 'low'), 'above medium'),
    (('young', 'short', 'athletic', 'medium'), 'above medium'),
    (('young', 'short', 'athletic', 'high'), 'none to very little'),
    (('young', 'short', 'athletic', 'extremely high'), 'extremely high'),
    (('young', 'short', 'extra pound', 'low'), 'medium'),
    (('young', 'short', 'extra pound', 'medium'), 'low'),
    (('young', 'short', 'extra pound', 'high'), 'high'),
    (('young', 'short', 'extra pound', 'extremely high'), 'medium'),
    (('young', 'average', 'thin', 'low'), 'low'),
    (('young', 'average', 'thin', 'medium'), 'high'),
    (('young', 'average', 'thin', 'high'), 'very low'),
    (('young', 'average', 'thin', 'extremely high'), 'high'),
    (('young', 'average', 'average', 'low'), 'none to very little'),
    (('young', 'average', 'average', 'medium'), 'very low'),
    (('young', 'average', 'average', 'high'), 'extremely high'),
    (('young', 'average', 'average', 'extremely high'), 'medium'),
    (('young', 'average', 'athletic', 'low'), 'above medium'),
    (('young', 'average', 'athletic', 'medium'), 'high'),
    (('young', 'average', 'athletic', 'high'), 'none to very little'),
    (('young', 'average', 'athletic', 'extremely high'), 'medium'),
    (('young', 'average', 'extra pound', 'low'), 'low'),
    (('young', 'average', 'extra pound', 'medium'), 'none to very little'),
    (('young', 'average', 'extra pound', 'high'), 'high'),
    (('young', 'average', 'extra pound', 'extremely high'), 'none to very little'),
    (('young', 'tall', 'thin', 'low'), 'high'),
    (('young', 'tall', 'thin', 'medium'), 'above medium'),
    (('young', 'tall', 'thin', 'high'), 'very low'),
    (('young', 'tall', 'thin', 'extremely high'), 'extremely high'),
    (('young', 'tall', 'average', 'low'), 'above medium'),
    (('young', 'tall', 'average', 'medium'), 'low'),
    (('young', 'tall', 'average', 'high'), 'extremely high'),
    (('young', 'tall', 'average', 'extremely high'), 'very low'),
    (('young', 'tall', 'athletic', 'low'), 'none to very little'),
    (('young', 'tall', 'athletic', 'medium'), 'very low'),
    (('young', 'tall', 'athletic', 'high'), 'extremely high'),
    (('young', 'tall', 'athletic', 'extremely high'), 'low'),
    (('young', 'tall', 'extra pound', 'low'), 'none to very little'),
    (('young', 'tall', 'extra pound', 'medium'), 'extremely high'),
    (('young', 'tall', 'extra pound', 'high'), 'low'),
    (('young', 'tall', 'extra pound', 'extremely high'), 'medium'),
    (('adult', 'short', 'thin', 'low'), 'none to very little'),
    (('adult', 'short', 'thin', 'medium'), 'very low'),
    (('adult', 'short', 'thin', 'high'), 'above medium'),
    (('adult', 'short', 'thin', 'extremely high'), 'medium'),
    (('adult', 'short', 'average', 'low'), 'extremely high'),
    (('adult', 'short', 'average', 'medium'), 'very low'),
    (('adult', 'short', 'average', 'high'), 'very low'),
    (('adult', 'short', 'average', 'extremely high'), 'extremely high'),
    (('adult', 'short', 'athletic', 'low'), 'low'),
    (('adult', 'short', 'athletic', 'medium'), 'extremely high'),
    (('adult', 'short', 'athletic', 'high'), 'low'),
    (('adult', 'short', 'athletic', 'extremely high'), 'very low'),
    (('adult', 'short', 'extra pound', 'low'), 'above medium'),
    (('adult', 'short', 'extra pound', 'medium'), 'high'),
    (('adult', 'short', 'extra pound', 'high'), 'high'),
    (('adult', 'short', 'extra pound', 'extremely high'), 'low'),
    (('adult', 'average', 'thin', 'low'), 'above medium'),
    (('adult', 'average', 'thin', 'medium'), 'medium'),
    (('adult', 'average', 'thin', 'high'), 'very low'),
    (('adult', 'average', 'thin', 'extremely high'), 'none to very little'),
    (('adult', 'average', 'average', 'low'), 'low'),
    (('adult', 'average', 'average', 'medium'), 'extremely high'),
    (('adult', 'average', 'average', 'high'), 'high'),
    (('adult', 'average', 'average', 'extremely high'), 'above medium'),
    (('adult', 'average', 'athletic', 'low'), 'above medium'),
    (('adult', 'average', 'athletic', 'medium'), 'above medium'),
    (('adult', 'average', 'athletic', 'high'), 'very low'),
    (('adult', 'average', 'athletic', 'extremely high'), 'very low'),
    (('adult', 'average', 'extra pound', 'low'), 'high'),
    (('adult', 'average', 'extra pound', 'medium'), 'very low'),
    (('adult', 'average', 'extra pound', 'high'), 'high'),
    (('adult', 'average', 'extra pound', 'extremely high'), 'none to very little'),
    (('adult', 'tall', 'thin', 'low'), 'none to very little'),
    (('adult', 'tall', 'thin', 'medium'), 'extremely high'),
    (('adult', 'tall', 'thin', 'high'), 'above medium'),
    (('adult', 'tall', 'thin', 'extremely high'), 'very low'),
    (('adult', 'tall', 'average', 'low'), 'low'),
    (('adult', 'tall', 'average', 'medium'), 'low'),
    (('adult', 'tall', 'average', 'high'), 'above medium'),
    (('adult', 'tall', 'average', 'extremely high'), 'low'),
    (('adult', 'tall', 'athletic', 'low'), 'above medium'),
    (('adult', 'tall', 'athletic', 'medium'), 'medium'),
    (('adult', 'tall', 'athletic', 'high'), 'low'),
    (('adult', 'tall', 'athletic', 'extremely high'), 'above medium'),
    (('adult', 'tall', 'extra pound', 'low'), 'above medium'),
    (('adult', 'tall', 'extra pound', 'medium'), 'none to very little'),
    (('adult', 'tall', 'extra pound', 'high'), 'medium'),
    (('adult', 'tall', 'extra pound', 'extremely high'), 'extremely high'),
    (('middle age', 'short', 'thin', 'low'), 'none to very little'),
    (('middle age', 'short', 'thin', 'medium'), 'extremely high'),
    (('middle age', 'short', 'thin', 'high'), 'high'),
    (('middle age', 'short', 'thin', 'extremely high'), 'above medium'),
    (('middle age', 'short', 'average', 'low'), 'medium'),
    (('middle age', 'short', 'average', 'medium'), 'high'),
    (('middle age', 'short', 'average', 'high'), 'extremely high'),
    (('middle age', 'short', 'average', 'extremely high'), 'high'),
    (('middle age', 'short', 'athletic', 'low'), 'extremely high'),
    (('middle age', 'short', 'athletic', 'medium'), 'medium'),
    (('middle age', 'short', 'athletic', 'high'), 'medium'),
    (('middle age', 'short', 'athletic', 'extremely high'), 'medium'),
    (('middle age', 'short', 'extra pound', 'low'), 'above medium'),
    (('middle age', 'short', 'extra pound', 'medium'), 'above medium'),
    (('middle age', 'short', 'extra pound', 'high'), 'none to very little'),
    (('middle age', 'short', 'extra pound', 'extremely high'), 'low'),
    (('middle age', 'average', 'thin', 'low'), 'very low'),
    (('middle age', 'average', 'thin', 'medium'), 'very low'),
    (('middle age', 'average', 'thin', 'high'), 'very low'),
    (('middle age', 'average', 'thin', 'extremely high'), 'none to very little'),
    (('middle age', 'average', 'average', 'low'), 'none to very little'),
    (('middle age', 'average', 'average', 'medium'), 'above medium'),
    (('middle age', 'average', 'average', 'high'), 'low'),
    (('middle age', 'average', 'average', 'extremely high'), 'high'),
    (('middle age', 'average', 'athletic', 'low'), 'none to very little'),
    (('middle age', 'average', 'athletic', 'medium'), 'low'),
    (('middle age', 'average', 'athletic', 'high'), 'medium'),
    (('middle age', 'average', 'athletic', 'extremely high'), 'very low'),
    (('middle age', 'average', 'extra pound', 'low'), 'very low'),
    (('middle age', 'average', 'extra pound', 'medium'), 'above medium'),
    (('middle age', 'average', 'extra pound', 'high'), 'very low'),
    (('middle age', 'average', 'extra pound', 'extremely high'), 'extremely high'),
    (('middle age', 'tall', 'thin', 'low'), 'none to very little'),
    (('middle age', 'tall', 'thin', 'medium'), 'very low'),
    (('middle age', 'tall', 'thin', 'high'), 'none to very little'),
    (('middle age', 'tall', 'thin', 'extremely high'), 'high'),
    (('middle age', 'tall', 'average', 'low'), 'none to very little'),
    (('middle age', 'tall', 'average', 'medium'), 'none to very little'),
    (('middle age', 'tall', 'average', 'high'), 'extremely high'),
    (('middle age', 'tall', 'average', 'extremely high'), 'medium'),
    (('middle age', 'tall', 'athletic', 'low'), 'medium'),
    (('middle age', 'tall', 'athletic', 'medium'), 'above medium'),
    (('middle age', 'tall', 'athletic', 'high'), 'low'),
    (('middle age', 'tall', 'athletic', 'extremely high'), 'high'),
    (('middle age', 'tall', 'extra pound', 'low'), 'above medium'),
    (('middle age', 'tall', 'extra pound', 'medium'), 'none to very little'),
    (('middle age', 'tall', 'extra pound', 'high'), 'very low'),
    (('middle age', 'tall', 'extra pound', 'extremely high'), 'none to very little'),
    (('old', 'short', 'thin', 'low'), 'extremely high'),
    (('old', 'short', 'thin', 'medium'), 'medium'),
    (('old', 'short', 'thin', 'high'), 'very low'),
    (('old', 'short', 'thin', 'extremely high'), 'none to very little'),
    (('old', 'short', 'average', 'low'), 'extremely high'),
    (('old', 'short', 'average', 'medium'), 'low'),
    (('old', 'short', 'average', 'high'), 'medium'),
    (('old', 'short', 'average', 'extremely high'), 'low'),
    (('old', 'short', 'athletic', 'low'), 'above medium'),
    (('old', 'short', 'athletic', 'medium'), 'none to very little'),
    (('old', 'short', 'athletic', 'high'), 'none to very little'),
    (('old', 'short', 'athletic', 'extremely high'), 'low'),
    (('old', 'short', 'extra pound', 'low'), 'low'),
    (('old', 'short', 'extra pound', 'medium'), 'medium'),
    (('old', 'short', 'extra pound', 'high'), 'above medium'),
    (('old', 'short', 'extra pound', 'extremely high'), 'above medium'),
    (('old', 'average', 'thin', 'low'), 'above medium'),
    (('old', 'average', 'thin', 'medium'), 'medium'),
    (('old', 'average', 'thin', 'high'), 'extremely high'),
    (('old', 'average', 'thin', 'extremely high'), 'very low'),
    (('old', 'average', 'average', 'low'), 'above medium'),
    (('old', 'average', 'average', 'medium'), 'none to very little'),
    (('old', 'average', 'average', 'high'), 'medium'),
    (('old', 'average', 'average', 'extremely high'), 'extremely high'),
    (('old', 'average', 'athletic', 'low'), 'low'),
    (('old', 'average', 'athletic', 'medium'), 'extremely high'),
    (('old', 'average', 'athletic', 'high'), 'above medium'),
    (('old', 'average', 'athletic', 'extremely high'), 'low'),
    (('old', 'average', 'extra pound', 'low'), 'medium'),
    (('old', 'average', 'extra pound', 'medium'), 'above medium'),
    (('old', 'average', 'extra pound', 'high'), 'very low'),
    (('old', 'average', 'extra pound', 'extremely high'), 'above medium'),
    (('old', 'tall', 'thin', 'low'), 'none to very little'),
    (('old', 'tall', 'thin', 'medium'), 'medium'),
    (('old', 'tall', 'thin', 'high'), 'none to very little'),
    (('old', 'tall', 'thin', 'extremely high'), 'medium'),
    (('old', 'tall', 'average', 'low'), 'none to very little'),
    (('old', 'tall', 'average', 'medium'), 'above medium'),
    (('old', 'tall', 'average', 'high'), 'high'),
    (('old', 'tall', 'average', 'extremely high'), 'very low'),
    (('old', 'tall', 'athletic', 'low'), 'low'),
    (('old', 'tall', 'athletic', 'medium'), 'very low'),
    (('old', 'tall', 'athletic', 'high'), 'above medium'),
    (('old', 'tall', 'athletic', 'extremely high'), 'extremely high'),
    (('old', 'tall', 'extra pound', 'low'), 'extremely high'),
    (('old', 'tall', 'extra pound', 'medium'), 'low'),
    (('old', 'tall', 'extra pound', 'high'), 'low'),
    (('old', 'tall', 'extra pound', 'extremely high'), 'none to very little'),
]
