import os

api_id = 27215374
api_hash = os.environ.get("API_HASH", "b4495d7b9db5bb280121b4eeeb68331c")
bot_token = os.environ.get("BOT_TOKEN")
auth_users = os.environ.get("AUTH_USERS", "6762856879")
sudo_users = [int(num) for num in auth_users.split(",")]
osowner_users = os.environ.get("OWNER_USERS", "6762856879")
owner_users = [int(num) for num in osowner_users.split(",")]
