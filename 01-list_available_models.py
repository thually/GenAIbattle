from rich import print
import sys
sys.path.append('./LIBS')
from WXlib import WX
print("[bold yellow]### Print all models IDs ###[/bold yellow]")
from rich.console import Console
from rich.syntax import Syntax

code_example = """# import helper libs
from WXlib import WX
# instantiate wx object
wx = WX()
# read models IDs
ids = wx.wxListAllModelIDs()"""

# Use rich to apply syntax highlighting
syntax = Syntax(code_example, "python", theme="monokai", line_numbers=True)

# Print to console with rich
console = Console()
console.print(syntax)


wx = WX()
ids = wx.wxListAllModelIDs()

print(ids)




