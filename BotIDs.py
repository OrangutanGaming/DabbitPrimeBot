import json
import os

dir = os.path.dirname(os.path.abspath(__file__))
with open(f"{dir}/settings.json") as data_file:
    settings = json.load(data_file)
    data_file.close()

clientID = settings["clientID"]
token = settings["token"]
ownerID = int(settings["ownerID"])
prefixes = settings["prefix"]

dev_id = 150750980097441792
dev_role = "."
dev_name = "Orangutan#9393"
dev_role_old = ["(._.)", "_"]
permissionsURL = "2146958463" # https://finitereality.github.io/permissions/
OAuth2 = "https://discordapp.com/oauth2/authorize?permissions={}&scope=bot&client_id={}".format(permissionsURL, clientID)
URL = OAuth2

GitHubUser = "OrangutanGaming"
GitHubRepo = "--Q--Bot"
GitHub = "https://github.com/{}/{}".format(GitHubUser, GitHubRepo)

Patreon = "https://www.patreon.com/OrangutanGaming"

imgur_clientID = settings["imgurID"]
imgur_Secret = settings["imgurSecret"]