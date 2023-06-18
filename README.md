# GST Utils

This repository provides HSN & SAC codes, gst news of Indian GST as json, csv. Generated using gitlab's CI/CD infra.
Data is refreshed every day, using gitlab's pipeline schedules.

Base URL: https://kskarthik.gitlab.io/gst-utils

## Endpoints

- `/hsn-codes.json`: Contains an array of hsn code as objects

- `/sac-codes.json`: Contains an array of sac code as objects
- `/hsn.csv`: HSN codes as csv
- `/sac.csv`: SAC codes as csv

Schema for all hsn/sac json files:

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
