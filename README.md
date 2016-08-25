# wescml
Water and Energy Supply and Consumption info model - A data standard for water and energy supply and consumption

##About 

The Water and Energy Supply and Consumption (WESC) data standard has been developed by CSIRO to support a common represention of data for supply and consumption of water and energy and its delivery via standardised OGC services.

The [WESC information model](http://wescml.org/#info-model) allows for data to be delivered in a consistent format and is the basis for the exchange format (XML schemas) for encoding datasets.

A key component of WESC is the set of agreed and shared [WESC vocabularies](http://wescml.org/vocab/) used to encode the content for each XML instance, such as result method used to measure a meter reading and units of measure.

Tools have been developed to support use of WESCML and to help data custodians deploy data infrastructure configured for WESCML. [docker-geoserver](https://github.com/CSIRO-enviro-informatics/docker-geoserver/) allows data custodians to create a deployment of Geoserver using Docker containerization technologies. [wesc-sf0-node](https://github.com/CSIRO-enviro-informatics/wesc-sf0-node) extends docker-geoserver with configurations of the WESCML-SF0 data model so that data custodians can plug in their WESC datasets and deliver them via WESCML and standardised OGC web services at a push of a button thus speeding up and easing the process of data provision.

See also [wescml.org](http://wescml.org#overview) for an overview.

##Suggested citations of the info model

- Simons, Bruce; Yu, Jonathan (2015): WESCML Information Model. v1. CSIRO. Data Collection. [http://doi.org/10.4225/08/574D1DEEA50DD](http://doi.org/10.4225/08/574D1DEEA50DD)
- Simons, Bruce; Yu, Jonathan; Leighton, Benjamin (2016): [WESCML: A Data Standard for Exchanging Water and Energy Supply and Consumption Data](http://dx.doi.org/10.1016/j.proeng.2016.07.451), 12th International Hydroinformatics Conference, Incheon, South Korea, August 2016., IWA. [dx.doi.org/10.1016/j.proeng.2016.07.451](http://dx.doi.org/10.1016/j.proeng.2016.07.451)

## Related papers

- Yu, Jonathan; Leighton, Ben; Mirza, Fareed; Singh, Ramneek. [Tools for enabling rapid deployment of water and energy consumption and supply data services](http://www.mssanz.org.au/modsim2015/C8/yu.pdf). In: MODSIM 2015; 29/11/15 to 4/12/15; Gold Coast, Queensland, Australia. Modelling and Simulation Society of Australia and New Zealand (MSSANZ); 2015. pp. 781-787.
- Yu, Jonathan; Lipkin, Felix; Moglia, Magnus. [Novel spatial analysis of residential resource consumption via the Melbourne train network](http://www.mssanz.org.au/modsim2015/M4/yu.pdf). In: Weber, T.; McPhee, M.J.; Anderssen, R.S., editor/s. MODSIM 2015; 29/11/15 to Friday 4/12/15; Gold Coast, Queensland, Australia. Modelling and Simulation Society of Australia and New Zealand (MSSANZ); 2015. p. 1188-1194.
- Yu, Jonathan; Inman, Matthew; Simons, Bruce. Protocols to integrate URBAN water data with energy and other sectors within AURIN. In: Ozwater 15; 12 - 14 May 2015; Adelaide. Australian water Association; 2015. 7pp.
