from webserver import keep_alive
import requests

channelID = 1153790993733255218
headers = {
    "authorization":
    "MTE5NzI1Mjg4MjA4OTY0NDEyMw.G1dM-r.zkp_Ybw9NURTueSCSZS7lJwRsv7yEdj43CN2-w"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
