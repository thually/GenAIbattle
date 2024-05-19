import requests

# url = "http://158.177.242.92:31534/api/question"
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

print("<|assistant|>: Welcome to the game 'Who am I?'! You can start by asking me a yes or no question to guess who I am.")
print("<|assistant|>: Type 'reset' to reset the conversation history.")
while True:
    prompt = input("<|user|>: ")

    data = {"question": prompt}

    response = requests.post(url, headers=headers, json=data)

    # If you want to print the response
    print("<|assistant|>: " + response.json()["answer"])