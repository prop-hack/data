# Local Places Data

This is Google Places integration for finding local information for any given location.
The data is retrieved using a script and the output is in a JSON format, suitable for saving to a file.

## What tools are available
1. The `get-local-places` is a command line tool that retrieves local places data for a given point.

## Notes on Schema
No schema is provided here as you may not necessarily want to store them permanently and retrieve these details on a real time basis only. If you do want to store them, then it is recommended to use a short to long term caching strategy so your data is not too stale.

## How to run the downloader

The `get-local-places.py` script requires a Google API key which you can get from their account dashboard.
Once you have the key you can either provide it as a parameter to the script or set is an environment variable called `GOOGLE_API_KEY`.

The general format for running this script is:

```get-local-places.py <lat> <long> [-p PAGE] [-k KEY]```

The provided key will override the environment variable and the page parameter is for retrieving the next page
of results for the same query. If there are multiple pages the output will provide a next page token which you can pass in here.