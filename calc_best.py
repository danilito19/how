from data import load_gas_data, load_rent_data

# home_rent = load_rent_data.get_rent_data('60615', 'RMP')
# work_rent = load_rent_data.get_rent_data('60601', 'RMP')
# gas_price = load_gas_data.get_gas_price('60615')

def calc_best(home_rent, work_rent, gas_price, miles, mpg):
    '''
    Function to calculate if it is cheaper to live near work
    and not commute (using cost of gas and miles to drive) or to
    live farther out and commute. 

    Miles is one way to work. This calculates monthly cost of gas
    for miles driven and specified car's mpg.

    Returns True if living at home (farther away from work) and
    commuting is cheaper. 
    '''
    return home_rent + ((miles * 40) / mpg *gas_price) < work_rent

#print calc_best(home_rent, work_rent, gas_price, 10, 10)