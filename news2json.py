import json, os
import requests as r


os.mkdir("news")

portal = "https://www.gst.gov.in/fomessage/newsupdates/"
# use custom user agent, as the gst website does not seem to allow other programs
# to access their public api
custom_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}


def generate_posts(news_summary):
    """Generate a single json file for each item in summary"""
    for item in news_summary:
        print(item)
        response = r.get(url=portal + str(item["id"]), headers=custom_headers)
        if response.status_code == 200:
            with open(f"news/{item['id']}.json", "w") as f:
                json.dump(response.json()["data"][0], f)
        else:
            print("failed to generate post")


def generate_summary():
    """Create news items json file"""
    # access the api
    news_summary = r.get(url=portal, headers=custom_headers)
    if news_summary.status_code == 200:
        with open("news/summary.json", "w") as f:
            json.dump(news_summary.json()["data"], f)

        generate_posts(news_summary.json()["data"])
    else:
        print("failed to get summary")


generate_summary()
