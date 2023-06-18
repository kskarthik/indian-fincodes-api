#!/usr/bin/env python3

"""
License: GPLv3 https://www.gnu.org/licenses/gpl-3.0-standalone.html

Summary:
========
Convert the hsn/sac spreadhseet provided by the GST portal
into valid json file

Author
============
Sai Karthik <kskarthik@disroot.org>
"""

import io, json, openpyxl, os, shutil, csv
import requests as r

print("📡 Getting HSN/SAC file from GST portal ...")

res = r.get("https://tutorial.gst.gov.in/downloads/HSN_SAC.xlsx").content
b = io.BytesIO(res)
wb = openpyxl.load_workbook(b)
hsn = wb["HSN"]
sac = wb["SAC"]
hsn_dict = {}
sac_dict = {}


def export_json():
    try:
        print("⚙ Extracting HSN/SAC from the spreadsheet ...")
        for i in hsn.values:
            if i[0] != "HSN Code":
                try:
                    # remove white spaces in between, for some codes
                    # sanitized_code_string = re.sub(r"\s+", "", str(i[0]), flags=re.UNICODE)
                    hsn_dict[i[0]] = i[1]
                except:
                    print(i[0], type(i[0]), i[1], type(i[1]))
                    raise

        for i in sac.values:
            if i[0] != "SAC Code":
                try:
                    sac_dict[i[0]] = i[1]
                except:
                    print(i[0], type(i[0]), i[1], type(i[1]))
                    raise

        print("HSN codes: ", len(hsn_dict))
        print("SAC codes: ", len(sac_dict))

        print("Total: ", len(hsn_dict) + len(sac_dict))

        print("Creating HSN/SAC json files ...")
        # create json/ directory
        try:
            os.mkdir("public")
        except:
            shutil.rmtree("public")
            os.mkdir("public")
        # generate hsn code json
        with open("public/hsn-codes.json", "w") as f:
            json.dump(hsn_dict, f)
        # generate SAC codes json
        with open("public/sac-codes.json", "w") as f:
            json.dump(sac_dict, f)
        print("Generated the json files")
    except Exception as e:
        print(e)
        raise


def export_csv():
    with open("public/hsn.csv", "w", newline="") as csvfile:
        w = csv.writer(csvfile)
        for i in hsn.values:
            w.writerow([i[0], i[1]])

    with open("public/sac.csv", "w", newline="") as csvfile:
        w = csv.writer(csvfile)
        for i in sac.values:
            w.writerow([i[0], i[1]])
    print("Created CSV files")


portal = "https://www.gst.gov.in/fomessage/newsupdates/"
# use custom user agent, as the gst website does not seem to allow other programs
# to access their public api
custom_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}


# news from gst portal
def generate_posts(news_summary):
    """Generate a single json file for each item in summary"""
    for item in news_summary:
        response = r.get(url=portal + str(item["id"]), headers=custom_headers)
        if response.status_code == 200:
            with open(f"public/news/{item['id']}.json", "w") as f:
                json.dump(response.json()["data"][0], f)
        else:
            print("failed to generate post")


def generate_summary():
    """Create news items json file"""

    os.makedirs("public/news", exist_ok=True)
    # access the api
    news_summary = r.get(url=portal, headers=custom_headers)
    if news_summary.status_code == 200:
        with open("public/news/summary.json", "w") as f:
            json.dump(news_summary.json()["data"], f)

        generate_posts(news_summary.json()["data"])
        print("Generated News")
    else:
        print("failed to get summary")


export_json()
export_csv()
generate_summary()
