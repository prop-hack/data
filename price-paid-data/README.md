# England and Wales Price Paid Data
This data is taken from [Land Registry Public Data](https://www.gov.uk/government/publications/hm-land-registry-data/public-data "Land Registry") and is meant to provide developers with an easy single place and programmatic access to the data as well as schema guidelines to store and process them.

The Price Paid data shows all property sales within England and Wales that were lodged with the Land Registry.

*Contains HM Land Registry data © Crown copyright and database right 2019. This data is licensed under the Open Government Licence v3.0.*

## What tools are available
1. The `pp-downloader` is a command line tool for downloading price paid data in **CSV** format

## How to run the downloader
The general format for running this script is:

```price-paid-downloader.py <type-of-data> -s [start-year] -e [end-year]```

The date is optional and will default to the current year. You can pass in a date range of several years and it will download the yearly files for that period. To download a single specific year, just specify the start year only.

All the dates should be in **YYYY** format and files are downloaded in **CSV** format.

If you get a 404 error, it generally means the data for that period is not available.

You can also run the help option at anytime:

```price-paid-downloader.py --help```

## What the data means

The data contains the following information:

- Date of Transfer
- Price paid
- Property Type (as a single character)
    - Detached (D)
    - Semi-Detached (S)
    - Terraced (T)
    - Flat/Maisonette (F)
    - Other (O)
- New Build (as a Y/N value)
- Estate Type (as a single character)
    - Freehold (F)
    - Leasehold (L)
- Address
    - Postcode
    - Primary Name / Number
    - Secondary Name / Number
    - Street
    - Town or City
    - District
    - County
- Category Type
    - A = Standard Price Paid entry, includes single residential property sold for full market value.
    - B = Additional Price Paid entry including transfers under a power of sale/repossessions, buy-to-lets (where they can be identified by a Mortgage) and transfers to non-private individuals.
- Record Status
    - A = Addition
    - C = Change
    - D = Delete

## Note on Record Status
It is important to use the Record Status in the CSV to update your stored data based on the Land Registry guidelines below:

**A** - Added records: records added into the price paid dataset in the monthly refresh due to new sales transactions

**C** - Changed records: records changed in the price paid dataset in the monthly refresh. You should replace or update records in any stored data using the unique identifier to recognise them

**D** - Deleted records: records deleted from the price paid dataset in the monthly refresh. You should delete records from any stored data using the unique identifier to recognise them.
