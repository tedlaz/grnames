import hug
from fake_data_generator import generate_all
from taxes import calc_tax


@hug.get('/greek_names_generator', versions=1)
@hug.local()
def greek_names_generator(number: hug.types.number = 10):
    """Returns a list of Greek fake name, surname,
    algorithmic valid vat and social security number"""
    fil = 'grnames.zip'
    return generate_all(
        fil, number=number, age_from=25, age_to=60, center=35, density=3)


@hug.get('/greek_tax', versions=1, examples='year=2002&income=15000&children=2')
@hug.local()
def greek_tax(year: hug.types.number,
              income: hug.types.number,
              children: hug.types.number = 0):
    """Returns greek tax given year, income and children"""
    return calc_tax(year, income, children)
