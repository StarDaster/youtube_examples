from netology.api_vk.cw import VkApiClient, token
from pprint import pprint


class CoinAPIClient:
    def action(self):
        return {"fields": "education, sex"}


class DBClient:
    def action(self):
        return {"user_ids": "1"}


class Application:
    def __init__(self, db_client: DBClient, coin_api_client: CoinAPIClient, vk_client: VkApiClient):
        self.db_client = db_client
        self.coin_api_client = coin_api_client
        self.vk_client = vk_client

    def run(self):
        print("Начал работу на локалхосте на порту 8000")

    def get_info_from_all_clients(self):
        data_from_db = self.db_client.action()
        user_ids = data_from_db["user_ids"]
        data_from_coin_api = self.coin_api_client.action()
        fields = data_from_coin_api["fields"]
        data_from_vk = self.vk_client.get_users_info(user_ids=user_ids, fields=fields)
        return data_from_vk


db_client = DBClient()
coin_api_client = CoinAPIClient()
vk_client = VkApiClient(token=token, api_version="5.131")
app = Application(db_client=db_client, coin_api_client=coin_api_client, vk_client=vk_client)
app.run()
pprint(app.get_info_from_all_clients())
