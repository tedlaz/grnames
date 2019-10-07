# grnames
A rest api to generate lists of fake Greek names, surnames, vat and social security numbers

the api generates:
1. names, male or female (from a list of ~1000 Greek names according to Greek population frequency) 
2. surnames 
3. VAT number (algorithmically valid)
4. Social Security Number (algorithmically valid)
for testing purposes.

Usage example:

>  docker run -d -p 8000:8000 --name grnames tedlaz/grnames

To get a list of 10 entries in json format: 
> http://localhost:8000/v1/greek_names_generator

For a sspecific number of entries:
> http://localhost:8000/v1/greek_names_generator?number=50

Have fun !
