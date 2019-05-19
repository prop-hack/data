# Transaction Data

Transaction data from
[Land Registry Public Data](https://www.gov.uk/government/publications/hm-land-registry-data/public-data "Land Registry")

This data has information about the number and type of applications that are completed each month. See below to understand what type of applications are covered.

The information is divided into data showing all applications completed, transactions for value, by region and local authority district. Transactions for value include freehold and leasehold sales.

We have created tools to easily download the Land Registry data you need, either a single file or bulk data from a date range. There are sample SQL schema files to get you started in putting this into a Database.

*Contains HM Land Registry data © Crown copyright and database right 2019. This data is licensed under the Open Government Licence v3.0.*

## What tools are available
1. The `trans-downloader` is a command line tool for downloading transaction data in **CSV** format
2. The `schema` is a SQL table definition that can load the transaction data. Only designed for regional and local authority data.

## How to run the downloader
The general format for running this script is:

```trans-downloader.py <type-of-data> -s [start-date] -e [end-date]```

The type is required, running help will show you the supported types of data you can download.

Date is optional and if you do not specify a date then it will attempt to download this month's data. You can download a range of data by specifiying a start and end date, the downloaded data will be split in to multiple monthly files.

To download a single month, you can just specify the start date.

All the dates should be in **YYYY-MM** format and files are downloaded in **CSV** format.

If you get a 404 error, it generally means the data for that period is not available.

You can also run the help option at anytime:

```trans-downloalder.py --help```

## Schema File
The provided SQL will create a normalised schema for holding this transaction data.

There are two tables, one for storing the actual transaction data and another table for storing the application definitions. The schema will populate the application definitions, letting you populate the main table with the CSV data using the downloader tool.

## What the data means

This data uses abbreviations, here is a snippet from [Land Registry](https://www.gov.uk/guidance/hm-land-registry-transaction-data) with all the definitions.

| Acronym |	Title | Description |
| --------|-------|-------------|
| DFL |	Dispositionary first lease | An application for the registration of a new lease granted by the proprietor of registered land |
| DLG | Dealing | An application in respect of registered land. This includes transfers of title, charges and notices |
| FR | First registration | An application for a first registration of land both freehold and leasehold. For leasehold this applies when the landlord’s title is not registered |
| TP | Transfer of part | An application to register the transfer of part of a registered title |
| OS(W) | Search of whole | An application to protect a transaction for value, such as purchase, lease or charge for the whole of a title |
| OS(P) | Search of part | An application to protect a transaction for value, such as purchase, lease or charge for part of a title |
| OS(NPW) |	Non-priority search of whole | An application to search the whole of the register without getting priority |
| OS(NPP) | Non-priority search of part | An application to search a part of the register without getting priority |
| OC1 | Official copy | An application to obtain an official copy of a register or title plan represents a true record of entries in the register and extent of the registered title at a specific date and time. The data includes historical editions of the register and title plan where they are kept by the registrar in electronic form |
| OC2 | Official copy of a deed or document | An application to obtain a copy of a document referred to in the register or relates to an application. This includes correspondence, surveys, application forms and emails relating to applications that are pending, cancelled or completed |
| SIM | Search of the index map | An application to find out whether or not land is registered and, if so, to obtain the title number |
