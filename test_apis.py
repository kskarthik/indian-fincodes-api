import meilisearch as ms

client = ms.Client('http://localhost:7700')

pincode_keys = ['id', 'Circle Name', 'Region Name', 'Division Name', 'Office Name', 'Pincode', 'OfficeType', 'Delivery', 'District', 'StateName']

bank_keys = ['IFSC', 'BANK', 'BRANCH', 'CENTRE', 'DISTRICT', 'STATE', 'ADDRESS', 'CONTACT', 'IMPS', 'RTGS', 'CITY', 'ISO3166', 'NEFT', 'MICR', 'UPI', 'SWIFT']

hsnsac_keys = ['id', 'code', 'desciption']

def test_index_count():
    assert client.get_indexes()['total'] == 3

def test_search_pincodes():
    hits = client.get_index("pincodes").search("500101")["hits"]
    assert len(hits) > 1

def test_pincode_keys():
    hits = client.get_index("pincodes").search("500101")["hits"]
    assert [*hits[0].keys()] == pincode_keys

def test_bank_keys():
    hits = client.get_index("banks").search("karol bagh")["hits"]
    assert [*hits[0].keys()] == bank_keys

def test_search_banks():
    hits = client.get_index("banks").search("karol bagh")["hits"]
    assert len(hits) > 1

def test_search_hsnsac():
    hits = client.get_index("hsn_sac_codes").search("razor")["hits"]
    assert len(hits) > 1

def test_hsnsac_keys():
    hits = client.get_index("hsn_sac_codes").search("razor")["hits"]
    assert [*hits[0].keys()] == hsnsac_keys
