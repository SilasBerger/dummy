import os
import requests
import json
from datetime import datetime
from pathlib import Path

# BASE_PATH = Path("/Users/silas/repos/actions-experients/gh-action-hello-world")
BASE_PATH = Path("/github/workspace")

out_dir = BASE_PATH.joinpath("data")
out_dir.mkdir(parents=True, exist_ok=True)

res_json = requests.get("https://randomuser.me/api/").json()
first_user = res_json["results"][0]
data = first_user["name"]
data["timestamp"] = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

file_path = out_dir.joinpath("user.json")
print(file_path)
with open(file_path, "w", encoding="utf-8") as outfile:
  json.dump(data, outfile, indent=2)

print("Done.")