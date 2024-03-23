# Indian Fincodes API ![docker ci badge](https://github.com/movim/movim/actions/workflows/docker.yml/badge.svg?event=push)

![image](https://github.com/kskarthik/indian-fincodes-api/assets/11899221/6f556c36-ec96-42fd-a016-20f3664b4c77)

This repository contains scripts which builds a REST API service which currently gives access to the following codes:

- Pincodes
- Banks
- HSN & SAC

The data is fetched from various sources, processed and indexed to the [meilisearch](https://www.meilisearch.com) docker image & a new image is created from it & pushed to docker hub.

[Docker repo](https://hub.docker.com/r/kskarthik/indian-fincodes-api)

```sh
docker pull kskarthik/indian-fincodes-api:latest

# set MEILI_MASTER_KEY to your preferred value
docker run --rm -d \
  -p 7700:7700 \
  -e MEILI_MASTER_KEY='MASTER_KEY'\
  kskarthik/indian-fincodes-api:latest
```

To access the Web UI, Visit `http://localhost:7700` in the browser
