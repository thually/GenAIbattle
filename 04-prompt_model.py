from rich import print
import sys
sys.path.append('./LIBS')
from WXlib import WX
print("[bold yellow]### Prompt LLAMA3 model ###[/bold yellow]")
from rich.console import Console
from rich.syntax import Syntax

code_example = """# import helper libs
from WXlib import WX
# instantiate wx object
wx = WX()
# Set the model parameters or model name only if you want to change the model ID or its default parameters.
modelParameters = {
    "decoding_method": "greedy",
    "max_new_tokens": 2048,
    "min_new_tokens": 0,
    "stop_sequences": [ ],
    "repetition_penalty": 1
}
wx.wxInstModel(modelID='meta-llama/llama-3-70b-instruct', modelParams=modelParameters)

# Set the prompt template only once if you want to change the model behavior or expected output.
promptTemplate = \"""
    <|system|>
    You carefully follow instructions. You are helpful and harmless and you follow ethical guidelines and promote positive behavior.
    <|user|>
    {{QUESTION}}
    <|assistant|>
\"""
promptVariables = {
    'QUESTION' : "Who was the president of USA in 1999?"
}

generated_text = wx.wxGenText(promptTemplate=promptTemplate, promptVariables=promptVariables)"""

# Use rich to apply syntax highlighting
syntax = Syntax(code_example, "python", theme="monokai", line_numbers=True)

# Print to console with rich
console = Console()
console.print(syntax)

# Instantiate the wx object only ONCE in your application.
wx = WX()

# Set the model parameters or model name only if you want to change the model ID or its default parameters.
modelParameters = {
    "decoding_method": "greedy",
    "max_new_tokens": 2048,
    "min_new_tokens": 0,
    "stop_sequences": [ ],
    "repetition_penalty": 1
}
wx.wxInstModel(modelID='meta-llama/llama-3-70b-instruct', modelParams=modelParameters)

# Set the prompt template only once if you want to change the model behavior or expected output.
promptTemplate = """
    <|system|>
    You carefully follow instructions. You are helpful and harmless and you follow ethical guidelines and promote positive behavior.
    <|user|>
    {{QUESTION}}
    <|assistant|>
"""
promptVariables = {
    'QUESTION' : "Who was the president of USA in 1999?"
}

generated_text = wx.wxGenText(promptTemplate=promptTemplate, promptVariables=promptVariables)

print({
    'question': promptVariables['QUESTION'],
    'answer'  : generated_text
})

