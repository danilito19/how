from load_data import get_rent_data

home_rent = get_rent_data('60615', 'RZSF')
work_rent = get_rent_data('60601', 'RZSF')

def calc_best_rent(home_rent, work_rent):
    '''
    Function to compare rent value at home and near work
    and return True if home rent is lower
    '''

    return home_rent < work_rent

print calc_best_rent(home_rent, work_rent)