import requests


# получить информацию о товаре
def test_get2():
    response = requests.get("http://shop.bugred.ru/api/items/get", params={'id': '257'})
    print(response.json())
    assert response.status_code == 200

