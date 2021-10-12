# (GLEIF) Data Parser/Loader

GLEIF provides open, standardized and high quality legal entity reference data. 
Use this for making your own NER model.

The list of fileds:
- lei
- legal_name
- first_address_line 
- city
- ..

## Description
- parse gleif.xml files ( file size > 2GB)
- validation using pydantic
- import data to PostgreSQL

## Tech
- [Python 3.9]
- [Pydantic]
- [SqlAlchemy]

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

## Usage

Download data file from official source. Then you need to set DATABASE_URI variable.

Install the dependencies

```sh
pip install -r requirements
```

Add data filepath to main.py

```sh
gleif_data('<filepath>')
```

## TODO
- pydantic: postgres dns validation

**Free Software, Hell Yeah!**

