#!/usr/bin/env python3

"""
License: 
========
GPLv3 https://www.gnu.org/licenses/gpl-3.0-standalone.html

Summary
=======
This file contains functions which fetch the codes from 
various sources, format the data & index them to the API server.

Author
======
Sai Karthik <kskarthik@disroot.org>
"""

import io
import meilisearch
import openpyxl
import csv
import requests as r
import requests
import threading
import time

client = meilisearch.Client("http://127.0.0.1:7700", "masterKey")

def index_ifsc_codes():
    "Checks for latest release of IFSC codes from razorpay/ifsc repo & downloads the latest one"
    try:
        api = "https://api.github.com/repos/razorpay/ifsc/releases?per_page=1"

        print("📡 Fetching the latest IFSC release ...")

        r = requests.get(api)

        if r.status_code == 200:
            body = r.json()

            latest_csv_url = body[0]["assets"][3]["browser_download_url"]

            print("⚙ Downloading", body[0]["tag_name"])

            r = requests.get(latest_csv_url)

            if r.status_code == 200:
                try:
                    raw_data = csv.DictReader(io.StringIO(r.text))
                    csv_list = []
                    for bank in raw_data:
                        csv_list.append(bank)

                    client.index("banks").add_documents(csv_list, primary_key="IFSC")
                    print(f"Indexed {len(csv_list)} IFSC codes")
                except Exception as e:
                    print("indexing err:", e)
            else:
                print("failed to download the csv")
        else:
            print("failed to connect with github API")

    except Exception as e:
        print(e)

def index_pin_codes():
    try:
        print("📡 Fetching the latest pincodes file from the gov.in portal ...")
        res = r.get("https://data.gov.in/files/ogdpv2dms/s3fs-public/dataurl31052019/Pincode_30052019.csv").text
        with open("pincodes.csv", "wt") as f:
            f.write(res)
    except Exception as e:
        print("Failed to fetch pincodes")
        print(e)

    with open("pincodes.csv", "rt") as f:
        codes = csv.DictReader(f)
        pincode_list = []
        count: int = 0
        for i in codes:
            i["id"] = count
            count += 1
            pincode_list.append(i)
        client.index("pincodes").add_documents(pincode_list, primary_key="id")
        print(f"Indexed {len(pincode_list)} pin codes")

def index_hsn_sac_codes():
    try:
        print("📡 Fetching the latest HSN/SAC file from the GST portal ...")
        res = r.get("https://tutorial.gst.gov.in/downloads/HSN_SAC.xlsx").content
        b = io.BytesIO(res)
        wb = openpyxl.load_workbook(b)
        hsn = wb["HSN"]
        sac = wb["SAC"]

        all_codes: list = []
        count: int = 0
        for i in hsn.values:
            if i[0] != "HSN Code":
                all_codes.append({"id": count, "code": i[0], "desciption": i[1]})
                count += 1

        for i in sac.values:
            if i[0] != "SAC Code":
                all_codes.append({"id": count, "code": i[0], "desciption": i[1]})
                count += 1

        client.index("hsn_sac_codes").add_documents(all_codes, primary_key="id")

        print(f"Indexed {len(all_codes)} HSN/SAC codes")
    except Exception as e:
        print("Failed to index HSN_SAC pincodes")
        print(e)


threading.Thread(target=index_ifsc_codes).start()
threading.Thread(target=index_pin_codes).start()
threading.Thread(target=index_hsn_sac_codes).start()

# index_ifsc_codes()
# index_pin_codes()
# index_hsn_sac_codes()

# portal = "https://www.gst.gov.in/fomessage/newsupdates/"
# # use custom user agent, as the gst portal allow other programs
# # to access their api
# custom_headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
# }

# def create_dump():
#     try:
#         client.create_dump()
#         print("creating dump")
#         return
#     except Exception as e:
#         print(e)

# def export_json():
#     try:
#         print("⚙ Extracting HSN/SAC from the spreadsheet ...")
#         for i in hsn.values:
#             if i[0] != "HSN Code":
#                 try:
#                     # remove white spaces in between, for some codes
#                     # sanitized_code_string = re.sub(r"\s+", "", str(i[0]), flags=re.UNICODE)
#                     hsn_dict[i[0]] = i[1]
#                 except:
#                     print(i[0], type(i[0]), i[1], type(i[1]))
#                     raise
#
#         for i in sac.values:
#             if i[0] != "SAC Code":
#                 try:
#                     sac_dict[i[0]] = i[1]
#                 except:
#                     print(i[0], type(i[0]), i[1], type(i[1]))
#                     raise
#
#         print("HSN codes: ", len(hsn_dict))
#         print("SAC codes: ", len(sac_dict))
#
#         print("Total: ", len(hsn_dict) + len(sac_dict))
#
#         print("Creating HSN/SAC json files ...")
#         # create json/ directory
#         try:
#             os.mkdir("public")
#         except:
#             shutil.rmtree("public")
#             os.mkdir("public")
#         # generate hsn code json
#         with open("public/hsn-codes.json", "w") as f:
#             json.dump(hsn_dict, f)
#         # generate SAC codes json
#         with open("public/sac-codes.json", "w") as f:
#             json.dump(sac_dict, f)
#         print("Generated the json files")
#     except Exception as e:
#         print(e)
#         raise


# def export_csv():
#     with open("public/hsn.csv", "w", newline="") as csvfile:
#         w = csv.writer(csvfile)
#         for i in hsn.values:
#             if i[0] == "HSN Code":
#                 w.writerow(["HSN", "Desciption"])
#             else:
#                 w.writerow([i[0], str(i[1])])
#
#     with open("public/sac.csv", "w", newline="") as csvfile:
#         w = csv.writer(csvfile)
#         for i in sac.values:
#             w.writerow([i[0], str(i[1])])
#     print("Created CSV files")


# # news from gst portal
# def generate_posts(news_summary):
#     """Generate a single json file for each item in summary"""
#     for item in news_summary:
#         response = r.get(url=portal + str(item["id"]), headers=custom_headers)
#         if response.status_code == 200:
#             with open(f"public/news/{item['id']}.json", "w") as f:
#                 json.dump(response.json()["data"][0], f)
#         else:
#             print("failed to generate post")
#

# def generate_summary():
#     """Create news items json file"""
#
#     os.makedirs("public/news", exist_ok=True)
#     # access the api
#     news_summary = r.get(url=portal, headers=custom_headers)
#     if news_summary.status_code == 200:
#         with open("public/news/summary.json", "w") as f:
#             json.dump(news_summary.json()["data"], f)
#
#         generate_posts(news_summary.json()["data"])
#         print("Generated News")
#     else:
#         print("failed to get summary")
