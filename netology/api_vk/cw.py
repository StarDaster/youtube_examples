"""
https://oauth.vk.com/authorize?client_id=51420426&display=page&scope=stats.offline&response_type=token&v=5.131
"""

with open("token.txt", "r") as file_object:
    token = file_object.read().strip()

import time
import requests
from pprint import pprint


# URL = "https://api.vk.com/method/users.get"
# params = {
#     "user_ids": "1",
#     "access_token": token,
#     "v": "5.131",
#     "fields": "education, sex"
# }
# res = requests.get(URL, params=params)
# pprint(res.json())


# получаем список групп по поисковому запросу
def search_group(query, sorting=0):
    """
    0 - сортировка по умолчания
    1 - сортировка по скорости роста
    2 - отношение дневной посещаемости
    3 - отношение количества лайков к количеству пользователей
    4 - комментариев к количеству пользователей
    5 - записей в обсуждениях к количеству пользователей
    """
    params = {
        "q": query,
        "access_token": token,
        "v": "5.131",
        "sort": sorting,
        "count": 300
    }
    resp = requests.get("https://api.vk.com/method/groups.search", params).json()
    print(resp)
    response_data = resp["response"]["items"]
    return response_data


# target_groups = search_group("python")
# pprint(target_groups)

# расширенная информация о группе
target_group_ids = "1, 2, 3, 4, 5"
params = {
    "access_token": token,
    "v": "5.131",
    "group_ids": target_group_ids,
    "fields": "members_count, activity, description"
}
resp = requests.get("https://api.vk.com/method/groups.getById", params)
pprint(resp.json()["response"])
