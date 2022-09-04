# GST JSON Files

This repository provides HSN & SAC codes of Indian GST as json files, Generated using gitlab's CI/CD infra

base_url: `htttps://kskarthik.gitlab.io/gst-json`

# Endpoints

- `/json/hsn-codes.json`: Returns a json which contains an array of hsn code as objects

Example:

```json
[
  {
    "code": `integer`,
    "desciption": `string`
  }
]
```

- `/json/sac-codes.json`: Returns a json which contains an array of sac code as objects

Example:

```json
[
  {
    "code": `integer`,
    "desciption": `string`
  }
]
```

- `/json/hsn-sac-codes.json`: Returns a json which contains an array of both hsn & sac code as objects

Example:

```json
[
  {
    "code": `integer`,
    "desciption": `string`
  }
]
```
