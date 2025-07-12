from InquirerPy import prompt
from InquirerPy.base.control import Choice
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress
import time

console = Console()

#welcome message
console.print("[bold magenta]Welcome to the README Generator![/bold magenta]\n"
              "[magenta]This tool aims to help create a README.md file for all projects[/magenta]")

#user input
questions = [
    {"type": "input", "name": "title", "message": "What is the title of your project?"},
    {"type": "input", "name": "description", "message": "Enter a description for your project:"},
    {"type": "input", "name": "installation",  "message": "Enter installation instructions:"},
    {"type": "input", "name": "usage", "message": "Enter usage information:"},
    {"type": "list", "name": "license", "message": "Choose a license for your project:", "choices": ["MIT", "Apache 2.0", "Mozilla 2.0",  "GNU LGPL v3", "GNU GPL v3", "Creative Commons", "Unlicense"]},
    {"type": "input", "name": "author", "message": "Enter your name & contact information:"},
]
answers = prompt(questions)

with Progress() as progress:
    task = progress.add_task("[bold green]Generating README...", total=100)
    for _ in range(10):
        time.sleep(0.3)
        progress.update(task, advance=10)

console.print("[bold cyan]Generated README.md content[/bold cyan]")
print(answers) #need to format this - maybe seperator?





#get user input - including title, description, installation, usage, license, author, and contact info.
#A dropdown list is used to select a license type.
#A `README.md` file is generated using GitHub markdown format based on the user's input.
# The codebase is structured using classes and organized into modules.
#A `requirements.txt` file is included listing all dependencies (including `PyInquirer`).
# A virtual environment is used for the project, and its setup is documented.
# Instructions for running the application are included.
#A demo video of the script running is submitted.
#A link to the GitHub repository is included with the submission.
