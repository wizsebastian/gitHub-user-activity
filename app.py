import requests as req
import json


class GitHubManager:
    def __init__(self, user_name: str):
        url_api_github = f"https://api.github.com/users/{user_name}/events"
        self.user_name = user_name
        self.url = url_api_github

    def get_user_info(self):
        try:
            res = req.get(self.url)
            data = res.json()
            # print(json.dumps(data, indent=4))
            self.organizeData(data)
        except ValueError as e:
            print(f"We have a error...{e}")

    def organizeData(self, data):
        event_list = []
        print("entro")
        for index, val in enumerate(data):
            print("TOP:", val)
            current_id = 0
            # event_list.append({**val, "counter": 0, "id": current_id})
            # current_id += 1
            # print("BOTTOM:", event_list)

            # print("***************K******************")
            # #     i.counter += 1
            # else:
            #     event_list.append({"type": i["type"], "counter": 0})


def main():
    print("work from main")
    user_name = "wizsebastian"

    core = GitHubManager(user_name)
    core.get_user_info()


if __name__ == "__main__":
    main()
