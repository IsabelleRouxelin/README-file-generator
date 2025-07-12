from PyInquirer import prompt
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress
import time

console = Console()

#welcome message
console.print("[bold green]Welcome to the README Generator![/bold green]\n"
              "[green]This tool aims to help you create a professional README.md file for all projects[/green]")

#user input
questions = [
    {"type": "input", "name": "title", "message": "What is the title of your project?"},
    {"type": "input", "name": "description", "message": "Enter a description for your project:"},
    {"type": "input", "name": "installation", "message": "Enter installation instructions:"},
    {"type": "input", "name": "usage", "message": "Enter usage information:"},
    {"type": "input", "name": "license", "message": "Choose a license for your project:"}, #needs to be a dropdown 
    {"type": "input", "name": "author", "message": "Enter your name:"},
    {"type": "input", "name": "name", "contact": "Enter your email address:"},
]
answers = prompt(questions)

#progress bar ?




#get user input - including title, description, installation, usage, license, author, and contact info.
#A dropdown list is used to select a license type.
#A `README.md` file is generated using GitHub markdown format based on the user's input.
# The codebase is structured using classes and organized into modules.
#A `requirements.txt` file is included listing all dependencies (including `PyInquirer`).
# A virtual environment is used for the project, and its setup is documented.
# Instructions for running the application are included.
#A demo video of the script running is submitted.
#A link to the GitHub repository is included with the submission.
