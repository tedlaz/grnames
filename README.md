# grnames

A rest api to generate lists of fake Greek names, surnames, vat and social security numbers

the api generates:

1. names, male or female (from a list of ~1000 Greek names according to Greek population frequency)
2. surnames
3. Father names
4. Mother names
5. VAT number (algorithmically valid)
6. Social Security Number (algorithmically valid)

for testing purposes **only**.

Usage example:

> docker run -d -p 8000:8000 --name grnames tedlaz/grnames

To get a list of 10 entries in json format:

> http://localhost:8000/v1/greek_names_generator

For a specific number of entries:

> http://localhost:8000/v1/greek_names_generator?number=50

![grnamesUsage](https://i.imgur.com/Z3aqre8.gif)

Have fun !
