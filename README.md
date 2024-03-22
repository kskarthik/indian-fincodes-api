# Indian Fincodes API

This repository contains scripts which builds a REST API service which currently gives access to the following codes:

- Pincodes
- IFSC
- HSN & SAC

The data is fetched from various sources, processed and indexed to the [meilisearch](https://www.meilisearch.com) docker image & creates a new image.

[Docker repo](https://hub.docker.com/r/kskarthik/indian-fincodes)

```sh
docker pull kskarthik/indian-fincodes:latest

# set MEILI_MASTER_KEY to your preferred value
docker run --rm -d \
  -p 7700:7700 \
  -e MEILI_MASTER_KEY='MASTER_KEY'\
  kskarthik/indian-fincodes:latest
```

To access the Web UI, Visit `http://localhost:7700` in the browser
