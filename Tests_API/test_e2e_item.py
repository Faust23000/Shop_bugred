import requests


def test_post():


    # шаг1 Создать товар
    create = requests.post("http://shop.bugred.ru/api/items/create/", params={
        "name": "Шортики",
        "section": "Платья",
        "description": "Модное платье из новой коллекции!",
        "color": "RED",
        "size": 44,
        "price": 666,
        "params": "dress"
    })
    print(create.json())
    item_id = create.json()["result"]["id"]

    # шаг2 проверить наличие товара
    response = requests.get("http://shop.bugred.ru/api/items/get/", params={"id": item_id})
    print(response.json())
    assert response.status_code == 200

    # шаг3 изменить товара
    response = requests.put("http://shop.bugred.ru/api/items/update/", params={
        "id": item_id,
        "name": "Юпочки",
        "section": "Платья",
        "description": "старая колекция",
    })
    print(response.json())
    assert response.status_code == 200

    # шаг4 проверить изменение товара
    response = requests.get("http://shop.bugred.ru/api/items/get/", params={"id": item_id})
    print(response.json())
    assert response.status_code == 200

    # шаг5 удалить товар
    response = requests.delete("http://shop.bugred.ru/api/items/delete", params={"id": item_id})
    print(response.json())

    # шаг6 проверить товар на удаление
    response = requests.get("http://shop.bugred.ru/api/items/get/", params={"id": item_id})
    print(response.json())
    assert response.status_code == 200
