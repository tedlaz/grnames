import hug
from fake_data_generator import generate_all


@hug.get(versions=1)
def greek_names_generator(number:hug.types.number=10):
    """Returns a list of Greek fake name, surname, algorithmic valid vat and social security number"""
    fil = 'grnames.zip'
    return generate_all(
        fil, number=number, age_from=25, age_to=60, center=35, density=3)
