# NHS Organisation Data Service (ODS)

## Scope

This method is useful to build a list of NHS organisations in ENGLAND.  Some organisations in WALES are also returned.

## Context

NHS Digital maintains a service called the Organisation Data Service which provides access to the definitive directories of NHS organisations in England.

It is worth consulting their [Standards Repository document](https://digital.nhs.uk/binaries/content/assets/website-assets/services/ods/odsstandards.pdf) for information about the different datasets available.

We can use this service to create lists of organisations of interest for our analysis of the ICTs they are using, eg finding all the organisations that have a relationship with a particular Integrated Care Board (ICB).

## Methods

There are 4 methods for obtaining a list of organisations from the definitive NHS Organisation Data Service.

### 1 - download pre-bundled CSV files

As of Sept 2024, CSV files are still being issued on a quarterly basis for core data sets and can be found at (https://digital.nhs.uk/services/organisation-data-service/export-data-files/csv-downloads)

The service has announced that it intends to retire this method in favour of using the search page as described in method 2 but there is not a fixed date for this as of 24/09/2024.

To build your directory, you will need to list the datasets of interest and find the filename for each of these, eg the file for GPs is called epraccur.csv and can be found at [this link](https://files.digital.nhs.uk/assets/ods/current/epraccur.zip)

The downloads are ZIP files that contain the data in a CSV file (eg approx 3.5MB for the GP list) and a PDF file describing the data.

### 2 - generate your own CSV file from the search page

The preferred method going forward is to use the new search and export service at (https://www.odsdatasearchandexport.nhs.uk/).

This includes an option for obtaining files like the epraccur.csv file that was previously offered as a download.

To try this go the main page, select 'Reports' on the top menu bar, scroll through the drop-down list to find 'epraccur \(Prescribing Cost Centres, including GP Practices\)', and choose 'Download as CSV \(including headers\)' from the Export button on the top right of the output list.

### 3 - programmatic access via the API

You can find information about gettng data at
(https://digital.nhs.uk/services/organisation-data-service/organisation-data-service-apis/choosing-an-organisation-data-service-api)

Organisation data can be obtained from the Organisation Reference Data \(ORD\) API.  NB there is [a section on rate limits](https://digital.nhs.uk/developer/guides-and-documentation/reference-guide#rate-limits) that is important to check before accessing this service.

### 4 - pulling data from the Technology Reference Update Distribution (TRUD)

NHS Digital provides a service that allows you to pull information about releases of datasets.

This has the catchy acronym TRUD \(Technology Reference Update Distribution\) and you can register for it at (https://isd.digital.nhs.uk/trud/users/guest/filters/0/home)

NHS Digital provides [guidance on building a baseline dataset](https://digital.nhs.uk/services/organisation-data-service/organisation-data-service-apis/technical-guidance-ord/creating-a-baseline) that recommends using the TRUD service for building a baseline dataset.

There are tools to help you use this baseline data XML file at (https://digital.nhs.uk/services/organisation-data-service/organisation-data-service-apis/technical-guidance-ord/xml-organisation-data-products-support-products-and-tools)
