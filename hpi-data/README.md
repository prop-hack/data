# UK House Price Index Data
This data is taken from [Land Registry Public Data](https://www.gov.uk/government/publications/hm-land-registry-data/public-data "Land Registry") and is meant to provide developers with an easy single place and programmatic access to the data as well as schema guidelines to store and process them.

The UK House Price data shows changes in the value of residential properties across the UK. The HPI is calculated based on the actual sold value (after conveyancing) according to Land Registry, which differs from others who may base it on asking prices.

*Contains HM Land Registry data © Crown copyright and database right 2019. This data is licensed under the Open Government Licence v3.0.*

## What tools are available
1. The `hpi-downloader` is a command line tool for downloading different HPI data in **CSV** format

## How to run the downloader
The general format for running this script is:

```hpi-downloader.py <type-of-data> -p [published]```

The type is required, running help will show you the supported types of data you can download.

The published date is optional and if not provided it will default to one (check the script help command). This date value usually means all data up to the published date has been used to produce the HPI data.

All the dates should be in **YYYY-MM** format and files are downloaded in **CSV** format.

If you get a 404 error, it generally means the data for that period is not available.

You can also run the help option at anytime:

```trans-downloalder.py --help```

## What the data means

Below is a snippet taken from [Land Registry](https://www.gov.uk/government/publications/about-the-uk-house-price-index/about-the-uk-house-price-index#data-tables) that explains the definition of acronyms and the column headers.

**The acronyms detail as:**

- FTB: first time buyer
- FOO: former owner occupier

**CSV Header Information:**

| Column Header	| Explanation |
| --------------|------------ |
| Date | The year and month to which the monthly statistics apply |
| RegionName | Name of geography (Country, Regional, County/Unitary/District Authority and London Borough) |
| AreaCode | Code of geography (Country, Regional, County/Unitary/District Authority and London Borough) |
| Average Price | Average house price for a geography in a particular period |
| Index	| House price index for a geography in a particular period (January 2015=100). |
| IndexSA |	Seasonally adjusted house price for a geography in a particular period |(January 2015=100).
| 1m%change | The percentage change in the Average Price compared to the previous month |
| 12m%change | The percentage change in the Average Price compared to the same period twelve months earlier. |
| AveragePricesSA | Seasonally adjusted Average Price for a geography in a particular period |
| Sales Volume | Number of registered transactions for a geography in a particular period |
| [Property Type]Price | Average house price for a particular property type (such as detached houses), for a geography in a particular period. |
| [Property Type]Index | House price index for a particular property type (such as detached houses), for a geography in a particular period (January 2015=100). |
| [Property Type]1m%change | The percentage change in the [Property Type] Price (such as detached houses) compared to the previous month |
| [Property Type]12m%change | The percentage change in the [Property Type] Price (such as detached houses) compared to the same period twelve months earlier. |
| [Cash/Mortgage]Price | Average house price by funding status (such as cash), for a geography in a particular period. |
| [Cash/Mortgage]Index | House price index by funding status (such as cash), for a geography in a particular period (January 2015=100). |
| [Cash/Mortgage]1m%change | The percentage change in the [Cash/Mortgage]Price compared to the previous month |
| [Cash/Mortgage]12m%change | The percentage change in the [Cash/Mortgage]Price compared to the same period twelve months earlier. |
| [Cash/Mortgage] Sales Volume | Number of registered transactions [Cash/Mortgage] for a geography in a particular period |
| [FTB/FOO]Price | Average house price by buyer status (such as first time buyer/former owner occupier), for a geography in a particular period. |
| [FTB/FOO]Index | House price index by buyer status (such as first time buyer/former owner occupier), for a geography in a particular period. (January 2015=100). |
| [FTB/FOO]1m%change | The percentage change in the [FTB/FOO]Price compared to the previous month |
| [FTB/FOO]12m%change | The percentage change in the [FTB/FOO]Price compared to the same period twelve months earlier. |
| [New/Old]Price | Average house price by property status (such as new or existing property), for a geography in a particular period. |
| [New/Old]Index | House price index by property status (such as new or existing property), for a geography in a particular period. (January 2015=100). |
| [New/Old]1m%change | The percentage change in the [New/Old]Price compared to the previous month |
| [New/Old]12m%change | The percentage change in the [New/Old]Price compared to the same period twelve months earlier. |
| [New/Old] Sales Volume | Number of registered transactions [New/Old] for a geography in a particular period |
