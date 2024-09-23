# Locating addresses in the UK

Buildings where health and care services are being delivered in the UK will commonly be identified by an address that consists of 3 to 4 lines of text and a postcode.

There are several methods we can use to find the precise coordinates for addresses to locate them relative to each other and any boundaries.

## UPRN and AddressBase

The UK Government has created a standard for more precise addressing by allocating a [Unique Property Reference Number](https://www.geoplace.co.uk/addresses-streets/location-data/the-uprn) (UPRN) to each property.

The definitive method for finding a UPRN and precise coordinates for a property from an address is to use [a service called AddressBase](https://www.ordnancesurvey.co.uk/products/addressbase).

The AddressBase service is provided by OrdnanceSurvey and offered as a charged-for product to anyone not in the public sector.

Public sector organisations should be able to access AddressBase without further charge on the back of a cross-government license.

## Google Maps

The Google Maps API will return lat/long coordinates for UK addresses and Google's own building identifier.

Google offers credits for the Maps API to Google Cloud users allowing for a few thousand lookups for free.

Google provides a [cost calculator](https://mapsplatform.google.com/pricing/) for large volume geocoding exercises.

## OpenStreetMap

It is possible to geocode against the OpenStreetMap database where the addresses have been recorded by OSM.

Coverage is not likely to be sufficient nationally in the UK but you get a sense of [how good it is for specific areas here](https://osm.mathmos.net/addresses/pc-stats/).
