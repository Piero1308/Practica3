from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from config.app import App
from controller.funcion import *
from controller.report import *

def menu(app:App):
    consola=Console()
    while True:
        menu_text=Text()
        menu_text.append("\n📊 Proyecto Datux\n", style="underline bold")
        menu_text.append("\n[1] 🟢 Ingestar Data\n", style="green")
        menu_text.append("[2] 📈 Reporte de Ventas\n", style="blue")
        menu_text.append("[3] ❌ Salir\n", style="red")
        consola.print(Panel(menu_text, title="🚀 [bold magenta]Menú Principal[/bold magenta]", expand=False, border_style="yellow"))
        opcion = Prompt.ask("Selecciona una opción", choices=["1", "2", "3"], default="3")
        if opcion=="1":
            IngestDataProducts(app)
            
        elif opcion=="2":
            GenerateReportVentas(app)
        elif opcion=="3":
            pass
            break
        else:
            print("opcion no reconocida")
        
        