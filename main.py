from InquirerPy import prompt
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator 
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress
import time

README_FILE = "README.md"
console = Console()

def main():
#calling the functions - explains the workflow - makes code modular
    #welcome message
    console.print(Panel.fit(
        "[bold magenta]Welcome to the README Generator![/bold magenta]\n"
        "[magenta]This tool aims to help create a README.md file for all projects[/magenta]",
        title= "README Generator",
        border_style="green"
    ))
  
    answers = user_input() # user input
    progress_bar() #show progress
    content = readme_content(answers) #generate readme
    write_readme(content) #write readme.md
    console.print(f"[bold magenta]README.md has been successfully created![/bold magenta]")

#user input
def user_input():
    questions = [
        {"type": "input", "name": "title", "message": "What is the title of your project?"},
        {"type": "input", "name": "description", "message": "Enter a description for your project:"},
        {"type": "input", "name": "installation",  "message": "Enter installation instructions:"},
        {"type": "input", "name": "usage", "message": "Enter usage information:"},
        {"type": "list", "name": "license", "message": "Choose a license for your project:", "choices": ["MIT", "Apache 2.0", "Mozilla 2.0",  "GNU LGPL v3", "GNU GPL v3", "Creative Commons", "Unlicense"]},
        {"type": "input", "name": "author", "message": "Enter your name & contact information:"},
    ]
    return prompt(questions)

def progress_bar():
    with Progress() as progress:
        task = progress.add_task("[bold green]Generating README...", total=100)
        for _ in range(10):
            time.sleep(0.3)
            progress.update(task, advance=10)

def readme_content(answers):
    console.print("[bold cyan]Generated README.md content[/bold cyan]")
    console.print("-" * 50) 

# Formats the README content
    readme_text = f"""# {answers['title']}
## Description
{answers['description']}

## Installation
{answers['installation']}

## Usage
{answers['usage']}

## License
This project is licensed under the {answers['license']} License.

## Author
{answers['author']}
"""
    console.print(Panel.fit(readme_text, title="Generated README", border_style="blue"))
    return readme_text 

def write_readme(content):
    """Write README content to file"""
    with open("README.md", "w", encoding="utf-8") as readme_file:
        readme_file.write(content)


if __name__ == "__main__": # NB ensures code runs only when executed directly 
    main()

