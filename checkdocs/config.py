functions_exclusion_list = ["__init__", "__main__"]

docstrings_regex = [
    {
        "regex": r"{param_name} \([^)]+\)",
        "sep": " ",
        "string_limits": [1, -1],
    },  # var_a (int): ...
    {
        "regex": r"{param_name} \: \S+",
        "sep": ":",
        "string_limits": [None, None],
    },  # var_a : int ...
]
