# WESC Vocabularies

Currently WESC vocabularies are deployed to a SISSVoc instance 
hosted by https:/wescml.org

Development and maintenance of vocabularies happen at 
http://registry.it.csiro.au/def/wesc/core

These are then reflected in the content in this directory as 
static snapshots.


## Deploying WESC vocabularies via SISSVoc

### docker-rdf4j

Run docker-compose.yml to spin up the RDF4J triple store.
It can then be used to host the WESC vocabularies.
```
$ docker-compose up -d
```

### elda/SISSVoc



