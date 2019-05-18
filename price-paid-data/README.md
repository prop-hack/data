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

- Price paid
- Address
    - Postcode
    - Building Name / Number
    - Street
    - Town or City
    - District
    - County
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
