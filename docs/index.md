# Checkdocs

This package just check if the Type Hint in the function definition matches with the Docstring.

## Commands

* `checkdocs file [filename]` - Check a single file.
* `checkdocs folder [foldername]` - Check all Python files inside a folder.


## Project layout

    checkdocs/
        main.py           # Project execution.
    tests/        
        test_.py          # Code tests. Typer App definition.
    pyproject.toml        # The project configuration.
    mkdocs.yml            # The configuration file of documentation.
    docs/        
        index.md          # The documentation homepage.
        ...               # Other markdown pages, images and other files.
