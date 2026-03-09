import subprocess
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
import time
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
# the unshell one command 

# lsdata = subprocess.run(["ls","-l"],capture_output=True,text=True)
# print("the command is running , the otpt is ")
# print(lsdata.stdout)
# print(lsdata.returncode)

# try:
#     sdata2 = subprocess.run(["lss","-l"],capture_output=True,text=True)
#     print("the command is running , the otpt is ")
#     print(lsdata2.stdout)
#     print(lsdata2.returncode)
# except FileNotFoundError:
#     print("oops looks like u made an error , do u mean ls idot")



#--------------------------------------------------------------------------

# command = "ls -l | grep 'py'"

# try:
#     pro = subprocess.run(command,shell=True,capture_output=True,text=True)
#     print(pro.stdout)
# except Exception as err:
#     print("the error is : ",err)




###################_______________________ rich lib ___________________________________##########################


console = Console()
# console.print("heey welcome t5o codex",style="blink red on white")

#miaking pannel
# command = Text("")
# pannel = Panel(
#     command,
#     title="[bold cyan] TESK COMMAND SHELL [/bold cyan]",
#     subtitle="[itallic]welcome to the shell hehehe[/itallic]",
#     border_style="bright_blue"
# )

# console.print(pannel)



# making the spinner 
# with console.status("[bold cyan] processing .... [/bold cyan]",spinner="dots"):
#     time.sleep(3)
#     console.print("[yellow] running the tests ...  [/yellow]")
#     time.sleep(4)
#     console.print("[green] test sucessfull[/green]")


# trying toolkit
hisfile = FileHistory(".his")
while True:
     prmpt = prompt("Tesk @ > ",history=hisfile)
     if (prmpt == "exit"):
        break