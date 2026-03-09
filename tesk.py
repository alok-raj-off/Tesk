#check mode comad like , modeckeck
import subprocess
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from rich.panel import Panel
from rich.console import Console

commands = {
    "checkMode": "it will print the current mode",
    "switch" : "it will switch the current mode in another",
    "/help" : "list all tyhe commands and mode ",
    "exit" : "it will exit the TESK program "

}

class Tesk:
    def __init__(self):
        self.mode = "college"
        self.console = Console()

    #making test function 
    # def testModefn():


    ## code to print the starting pannel 
    def cretepanel(self):
        panelshow = Panel(
                "[bold cyan] welcome to the Tesk CL [/bold cyan]",
                title=("[bold] system ready [/bold]"),
                subtitle=('[italic blue] this is where you learn and attcak at the same time [/italic blue]'),
                border_style="bright_blue"
        )
        self.console.print(panelshow)
        self.console.print(f"[grey] current mode : {self.mode} [/grey]")
    
    def testMode(self,userpro):
        #testHisFile = FileHistory(".testhis")
        try:
            while True:
                testPro  = prompt("@Tesk(test)> :")
                lsdata = subprocess.run(testPro,capture_output=True,text=True,shell=True)
                self.console.print(lsdata.stdout)
                if(testPro == "exit"):
                    break
        except Exception as err:
            self.console.print("the error is : ",err)



    def runTesk(self):
        self.cretepanel()
        historyOfCOmmands = FileHistory(".historyTesk")
        
        while True:
            try: 
                userpro = prompt("@Tesk > ",history=historyOfCOmmands)
                if(userpro == "exit"):
                    break
                elif(userpro == "checkMode"):
                    self.console.print(f"[magenta]The current mode is : {self.mode} [/magenta]")
                elif(userpro == "switch"):
                    if(self.mode == "college"):
                        self.console.print("[bold #ffbe30]mode switched to test[/bold #ffbe30]")
                        self.mode = "test"
                    # run test funxction

                        self.testMode(userpro)

                    elif(self.mode == "test"):
                        self.console.print("[bold #ffbe30]mode switched to college[/bold #ffbe30]")
                        self.mode = "college"
                        # college test funxction
                elif(userpro == "/help"):
                    i = 0
                    self.console.print(" ")
                    for key in commands:
                        self.console.print(f"[#E491C9]{key}[/#E491C9] => [#6984A9]{commands[key]} [/ #6984A9]")
                        i += 1
                    self.console.print(" ")
                else:
                    self.console.print("[red] no such command exist, use keyword '/help' to explore [/red]")
            except KeyboardInterrupt:
                self.console.print("key intrupted")

if __name__ == "__main__":
    teskrun = Tesk()
    teskrun.runTesk()