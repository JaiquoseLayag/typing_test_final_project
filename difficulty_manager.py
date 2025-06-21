# Create a class to manage different difficulties
class DifficultyManager:
    def __init__(self):
        self.word_levels = {
            "easy": [
                "code", "data", "loop", "func", "var", "int", "str", "list", "dict", "set",
                "tuple", "def", "class", "True", "False", "None", "if", "else", "elif", "for",
                "while", "try", "except", "pass", "break", "cont", "ret", "arg", "kwarg", "self",
                "init", "main", "path", "file", "read", "write", "open", "close", "sort", "map",
                "filt", "iter", "next", "call", "obj", "type", "cast", "comp", "pip", "env"
            ],