# Indian Financial codes API ![docker ci badge](https://github.com/movim/movim/actions/workflows/docker.yml/badge.svg?event=push)

![image](https://github.com/kskarthik/indian-fincodes-api/assets/11899221/6f556c36-ec96-42fd-a016-20f3664b4c77)

This repository contains scripts which builds a REST API service in a docker image

The following data is provided:

- Pincodes [source](https://data.gov.in/catalog/all-india-pincode-directory)
- Banks [source](https://github.com/razorpay/ifsc/)
- HSN & SAC [source](https://services.gst.gov.in/services/searchhsnsac)

# How it's done
The data is fetched from various sources, processed and indexed to the [meilisearch](https://www.meilisearch.com) docker image & a new image is created from it & pushed to docker hub. All this process is automated using github actions.

# Links

- [Docker repo](https://hub.docker.com/r/kskarthik/indian-fincodes-api)
- [Meilisearch API Reference](https://www.meilisearch.com/docs/reference/api/overview)

# Usage

```sh
docker pull kskarthik/indian-fincodes-api:latest

# set MEILI_MASTER_KEY to your preferred value
docker run --rm -d \
  -p 7700:7700 \
  -e MEILI_MASTER_KEY='MASTER_KEY'\
  kskarthik/indian-fincodes-api:latest
```

To access the server, Visit `http://localhost:7700` in the browser

# Examples

Get the list of indexes:

```sh
curl http://localhost:7700/indexes 
{
  "results": [
    {
      "uid": "banks",
      "createdAt": "2024-03-27T10:57:53.787331548Z",
      "updatedAt": "2024-03-27T10:58:11.549315386Z",
      "primaryKey": "IFSC"
    },
    {
      "uid": "hsn_sac_codes",
      "createdAt": "2024-03-27T11:03:32.334812729Z",
      "updatedAt": "2024-03-27T11:03:34.449263657Z",
      "primaryKey": "id"
    },
    {
      "uid": "pincodes",
      "createdAt": "2024-03-27T11:03:16.545030985Z",
      "updatedAt": "2024-03-27T11:03:24.393231938Z",
      "primaryKey": "id"
    }
  ],
  "offset": 0,
  "limit": 20,
  "total": 3
}
```

Perform search on an index:

```sh
 curl -s -X POST 'http://localhost:7700/indexes/pincodes/search' \
 -H 'Content-Type: application/json' \
 --data-binary '{
    "q": "500001",
    "limit": 2
  }'

{
  "hits": [
    {
      "id": 4678,
      "officename": "Moazzampura S.O",
      "pincode": "500001",
      "officeType": "S.O",
      "Deliverystatus": "Non-Delivery",
      "divisionname": "Hyderabad City",
      "regionname": "Hyderabad City",
      "circlename": "Andhra Pradesh",
      "Taluk": "Nampally",
      "Districtname": "Hyderabad",
      "statename": "ANDHRA PRADESH"
    },
    {
      "id": 4704,
      "officename": "Seetharampet S.O",
      "pincode": "500001",
      "officeType": "S.O",
      "Deliverystatus": "Non-Delivery",
      "divisionname": "Hyderabad City",
      "regionname": "Hyderabad City",
      "circlename": "Andhra Pradesh",
      "Taluk": "Nampally",
      "Districtname": "Hyderabad",
      "statename": "ANDHRA PRADESH"
    }
  ],
  "query": "500001",
  "processingTimeMs": 0,
  "limit": 2,
  "offset": 0,
  "estimatedTotalHits": 213
}
```
