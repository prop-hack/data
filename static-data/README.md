# Static Data
We have attempted to extract and separate out static data from the various property data available.
Currently this includes some of the regional and local authority data as well as postcode geo data.

By separating out these static data into separate tables, it allows us to better connect them with sources of property data from different sources and run analytics on this connected data.

There are static data loaders and table schema designs that can be used as a base for you to build upon.
More details on each data below.

## Region Data
This is taken from Land Registry where they often have regional separation on some of their data, e.g. Wales, Greater London, East Anglia etc.

Currently this is just pure static data without much geolocation information. One improvement would be to extend this table with geometry information that can plot the boundaries of each region, this will allow for enhanced geolocation based queries with other geo data such as postcodes.

## Local Authority
This is again extracted from Land Registry data that often have separation by Local Authority, these can be treated as location information as each Authority covers a certain geo area.

Similar advice to region data, extending this with geolocation information (longitude and latitude) will enhance geolocation based queries and connect it up to Region data.

## Area
This is also extracted from the Land Registry HPI data which has area and area code information.
See the hpi-data folder on how to extract this information from the HPI data CSV files.

Similar adive to region and local authority is to extend this table with geolocation information, either with latitude and longitude pointing to a central location or a geometry boundary specifying the area it covers.

## Postcode
Postcode data are inherently harder to get a hold of and there are various organisations that will keep different types of postcode data.
The one that we recommend which is available free to get is is the [Open Postcode Geo](https://www.getthedata.com/open-postcode-geo)

The schema file takes a simplified approach to store data based on the Open Postcode Geo but if you wish to have more postcode centric search and indexing then we recommend you take a look at their own SQL schema file. However we do recommend you use spatial data types and not float/decimal to maximise your geo handling capability.

## Tips
Re-iterating some tips and avice from before:
- Enhance static data with geolocation and boundary data
- Use Geo API or Map api services to extract this geolocation data
- Buy licencsed data that has all the UK and Scotland geo information
- There are some free services that provide a small subset of details such as: https://www.latlong.net/