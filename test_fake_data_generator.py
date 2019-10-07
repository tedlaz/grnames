from fake_data_generator import generate_all


if __name__ == "__main__":
    fil = 'grnames.zip'
    print(generate_all(fil, number=10, age_from=25, age_to=60, center=35, density=3))
