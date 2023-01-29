import json, pathlib

hsn_sac_data: list
hsn_data: list
sac_data: list

project_root = pathlib.Path("./").resolve()

with open(f"{project_root}/json/hsn-sac-codes.json") as f:
    hsn_sac_data = json.loads(f.read())

with open(f"{project_root}/json/hsn-codes.json") as f:
    hsn_data = json.loads(f.read())

with open(f"{project_root}/json/sac-codes.json") as f:
    sac_data = json.loads(f.read())

# check combined hsn & sac file
def test_check_length():
    assert len(hsn_sac_data) > 0


def test_hsn_exists():
    code_found = False
    for i in hsn_sac_data:
        if i["code"] == 8212:
            code_found = True
    assert code_found


def test_sac_exists():
    code_found = False
    for i in hsn_sac_data:
        if i["code"] == 995414:
            code_found = True
    assert code_found


# check individual hsn & sac files
def test_hsn_codes():
    assert len(hsn_data) > 0


def test_hsn_exists_in_hsn_codes():
    code_found = False
    for i in hsn_sac_data:
        if i["code"] == 8212:
            code_found = True
    assert code_found


def test_sac_codes():
    assert len(sac_data) > 0


def test_sac_exists_in_sac_codes():
    code_found = False
    for i in hsn_sac_data:
        if i["code"] == 995414:
            code_found = True
    assert code_found


def test_news_summary():
    with open("news/summary.json", "r") as f:
        news_list = json.loads(f.read())
        assert len(news_list) > 0
