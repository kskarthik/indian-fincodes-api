# GST JSON Files

This repository provides HSN & SAC codes, gst news of Indian GST as json files, Generated using gitlab's CI/CD infra.
Data is refreshed every 6 hours, using gitlab's pipeline schedules.

Base URL: https://kskarthik.gitlab.io/gst-json

## Endpoints

- `/json/hsn-codes.json`: Contains an array of hsn code as objects

- `/json/sac-codes.json`: Contains an array of sac code as objects

- `/json/hsn-sac-codes.json`: Contains an array of both hsn & sac code as objects

Schema for all hsn/sac json files:

```json
[
  {
    "code": integer,
    "desciption": string
  }
]
```

- `news/summary.json` - Contains gst news summary from portal as an array of objects

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

- `news/{id}.json` - Contains detailed news info, where {id} is the key of a news object in `summary.json`

Schema:

```json
{
  "content": string,
  "refID": integer,
  "title": string,
  "date": string
}
```
