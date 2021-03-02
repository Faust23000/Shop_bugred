import requests


class ShopBugredClient:
    _s = requests.session()
    host = None

    def __init__(self, host):
        self.host = host

    def login(self, email, password):
        data = {"email": email, "password": password}
        return self._s.post(self.host + "/auth", json=data)

    def autorize(self, email, password):
        res = self.login(email, password)
        if res.status_code != 200:
            raise Exception("Unable to authorize using given credentials")
        session_token = res.json().get("token")
        cookie = requests.cookies.create_cookie("token", session_token)
        self._s.cookies.set_cookie(cookie)

    def create_item(self, data: dict):
        return self._s.post(self.host + f"/api/items/create", json=data)

    def update_item(self, uid: int, data: dict):
        return self._s.put(self.host + f"/api/items/update/{uid}", json=data)

    def get_item(self, uid: int):
        return self._s.get(self.host + f"/api/items/get/{uid}")

    def delete_item(self, uid: int):
        return self._s.delite(self.host + f"/api/items/delete/{uid}")


