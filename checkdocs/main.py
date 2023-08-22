from rich import print
from typer import Argument, Typer
from typing_extensions import Annotated

from checkdocs.checkers.check_file import check_file

app = Typer()


@app.command()
def file(
    name: Annotated[str, Argument(help="Filename to check. Only [.py] files.")],
):
    print(check_file(name))


@app.command()
def folder(
    name: Annotated[
        str, Argument(help="Folder name to check. Only [.py] files will be checked.")
    ],
):
    print(f"Mock Funtion to Check Folder {name}!")
