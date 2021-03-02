import requests


def test_get_locations_for_us_90210_check_status_code_equals_200():
    response = requests.get("http://api.zippopotam.us/us/90210")
    assert response.status_code == 200
# headers = {
#     "User-Agent": "anonymus"
# }
# #response = requests.get('https://httpbin.org/get', headers=headers, params={'a': 'b', 'c': 10})
#
#
# response = requests.post('https://httpbin.org/post',
#                          headers=headers,
#                          params={'a': 'b', 'c': 10},
#                          json={'username': 'supersecret'})
# print(response.content)

# item_id = None

# def test_get():
#     response = requests.get("http://shop.bugred.ru/")
#     assert response.status_code == 200


# # создать товар
# def test_post():
#     create = requests.post("http://shop.bugred.ru/api/items/create/", data={
#         "name": "Шортики",
#         "section": "Платья",
#         "description": "Модное платье из новой коллекции!",
#         "color": "RED",
#         "size": 44,
#         "price": 666,
#         "params": "dress"
#     })
#     item_id = create.json()["result"]["id"]
#     print(create.json())
#
#
# # проверить наличие товара
# def test_get3():
#     response = requests.get("http://shop.bugred.ru/api/items/get/", params={"id": "item_id"})
#     print(response.json())
#     assert response.status_code == 200
#
# # изменить товар
# def test_put():
#     response = requests.put("http://shop.bugred.ru/api/items/update/", data={
#         "id": item_id,
#         "name": "Юпочки",
#         "section": "Платья",
#         "description": "старая колекция",
#     })
#     print(response.json())
#     assert response.status_code == 200
#
#
# # проверить изменение товара
# def test_get4():
#     response = requests.get("http://shop.bugred.ru/api/items/get", data={"id": item_id})
#     print(response.json())
#     assert response.status_code == 200
#
# # удалить товар
# def test_delete():
#     response = requests.delete("http://shop.bugred.ru/api/items/delete", data={'id': item_id})
#     print(response.json())
#     assert response.raise_for_status()
