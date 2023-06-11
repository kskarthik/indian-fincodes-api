import json, pathlib

hsn_data: dict
sac_data: dict

project_root = pathlib.Path("./").resolve()

with open(f"{project_root}/json/hsn-codes.json") as f:
    hsn_data = json.loads(f.read())

with open(f"{project_root}/json/sac-codes.json") as f:
    sac_data = json.loads(f.read())


def test_hsn_exists():
    code_found = False
    for k, v in hsn_data.items():
        if k == "8212":
            print(v)
            code_found = True
    assert code_found


def test_sac_exists():
    code_found = False
    for k, v in sac_data.items():
        if k == "995414":
            print(v)
            code_found = True
    assert code_found


# check individual hsn & sac files
def test_hsn_codes():
    assert len(hsn_data) > 0


def test_sac_codes():
    assert len(sac_data) > 0


def test_news_summary():
    with open("news/summary.json", "r") as f:
        news_list = json.loads(f.read())
        assert len(news_list) > 0
