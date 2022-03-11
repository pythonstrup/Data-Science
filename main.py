import re

re_examples = [
    not re.match("a", "cat"),
    re.search("a", "cat"),
    not re.search("c", "dog"),
    3 == len(re.split("[ab]", "carbs")),

    "R-D-" == re.sub("[0-9]", "-", "R2D2")
]

print(re_examples)
assert all(re_examples), "all the regex examples should be True"