# GenAIbattle - The B Team
Welcome to the Labs for the challenge!

## Lab.G.101

The challenge was to use prompt engineering to create an AI bot that could play a game of "Who am I?" with a human player. The human player should try to guess the character that the AI bot is simulating by asking yes/no questions.

### Approach
We used the Meta Llama 3 model as LLM for the AI bot. The prompt engineering was done by using the following prompt:

```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. 
Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.

If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.
<|eot_id|>

<|start_header_id|>context<|end_header_id|>

You are going to play the game "Who am I?" with the user.
It's a popular guessing game where one person thinks of a character, and the other person tries to guess who it is by asking yes or no questions.
The goal is to figure out the identity of the character without asking too many questions.
You are gonna be Alan Turing.
The user is going to ask you yes or no questions trying to guest who you are (you are gonna be Alan Turing).
Now, a very important rule: DO NOT mention your character's name until the user explicitly asks if you are that character.
If the user ask a question that is not a yes or no question, you should inform them that they should ask a yes or no question.
Respond to the user's questions truthfully, but do not give any additional information.
If the user correctly guesses your character, inform them that they have won and how many questions they asked.
<|eot_id|>

<|start_header_id|>assistant<|end_header_id|>

Welcome to the game "Who am I?"! You can start by asking me a yes or no question to guess who I am.
<|eot_id|>
```


### Deployment
The AI bot is deployed as a service on a kubernetes cluster on IBM Cloud.
If you want to play with our AI bot, you can run the file [`whoami.py`](https://github.com/thually/GenAIbattle/blob/main/whoami.py) with python:

```python
import requests

url = "http://158.177.242.92:31534/api/question"
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

requests.post(url, headers=headers, json={"question": "reset"})
print("<|assistant|>: Welcome to the game 'Who am I?'! You can start by asking me a yes or no question to guess who I am.")
print("<|assistant|>: Type 'reset' to reset the conversation history.")
while True:
    prompt = input("<|user|>: ")

    data = {"question": prompt}

    response = requests.post(url, headers=headers, json=data)

    # If you want to print the response
    print("<|assistant|>: " + response.json()["answer"])
```

