"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [1729],
            "answer": [12, 1],
        },
        {
            "input": [8],
            "answer": [2],
        },
        {
            "input": [11],
            "answer": None,
        },
    ],
    "Extra": [
        {
            "input": [100],
            "answer": [4, 3, 2, 1],
        },
        {
            "input": [216],
            "answer": [6],
        },
        {
            "input": [855],
            "answer": [9, 5, 1],
        },
        {
            "input": [sum([n*n*n for n in range(11)])],
            "answer": [14, 6, 4, 1],
        },
        {
            "input": [sum([n*n*n for n in range(1001)])],
            "answer": [6303, 457, 75, 14, 9, 7, 5, 4],
        },
    ]
}
