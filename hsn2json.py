#!/usr/bin/env python3

"""
License: GPLv3 https://www.gnu.org/licenses/gpl-3.0-standalone.html

Summary:
========
Convert the hsn/sac spreadhseet provided by the GST portal
into valid json file

Contributors
============
Sai Karthik <kskarthik@disroot.org>
"""

import requests, io, json, openpyxl, os, re, shutil

try:

    print("📡 Getting HSN/SAC file from GST portal ...")

    r = requests.get("https://tutorial.gst.gov.in/downloads/HSN_SAC.xlsx").content
    b = io.BytesIO(r)
    wb = openpyxl.load_workbook(b)
    hsn = wb["HSN"]
    sac = wb["SAC"]
    hsn_array = []
    sac_array = []

    print("⚙ Extracting HSN/SAC from the spreadsheet ...")
    for i in hsn.values:
        if i[0] != "HSN Code":
            try:
                # remove white spaces in between, for some codes
                sanitized_code_string = re.sub(r"\s+", "", str(i[0]), flags=re.UNICODE)
                hsn_array.append({"code": int(sanitized_code_string), "desciption": i[1]})
            except:
                print(type(i[0]), type(i[1]))
                raise

    for i in sac.values:
        if i[0] != "SAC Code":
            try:
                sac_array.append({"code": int(i[0]), "description": i[1]})
            except:
                print(i[0], i[1])
                raise

    print("HSN codes: ", len(hsn_array))
    print("SAC codes: ", len(sac_array))

    print("Total: ", len(hsn_array) + len(sac_array))

    print("Creating HSN/SAC json files ...")
    # create json/ directory
    try:
        os.mkdir("json")
    except:
        shutil.rmtree("json")
        os.mkdir("json")
    # generate hsn code json
    with open("json/hsn-codes.json", "w") as f:
        json.dump(hsn_array, f)
    # generate SAC codes json
    with open("json/sac-codes.json", "w") as f:
        json.dump(sac_array, f)
    # join SAC & HSN arrays
    hsn_array.extend(sac_array)
    # generate a json file with both hsn & sac codes
    with open("json/hsn-sac-codes.json", "w") as f:
        json.dump(hsn_array, f)

except Exception as e:
    print(e)
