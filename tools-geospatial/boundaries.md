# UK Boundaries and Lookups

If we want to analyse health and care services by geographic area, we need to be able to link locations to service delivery areas.

Fortunately, the Office for National Statistics (ONS) has a very good [Open Geography Portal](https://geoportal.statistics.gov.uk/) which offers free downloads of most of the data we want.

## Health Area Boundaries

UK public services are frequently reorganised and the ONS usually provides data files in common geographical information system formats for any newly agreed sets of boundaries. 

The ONS provides a [handy guide to UK geographies](https://geoportal.statistics.gov.uk/datasets/d1f39e20edb940d58307a54d6e1045cd/about) that is worth reading as a primer.

There is [a section within the portal that lists all boundary datasets associated with health](https://geoportal.statistics.gov.uk/search?q=BDY_HLT) (161 of them as of Sept 2024).

For health and care in England, we are interested in the Integrated Care Board areas which are provided at 4 different resolutions.

BUC - Boundary Ultra-generalised Clipped - lowest resolution (500m)
BSC - Boundary Super-generalisd Clipped - low resolution (200m)
BGC - Boundary Generalised Clipped - general resolution (20m)
BFC - Boundary Full resolution Clipped - highest resolution

ONS Boundary file sometimes end in 'C' for Clipped which means they are mapped to the high water mark of any coastline, and sometimes in 'E' which means they extend to the full Extent of the realm, ie include offshore areas.

Each of the datasets can be downloaded in various formats that are useful with different geographical information systems (GIS) and can be requested via API calls.

## Linking Services to Boundaries

The ONS also provides [a dataset called NHSPD](https://geoportal.statistics.gov.uk/search?q=PRD_NHSPD) linking postcodes to NHS boundaries that will allow most UK addresses to be associated with NHS organisations.


