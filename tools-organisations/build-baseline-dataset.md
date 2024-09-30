# Building a Baseline Organisation Dataset

## CONTEXT

We want to analyse the ICTs being used by a variety of different health and care organisations.

We can create our own database of relevant organisations to support this analysis and then update this over time.

We are not running a real-time, operational system so periodic updates are fine for our purposes.

This document describes the process for obtaining an initial dataset of organisations who have records in a central repository.

For more information on the various sources of data see [this document](ods.md)

## STEP 1 - register for the Technology Reference Update Distribution (TRUD) service

You can do this here - https://isd.digital.nhs.uk/trud/users/guest/filters/0/home

## STEP 2 - subscribe to the Organisation Data Service (ODS) downloads.

Once you have a TRUD account you will see various datasets listed on the left side of the page including one labelled "Organisation Data Service and Spine Directory Service".

Clicking on this will take you to a page where you will see listed a dataset called "ODS XML Organisation Data".

Click on this and you will see a list of inactive datasets with a "Subscribe" link above this.  Once you have subscribed then the datasets will become clickable. https://isd.digital.nhs.uk/trud/users/authenticated/filters/0/categories/5/items/341/releases

## STEP 3 - download the master XML file

The datasets are listed with the most recent at the top and have clickable links that will start the file download in your browser.  

The filename is in the format "hscorgrefdataxml_data_x.y.z_YYYYMMDD000001.zip" where x.y.z is the release number, eg for the Sept 2024 release the file is called "hscorgrefdataxml_data_9.0.0_202409D27000001.zip".

This will fetch a ZIP file of around 34MB to your local machine.

## STEP 4 - extract the master XML file

You can extract the contents of the downloaded ZIP file using whichever tool is handy for your local machine (most modern operating systems have some kind of UNZIP tool built in).

The first stage of extraction produces two more ZIP files called fullfile.zip and archive.zip. 

To build our baseline directory, we want to extract fullfile.zip into a suitable working directory noting that the extracted data will be a single very large XML file of around 585MB for the Sept 2024 release.

We might rename the file for convenience when running command line tools late, eg to ods_base.xml

## STEP 5 - get the tools to pull data from the XML file into CSV files

You can run routines with this large XML file if that is your preferred method and you have a suitably powerful machine.

For this project, we generally prefer to store data in CSV files for simplicity of manipulation using multiple tools and for their human-readability.

The TRUD team offers a tool written in Java for creating CSV files from the XML files that we have tested and seems to do the job.

This tool can be found from the TRUD ODS page in a section called "ODS XML Organisation Data supporting products" - https://isd.digital.nhs.uk/trud/users/authenticated/filters/0/categories/5/items/343/releases

You will again need to "Subscribe" to this product to enable the download links. Once you are subscribed you can pull a file in the format hscorgrefdataxml_support_x.y.z_YYYYMMDD000001.zip where x.y.z is the version number, eg hscorgrefdataxml_support_14.0.0_20240426000001.zip for the current version as of 30th Sept 2024.

Download this file (approx 16MB) to a suitable working directory.

There are several useful documents and tools within the ZIP file that are worth extracting for later processes.  For the CSV file creation process we want to extract the ZIP file called "transform.zip" into our working directory.

There is another layer of ZIP file nesting with the tools we want contained within a file called HSCOrgRefData_xlst.zip in the transform directory.

With that file extracted, we can rename the HSCOrgRefData_xlst to something easier like ods_csv for convenience.

There are two more layers of directory to get to the actual tool called "saxon" and "Java" where you will find "saxon9he.jar".

This Java file should run on any machine with a standard Java Runtime Environment and we have tested it on Linux within a Chromebook.

## STEP 6 - run the CSV file extraction process

For convenience, we can put the XML file and the Java file into a single working directory, eg ods_xml_csv

We drop our extracted master XML file into this, eg ods_base.xml, and a copy of the saxon9he.jar file.

We also need to drop in an XML transformation file called HSCOrgRefData_xmltocsv.xslt that is found in the extracted "transform" ZIP file.

Now we can run this from the command line where we have Java Runtime Environment installed for our platform (a quick check that JRE is available is to run "java -version" at the command line and this should return some info on your install.  If it fails then you should check how to install JRE on your device).

There is a guide to the command line options bundled into the ZIP file called HSCOrgRefData_XMLtoCSVSupportDocumentation.pdf

This is a command line version that we found works at a Linux prompt on a Chromebook. It assumes that the XML data file, the Java executable and the XSLT template file are all in the same directory.

java -jar saxon9he.jar -t -s:ods_base.xml -xsl:HSCOrgRefData_xmltocsv.xslt

## STEP 9 - find and use the extracted CSV files

The output configuration is Windows-y and hardcoded in but still runs on a Linux system. We found the above command line created a directory in root called "'\\\\C:'" and the process created a subdirectory of this called "HSCOrgRefData" where all the CSV files were written.

We can move all the CSV files to the directory where we want them for further processing and analysis and delete this oddly formatted output directory, eg "mv HSCOrgRefData /home/MY_USER_NAME"

There should be 10 CSV files with a total file size of less than 200MB.











