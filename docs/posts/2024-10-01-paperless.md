---
layout: default
title: Paperless NHS
---

The NHS has committed to replacing paper medical records with digital records several times, but this has not happened.

We can see the persistence of paper records by looking at how much NHS trusts say they are spending on medical records storage in their [annual estates return](https://digital.nhs.uk/data-and-information/publications/statistical/estates-returns-information-collection).

Read our findings below - and get involved!

## Contents

- [Headline findings](#headline-findings)
- [See how your trust compares](#table)
- [See a map](#map)
- [See the analysis and raw data](#analysis)
- [Get involved!](#contribute)

## Headline findings

- NHS Trusts in England still spend nearly **£250 million a year** on storing and handling medical records.
- This total is going up - meaning spending on medical records storage is set to be more than **£1 billion** in this Parliament.
- Some Trusts are especially high spenders - out of 200 Trusts, the top 10 account for nearly a quarter of all spending.
- The rollout of Electronic Patient Records (EPR) systems is patchy and Trusts with EPRs may still have significant storage costs.

<div class="flourish-embed flourish-chart" data-src="visualisation/20840143"><script src="https://public.flourish.studio/resources/embed.js"></script><noscript><img src="https://public.flourish.studio/visualisation/20840143/thumbnail" width="100%" alt="chart visualization" /></noscript></div>

## <span id="table">See how your trust compares</span>

<div class="flourish-embed flourish-table" data-src="visualisation/20545557"><script src="https://public.flourish.studio/resources/embed.js"></script><noscript><img src="https://public.flourish.studio/visualisation/20545557/thumbnail" width="100%" alt="table visualization" /></noscript></div>

## <span id="map">See trusts on a map</span>
 
<div class="flourish-embed flourish-map" data-src="visualisation/20763444"><script src="https://public.flourish.studio/resources/embed.js"></script><noscript><img src="https://public.flourish.studio/visualisation/20763444/thumbnail" width="100%" alt="map visualization" /></noscript></div>

## <span id="analysis">See the analysis and raw data</span>

If you just want the raw combined medical records costs data, you can [find it here](https://raw.githubusercontent.com/regulate-tech/nhstech/refs/heads/main/subject-mrc/data/output/trust_mrc_clean.csv).

Our notebooks show how we did this analysis:

1. [Collect ERIC data](https://github.com/regulate-tech/nhstech/blob/main/subject-mrc/1_obtain_eric_data.ipynb) - Collects and combines data on spending.
2. [Add other data](https://github.com/regulate-tech/nhstech/blob/main/subject-mrc/2_add_other_data.ipynb) - Join this with other data on trust EPR sytems and catchment populations.
3. [Analyse the findings (1)](https://github.com/regulate-tech/nhstech/blob/main/subject-mrc/3_exploratory_analysis.ipynb) - top-level analysis of the findings.
4. [Analyse the findings (2)](https://github.com/regulate-tech/nhstech/blob/main/subject-mrc/4_further_analysis.ipynb) - further analysis, diving into individual trusts.
5. [Explore site data](https://github.com/regulate-tech/nhstech/blob/main/subject-mrc/5_site_and_pfi_analysis.ipynb) - explore site-level spending data.
6. [Output data](https://github.com/regulate-tech/nhstech/blob/main/subject-mrc/6_output_flourish_data.ipynb) - output clean data for visualisations.

The data visualisations are all made in [Flourish](https://flourish.studio/).

The data sources we use are as follows:

1. [Medical records spending](https://digital.nhs.uk/data-and-information/publications/statistical/estates-returns-information-collection) - Official statistics from NHS Digital, the Estates Returns Information Collection. These are official statistics produced an annual return from NHS trusts covering their operational costs, including spending on medical records storage. 
2. [Trust populations](https://www.eastsussexjsna.org.uk/resources/nhs-acute-hospital-trust-catchment-populations/) - Experimental statistics produced by the Office for Health Improvement and Disparities. These are modelled estimates of the catchment populations for hospital provider trusts in England.
3. Trust locations - Trust locations are mapped via postcodes in the [Organisation Data Service](https://www.odsdatasearchandexport.nhs.uk/) and latlngs in the [NHS Postcode Directory](https://www.datadictionary.nhs.uk/supporting_information/nhs_postcode_directory.html?hl=nhspd).

## <span id="health-warnings">Health Warnings</span>

- NHS Trusts are often reorganised so some changes over time may reflect changes in the make-up of the Trust rather than individual sites doing things differently.
- We are relying on the central guidance on which costs to include in returns and the central quality control process for assurance that the data from Trusts is consistent and comparable. 
- We are only showing the top level data from the returns in this analysis and have not yet sourced more detailed data from individual Trusts.
- The guidance says to include costs of storing records from medical trials which are likely to be subject to particular retention regulations.

## <span id="contribute">Get involved!</span>

There are many good people doing great work improving the way in which technology is used in health and care and this project aims to support rather than undermine their efforts.

This analysis is intended as a contribution to the broad debate around the best ways for the UK health and care systems to implement and use electronic patient records systems.

These are some of the questions that we think would be interesting to explore further :-
- What does this spending look like at Trust level? What is it being spent on and who is providing the services?
- What is relationship between this spending and spending on EPRs? Does it decrease/increase/stay the same when an EPR is introduced?
- How much of the spending relates to historical records and how much to the ongoing production of paper medical records?
- Are there examples of Trusts digitising old paper records and how does this stack up in terms of costs and savings?

We are offering all of our working up in the hope that others will find this useful and want to build on and/or challenge it.  You may feel confident to do some of this further analysis yourself and, if so, please do share it with us.

Or you have may not be confident doing your own analysis but have information that would help us to understand what is happening and where to look for other useful data, and, if so, please do get in touch.

You can contact us by email to nhstech [AT] ricallan.uk
