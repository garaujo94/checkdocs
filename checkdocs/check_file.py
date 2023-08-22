import ast

from checkdocs.config import functions_exclusion_list
from checkdocs.make_check import checkdocs


def check_file(file: str) -> dict:
    tree = parse_file(file)
    functions = get_functions(tree)

    for function in functions:
        if function.name in functions_exclusion_list:
            continue

        result = checkdocs(function)

    return result


def parse_file(file: str) -> ast.Module:
    with open(file, "r") as f:
        tree = ast.parse(f.read())
    return tree


def get_functions(tree: ast.Module) -> list[ast.FunctionDef]:
    result = [
        tree_function
        for tree_function in ast.walk(tree)
        if isinstance(tree_function, ast.FunctionDef)
    ]

    return result
