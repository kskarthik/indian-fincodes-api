import meilisearch as ms

client = ms.Client('http://localhost:7700')

def test_index_count():
    assert client.get_indexes()['total'] == 3

def test_search_pincodes():
    hits = client.get_index("pincodes").search("500101")["hits"]
    assert len(hits) > 1

def test_search_banks():
    hits = client.get_index("banks").search("karol bagh")["hits"]
    print(hits)
    assert len(hits) > 1

def test_search_hsnsac():
    hits = client.get_index("hsn_sac_codes").search("razor")["hits"]
    assert len(hits) > 1
