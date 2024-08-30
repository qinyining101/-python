import requests
API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/bcd513d37a8f934e1fb26ce2b14ae2da/ai/run/"
headers = {"Authorization": "Bearer AggngFNvBULWcZOY4L9rClL8yF0ZvO8y0It5-A3P"}
 
def run(model, inputs):
    input = { "messages": inputs }
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response.json()
 
inputs = [
    { "role": "system", "content":input("输入提示词：") },
    { "role": "user", "content": input("输入问题：")}
]

while True:
    output = run("@cf/openchat/openchat-3.5-0106", inputs)
    print(output['result']['response'])
