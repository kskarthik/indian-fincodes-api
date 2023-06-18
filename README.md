# GST Utils

This repository provides HSN & SAC codes, gst news of Indian GST as json, csv. Generated using gitlab's CI/CD infra.
Data is refreshed every day, using gitlab's pipeline schedules.

Base URL: https://kskarthik.gitlab.io/gst-utils

## Endpoints

- `/hsn-codes.json`: HSN codes json
- `/sac-codes.json`: SAC codes json
- `/hsn.csv`: HSN codes as csv
- `/sac.csv`: SAC codes as csv

## Examples

Get the response using curl

```sh
curl https://kskarthik.gitlab.io/gst-utils/sac-codes.json
```

Download the csv with wget

```sh
wget https://kskarthik.gitlab.io/gst-utils/hsn.csv
```

## Schema

For hsn/sac json files

```json
{
  "code": "description"
}
```

## GST News

`/news/summary.json` - Contains gst news summary from portal as an array of objects

Schema:

```json
[
    {
      "id": integer,
      "title": string,
      "order": integer,
      "date": string,
      "IsExternal": string,
      "linkURl": null
    },
]
```

`/news/{id}.json` - Contains detailed news info, where {id} is the key of a news object in `summary.json`

Schema:

```json
{
  "content": string,
  "refID": integer,
  "title": string,
  "date": string
}
```

#### Example:

For summary of news:

```sh
curl https://kskarthik.gitlab.io/gst-utils/news/summary.json
```

For each news item in detail:

```sh
curl https://kskarthik.gitlab.io/gst-utils/news/588.json
```
